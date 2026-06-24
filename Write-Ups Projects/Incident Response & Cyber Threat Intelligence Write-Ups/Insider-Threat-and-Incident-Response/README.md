<h1>Insider Threat & LOLBin Analysis: Incident Response Investigation via Splunk</h1>

<br>
<h2>Executive Summary</h2>
<p>During a routine security assessment, a client's Intrusion Detection System (IDS) flagged anomalous network activity originating from the Human Resources (HR) logical segment. Initial alerts suggested local host compromise, indicated by the unauthorized execution of network discovery utilities and persistence mechanisms. Due to aggressive log rotation and resource constraints, forensics was restricted to host-centric Windows Event Logs (Event ID 4688: Process Creation)</p>
<p>These logs were centralized and ingested into a SIEM (Splunk) platform for historical analysis. A thorough timeline reconstruction uncovered an insider threat vector via an imposter account, alongside an external exploitation chain involving Living-off-the-Land Binaries (LOLBins) used to download an unauthorized second-stage payload. The affected assets were successfully identified for isolation and remediation.</p>
