<h1>Insider Threat & LOLBin Analysis: Incident Response Investigation via Splunk</h1>

<br>
<h2>Executive Summary</h2>
<p>During a routine security assessment, a client's <b>Intrusion Detection System (IDS)</b> flagged anomalous network activity originating from the <b>Human Resources (HR)</b> logical segment. Initial alerts suggested local host compromise, indicated by the unauthorized execution of network discovery utilities and persistence mechanisms. Due to aggressive log rotation and resource constraints, forensics was restricted to host-centric <b>Windows Event Logs (Event ID 4688: Process Creation)</b>.</p>
<p>These logs were centralized and ingested into a <b>SIEM (Splunk)</b> platform for historical analysis. A thorough timeline reconstruction uncovered an insider threat vector via an imposter account, along with an external exploitation chain involving <b>Living-off-the-Land Binaries (LOLBins)</b> to download an unauthorized second-stage payload. The affected assets were successfully identified for isolation and remediation.</p>
