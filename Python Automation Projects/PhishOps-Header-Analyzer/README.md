<h1>PhishOps Mail Header Analyzer</h1>
<p>A high-performance, privacy-centric Mail Header Analyzer (MHA) engineered for Security Operations Center (SOC) environments and Incident Responders. This automation tool locally processes raw `RFC 822` email headers, maps tracking assets, correlates chronological transit server hop pipelines with absolute UTC delta timestamps, and evaluates underlying security gateway mechanics.</p>

<h2>Executable Preview</h2>
<p><img width="476" height="621" alt="image" src="https://github.com/user-attachments/assets/b76baf75-ed52-45fd-ad15-a0cb117ff7e3" />
</p>

<br>
<h2>Executive Summary</h2>
<p>Manual verification of raw email envelopes during phishing triage is an error-prone task for security operations. In contrast, cloud-based public header analysis utilities pose severe data privacy challenges, risking the exposure of sensitive internal network metadata or corporate communication paths to third-party vendors.</p>
<p>PhishOps Mail Header Analyzer eliminates this operational dilemma. It acts as a locally hosted, lightweight defensive triage component that reads unstructured tracking headers, standardizes inconsistent temporal data, flags immediate impersonation indicators, and neatly categorizes vendor-specific tracking matrix elements—guaranteed to preserve 100% data sovereignty.</p>

<br>
<h2>Objective</h2>
<p>The core objective of this project is to automate the forensic extraction and timeline mapping of electronic mail metadata streams. By parsing raw text streams directly within a local runtime environment, the engine converts convoluted, out-of-order Received: headers into a sequential, human-readable audit trail that accurately measures routing delays and checks protocol signatures (<b>SPF</b>, <b>DKIM</b>, <b>DMARC</b>) for evidence of tampering.</p>

<br>
<h2>Organizational Value</h2>
<ul>
  <li><b>Zero-Leak Threat Intelligence:</b> Ensures that high-value indicators of compromise (IoCs), internal IP schema, and confidential recipient identities are never submitted to public scanning portals.</li>
  <li><b>Reduction in Mean Time to Resolution (MTTR):</b> Decreases the analyst verification window from several minutes of manual parsing to a sub-second, single-command automated output.</li>
  <li><b>Regulatory Compliance Realization:</b> Aligns defensive alert response handling directly with strict corporate compliance protocols, including GDPR, HIPAA, and PCI-DSS, by maintaining rigorous data control bounds.</li>
</ul>

<br>
<h2>Step-by-Step Guide</h2>
<h3>Pre-requisites</h3>
<u>
  <li>Python 3.7+ installed on the local system.</li>
  <li>A native terminal program capable of processing basic ASCII text layouts (e.g., Git Bash, PowerShell, Linux Bash, macOS Terminal).</li>
  <li>Standard standard library modules (<b>re</b>, <b>os</b>, <b>email</b>, <b>datetime</b>) which are bundled natively with standard Python packages (no external pip dependencies needed).</li>
</u>

<h3>Installation Setup</h3>
<ol>
  <li>Clone the Repository</li>
  
  <li>Initialize the Workspace Environment:<br>
  Run the application once to build the text pipeline wrapper automatically:</li>

    python mha.py

<p><b>NOTE:</b> If <b>email_input.txt</b> is missing from the directory, the engine will gracefully catch the exception, create the target file automatically, and pause execution.</p>
  <li>Stage and Ingest the Payload:<br> Open the newly generated <b>email_input.txt file</b>, paste the complete raw text headers extracted from your suspicious email asset, and save the document.</li>
  <li>Execute the mail header analysis engine:</li>

    python mha.py
</ol>

<br>
<h2>How This Project Helps the Organization or Company</h2>
<p>This utility enhances corporate email defenses by implementing a deterministic verification gate. Rather than relying on disparate monitoring tools or end-user guesswork, the organization receives standardized, verifiable reporting whenever a phishing campaign hits internal mail servers. By programmatically evaluating the alignment between visible addresses (<b>From:</b>) and return pathways (<b>Return-Path:</b>), it automatically blocks domain spoofing vectors that target executives and critical supply-chain communication channels.</p>

<br>
<h2>How This Project Helps the SOC Analyst</h2>
<p>As an incident response utility, this script acts as a powerful asset for a Tier 1 / Tier 2 SOC Analyst:</p>
<u>
  <li><b>Automated Transit Routing Normalization:</b> Eliminates the exhausting task of manually matching multi-region server offsets. The script automatically converts varied server times into standard UTC values, allowing analysts to instantly spot intentional delivery delays or malicious middleman routing.</li>
  <li><b>Contextual Category Matrix Isolation:</b> Isolates platform markers like Mailgun assets, Microsoft exchange transport actions, or internal Google distribution clusters into structured terminal frames, instantly highlighting rogue infrastructure.</li>
  <li><b>Clean, Legible Presentation Layer:</b> Replaces thousands of lines of cluttered email header strings with a clean, scannable console report featuring bolded category fields, giving analysts the clear visibility needed to make confident, high-pressure triage decisions.</li>
</u>





