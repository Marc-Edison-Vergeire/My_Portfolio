<h1>Project Espresso: Insider Threat and Intellectual Property Exfiltration Investigation</h1>

<br>
<h2>Executive Summary</h2>
<p>During a recent targeted digital forensics engagement, a comprehensive "<b>dead-box</b>" forensic triage was conducted on a confiscated workstation to investigate suspected intellectual property theft and unauthorized data exfiltration by a rogue IT administrator. By performing deep-dive analysis on isolated Windows Registry hives—specifically <b>SYSTEM</b>, <b>SOFTWARE</b>, <b>SAM</b>, <b>NTUSER.DAT</b>, and the other two—the investigation successfully reconstructed the adversary’s execution chain and confirmed malicious intent. Initial analysis identified the exact host parameters and mapped the suspect's network footprint, proving persistent remote access through a commercial VPN provider. Forensic extraction of local Security Account Manager (<b>SAM</b>) data further revealed a critical privilege escalation event, uncovering a stealthily deployed local administrative backdoor configured with a suspicious Relative Identifier (<b>RID 1013</b>) designed to maintain persistent network access.</p>
<p>Defensible evidence of data compromise was definitively established through the analysis of user-specific artifacts. Examination of <b>RecentDocs</b> registry keys proved the suspect directly targeted and accessed highly confidential proprietary data files. Furthermore, an evaluation of <b>WordWheelQuery</b> and <b>UserAssist</b> keys provided a granular timeline of the adversary's pre-operational activity, exposing explicit search queries for network utility tools like <b>netcat</b> alongside recorded execution counts for unauthorized system-indexing software. The resulting forensic timeline provides a legally defensible, end-to-end reconstruction of the insider threat, mapping the trajectory from initial system exploitation and backdoor persistence to the final unauthorized access of sensitive corporate assets.</p>

<br>
<h2>Objective</h2>
<p>The primary objective of this forensic engagement was to conduct a rigorous, offline "<b>dead-box</b>" examination of critical Windows Registry hives to definitively prove or disprove allegations of intellectual property theft and malicious insider activity by a privileged user. Operating under the constraint of a non-live environment, the investigation aimed to locate, extract, and interpret low-level forensic artifacts within the <b>SYSTEM</b>, <b>SOFTWARE</b>, <b>SAM</b>, <b>NTUSER.DAT</b> and the other two hives to establish a legally defensible timeline of adversary behavior. Specifically, the scope of work mandated identifying the suspect workstation's network configuration, uncovering any covert persistence mechanisms or backdoor administrative accounts, and verifying whether proprietary corporate data assets were target-searched, accessed, or staged for exfiltration. Ultimately, the goal was to convert raw registry structures into actionable threat intelligence and structured evidence, providing stakeholders with an airtight verification of the scope of compromise to support subsequent corporate or legal remediation.</p>

<br>
<h2>Scenario</h2>
<p>Jasmine owns <b><i>Coffely</i></b>, a prominent New York coffee shop celebrated city-wide for its unique, proprietary coffee recipes. To safeguard this competitive advantage, the original copies of these highly guarded recipes are exclusively stored on Jasmine's corporate laptop. Last week, James from the IT department was granted access to the device to perform authorized technical repairs; however, subsequent anomalies led to suspicions that he may have illicitly copied the secret recipes onto his own corporate workstation.
Although initial inspection of James's confiscated machine yielded no immediate evidence of the stolen files, the corporate security department successfully extracted critical offline registry hives (<b>SYSTEM</b>, <b>SOFTWARE</b>, <b>SAM</b>, <b>NTUSER.DAT</b>, and other two) to preserve the digital crime scene. As a Security Operations Center (SOC) Analyst, I was formally tasked with conducting a dead-box forensic examination of these registry artifacts. Utilizing advanced registry parsing tools, the primary directive was to reconstruct the suspect's administrative actions, identify hidden persistence mechanisms, and establish definitive forensic proof regarding the presence, tracking, and potential exfiltration of <b><i>Coffely</i></b>'s proprietary data assets.
</p>

