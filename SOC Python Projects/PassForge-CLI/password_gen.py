ascii="""
   _____ ____  ______    ___                __           __    ______            __
  / ___// __ \/ ____/   /   |  ____  ____ _/ /_  _______/ /_  /_  __/___  ____  / /
  \__ \/ / / / /       / /| | / __ \/ __ `/ / / / / ___/ __/   / / / __ \/ __ \/ / 
 ___/ / /_/ / /___    / ___ |/ / / / /_/ / / /_/ (__  ) /_    / / / /_/ / /_/ / /  
/____/\____/\____/   /_/  |_/_/ /_/\__,_/_/\__, /____/\__/   /_/  \____/\____/_/   
                                         /____/                                 

                              by Marc Edison Vergeire
                                       2026
"""
print(ascii)

import secrets
import string
import sys


def get_valid_input(prompt):
    """Ensures the user provides a definitive yes or no answer."""
    while True:
        response = input(prompt).strip().lower()
        if response in ["y", "yes"]:
            return True
        if response in ["n", "no"]:
            return False
        print("❌ Invalid input. Please type 'y' for Yes or 'n' for No.")


def get_valid_length():
    """Validates that the password length requested is a safe, realistic positive integer."""
    while True:
        try:
            length = int(
                input("🔑 Enter desired password length (e.g., 1 to 64+): ")
            )
            if length <= 0:
                print("❌ Length must be a positive number greater than 0.")
                continue
            if length < 12:
                print(
                    "⚠️ Note: Industry standards recommend at least 12+ characters for optimal security."
                )
            return length
        except ValueError:
            print("❌ Invalid input. Please enter a valid whole number.")


def generate_secure_password(length, letters, numbers, symbols):
    """Assembles the character pool and generates a cryptographically secure string."""
    character_pool = ""

    if letters:
        character_pool += string.ascii_letters  # Contains dynamic a-z and A-Z
    if numbers:
        character_pool += string.digits  # Contains 0-9
    if symbols:
        # Custom curated list of universally web-safe special symbols
        character_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Defensive Guardrail: If no character pools are chosen, generation cannot happen
    if not character_pool:
        return None

    # Cryptographically secure random selection pipeline
    password = "".join(secrets.choice(character_pool) for _ in range(length))
    return password


def main():
    print("\n" + "=" * 20 + " [🛡️ WELCOME TO PASSFORGE-CLI] " + "=" * 20)
    print("Generate cryptographically secure passwords natively in your terminal.\n")

    # Step 1: Gather parameter constraints
    length = get_valid_length()

    print("\n--- ⚙️ CONFIGURING CHARACTER SELECTION POOLS ---")
    include_letters = get_valid_input("🔹 Include Alphabetical Letters? (y/n): ")
    include_numbers = get_valid_input("🔹 Include Numeric Digits? (y/n): ")
    include_symbols = get_valid_input("🔹 Include Special Symbols? (y/n): ")

    # Step 2: Attempt password generation logic
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
        print("   ↳ You must select at least ONE character pool type (Letters, Numbers, or Symbols).")

    print("-" * 55 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Gracefully handle manual Ctrl+C closures without messy Python stack traces
        print("\n\n[-] Session terminated early by user. Goodbye.")
        sys.exit(0)