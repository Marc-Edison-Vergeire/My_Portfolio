<h1>Phishing Engine with Email Authentication Tool</h1>
<p>A zero-dependency, automated security orchestration and threat intelligence utility built to ingest raw email headers and body text (MIME data), extract indicators of compromise (IoCs), validate core email authentication frameworks, and cross-reference extracted assets against the VirusTotal API v3 endpoint in real time.</p>

<h2>Execution Preview</h2>
<img width="941" height="652" alt="image" src="https://github.com/user-attachments/assets/394d7d42-2b97-4f91-88aa-6edf3f4dab09" />

<h2>Executive Summary</h2>
<p>In modern enterprise environments, phishing remains the number one initial access vector for threat actors. Tier-1 security analysts face significant alert fatigue, frequently spending 10 to 15 minutes per reported email manually parsing text files, interpreting raw headers, and copy-pasting indicators into threat intelligence platforms.</p>
<p>The <b>Phishing Engine with Email Authentication Tool</b> serves as a lightweight, <b>"SOAR-lite"</b> (Security Orchestration, Automation, and Response) pipeline. It bridges the gap between raw data collection and defensive action, bringing immediate clarity to an incident ticket without requiring expensive enterprise licensing.</p>

<h2>Objective</h2>
<p>The primary goal of this project is to eliminate manual overhead and alert fatigue in Security Operations Centers (SOCs) by automating the initial triage phase of suspicious email analysis. This tool safely processes raw email source data to confirm sender authenticity and uncover malicious infrastructure in under two seconds—completely bypassing the need to open or execute untrusted files within a traditional, vulnerable mail client or browser context.</p>

<h2>How It Works</h2>
<p>The engine executes its automated defensive assessment through a sequential four-tier pipeline:
  <ul>
    <li><b>Defensive Ingestion:</b> The script checks its local execution context for an active email asset file. If missing, it builds a placeholder template to prevent script execution crashes and ensure immediate, friction-free deployment.</li>
    <li><b>Protocol Authentication Layer:</b> The system reads raw transport data, parsing Authentication-Results and Received-SPF arrays to determine if the email passed SPF, DKIM, and DMARC checks. This instantly detects exact-domain spoofing and Business Email Compromise (BEC) attempts.</li>
  <li><b>Artifact Extraction & Heuristics:</b> Utilizing specialized regular expressions (Regex), the utility strips the routing path to extract the true originating sender IP address along with all embedded hyperlinks. Concurrently, a behavioral heuristics pass screens the subject and body text for psychological manipulation patterns (e.g., coercion, financial trickery, administrative spoofing).</li>
  <li><b>Threat Intelligence Automation:</b> Extracted URLs are transformed into an unpadded Base64 string format required by the VirusTotal API v3 endpoint. The engine securely queries the global database, returning localized vendor reputations without relying on third-party HTTP libraries like requests.</li>
  </ul>
</p>

<h2>Organizational Value</h2>
<p>By automating the tedious process of text parsing and reputation querying, this tool reduces the Mean Time to Resolution (MTTR) for phishing indicators from minutes to seconds. It provides organizations with a cost-free, easily auditable utility that protects internal teams from accidental browser-based drive-by downloads while accelerating incident response capabilities.</p>

<h2>Step-by-Step Guide</h2>
<h3>Pre-requisites:</h3>
<ul>
  <li><b>Python 3.x Installed:</b> Ensure Python is available on your system path (i.e. VSCode or any Linux VM).</li>
  <li><b>VirusTotal API Key:</b> Register for a free account at <a href="https://www.virustotal.com/" target=_blank>VirusTotal</a> to obtain a developer API key.</li>
</ul>

<h3>Installation Setup</h3>
<ol>
  <li><b>Clone or Save the Code:</b> Save the provided Python script to a local directory as <b>analyzer.py</b> (or any name of your choice).</li>
  <li><b>Configure Your API Key:</b> Open <b>analyzer.py</b>analyzer.py in a text editor or IDE of your choice, locate the configuration block at the top of the file, and input your VirusTotal API key inside the quotation marks:</li>
  
     VIRUSTOTAL_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"

  <li><b>Initialize the Staging Workspace:</b> Open your terminal, navigate to the folder containing your script, and run it once to automatically generate the necessary input staging file:</li>
  
    python analyzer.py

<p><i>The tool will detect that no target email file exists and gracefully generate a blank template file named <b>email_to_analyze.txt</b> in the exact same directory or folder.</i></p>

<li><b>Review the Security Output:</b> The terminal will generate a structured, scannable incident response report detailing the mail profile, authentication posture, extracted IoCs, and their live global security reputation.</li>
</ol>

<h2>How This Project Helps the Organization or Company</h2>
<ul>
  <li><b>Significant Reduction in MTTR (Mean Time to Resolution):</b> During an active, targeted phishing campaign, early containment is critical. Shrinking triage timelines from 15 minutes to under 2 seconds allows defensive teams to implement global blocks or purge malicious mailboxes before an employee interacts with the payload.</li>
  <li><b>Operational Cost Savings:</b> The engine relies entirely on Python's built-in standard library architecture. It contains zero external package dependencies (no pip install required), allowing it to be compiled into a standalone binary and deployed across Windows, macOS, or Linux endpoints without licensing fees, package registry restrictions, or software supply chain risks.</li>
  <li><b>Vendor & Supply Chain Risk Defense:</b> By checking explicit cryptographic alignments via SPF, DKIM, and DMARC headers, the business can immediately track whether partner or vendor identities are being actively spoofed, safeguarding corporate B2B transactions against financial wire fraud.</li>
</ul>

<h2>How This Project Helps the SOC Analyst</h2>
<ul>
  <li><b>Mitigates Critical Workspace Risks:</b> Analysts never have to render complex, malicious HTML messages or open suspicious hyperlinks inside a standard web browser to investigate them. The script extracts data safely as raw text strings, completely isolating the analyst's host operating system from drive-by browser compromises or tracker beacon triggers.</li>
  <li><b>Combats Cognitive Alert Fatigue:</b> Instead of executing multiple separate workflows—such as manually cross-referencing domains on external intelligence sites, reading raw header files line-by-line, and scanning text for behavioral triggers—the analyst receives a single, unified, cleanly formatted command-line dashboard.</li>
  <li><b>Enables Contextual Intelligence Triage:</b> The tool isolates Unrated (<b>❔</b>) resources. This signals to the analyst that a link is completely new and unrecognized globally—a primary characteristic of Newly Registered Domains (NRDs) commonly utilized in sophisticated, highly targeted advanced persistent threat (APT) campaigns. This visibility helps analysts shift their focus toward deeper sandbox analysis when automated tools return an ambiguous rating.</li>
</ul>