<br>
<h2>Skills Learned</h2>
<ul>
  <li><b>Dead-Box Forensics & Registry Hive Parsing: </b>Proficient in the offline extraction, processing, and analytical interpretation of isolated Windows Registry hives without relying on live-system dependencies.</li>
  <li><b>Adversary Persistence Tracking & SAM Analysis: </b>Advanced capability in auditing local Security Account Manager (<b>SAM</b>) structures to uncover privilege escalation, identify hidden administrative backdoors, and correlate Relative Identifiers (<b>RID</b>s) with unauthorized account creation.</li>
  <li><b>User Activity Reconstruction via System Artifacts: </b>Expertise in interrogating forensic key structures—including <b>RecentDocs</b>, <b>UserAssist</b>, and <b>WordWheelQuery</b>—to calculate program execution counts, determine application focus times, and establish proof of target file access.</li>
  <li><b>Network Artifact Attribution: </b>Competent in mapping host identifiers and isolating historical network footprints by extracting DHCP interfaces, network adapter parameters, and historical connection states directly from underlying system keys.</li>
  <li><b>Adversarial Timeline Development: </b>Skilled in converting disparate, low-level registry timestamps into a cohesive, legally defensible chronological timeline that maps an insider threat's end-to-end execution chain.</li>
  <li><b>Forensic Tool Utility: </b>Mastery of specialized open-source and industry-standard forensic triage utilities, specifically Eric Zimmerman's <b>Registry Explorer</b>, to conduct rapid, deep-dive artifact hunting.</li>
</ul>

<br>
<h2>Tools Utilized</h2>
<ul>
  <li><b>Eric Zimmerman's Registry Explorer (GUI): </b>Leveraged as the primary forensic powerhouse to parse, search, and navigate raw, offline registry hives while automatically processing associated transaction logs to ensure data completeness.</li>
  <li><b>Built-in Hex Viewer & Data Interpreter: </b>Utilized directly within the Registry Explorer architecture to decode raw binary payloads, translate <b>ROT13</b>-encoded application strings, and interpret complex Windows 64-bit FILETIME timestamps.</li>
  <li><b>Registry Explorer Bookmark Architecture: </b>Employed to systematically isolate, group, and tag critical forensic keys (such as <b>UserAssist</b> and <b>RecentDocs</b>), accelerating the triage process and streamlining timeline generation.</li>
</ul>

<br>
<h2>Artifacts</h2>
<p>The forensic package delivered for analysis was divided into two distinct logical directories on the analyst workstation, isolating the raw evidence from the court-accepted tools required for deep-dive parsing:</p>
<ul>
  <li><b>EZ Tools Directory: </b>Comprised a specialized suite of Eric Zimmerman's forensic utilities, selected to ensure structural integrity and execution logging while parsing raw binary configurations.</li>
  <li><b>Artifacts Directory:</b>
  <ul>
    <li><b>SYSTEM Hive Asset: </b>Extracted to reconstruct underlying hardware environments, verify the host identity, map active interfaces, and track historical network interface metrics.</li>
    <li><b>SECURITY Hive Asset: </b>Maintained to evaluate local machine-level security structures, system-wide licensing parameters, and macro-level defensive configurations.</li>
    <li><b>SOFTWARE Hive Asset: </b>Interrogated to identify local application footprints, verify the installation parameters of unauthorized tools, and audit system-wide application configurations.</li>
    <li><b>SAM Hive Asset: </b>Analyzed to map local security account structures, determine creation timestamps for default groups, and uncover hidden administrative accounts or backdoor Relative Identifiers (<b>RID</b>s).</li>
    <li><b>NTUSER.DAT Hive Asset:</b>Exploited to reconstruct user-specific behaviors, capture individual file interactions (<b>RecentDocs</b>), track console inputs (<b>RunMRU</b>), and extract application focus times via user execution telemetry.</li>
    <li><b>UsrClass.dat Hive Asset: </b>Extracted to support user-level context by parsing Shellbags and parsing execution artifacts related to unique user interaction and local folder configurations.</li>
  </ul>
  </li>
