<h1>Insider Threat & LOLBin Analysis: Incident Response Investigation via Splunk</h1>

<br>
<h2>Executive Summary</h2>
<p>During a routine security assessment, a client's <b>Intrusion Detection System (IDS)</b> flagged anomalous network activity originating from the <b>Human Resources (HR)</b> logical segment. Initial alerts suggested local host compromise, indicated by the unauthorized execution of network discovery utilities and persistence mechanisms. Due to aggressive log rotation and resource constraints, forensics was restricted to host-centric <b>Windows Event Logs (Event ID 4688: Process Creation)</b>.</p>
<p>These logs were centralized and ingested into a <b>SIEM (Splunk)</b> platform for historical analysis. A thorough timeline reconstruction uncovered an insider threat vector via an imposter account, along with an external exploitation chain involving <b>Living-off-the-Land Binaries (LOLBins)</b> to download an unauthorized second-stage payload. The affected assets were successfully identified for isolation and remediation.</p>

<br>
<h2>Objective</h2>
<p>The primary objective of this investigation was to conduct a comprehensive threat-hunting exercise within the <b>win_eventlogs</b> index to fully scope the extent of the HR department compromise. This involved isolating anomalous process creation events, identifying the specific threat actors or compromised accounts, mapping the adversarial techniques to the <b>MITRE ATT&CK</b> framework, and extracting actionable <b>Indicators of Compromise (IoCs)</b> to prevent future exploitation across the corporate network.</p>

<br>
<h2>Scenario</h2>
<p>An enterprise network, logically segmented into IT, HR, and Marketing departments, experienced a targeted security incident. The threat hunter was tasked with analyzing a 30-day window of <b>Windows Event ID 4688</b> logs in <b> Splunk</b>. The environment consisted of known, legitimate corporate identities across three business units:</p>
<ul>
  <li><b>IT Department:</b> James, Moin, Katrina</li>
  <br><li><b>HR Department: </b>Haroon, Chris, Diana</li>
  <br><li><b>Marketing Department:</b> Bell, Amelia, Deepak</li>
</ul>
<p>The investigation focused on determining how security controls were bypassed, identifying which valid users were compromised, and tracking the post-exploitation commands executed by the threat actor.</p>

<br>
<h2>Skills Learned</h2>
<ul>
  <li><b>SIEM Log Parsing:</b> Querying, filtering, and structuring unstructured Windows Event Logs within Splunk.</li>
  <br><li><b>Threat Hunting Methodology:</b> Utilizing statistical anomalies (Rare Values) to identify malicious activity buried in high-volume baseline logs.</li>
  <br><li><b>Identity & Access Auditing:</b> Detecting defense evasion techniques, such as typosquatting and account impersonation.</li>
  <br><li><b>LOLBin Analysis:</b> Identifying and deconstructing the abuse of legitimate operating system binaries for malicious purposes.</li>
</ul>

<br>
<h2>Tool Utilized</h2>
<ul>
  <li><b>Splunk Enterprise:</b> Centralized log analysis, statistical aggregation, and event correlation.</li>
</ul>

<br>
<h2>Artifacts</h2>
<ul>
  <li><b>Windows Security Event Logs:</b> Event ID 4688 (Process Creation).</li>
  <li><b>Command Line Arguments:</b> Extracted strings from the <b>CommandLine</b> field detailing attacker execution.</li>
</ul>

<br>
<h2>Findings</h2>
<h3>Phase 1: Ingestion and Baseline Analysis</h3>
<p>The investigation initiated with the ingestion of the <b>win_eventlogs</b> index to establish a baseline of process creation events.</p>

    index=win_eventlogs

<p>Because the incident was reported to have occurred within <b>March 2022</b>, the time picker was restricted to a static range from <b>March 1, 2022</b>, to <b>March 31, 2022</b>. This initial query returned a total volume of <b>13,959 events</b>, creating the baseline dataset for deeper analysis.</p>

<p><img width="802" height="539" alt="image" src="https://github.com/user-attachments/assets/53aa4b68-bec5-4b72-9c47-34128b5ef062" />
</p>
<p><img width="807" height="677" alt="image" src="https://github.com/user-attachments/assets/8a817dea-d7e7-4044-881d-fe2ebf078aa9" />
</p>
<p><img width="726" height="495" alt="image" src="https://github.com/user-attachments/assets/f3a668ca-0a06-4cc1-a7bf-0b079caa31ea" />
</p>
<p><img width="696" height="446" alt="image" src="https://github.com/user-attachments/assets/d0b849bd-310a-4f78-8a47-50a83d305fac" />
</p>

<br>
<h3>Phase 2: Identity Analysis & Imposter Detection</h3>














