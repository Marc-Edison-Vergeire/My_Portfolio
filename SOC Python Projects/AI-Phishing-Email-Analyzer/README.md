<h1>AI Phishing Email Analyzer</h1>
<p><img width="726" height="155" alt="ai-soc-analyst-tool" src="https://github.com/user-attachments/assets/c32be4cb-b7c5-4d52-b1f4-72ef51177da9" />
</p>

<br>
<h2>Executable Preview</h2>
<p><img width="1917" height="797" alt="image" src="https://github.com/user-attachments/assets/3535d1b4-2ef2-450b-bbfe-61e2c08cff03" />
</p>

<br>
<h2>Executable Summary</h2>
<p>In an era dominated by targeted <b>Business Email Compromise (BEC)</b> and sophisticated social engineering, traditional secure email gateways frequently fall short against zero-day phishing infrastructure. This production-ready security engineering solution addresses this gap by combining lower-level cryptographic header verification, global threat intelligence syndication via the <b>VirusTotal API v3</b>, and advanced semantic reasoning using Google’s <b>gemini-2.5-flash</b> model.</p>
<p>By running a localized file discovery script, the tool automatically ingests suspicious emails, verifies routing alignment, checks URL reputations, and generates real-time defensive remediation plans. The implementation shifts security workflows from manual, disconnected validation checks to an automated, cognitive triage asset designed to contain advanced email threats at machine speed.</p>

<br>
<h2>Objective</h2>
<p>The primary objective of this project is to eliminate alert fatigue and slash the <b>Mean Time to Resolution (MTTR)</b> for suspicious emails entering enterprise environments. By programmatically standardizing the initial collection and parsing of complex email components, the application extracts critical <b>indicators of compromise (IOCs)</b> such as source IPs, active hyperlinks, and protocol alignment markers <b>(SPF/DKIM/DMARC)</b>.</p>
<p>The system then feeds this extracted telemetry into a tightly constrained <b>Large Language Model (LLM)</b> configuration to provide security operations with immediate behavioral context and actionable hardening playbooks.</p> 
<p>Ultimately, this engine aims to operationalize advanced cognitive AI inside defensive workflows, changing how incident responders isolate corporate infrastructure from weaponized incoming content.</p>

<br>
<h2>Step-by-Step Guide</h2>
<h3>Pre-requisites</h3>
<ul>
  <li><b>Operating System:</b> Linux Environment (Fully optimized and tested on Kali Linux CLI)</li>
  <li><b>Runtime Core:</b> Python 3.12+ environment</li>
  <li><b>Access Control:</b> A valid API Key from Google AI Studio and VirusTotal</li>
</ul>

<h3>Installation Setup</h3>
<h4>1. Google Gemini API Key Acquisition</h4>
  <p>You must first acquire an operational <b>API Key</b> from the <b>Google Gemini Developer</b> portal. Once obtained, open your local <b>ai-email-analyzer.py</b> script, locate the dedicated configuration block, and replace the placeholder text with your real key:</p>

    # =========================================================================
    # 🔑 ENTERPRISE API CONFIGURATION
    # =========================================================================
    GEMINI_API_KEY = "YOUR_ACQUIRED_API_KEY_HERE"
    VIRUSTOTAL_API_KEY = "YOUR_ACQUIRED_API_KEY_HERE"
    # =========================================================================

 <br>
<h4>2. Update the System Packages</h4>
<p>Synchronize the local package repository index to ensure system references are fresh, and install the native Python package manager and isolated virtual environment creator tools:</p>

    sudo apt update && sudo apt install python3-pip python3-venv -y

<br>
<h4>3. Navigate to Your Project Directory</h4>
<p>Change your active shell terminal location to the target folder where you have saved the script components (for example, your local Downloads folder):</p>

    cd ~/Downloads