</ul>

<br>
<h2>Findings</h2>
<h3>Phase 1: Environment Setup & Evidence Ingestion</h3>
<p>This computer is owned by <b>James</b>’ (<b>IT Department</b>) confiscated corporate workstation. It contains two folders; Artifacts folder (which contains the registry Hives to examine) and EZ Tools (which includes all the required tools to analyze the artifacts).</p>
<p>The investigation commenced with a forensically sound ingestion of the isolated evidence files. Using the (Eric Zimmarman’s) Registry Explorer, six raw, offline registry hives (<b>SYSTEM</b>,<b> SECURITY</b>, <b>SOFTWARE</b>, <b>SAM</b>, <b>NTUSER.DAT</b>, and <b>UsrClass.dat</b>)  were unmounted and parsed, automatically replaying associated traction logs to guarantee data preservation and structural integrity.</p>
<p><img width="975" height="858" alt="image" src="https://github.com/user-attachments/assets/22275240-ddc9-4c85-8968-12f1b86d8308" />
</p>
<p>I opened the <b>Registry Explorer</b> to ingest or load up the six (6) artifacts.</p>
<p><img width="746" height="657" alt="image" src="https://github.com/user-attachments/assets/4fb5a468-7a0f-4fb2-ac92-f4607f786d02" />
</p>
<p><img width="975" height="799" alt="image" src="https://github.com/user-attachments/assets/b9216d3e-1621-464e-ac8e-6f28af2408fc" />
</p>
<p>I selected the  <b>File</b> to load up the artifacts.</p>
<p><img width="975" height="403" alt="image" src="https://github.com/user-attachments/assets/e4742d74-1477-43a9-bd74-50e1a01c4d0d" />
</p>
<p><img width="750" height="580" alt="image" src="https://github.com/user-attachments/assets/ca8c099b-ec26-468b-9a51-c2d844aff87f" />
</p>
<p><img width="975" height="398" alt="image" src="https://github.com/user-attachments/assets/06e617da-bdc8-4297-a7b6-0558e853290b" />
</p>

<br>
<h3>Phase 2: Host Identification & Base Baseline Construction</h3>
<p>After loading the artifacts, I investigated the computer name of the machine found in the registry and I found out that the name is <b>JAMES</b>.</p>
<p><img width="975" height="572" alt="image" src="https://github.com/user-attachments/assets/6b14c77c-1db9-4fb5-8e71-da2c5f59f0b4" />
</p>
<p><img width="975" height="642" alt="image" src="https://github.com/user-attachments/assets/a41618fd-eb88-40ff-85d5-bd9a54be2b10" />
</p>
<p>Now, I gathered more detail that the <b>Administrator</b> account created on this machine is on <b>2021-03-17</b> at <b>14:58:48</b>.</p>
<p><img width="975" height="607" alt="image" src="https://github.com/user-attachments/assets/1446ec28-9567-456a-8e01-02462556f38f" />
</p>
<p>Using the same result, the RID (User ID) associated with the <b>Administrator</b> account is <b>500</b>.</p>
<p><img width="975" height="537" alt="image" src="https://github.com/user-attachments/assets/b616eb42-c4cc-4324-84f5-8a6d4ed80c22" />
</p>
<p>Based on my analysis, I found out that there are seven (7) user accounts were observed on this machine.</p>
<p><img width="975" height="537" alt="image" src="https://github.com/user-attachments/assets/102d8610-3a70-4494-848a-34aa12076865" />
</p>

