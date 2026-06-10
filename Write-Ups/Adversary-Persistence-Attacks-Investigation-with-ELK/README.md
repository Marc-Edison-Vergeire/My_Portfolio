<h1>Anatomy of a Breach: Analyzing and Investigating Adversary Persistence and Multi-Stage Spear-Phishing Attacks in Enterprise Networks with ELK Stack Analytics</h1>

<br>
<h2>Executive Summary</h2>
<p>During a recent targeted cyber campaign, an advanced persistent threat (APT) actor successfully compromised an enterprise network belonging to a logistics company through a highly sophisticated, multi-stage attack chain. The intrusion initiated with a spear-phishing email targeting executive leadership, which deployed a malicious HTML Application (<b>.hta</b>) payload via <b>mshta.exe</b>. This dropper established command-and-control (C2) communication and secured persistence by scheduling malicious PowerShell tasks. Leveraging advanced post-exploitation techniques, the adversary executed a User Account Control (<b>UAC</b>) bypass via <b>fodhelper.exe</b> to elevate privileges to local administrator, subsequently dumping local credentials using Mimikatz. The attacker then moved laterally across the network to administrative endpoints and targeted the Domain Controller via a DCSync attack, ultimately aiming to deploy ransomware. Using Sysmon telemetry ingested into an ELK (Elasticsearch, Logstash, Kibana) stack, security analysts successfully triaged the alerts, mapped the adversary's tactics to the MITRE ATT&CK framework, and reconstructed the chronological timeline of the breach to ensure complete containment and remediation.</p>

<br>
<h2>Objective</h2>
<p>The primary objective of this case study is to demonstrate advanced security operations center (SOC) triage, threat hunting, and incident reconstruction capabilities within an enterprise ELK (Elasticsearch, Logstash, Kibana) environment. By systematically analyzing complex telemetry, this investigation aims to uncover the full lifecycle of a multi-stage threat actor campaign—spanning initial access via defense evasion, persistence mechanisms, local privilege escalation, and lateral movement leading to Active Directory domain compromise. Ultimately, this analysis serves to validate proficiency in translating raw log data into actionable threat intelligence, mapping adversary behaviors to the MITRE ATT&CK framework, and delivering executive-ready technical findings essential for effective incident containment and remediation.</p>

<br>
<h2>Scenario</h2>
<p>Recognizing the need to fortify its defenses against persistent digital threats, a logistics company onboarded a Managed Security Service Provider (MSSP) to oversee its Security Operations Center (SOC). Despite these enhanced monitoring capabilities, an advanced threat actor successfully bypassed the organization's initial perimeter defenses, covertly compromising an employee's account to establish an undetected foothold. Leveraging this authenticated internal access to maximize perceived legitimacy, the adversary launched a targeted, high-importance spear-phishing campaign directed at the Chief Executive Officer (CEO), masquerading as the Chief Finance Officer regarding an urgent financial matter. Despite initial skepticism, the executive opened the malicious attachment. When no immediate visual payload executed, the CEO proactively forwarded the suspicious email to the internal security team. This crucial user report served as the initial trigger for the SOC team to launch a comprehensive incident response investigation, utilizing enterprise SIEM analytics to uncover a deeply embedded, multi-stage attack chain.</p>

<br>
<h2>Skills Learned</h2>
<ul>
  <li><b>Enterprise SIEM Triage & Log Analysis: </b>Developed advanced proficiency in using the ELK (Elasticsearch, Logstash, Kibana) stack to ingest, filter, and query complex Sysmon telemetry to trace threat actor activity.</li>
  <li><b>Adversary Behavior Mapping (MITRE ATT&CK): </b>Mastered the ability to map raw, technical artifacts and process executions to standardized tactical frameworks, tracking the adversary from Initial Access down to Impact.</li>
  <li><b>Endpoint Telemetry Interpretation: </b>Gained deep technical insight into Windows process forensics, specifically identifying malicious parent-child process relationships involving native binaries like <b>mshta.exe</b>, <b>xcopy.exe</b>, and <b>rundll32.exe</b>.</li>
  <li><b>Advanced TTP Detection: </b>Developed specialized knowledge in identifying sophisticated post-exploitation maneuvers, including User Account Control (UAC) bypass mechanisms via <b>fodhelper.exe</b> and credential dumping techniques.</li>
  <li><b>Active Directory Defense & Threat Hunting: </b>Enhanced understanding of enterprise network exploitation vectors by identifying lateral movement patterns and detecting critical Active Directory attacks such as DCSync.</li>
  <li><b>Chronological Incident Reconstruction: </b>Refined the ability to correlate disparate host and network events into a cohesive, timeline-driven incident response narrative essential for containment and executive reporting.</li>