<br>
<h4>4. Prepare the Email Material (<i>email_to_analyze.txt</i)</h4>
<p>The triage engine is designed to parse raw email infrastructure data directly out of a companion text asset. In your email client (e.g., Gmail), click on the vertical three dots in the upper-right corner of the target email panel, select "<b>Show original</b>", and click "<b>Copy to clipboard</b>". Create a new file named <i>email_to_analyze.txt</i> inside the same folder as your script (<b>~/Downloads/</b>), paste the raw content inside, and save it.</p>

<br>
<h4>5. Build and Initialize an Isolated Virtual Environment</h4>
<p>Kali Linux enforces <b>PEP 668 (Externally Managed Environments)</b> as a defensive control to prevent third-party library conflicts from breaking system penetration testing tools. Securely bypass this constraint by spinning up a sandboxed environment named <b>>gemini-env</b and activating it:</p>

    python3 -m venv gemini-env
    source gemini-env/bin/activate

<p><i>(Once activated, your terminal shell prompt prefix will visually change to show (<b>gemini-env</b>), verifying that all subsequent Python packages remain completely isolated within this directory).</i></p>

<br>
<h4>6. Install the Google GenAI SDK</h4>
<p>Execute the Python dependency manager inside the active virtual session to pull the official cloud AI communication SDK package:</p>

    pip install google-genai
<br>
<h4>7. Execute Your Script</h4>
<p>Launch the upgraded, AI-integrated password generator wrapper to begin production operation:</p>

    python3 ai-email-analyzer.py

<br>
<h3>⚠️ Quick Tips for Future Sessions ⚠️</h3>
<ul>
  <li><b>Resuming Lab Work:</b> When closing or restarting your Kali Linux Virtual Machine, you do not need to rerun the installation steps. Simply move to your workspace and re-activate the virtual sandbox:</li>
  
     cd ~/Downloads
     source gemini-env/bin/activate
     python3 ai-email-analyzer.py
     
  <br><li><b>Exiting the Sandbox:</b> When your tasks conclude, and you need to pivot your terminal back to standard global operating system instructions, drop out of the environment stack cleanly by running:</li>

    deactivate

  <br><li><b>Fix the Virtual Environment & Run the Script</b>: Since you are inside <b>~/Downloads/</b>, let's initialize and activate the virtual environment right inside this directory to keep everything perfectly contained.</li> 
  <br>Run these exact commands in your terminal:

    # 1. Create the isolated virtual environment inside this folder
    python3 -m venv gemini-env

    # 2. Activate it (Notice your prompt will change to include "(gemini-env)")
    source gemini-env/bin/activate

    # 3. Install the official Google GenAI SDK inside your active sandbox
    pip install google-genai

    # 4. Now execute your script safely
    python3 ai-email-analyzer.py
</ul>

<br>
<h2>How this project helps the Organization or Company</h2>
<p>This project helps organizations establish a unified, robust first line of defense against targeted electronic fraud, drastically shrinking the exposure window during active campaigns. By replacing slow, human-driven spreadsheet analysis with structured AI-assisted validation, the organization can scale its defensive response automatically across thousands of daily employee submissions without adding headcount</p>
<p>This programmatic workflow prevents system engineers from missing subtle, hidden email header mismatches that lead to ransomware execution. By automatically generating immediate incident containment blueprints, the business can rapidly enforce perimeter blocks, lower security operations overhead, and prevent brand damage from email impersonation attacks.</p>

<br>
<h2>How this project helps the SOC Analyst</h2>
<p>For the frontline Security Operations Center (SOC) Analyst, this tool serves as a force multiplier that eliminates repetitive triage and simplifies deep forensic auditing. Instead of manually inspecting header formats, calculating URL hashes, tracking down base64 strings, and querying separate OSINT tabs, the analyst gets a comprehensive, unified telemetry report directly in their console.</p>
<p>The integrated cognitive layer provides instant context on the psychological angles used in the email, enabling Tier 1 and Tier 2 responders to spot sophisticated social engineering trends early. By delivering a prioritized risk matrix and clear remediation instructions, the application removes guesswork, mitigates operational stress, and allows modern defenders to focus on threat hunting and strategic environment hardening.</p>