<br>
<h3>Phase 3: Defensive Evasion & Persistence Identification</h3>
<p>Upon investigation, there’s a suspicious account created as a backdoor with <b>RID 1013</b>, and the account name is <b>bdoor</b>.</p>
<p><img width="975" height="537" alt="image" src="https://github.com/user-attachments/assets/4b617ace-4d02-426f-b5d5-b9c8d2b499d4" />
</p>
<p><img width="975" height="506" alt="image" src="https://github.com/user-attachments/assets/57a3a628-667e-4969-a829-557dfe3e64a1" />
</p>
<p>I moved my attention to the network and investigated that the VPN connection this host connected to is <b>ProtonVPN</b> and the first VPN connection observed is on <b>2022-10-12</b> at <b>19:52:36</b>.</p>
<p><img width="975" height="683" alt="image" src="https://github.com/user-attachments/assets/476cfe38-a7e8-474c-9398-079953d25553" />
</p>
<p><img width="975" height="525" alt="image" src="https://github.com/user-attachments/assets/d46fdb21-02fa-4e42-aabe-3202b2e999a6" />
</p>
<p>More on my investigation, there were three shared folders observed on his machine. The path of the third share is <b>C:\RESTRICTED FILES</b>.</p>
<p><img width="975" height="399" alt="image" src="https://github.com/user-attachments/assets/176cbf91-b976-4d6b-82ad-cea9032f7ad1" />
</p>
<p>The last DHCP IP assigned to this host is <b>172.31.2.197</b>.</p>
<p><img width="975" height="433" alt="image" src="https://github.com/user-attachments/assets/5e7fd6c7-4eeb-4eff-8f1d-74db685d4733" />
</p>

<br>
<h3>Phase 4: Evidence of Target File Access (Data Targeting)</h3>
<p>Based on my investigation, the suspect seems to have accessed a file containing the secret coffee recipe and the name of the file is <b>secret-recipe.pdf</b>.</p>
<p><img width="975" height="536" alt="image" src="https://github.com/user-attachments/assets/364eb6fc-0ef8-4d9c-9e8c-5a3b5cdda939" />
</p>
<p>At the same time, the recent text file opened by the suspect is <b>secret-code.txt</b>.</p>
<p><img width="975" height="541" alt="image" src="https://github.com/user-attachments/assets/1bf54794-f9b5-41bd-afe2-1960eccef620" />
</p>

<br>
<h3>Phase 5: Adversarial Capability & Execution Chronology</h3>
<p>Another thing I found out that the suspect executed multiple commands using the Run window, thus, the command was used to enumerate the network interfaces is <b>pnputil /enum-interfaces</b>.</p>
<p><img width="975" height="656" alt="image" src="https://github.com/user-attachments/assets/019b4122-8617-4c47-99fa-3d4f65071e2c" />
</p>
<p><img width="975" height="611" alt="image" src="https://github.com/user-attachments/assets/cabb9068-f34c-44ba-af8e-11ec2f9d5e6b" />
</p>
<p>The user searched for a network utility tool to transfer files using the file explorer, and the name of the tool is <b>netcat</b>.</p>
<p><img width="975" height="623" alt="image" src="https://github.com/user-attachments/assets/783b0bdb-ee8b-4bcb-a464-46bd327875a9" />
</p>
<p><img width="975" height="516" alt="image" src="https://github.com/user-attachments/assets/a1f544f5-e228-4aba-b0a4-9f7f98fdbd25" />
</p>
<p>Upon investigation, I filtered <b>Count</b> to see how many times the <b>Powershell</b> run and I checked the folders, so, assumed the selected folder is the right one because it showed <b>46</b> number of values, which means number of folders inside. After that, I filtered <b>Powershell</b> on the right-side to make it much easier for me to find out. Based on my investigation, the PowerShell executed on this host <b>3 times</b>.</p>
<p><img width="975" height="637" alt="image" src="https://github.com/user-attachments/assets/d33a6211-73c6-41c2-a4a9-1c3b827ab4e5" />
</p>
<p><img width="975" height="583" alt="image" src="https://github.com/user-attachments/assets/b9ca1406-4470-4e9c-b2a0-47ec3a74dca1" />
</p>
<p><img width="975" height="420" alt="image" src="https://github.com/user-attachments/assets/5541c956-0a9b-4f88-989e-01af69121ada" />
</p>
<p>As I analyzed, the suspect also executed a network monitoring tool and with the name is <b>Wireshark</b>.</p>
<p><img width="975" height="401" alt="image" src="https://github.com/user-attachments/assets/99a44b70-e62a-492e-9b60-2a0e2170319b" />
</p>
<p>The Registry Hives also note the amount of time a process is in focus. As I examined the Hives and confirmed that the ProtoVPN executed <b>343</b> seconds. Based on the result on the <b>Focus Time</b>, which is 5 minutes, I convert it into seconds and gave me 300 seconds, plus 43 seconds, which gives me, <b>343</b> seconds. I filtered <b>ProtonVPN</b>, in order for me to find it more faster</p>
<p><img width="975" height="580" alt="image" src="https://github.com/user-attachments/assets/633f1f73-a61c-45c4-bd37-89964a9b0d54" />
</p>
<p><img width="975" height="401" alt="image" src="https://github.com/user-attachments/assets/e2ff4b16-8bac-4146-87c8-be23f7ada55c" />
</p>
<p><img width="975" height="401" alt="image" src="https://github.com/user-attachments/assets/c5a50c93-f401-43e5-b2f7-bed184693f7a" />
</p>
<p>Lastly, using the same result, I filtered <b>Everything.exe</b>, which is a utility used to search for files in a Windows machine. The full path from which <b>Everything.exe</b> was executed is</p> 
          
          C:\Users\Administrator\Downloads\tools\Everything\Everything.exe
