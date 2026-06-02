<h1>PassForge-CLI: Cryptographically Secure Password Generation Engine</h1>
<p>A robust, defensively engineered command-line utility powered by Python's native CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) pipeline to generate high-entropy, mathematically unpredictable credentials, tokens, and keys.</p>

<h2>Executable Preview</h2>
<img width="810" height="477" alt="image" src="https://github.com/user-attachments/assets/8e8ee36e-17e0-4af6-9ac9-bc159103e2c9" />

<h2>Executive Summary</h2>
<p>In the cybersecurity landscape, weak or predictable credentials remain an open invitation for credential-stuffing and brute-force attacks. Many entry-level or standard password generators rely on Python's built-in random module, which uses standard pseudo-random algorithms that are mathematically predictable and inherently unsafe for security purposes.</p>

<p><b>PassForge-CLI</b> solves this structural flaw by utilizing true hardware-level entropy systems via Python's native secrets module. It bridges the gap between simple script functionality and enterprise-level defensive requirements, providing an interactive, user-validated terminal engine that allows custom length and complexity scaling without introducing third-party package dependencies.</p>

<h2>Objective</h2>
<p>The primary objective of this project is to give organizations, administrators, and security professionals an offline, completely private environment to engineer elite-tier credentials. By replacing predictable software algorithms with cryptographically secure random generation, this tool eliminates intercept vectors, tracking beacons, or telemetry logging risks associated with online web-based password generators.</p>

<h2>Organizational Value</h2>
<ul>
  <li><b>Zero Supply Chain Vulnerabilities:</b> Built entirely using Python's internal standard library framework. It requires zero external packages (no pip install), eliminating software inventory tracking overhead and third-party code tampering risks.</li>
  <li><b>Strict Privacy Boundary Enforcement:</b> Because the utility runs 100% locally on the host terminal, high-value infrastructure passwords, database strings, and service account tokens are never exposed to the public internet or external web server logs.</li>
  <li><b>Proactive Security Alerting:</b> The script includes built-in compliance warnings. If a user attempts to generate a password beneath the modern industry standard baseline (less than 12 characters), the engine prints a prominent security alert warning them of reduced brute-force resistance.</li>

<h2>Step-by-Step Guide</h2>
<h3>Pre-requisites</h3>
  <ul>
    <li><b>Python 3.x:</b> Ensure Python 3 is installed and configured correctly on your local terminal environment variable path.</li>
  </ul>
</ul>

  <h3>Installation Setup</h3>
  <ul>
    <li><b>Clone or Save the Script:</b> Download or save the core utility source code to your machine as <b>password_gen.py</b>.</li>
    <li><b>Open Terminal Context:</b> Open your preferred command terminal (PowerShell, Command Prompt, or Bash) and navigate to the directory where the file resides:</li>
    
    cd /path/to/your/folder
    
  <li><b>Execute the Utility:</b> Start the interactive generation sequence by running the script command:</li>
  
    python password_gen.py
  
  <li><b>Define Your Scope:</b> Follow the explicit interactive prompts to configure your ideal security posture:</li>

    🔑 Enter desired password length (e.g., 1 to 64+): 24
    🔹 Include Alphabetical Letters? (y/n): y
    🔹 Include Numeric Digits? (y/n): y
    🔹 Include Special Symbols? (y/n): y

  <li><b>Secure Your Credential:</b> The engine will instantly format and output your secure string. Copy the password and store it safely within an authorized enterprise credential vault.</li>
  </ul>

<h2>How This Project Helps the Organization or Company</h2>
<ul>
  <li><b>Hardens Internal Infrastructure Access:</b> Organizations can mandate the use of this tool for setting up secure, local account profiles, database credentials, and temporary fallback access keys, preventing employees from using easily guessable phrases.</li>
  <li><b>Secure API & DevOps Integration:</b> Because it prints raw strings directly to stdout, the logic can easily be automated or called via external deployment shell scripts to generate completely secure API tokens and secrets during continuous deployment configurations.</li>
  <li><b>Eliminates Shadow IT Web Lookups:</b> Employees frequently use Google to find "random password generators." This introduces data leakage risks if those sites log generated values. Deploying this tool internally provides a safe, locally sanctioned alternative.</li>
</ul>

<h2>How This Project Helps the SOC Analyst</h2>
<ul>
  <li><b>Accelerates Incident Response Containment:</b> When an analyst discovers a compromised account during an investigation, they must rotate credentials immediately. PassForge-CLI lets an analyst spin up a 64+ character temporary "break-glass" administrative password in milliseconds without minimized window-switching overhead.</li>
  <li><b>Facilitates Isolated Testing Environments:</b> During malware analysis, digital forensics, or sandbox testing setups, analysts frequently need to provision disposable target accounts. This utility allows for quick creation of compliant strings that keep testing sandboxes secure from cross-contamination.</li>
  <li><b>Guarantees Zero Cryptographic Predictability:</b> Unlike standard scripts that rely on system clock times to seed pseudo-random number generators (which can allow an attacker to mathematically recalculate the password), the CSPRNG backbone guarantees that every string generated is completely immune to time-based derivation attacks.</li>
</ul>
