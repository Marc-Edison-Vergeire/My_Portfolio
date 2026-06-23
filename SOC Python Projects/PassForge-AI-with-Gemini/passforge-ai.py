ascii=r"""

   ___   ____    ________  _____    ___             __         __     ______          __
  / _ | /  _/   / __/ __ \/ ___/   / _ | ___  ___ _/ /_ _____ / /_   /_  __/__  ___  / /
 / __ |_/ /    _\ \/ /_/ / /__    / __ |/ _ \/ _ `/ / // (_-</ __/    / / / _ \/ _ \/ / 
/_/ |_/___/   /___/\____/\___/   /_/ |_/_//_/\_,_/_/\_, /___/\__/    /_/  \___/\___/_/  
                                                   /___/                                

                             by Marc Edison Vergeire
				     2026
"""

print(ascii)



import secrets
import string
import sys
import json
from google import genai
from google.genai import types

# =========================================================================
# 🔑 ENTERPRISE API CONFIGURATION
# =========================================================================
GEMINI_API_KEY = "YOUR_ACQUIRED_API_KEY_HERE"
# =========================================================================

def parse_password_intent_with_gemini(user_prompt):
    """
    Feeds the natural language request into the Gemini Cloud API to extract 
    structural parameters and password constraints as a clean JSON configuration block.
    """
    print("\n--- 🧠 AI COGNITIVE INTENT ANALYSIS ---")
    print("[*] Dispatching requirements to Google Gemini Cloud API...")

    system_prompt = (
        "You are a strict security architecture engine. Your job is to read a user's natural language "
        "request for a password and extract the exact parameters they want. "
        "You must respond ONLY with a valid JSON object. Do not include any markdown backticks, explanations, or conversational text.\n\n"
        "The JSON object must use exactly these keys with these default values if not specified:\n"
        "{\n"
        '  "length": 16,      // Must be an integer. Default to 16 if unspecified.\n'
        '  "letters": true,   // Boolean. True if they want characters like a-z, A-Z.\n'
        '  "numbers": true,   // Boolean. True if they want digits 0-9.\n'
        '  "symbols": true    // Boolean. True if they want special characters.\n'
        "}"
    )

    try:
        # Initialize the GenAI client with your hardcoded API Key
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json" # Forces Gemini to strictly output clean JSON data
            )
        )
        
        # Parse the clean JSON string back into a Python dictionary
        config = json.loads(response.text.strip())
        return config

    except Exception as e:
        print(f"❌ Gemini Cloud API Error: {str(e)}")
        print("[*] Falling back to default highly-secure configuration blueprint.")
        return {"length": 16, "letters": True, "numbers": True, "symbols": True}


def generate_secure_password(length, letters, numbers, symbols):
    """Assembles the character pool and generates a cryptographically secure string."""
    character_pool = ""

    if letters:
        character_pool += string.ascii_letters  
    if numbers:
        character_pool += string.digits  
    if symbols:
        character_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not character_pool:
        return None

    # Preserves your cryptographically secure random selection engine
    password = "".join(secrets.choice(character_pool) for _ in range(length))
    return password


def main():
    print("\n" + "=" * 20 + " [🛡️ WELCOME TO PASSFORGE-AI via GEMINI] " + "=" * 20)
    print("Generate cryptographically secure passwords natively using natural language.\n")

    print("💡 Prompt Examples:")
    print("   - 'Give me an ultra-secure 32 character password with numbers and letters, but zero symbols'")
    print("   - 'I need a short pin-style password, only numbers, length 6'")
    print("   - 'Generate something crazy with a ton of special characters, 24 characters long'\n")
    
    user_prompt = input("🗣️ Describe your password requirements: ").strip()

    if not user_prompt:
        print("[-] Input string was blank. Aborting execution pipeline.")
        return

    # Call the cloud analyzer
    ai_config = parse_password_intent_with_gemini(user_prompt)

    # Extract the variables translated by Gemini
    length = ai_config.get("length", 16)
    include_letters = ai_config.get("letters", True)
    include_numbers = ai_config.get("numbers", True)
    include_symbols = ai_config.get("symbols", True)

    # Output extracted operational constraints to console
    print("\n--- ⚙️ EXTRACTED TARGET CONFIGURATIONS ---")
    print(f" 📐 Parsed Target Length: {length} characters")
    print(f" 🔤 Include Letters:     {'✅ YES' if include_letters else '❌ NO'}")
    print(f" 🔢 Include Numbers:     {'✅ YES' if include_numbers else '❌ NO'}")
    print(f" 🔣 Include Symbols:     {'✅ YES' if include_symbols else '❌ NO'}")

    # Security check validation warning
    if length < 12:
        print("\n⚠️  [SECURITY WARNING]: Industry standards recommend at least 12+ characters for optimal security.")

    # Generate password
    password = generate_secure_password(
        length, include_letters, include_numbers, include_symbols
    )

    print("\n" + "-" * 55)
    if password:
        print("🚀 SUCCESS! Your securely engineered password is:")
        print(f"\n👉  {password}  \n")
        print("🔒 [CONFIDENTIAL] Keep this credential isolated and do not share it.")
    else:
        print("❌ GENERATION ERROR: Process aborted.")
        print("   ↳ The AI context disabled all character pools. Try specifying explicit inclusions.")

    print("-" * 55 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[-] Session terminated early by user. Goodbye.")
        sys.exit(0)