<p><img width="975" height="448" alt="image" src="https://github.com/user-attachments/assets/b0469805-6dca-40d1-9c68-7ff2f1a89bff" />
</p>

<br>
<h2>MITRE ATT&CK</h2>
<ul>
  <li><b>Valid Accounts (T1078): </b>Exploited authorized IT administrator privileges to access sensitive corporate assets and perform unauthorized maintenance on the target laptop.</li>
  <li><b>Create Account: Local Account (T1136.001):</b> Generated a hidden local administrative account within the Security Account Manager (<b>SAM</b>) hive to secure persistent access to the network.</li>
  <li><b>Abuse Elevation Control Mechanism (T1548): </b>Manipulated system permissions and utilized the newly created local administrative backdoor (<b>RID 1013</b>) to bypass standard corporate security controls.</li>
  <li><b>Hide Artifacts (T1564): </b>Attempted to conceal the presence of unauthorized utility applications and circumvent local network auditing by routing traffic through a commercial VPN.</li>
  <li><b>Data from Local System (T1119): </b>Located, targeted, and directly accessed proprietary data files (<b>secret-recipe.pdf</b>) stored locally on the compromised corporate machine.</li>
  <li><b>Exfiltration Over Alternative Physical Medium (T1011): </b>Staged and exfiltrated highly guarded intellectual property from the primary device to an unauthorized secondary asset.</li>
</ul>

<br>
<h2>Indicators of Compromised (IoCs)</h2>
<ul>
  <li><b>Host Endpoint Attribution: </b>System configuration identifiers mapped explicitly to host computer name <b>JAMES</b>.</li>
  <li><b>Network Interface Footprint: </b>Last active DHCP network assignment mapped to internal IPv4 address <b>172.31.2.197</b>.</li>
  <li><b>Persistence Backdoor Account: </b>Unauthorized local user account named <b>bdoor</b> provisioned with Relative Identifier <b>RID 1013</b>.</li>
  <li><b>Target Data Compromise: </b>System-tracked user interactions with sensitive target files named <b>secret-recipe.pdf</b> and <b>secret-code.txt</b>.</li>
  <li><b>Network Obfuscation Utility: </b>Execution profile of <b>ProtonVPN</b> capturing an active application focus time of 343 seconds.</li>
  <li><b>Interface Enumeration Command: </b>Local console execution trace of the utility string <b>pnputil /enum-interfaces</b>.</li>
  <li><b>Unauthorized Monitoring Tools: </b>System execution footprint capturing the installation and usage of the network sniffer <b> Wireshark </b>.</li>
  <li><b>Targeted Search Footprint:</b> File Explorer query strings identifying active attempts to locate and deploy the network utility <b>netcat</b>.</li>
  <li><b>Staged Directory Path: </b>Unsanctioned file system indexing executing directly out of the directory path <b>C:\Users\Administrator\Downloads\tools\Everything\Everything.exe</b>.</li>
