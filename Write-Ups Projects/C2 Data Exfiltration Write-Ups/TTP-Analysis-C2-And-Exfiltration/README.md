<h1>TTP Analysis with Elastic Stack (Kibana): C2 and Exfiltration</h1>

<br>
<h2>Executive Summary</h2>
<p>During routine <b>Security Operations Center (SOC)</b> monitoring, an alert triggered on the <b>Intrusion Detection System (IDS)</b> indicating potential <b>Command and Control (C2)</b> beaconing activity originating from a host within the <b>Human Resources</b> department. To scope the extent of the suspected compromise, an incident response triage was initiated on a week-long dataset of <b>HTTP network traffic</b>, resulting in the ingestion of <b>1,482</b> relevant events into the <b>connection_logs</b> index within the <b>Elastic Stack (Kibana) SIEM</b> for the period of <b>March 1</b> to <b>March 30, 2022</b>.</p>
<p>Forensic analysis of the selected network fields successfully mapped the internal corporate asset to source IP <b>192[.]168[.]65[.]54</b> and isolated anomalous, external communications targeting destination IP <b>104[.]23[.]99[.]190</b>. Deep-dive inspection of the HTTP user-agent fields revealed that the threat actor leveraged a <b>Living-off-the-Land (LotL)</b> tactic by abusing a legitimate, native <b>Windows binary</b>—the <b>Background Intelligent Transfer Service (bitsadmin.exe)</b>—to obfuscate the malicious download and evade traditional application whitelisting controls.</p>
<p> Furthermore, log analysis confirmed the adversary utilized a trusted, public file-sharing service as a dead-drop C2 infrastructure, mapping the egress traffic directly to <b>pastebin[.]com</b>. By cross-referencing the <b>host headers</b> and <b>uniform resource identifiers (URIs)</b> extracted from the <b>SIEM</b>, the full C2 URL was reconstructed as <b>[pastebin[.]com/yTg0Ah6a](https[:]//pastebin[.]com/yTg0Ah6a)</b>.</p>
<p> External threat intelligence verification of this endpoint confirmed the unauthorized access and exfiltration of a highly sensitive payload named <b>secret[.]txt</b>, which contained compromised corporate credentials, establishing a confirmed data exfiltration event and a critical breach of credential integrity.</p>

<br>
<h2>Objective</h2>
<p>The primary objective of this case study is to conduct a rigorous, network-centric incident triage to detect, isolate, and reconstruct a post-exploitation <b>Command and Control (C2)</b> lifecycle within an enterprise environment. By leveraging the <b>Elastic Stack (Kibana) SIEM</b> to analyze unstructured network connection logs, the investigation aims to identify critical <b>indicators of compromise (IoCs)</b>, trace anomalous egress communication channels, and uncover stealth tactics—specifically the abuse of native Windows utilities for <b>Living-off-the-Land (LotL)</b> execution.</p>
<p> Ultimately, this analysis serves to establish a comprehensive timeline of the threat actor's methodology, validate the integrity of affected corporate assets, and provide the actionable threat intelligence necessary to mitigate data exfiltration risks and reinforce the organization's defensive posture.</p>

<br>
<h2>Scenario</h2>
<p>During routine <b>security operations center (SOC)</b> monitoring, an automated alert triggered on the corporate <b>Intrusion Detection System (IDS)</b>, flagging an anomalous network beacon indicating potential <b>Command and Control (C2)</b> activity originating from an endpoint assigned to the <b>Human Resources (HR)</b> department. Preliminary indicators suggested an unauthorized file access event involving sensitive, plain-text corporate credentials. </p>
<p>Due to immediate operational constraints and limited asset visibility, forensic collection was restricted to a week-long archive of raw HTTP network traffic. These telemetry logs were subsequently ingested into a dedicated <b>connection_logs</b> index within the <b>Elastic Stack (Kibana) SIEM</b>. Tasked as the primary <b>SOC Analyst</b> handling this incident, the mandate is to execute an isolated network triage, meticulously analyze the user's connection artifacts to isolate the malicious external endpoint, reconstruct the precise execution URL used by the threat actor, and verify the specific payload contents compromised during the security breach.</p>

<br>
<h2>Skills Learned</h2>
<ul>
  <li><b>SIEM Triage & Log Analysis: </b>Proficient in navigating the <b>Elastic Stack (Kibana)</b> to filter, query, and analyze massive datasets within a designated index (<b>connection_logs</b>).</li>
  <br><li><b>Indicator of Compromise (IoC) Isolation: </b>Skilled in extracting critical network artifacts, including source/destination IP pairings, host headers, and <b>Uniform Resource Identifiers (URIs)</b>, to trace malicious footprints.</li>
   <br><li><b>Living-off-the-Land (LotL) Detection: </b>Experienced in identifying the abuse of native Windows utilities—specifically <b>Background Intelligent Transfer Service (bitsadmin.exe)</b>—used by threat actors to evade application controls.</li>
   <br><li><b>C2 Architecture De-obfuscation: </b>Capable of reconstructing malicious <b>Command and Control (C2)</b> communication channels that rely on trusted, public file-sharing platforms (<b>pastebin[.]com</b>) to bypass traditional network defenses.</li>
   <br><li><b>Incident Scoping & Threat Intel Verification: </b>Competent in validating external endpoints to determine the exact payload delivery mechanism (<b>secret.txt</b>) and assessing the overall operational impact of a data exfiltration event.</li>
</ul>

<br>
<h2>Tools Utilized</h2>
<ul>
  <li><b>Elastic Stack (Kibana) SIEM: </b>Utilized as the central security analytics platform to query, filter, and parse the <b>connection_logs</b> index during data triage.</li>
   <br><li><b>Pastebin (Public Dead-Drop C2): </b>Investigated as the external, trusted third-party web service leveraged by the adversary to host malicious payloads and obfuscate egress traffic.</li>
</ul>

<br>
<h2>Artifacts</h2>
<ul>
  <li><b>Infected Host Asset IP (192[.]168[.]65[.]54): </b>Isolated as the internal source IP address assigned to the compromised Human Resources endpoint.</li>
  <br><li><b>Adversary Infrastructure IP (104[.]23[.]99[.]190): </b>Identified as the external destination IP address facilitating anomalous network communications.</li>
  <br><li><b>Malicious HTTP User-Agent (bitsadmin): </b>Caught via log analysis as the native Windows command-line tool was abused to execute the unauthorized file download.</li>
  <br><li><b>Dead-Drop C2 Domain (pastebin[.]com): </b>Uncovered as the trusted public web service hijacked by the threat actor to obfuscate command-and-control egress traffic.</li>
  <br><li><b>Reconstructed C2 URI/URL (pastebin[.]com/yTg0Ah6a):</b> Formulated by combining the host header and specific resource path string extracted from the SIEM logs.</li>
  <br><li><b>Exfiltrated Payload (secret[.]txt): </b>Confirmed as the sensitive, external text file accessed by the adversary containing compromised corporate credentials.</li>
</ul>

<br>
<h2>Findings</h2>
<h3>Phase 1: SIEM Initialization & Scope Definition</h3>
<p>I opened the Elastic Stack SIEM with <b>connection_logs</b> ingested in it. I changed the date from <b>March 1, 2022</b> at 00:00H to <b>March 30, 2022</b> at 23:30H, in order to analyze and investigate how many events would return. Based on the result, it provided <b>1,482</b> hits. </p>
<p><img width="975" height="348" alt="image" src="https://github.com/user-attachments/assets/656262af-146d-4052-bd87-0c500c8c7cc5" />
</p>

<br>
<h3>Phase 2: Host Isolation & Traffic Triage</h3>
<p>I hovered over the source IP to investigate if there are any suspicious IPs and found out that the IP associated with the suspected user in logs is <b>192[.]168[.]65[.]54</b>. I selected the <b>source_ip</b> and <b>destination_ip</b> in the <b>Selected Fields</b> to check what IP addresses it interacts with, and it seems there’s one, IP address <b>104[.]23[.]99[.]190</b>.</p>
<p><img width="975" height="345" alt="image" src="https://github.com/user-attachments/assets/c4321267-3272-438d-8780-853110d40e25" />
</p>
<p><img width="975" height="270" alt="image" src="https://github.com/user-attachments/assets/2dd7b168-f53d-4969-9e75-629c29a4c9b1" />
</p>

<br>
<h3>Phase 3: User-Agent & Tactical (TTP) Analysis</h3>
<p>I focused on filtering this IP address and filtered more in the <b>Selected fields</b> to go deeper investigation. The user’s machine used a native legit Windows binary (<b>user_agent</b>) to download a file from the C2 server, and the name of the binary is <b>bitsadmin</b>.</p>
<p><img width="975" height="126" alt="image" src="https://github.com/user-attachments/assets/d3960b21-4498-4906-af03-73500ddfb5b7" />
</p>

<br>
<h3>Phase 4: Infrastructure & C2 Reconstruction</h3>
<p>As I analyzed the result, the infected machine connected with a famous filesharing site (<b>host</b>) in this period, which also acts as a command-and-control (C2) server used by the malware authors to communicate. The name of that file sharing site is <b>pastebin[.]com</b>.</p>
<p><img width="975" height="110" alt="image" src="https://github.com/user-attachments/assets/fc9c033e-64c7-4181-8b1d-07a642ea000e" />
</p>
<p>I combined the filesharing site (<b>host</b>) and the <b>uri</b>, it make sense that the full URL of the C2 to which the infected host is connected is <b>pastebin[.]com/yTg0Ah6a</b>.</p>
<p><img width="975" height="110" alt="image" src="https://github.com/user-attachments/assets/83b00a73-0088-4748-9fda-78a14f2b3ae5" />
</p>

<br>
<h3>Phase 5: Payload Verification & Impact Assessment</h3>
<p>I utilized the full URL and accessed over the internet to investigate if a file was accessed on this filesharing site (<b>pastebin[.]com/yTg0Ah6a</b>) from the HR Department, and found out that the name of the file is <b>secret[.]txt</b>.</p>
<p><img width="975" height="176" alt="image" src="https://github.com/user-attachments/assets/4db189bc-37d0-4bfe-9e30-1e42940d8a3a" />
</p>
<p><img width="975" height="382" alt="image" src="https://github.com/user-attachments/assets/3f3bba70-1041-440c-99bf-67cb3eb48927" />
</p>
<p>Lastly, I opened the accessed file or document if what was acquired, and it was credentials.</p>
<p><img width="975" height="202" alt="image" src="https://github.com/user-attachments/assets/d2f57bff-1705-4999-9dce-712f1cd9852f" />
</p>

<br>
<h2>MITRE ATT&CK Framework</h2>
<ul>
  <li><b>Reconnaissance / Resource Development (T1583.001 - Domains): </b>Adversary leveraged a pre-existing, public web infrastructure domain (<b>pastebin[.]com</b>) to host a malicious payload and avoid registration alerts.</li>
  <li><b>Execution (T1059 - Command and Scripting Interpreter): </b>Utilization of command-line mechanics to trigger system processes and execute the unauthorized download script.</li>
  <li><b>Defense Evasion (T1218 - System Binary Proxy Execution): </b>Misuse of a legitimate, trusted Windows binary (<b>bitsadmin.exe</b>) to bypass application whitelisting and blend into normal network traffic.</li>
  <li><b>Command and Control (T1071.001 - Web Protocols): </b>Communication with external infrastructure over standard HTTP traffic to blend malicious </li>
  <li><b>Command and Control (T1102 - Web Service):</b> Strategic deployment of a common, trusted file-sharing web service as a dead-drop C2 mechanism to bypass strict egress filtering.</li>
  <li><b>Exfiltration / Impact (T1048 - Exfiltration Over Alternative Protocol): </b>Unauthorized access and retrieval of a sensitive corporate credential payload (<b>secret[.]txt</b>) via an asymmetric web channel.</li>
</ul>

<br>
<h2>Indicators of Compromise (IoCs)</h2>
<ul>
  <li><b>Internal Source IP (192[.]168[.]65[.]54): </b>Identifies the compromised endpoint assigned to the Human Resources department initiating anomalous egress traffic.</li>
  <li><b>External Destination IP (104[.]23[.]99[.]190): </b>Flags the rogue host infrastructure facilitating unauthorized out-of-band communication channels.</li>
  <li><b>Malicious User-Agent (bitsadmin):</b>Signals an alert for defensive evasion through the misuse of a native Windows binary to download files.</li>
  <li><b>C2 Infrastructure Domain (pastebin[.]com): </b>Marks the trusted public file-sharing service weaponized by the threat actor to act as a dead-drop server.</li>
  <li><b>Malicious URI Endpoint (/yTg0Ah6a): </b>PINpoints the specific resource locator string tied directly to the hostile command-and-control server configuration.</li>
  <li><b>Staged Payload Name (secret[.]txt): </b>Uncovers the highly sensitive target file compromised during the event, containing plaintext corporate credentials.</li>
</ul>

<br>
<h2>Lessons Learned</h2>
<ul>
  <li><b>Implement Strict Egress Filtering: </b>Restrict internal endpoints from establishing direct outbound connections to public text-sharing and code-hosting platforms (<b>e.g., pastebin[.]com</b>) unless explicitly authorized by business needs.</li>
  <li><b>Restrict Native System Binaries:</b> Enforce application control rules (such as <b>AppLocker</b> or <b>Windows Defender Application Control</b>) to block or monitor non-administrative execution of powerful native utilities like <b>bitsadmin.exe</b>.</li>
  <li><b>Enhance SIEM Detection Engineering: </b>Develop specific correlation rules to alert on anomaly patterns where administrative tools (<b>bitsadmin</b>, <b>powershell</b>, <b>certutil</b>) are paired with external web user-agents.</li>
  <li><b>Enforce Credential Hygiene & Masking: </b>Ensure all corporate credentials are encrypted at rest and managed via enterprise-grade password vaults rather than being stored in plaintext documents like <b>secret[.]txt</b>.</li>
  <li><b>Deploy Host Telemetry Logging: </b>Supplement network connection logs with endpoint detection logs (such as <b>Sysmon</b> or <b>EDR</b> telemetry) to gain deeper visibility into the parent processes triggering network events.</li>
</ul>

<br>
<h2>Recommendations</h2>
<p>To fortify the organization’s defensive posture against similar post-exploitation tactics, it is highly recommended to implement a multi-layered security strategy focused on aggressive attack surface reduction and enhanced detection engineering.</p>
<p> First, network security teams must enforce strict egress filtering rules to block or heavily restrict outbound traffic to unvetted public file-sharing and text-hosting services, such as <b>pastebin[.]com</b>, which are commonly weaponized for dead-drop C2 architecture.</p>
<p> Second, host-defense mechanisms must be strengthened by deploying robust application control policies—such as <b>AppLocker</b> or <b>Windows Defender Application Control (WDAC)</b>—to monitor, restrict, or entirely disable non-administrative execution of high-risk native binaries like <b>bitsadmin.exe</b>. Additionally, the <b>SOC</b> should implement dedicated SIEM correlation rules designed to trigger high-severity alerts whenever default system utilities generate external network traffic.</p>
<p> Finally, to eliminate the risk of severe data exfiltration, the organization must transition away from plain-text credential storage by mandating an enterprise-grade <b>privileged access management (PAM)</b> solution, coupled with immediate credential revocation and password resets for the affected <b>Human Resources<b> assets.</p>

<br>
<h2>References & Acknowledgement</h2>
<p>This network triage and incident response case study was conducted using <b>ItsyBitsy</b>, a specialized defensive security environment provided by the <b>TryHackMe</b> platform. All network connection logs, telemetry datasets, user-agent profiles, and command-and-control artifacts analyzed throughout this investigation originate directly from their defensive security training curriculum.</p>
<p> This controlled simulation was completed to enhance tactical threat-hunting awareness, deepen technical proficiency in SIEM log analysis using the <b>Elastic Stack (Kibana)</b>, and cultivate practical incident response skills that can be directly applied to protecting and hardening enterprise environments against sophisticated persistent threats.</p>