</ul>

<br>
<h2>Tools Used</h2>
<ul>
  <li><b>ELK Stack (Elasticsearch, Logstash, Kibana):</b> Utilized as the primary Security Information and Event Management (SIEM) platform to centralize visibility, execute deep-dive forensic searches, and visualize the entirety of the multi-stage attack lifecycle.</li>
  <li><b>Kibana Query Language (KQL):</b> Applied extensively to build structured search strings, isolate malicious process executions, and track lateral movement across enterprise data logs.</li>
</ul>

<br>
<h2>Artifacts Investigated</h2>
<ul>
  <li><b>Malicious HTML Application (.hta): </b>The initial stage-1 file dropped via the spear-phishing email, which executed via the native Windows utility <b>mshta.exe</b> (PID 6392) to kickstart the infection chain.</li>
  <li><b>review.dat: </b>A malicious payload dropped into the user's local Temp directory using <b>xcopy.exe</b>, serving as the primary dropper executed via <b>rundll32.exe</b>.</li>
  <li><b>Scheduled Task ("Review"): </b>A persistence mechanism established by the adversary using PowerShell to ensure continuous access to the compromised endpoint.</li>
  <li><b>Malicious External IP & C2 Infrastructure: </b>Outbound network connections over port 80 initiated by the malicious payload to establish a command-and-control communication channel.</li>
  <li><b>fodhelper.exe Execution Logs: </b>System artifacts indicating a User Account Control (UAC) bypass, allowing the threat actor to silently elevate their privileges to local administrator.</li>
  <li><b>Mimikatz Binary & Credential Dumps: </b>Artifacts demonstrating the retrieval and execution of credential-dumping tools to harvest local hashes for further network exploitation.</li>
</ul>

<br>
<h2>Findings</h2>
<h3>Phase 1: Initial Triage & Execution Tracking</h3>
<p>Upon receiving the phishing email report, I, as a SOC Analyst, investigated the workstation of the CEO. During this activity, I discovered the email attachment in the downloads folder.</p>
<p><img width="975" height="188" alt="image" src="https://github.com/user-attachments/assets/92c2987f-6c7f-444a-b387-7ba077a7b531" />
</p>
<p>In addition, I also observed a file inside the ISO payload, as shown in the image below.</p>
<p><img width="975" height="367" alt="image" src="https://github.com/user-attachments/assets/4f16be2e-d460-4887-92c6-97709cd2412c" />
</p>
<p>The incident occurred between <b>August 29 and August 30, 2023</b>. Given the initial findings, I am tasked to analyze, investigate, and assess the impact of the compromise.</p>
<p>
I opened the Elastic and presumed that the incident occurred between <b>August 29</b> and <b>August 30, 2023</b>.
</p>
<p><img width="975" height="349" alt="image" src="https://github.com/user-attachments/assets/2decce5e-946c-4f03-9bb5-c06c966c7285" />
</p>
<p>I input the name of the email attachment (<b>*ProjectFinancialSummary_Q3.pdf*</b>) from the downloads folder of the victim in the free text search bar of Elastic, and it showed up; however, I need to investigate the PID of the process that executed the initial stage 1 payload. I filtered the available process IDs, such as <b>process.parent.id</b>, <b>process.command_line</b> and <b>process.pid</b> to make it more easier.</p>
<p><img width="975" height="348" alt="image" src="https://github.com/user-attachments/assets/5f818119-216a-466a-996a-5e6678f1003e" />
</p>
<p>As a result, the PID of the process is <b>6392</b>.</p>
<p><img width="975" height="350" alt="image" src="https://github.com/user-attachments/assets/21da3037-c184-4863-bd36-a9034633c9ba" />
</p>
<p>Further investigation, the stage 1 payload attempted to implant a file to another location, so, I located the full command-line value of this execution by entering the “<b>mshta.exe</b>” command in the search bar, and found out that the command-line was:</p>

    C:\Windows\System32\xcopy.exe" /s /i /e /h D:\review.dat C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat

<p><img width="975" height="349" alt="image" src="https://github.com/user-attachments/assets/166aa9ec-6ecd-4e6a-9d50-bf808a8a6e49" />
</p>
<p>I analyzed and filter in the search bar using “<b>review.dat</b>” to investigate if the implanted file was eventually used and executed by the stage 1 payload, and found out that the full command-line value of the execution was:</p>

    C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer

<p><img width="975" height="348" alt="image" src="https://github.com/user-attachments/assets/1456c987-f61f-482d-99d4-053e13d06092" />
</p>
<p>Based from the previous result, I noticed that the stage 1 payload established a persistence mechanism. The name of the scheduled task created by the malicious script is <b>Review</b>.</p>
<p><img width="975" height="362" alt="image" src="https://github.com/user-attachments/assets/c1b787bd-6358-46de-b19b-069e13d8e8f7" />
</p>

<br>
<h3>Phase 2: Persistence & Command-and-Control (C2) Establishment</h3>
<p>Now, based on my investigation, the execution of the implanted file inside the machine has initiated a potential command-and-control (<b>C2</b>) connection, and found out that the IP is <b>165.232.170.151</b> and the port number is <b>80</b>.</p>
<p><img width="975" height="362" alt="image" src="https://github.com/user-attachments/assets/d3645b82-7cfc-4cb6-84aa-fcd227b487f4" />
</p>
<p>After I identified the IP address and the port number of the destination, the attacker has discovered that the current access is a local administrator. In addition, the name of the process used by the attacker to execute a UAC bypass is <b>fodhelper</b>.</p>
<p><img width="975" height="362" alt="image" src="https://github.com/user-attachments/assets/0f96fd74-aa8f-4b9e-90a4-23091bd0056c" />
</p>

<br>
<h3>Phase 3: Privilege Escalation & Credential Harvesting</h3>
<p>Having a high privilege machine access, the attacker attempted to dump the credentials inside the machine. By entering <b>*github*</b> command inside the search bar, I investigated further and the GitHub link used by the attacker to download a tool for credential dumping is:</p>

    https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip

<p><img width="975" height="357" alt="image" src="https://github.com/user-attachments/assets/aa597971-bd32-4d46-804d-23a11fe9c42e" />
</p>
<p>After the attacker successfully dumping the credentials inside the machine of the CEO, I identified that the attacker used the credentials to gain access to another machine (lateral movement). I investigated and found out that the username is <b>itadmin</b> with the hash value of <b>F84769D250EB95EB2D7D8B4A1C5613F2</b> of the new credential pair by using and filtering the previous result, which is the <b>mimikatz</b>, combined with the CEO’s name.</p>

<br>
<h3>Phase 4: Lateral Movement & Network Enumeration</h3>
<p>Since the attacker used the new username, which is <b>itadmin</b>, I assumed that the attacker gained access in one of the workstation in the IT department, and maybe attempted to enumerate accessible file shares. I filtered “<b>IT</b> AND <b>Files</b> ” to investigate and analyze if my assumptions are correct. So, I found out that the name of the file accessed by the attacker from a remote share is <b>IT_Automation.ps1</b>.</p>
<p><img width="975" height="350" alt="image" src="https://github.com/user-attachments/assets/86a083d7-a24d-4d12-ad1e-bafb466f2b1f" />
</p>
<p>After getting the contents of the remote file, the attacker used the new credentials to move laterally. I input <b>*credential*</b> command in the search bar, in order to produce the potential credentials that I need to investigate through analyzing the command-lines. The new credentials is <b>QUICKLOGISTICS\allan.smith</b> with the password or <b>Tr!ckyP@ssw0rd987</b>.</p>
<p><img width="975" height="350" alt="image" src="https://github.com/user-attachments/assets/ba7358bc-5c0d-4df3-9f50-c36e6c32b821" />
</p>
<p>Using the same result, I analyzed and found out that the hostname of the attacker’s lab machine used for its lateral movement attempt is <b>WKSTN-1327</b>.</p>
<p><img width="975" height="350" alt="image" src="https://github.com/user-attachments/assets/d50d6a88-5bcc-4a46-98a5-4d1a667bea45" />
</p>
<p>Using the malicious command executed by the attacker from the first machine (<b>host.hostname: WKSTN-1327</b>) to move laterally, I investigated and found out that the parent process name of the malicious command executed on the second compromised machine is <b>wsmprovhost.exe</b>. In addition for filtering the command <b>host.hostname: WKSTN-1327</b> in the search bar, I added another command, which is the <b>winlog.event_id: 1</b>, because it is the process of creation events from the second machine involved in the lateral movement.</p>
<p><img width="975" height="349" alt="image" src="https://github.com/user-attachments/assets/b997bdb9-c131-40a6-9bf3-993bd77cf89b" />
</p>

