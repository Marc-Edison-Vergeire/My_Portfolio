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