</ul>

<br>
<h2>Lesson Learned</h2>
<p>Analyzing the technical progression of this insider threat incident yields critical engineering and architectural lessons that directly inform modern corporate cyber defense strategies. </p>
<p>First, organizations must implement a strict Principle of Least Privilege (<b>PoLP</b>) by enforcing rigid role-based access control (<b>RBAC</b>), ensuring that IT administration accounts are inherently restricted from accessing sensitive, non-technical corporate data directories. To complement this, a separation of duties for IT support must be enforced, mandating dual-authorization protocols and supervised access logging whenever internal or third-party IT staff perform physical or remote maintenance on high-value endpoints. From a monitoring perspective, security teams should deploy host-based registry auditing to operationalize continuous surveillance and centralized SIEM logging for high-fidelity registry locations, specifically tracking unexpected writes to the SAM hive, <b>UserAssist</b>, and <b>RecentDocs</b> keys.</p>
<p>Furthermore, restricting local administrator creation through Endpoint Detection and Response (EDR) blocking policies is essential to instantly alert on and prevent the unsanctioned generation of local user accounts or anomalous Relative Identifier (RID) provisioning. Defense-in-depth should be solidified by establishing application whitelisting via tools like AppLocker to completely block unapproved network utility binaries, commercial VPNs, and file-indexing software on corporate assets. </p>
<p>Finally, implementing robust host-based Data Loss Prevention (<b>DLP</b>) controls ensures the organization can actively monitor, alert, and block the unauthorized copying or physical exfiltration of highly classified proprietary documents to external media or alternative network interfaces.</p>


<br>
<h2>Recommendations</h2>
<p>To translate these forensic findings into immediate, proactive defense measures, the organization must adopt a series of strategic and tactical engineering enhancements to harden its endpoint security posture.</p>
<p>First, it is critical to implement host-based Data Loss Prevention (<b>DLP</b>) by deploying enterprise-grade controls that actively monitor, intercept, and block the unauthorized access, duplication, or alternative transmission of proprietary data assets on all corporate endpoints. Alongside data monitoring, the enterprise must enforce strict privilege management and Just-In-Time (<b>JIT</b>) access, which restricts domain and local administrative permissions to ensure IT support personnel are only granted scoped, time-bound, and fully audited access to necessary system maintenance directories. </p>
<p>To maintain robust visibility, security teams should operationalize centralized registry and event log auditing, configuring endpoints to forward high-fidelity events—specifically targeting unauthorized writes to the local SAM hive, <b>UserAssist</b>, and <b>RecentDocs</b> keys—directly to a centralized SIEM platform for real-time behavioral alerting.</p>
<p>Furthermore, deploying robust application whitelisting via AppLocker or Windows Defender Application Control (<b>WDAC</b>) is necessary to systematically block the execution of unapproved software, commercial VPN clients, and unauthorized network utilities across the environment. This should be coupled with enforcing Zero-Trust Network Access (<b>ZTNA</b>) and strict VPN monitoring, implementing contextual, multi-factor authentication requirements for all network interfaces alongside anomaly detection mechanisms designed to flag unauthorized VPN persistence or unexpected administrative traffic.</p>
<p>Finally, the organization must establish supervised hardware maintenance protocols, mandating that all technical support or hardware remediation performed on high-value executive assets be conducted strictly under dual-custody verification with explicit, documented chain-of-custody logging.</p>

<br>
<h2>References & Acknowledgement</h2>
<p>This digital forensics case study was conducted using <b>Secret Recipe</b> challenge, an advanced dead-box registry forensics environment on the <b>TryHackMe</b> platform. All raw registry hives analyzed throughout this investigation originate directly from their specialized cybersecurity training curriculum. This controlled simulation was completed to enhance tactical threat-hunting awareness, deepen technical proficiency in Windows registry architecture, and cultivate practical incident response skills that can be directly applied to detecting insider threats and protecting enterprise intellectual property.</p>