<br>
<h3>Phase 5: Domain Compromise & Ransomware Staging</h3>
<p>After that, the attacker then dumped the hashes into this second machine. I investigated and found out that the username and hash of the newly dumped credentials are <b>administrator</b>with the hash of <b> 00f80f2538dcb54e7adc715c0e7091ec</b>. I filtered the search bar with <b>mimikatz</b> because it was shown earlier in this result.</p>
<p><img width="975" height="349" alt="image" src="https://github.com/user-attachments/assets/e0e5c770-ab40-412b-91b7-af06240a578d" />
</p>
<p>After gaining access to the domain controller, the attacker attempted to dump the hashes via a DCSync attack. Aside from the administrator account, the account the attacker dumped is <b>backupda</b>.</p>
<p><img width="975" height="350" alt="image" src="https://github.com/user-attachments/assets/5b80b3ad-c0a7-4cb4-bdac-29a81d53dee3" />
</p>
<p>Lastly, after dumping the hashes, the attacker attempted to download another remote file to execute ransomware. Based on my investigation, I entered “<b>*ransom* AND user.name: Administrator</b>” and found out that the link used by the attacker to download the ransomware binary is:</p>

        http://ff.sillytechninja.io/ransomboogey.exe

<p><img width="975" height="351" alt="image" src="https://github.com/user-attachments/assets/26aeaec7-92ae-431e-b47b-b2ca59c04993" />
</p>


<br>
<h2>MITRE ATT&CK Mapping</h2>
<ul>
  <li><b>Initial Access (T1566 - Spear-phishing Attachment): </b>The adversary gained an initial foothold in the organization by sending a targeted, high-importance email containing a malicious, masqueraded attachment inside an ISO container.</li>
  <li><b>Execution (T1218.005 - Signed Binary Proxy Execution: Mshta): </b>The attacker leveraged native Windows system utilities to execute malicious scripts, utilizing <b>mshta.exe</b> (PID 6392) to process the initial stage-1 payload.</li>
  <li><b>Persistence (T1053.005 - Scheduled Task/Job: Scheduled Task): </b>To maintain long-term access and survive system reboots, the threat actor registered an unauthorized persistence mechanism named <b>"Review"</b> via PowerShell.</li>
  <li><b>Defense Evasion (T1548.002 - Abuse Elevation Control Mechanism: Bypass User Account Control): </b>The adversary silently elevated their system privileges without triggering security warnings by exploiting a native Windows binary, executing a UAC bypass via <b>fodhelper.exe</b>.</li>
  <li><b>Credential Access (T1003.001 - OS Credential Dumping: LSASS Memory): </b>Operating with elevated local administrator rights, the attacker downloaded and executed Mimikatz from a remote repository to harvest plaintext credentials and NTLM hashes.</li>
  <li><b>Lateral Movement (T1021.006 - Remote Services: Windows Remote Management): </b>The threat actor used stolen administrative credentials (<b>itadmin</b>) to pivot across the internal network, abusing WinRM services (<b>wsmprovhost.exe</b>) to execute commands on secondary workstations.</li>
  <li><b>Impact (T1486 - Data Encrypted for Impact): </b>In the final stage of the attack lifecycle, the adversary attempted to achieve their ultimate objective by staging and pulling down a remote ransomware binary (<b>ransomboogey.exe</b>) to encrypt enterprise data.</li>
</ul>

<br>
<h2>Indicators of Compromise (IoCs)</h2>
<ul>
  <li><b>Network Indicators</b></li>
  <ul>
    <li><b>165.232.170.151 (Malicious IPv4 Address): </b>Identified as the external command-and-control (C2) server infrastructure utilized by the adversary for outbound beaconing and remote command execution over port 80.</li>
    <li><b>ff.sillytechninja.io (Malicious Domain): </b>The external host domain used by the threat actor to stage and distribute the final-stage ransomware payload (<b>ransomboogey.exe</b>).</li>
  </ul>
  <br>
  <li><b>Host & File Indicators</b></li>
  <ul>
    <li><b>ProjectFinancialSummary_Q3.pdf (Malicious Attachment Name): </b>The masqueraded initial access payload packaged inside a rogue ISO container used to lure the executive into triggering the infection chain.</li>
    <li><b>review.dat (Malicious Dropper File): </b>A secondary malicious file implanted into the local user Temp directory via <b>xcopy.exe</b> and subsequently compiled and executed using <b>rundll32.exe</b>.</li>
    <li><b>F84769D250EB95EB2D7D8B4A1C5613F2 (NTLM Hash): </b>The compromised credential hash extracted via local memory dumping for the administrative service account (itadmin), which was leveraged for internal lateral movement.</li>
    <li><b>00f80f2538dcb54e7adc715c0e7091ec (NTLM Hash):</b>The high-privilege domain administrator hash harvested by the adversary to execute the DCSync directory replication attack on the Domain Controller.</li>
    <li><b>ransomboogey.exe (Malicious Binary):</b>The malicious encryption executable targeted for download in the final phase of the attack lifecycle to achieve data encryption for impact.</li>
  </ul>
</ul>

<br>
<h2>Lessons Learned</h2>
<p>This incident highlights the critical necessity of an interconnected, defense-in-depth architecture to mitigate complex, multi-stage adversary campaigns.</p>
<p>First, while perimeter filters failed to block the initial spear-phishing email, the latency between the execution of the initial payload and the final ransomware staging underscores the vital importance of continuous host visibility; establishing robust endpoint detection and response (EDR) solutions alongside centralized SIEM logging is non-negotiable for detecting living-off-the-land (<b>LOL</b>) techniques such as <b>mshta.exe</b> and <b>fodhelper.exe</b> abuse. </p>
<p>Second, the threat actor's rapid progression from local administrator to domain controller compromise exposes a critical vulnerability in credential hygiene and Active Directory architecture. To prevent similar lateral movement and directory replication threats, the enterprise must enforce the principle of least privilege, severely restrict local administrator cached credentials, implement strict network segmentation to isolate administrative service accounts, and block unauthorized outbound communication over port 80 to known unrated or malicious IP infrastructure. </p>
<p>Finally, while the executive's proactive submission of the suspicious email served as a vital initial trigger for the security team, ongoing, simulation-based security awareness training must be reinforced to ensure users recognize the inherent dangers of interacting with unverified attachments, transforming the human element into a more resilient first line of organizational defense.</p>

<br>
<h2>Recommendations</h2>
<p>To effectively mitigate the risk of future multi-stage network intrusions and safeguard the enterprise against advanced persistent threat actors, a comprehensive hardening strategy must be implemented across the email, host, and network layers. </p>
<p>First, the organization should deploy robust Endpoint Detection and Response (EDR) solutions alongside strict application whitelisting policies to monitor and restrict the execution of native Windows binaries commonly abused for defense evasion, specifically disabling or auditing the use of <b>mshta.exe</b>, <b>rundll32.exe</b>, and <b>fodhelper.exe</b>. </p>
<p>Second, Active Directory security must be reinforced by enforcing a strict tier-based administrative model, implementing the principle of least privilege, disabling local administrator caching, and applying rigorous monitoring controls over Directory Replication Service (DRS) functions to proactively detect unauthorized DCSync attacks. </p>
<p>Furthermore, network-level security should be enhanced by implementing strict internal segmentation to prevent lateral movement between standard workstations and administrative servers, enforcing the use of secure administration protocols like WinRM over HTTPS while restricting its access exclusively to designated jump hosts, and configuring perimeter firewalls to block outbound traffic to untrusted or newly registered external IP addresses. </p>
<p>Finally, email security gateways must be optimized with advanced sandboxing capabilities to quarantine incoming ISO containers and archived file types, which should be paired with continuous, targeted security awareness training to ensure that executive leadership and high-value targets can successfully recognize and report sophisticated spear-phishing attempts before document interaction.</p>

<br>
<h2>References & Acknowledgement</h2>
<p>This incident response case study was conducted using the <b>Boogeyman 3</b> educational environment provided by the <b>TryHackMe</b> platform. All enterprise ELK (Elasticsearch, Logstash, Kibana) logs are artifacts analyzed throughout this report originate from their advanced defensive security training curriculum. This controlled, multi-stage simulation was completed to validate advanced threat hunting capabilities, refine complex log correlation methodologies, and sharpen the practical skills necessary to detect, isolate, and remediate sophisticated adversary campaigns within enterprise production environments.</p>















