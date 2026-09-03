<h1>Complete Virtual Cybersecurity Lab (SOC Home Lab)</h1>
<p><img width="1024" height="558" alt="image" src="https://github.com/user-attachments/assets/910fd61e-c89b-41d0-9927-dd3c67bf944b" />
</p>
<p><i>Virtual Cybersecurity (SOC) Lab Network Topology</i></p>

<br>
<h2>Executive Summary</h2> <p>This environment serves as a rigorous testing ground where an adversarial <b>Kali Linux</b> platform (<b>10.0.2.3</b>) executes diverse attack vectors—including SSH brute-forcing, unauthorized RDP access, phishing email, and other tactical exploits—against a hardened <b>Windows 10 Pro</b> target machine (<b>10.0.2.15</b>). Advanced endpoint visibility is achieved via <b>Microsoft System Monitor (Sysmon)</b>, which captures detailed behavioral events and safely ships them alongside core system logs to a centralized <b>Ubuntu Server</b> running <b>Wazuh Manager</b> (<b>10.0.2.12</b>). To further strengthen network-level visibility and threat detection, <b>Suricata</b> is deployed as a network intrusion detection and analysis engine, monitoring traffic between the adversarial and target systems, generating security alerts, and providing additional network telemetry that complements the endpoint data collected by Sysmon and the centralized monitoring capabilities of Wazuh.</p> <p>By correlating endpoint and network telemetry, analyzing live security events, and managing incident alerts, this project successfully validates my hands-on technical proficiency in <b>SIEM</b> engineering, network intrusion detection, log parsing, event correlation, and detection validation. The integration of <b>Suricata</b>, <b>Sysmon</b>, and <b>Wazuh</b> demonstrates a layered defensive architecture capable of providing visibility across both host and network activity—proving that elite defensive analysis requires critical problem-solving, effective telemetry correlation, and architectural agility far more than unlimited hardware.</p>

<br>
<h2>Project Objective</h2> <p>This project represents my <b>SOC Home Lab</b>, with the primary objective of building a functional and high-fidelity security monitoring environment using <b>Sysmon</b>, <b>Suricata</b>, and <b>Wazuh</b>. The lab consists of an adversarial <b>Kali Linux</b> machine used to simulate realistic attack activity, a hardened <b>Windows 10 Pro</b> endpoint for generating host-based security telemetry, and an <b>Ubuntu Server</b> responsible for centralized log collection, analysis, alert management, and security monitoring through <b>Wazuh</b>.</p> <p><b>Sysmon</b> provides detailed endpoint-level visibility into processes, network connections, file activity, and other system behaviors, while <b>Suricata</b> provides network-level intrusion detection and traffic analysis. These telemetry sources are centralized and correlated through <b>Wazuh</b>, enabling the detection and investigation of simulated attacks such as <b>SSH brute-force attempts</b>, <b>unauthorized RDP access</b>, <b>phishing activity</b>, and other adversarial techniques. The overall objective is to develop practical skills in <b>SOC operations</b>, <b>SIEM engineering</b>, <b>network intrusion detection</b>, <b>endpoint monitoring</b>, <b>log analysis</b>, <b>alert investigation</b>, and <b>threat detection validation</b> within a controlled home-lab environment.</p>

<br>
<h2>Lab Overview</h2>
<p><img width="1024" height="669" alt="image" src="https://github.com/user-attachments/assets/27a57df1-be17-4c50-8e14-49ef8ab7736a" />
<p><i>Basic Network Topology Layout</i></p>
</p>
<p>To replicate the daily workflows of a SOC Analyst under local hardware constraints, this lab features a targeted deployment of three core virtual machines within a custom <b>VirtualBox NAT network</b>: a <b>Kali Linux</b> attacker platform, a <b>Windows 10 Pro</b> endpoint equipped with <b>Sysmon</b> for detailed endpoint telemetry, and a centralized <b>Ubuntu Server</b> hosting the <b>Wazuh SIEM</b> and <b>Suricata IDS/IPS</b>. Suricata provides network-level traffic monitoring and intrusion detection, complementing the host-based visibility provided by Sysmon. Together, these components create an isolated environment capable of simulating realistic attacks, generating endpoint and network telemetry, and supporting end-to-end security investigations, detection engineering, alert analysis, and live log monitoring.</p>


<br>
<h2>Cyber Threat Simulation Scenario</h2>
<p>To simulate real-world enterprise threats within a controlled, resource-optimized framework, this architecture sets up a comprehensive environment modeling a cyber adversary attempting to compromise a critical corporate endpoint/s belonging to an employee.</p> 
<p>Operating from an isolated platform represented by the <b>Kali Linux</b> instance (<b>10.0.2.3</b>), the lab is fully provisioned to support any multi-stage attack lifecycle targeting the <b>Windows 10 Pro</b> workstation (<b>10.0.2.15</b>)—including aggressive reconnaissance, unauthorized credential harvesting, network-level exploits, remote connection attacks like SSH and RDP brute-forcing, and et cetera.</p>
<p>With the core engineering phase complete, this deployment stands fully operational and optimized for defensive validation. As future simulations trigger malicious executions or privilege escalation techniques, <b>Microsoft System Monitor (Sysmon)</b> remains active on the target machine to capture granular, low-level behavioral event logs. This high-fidelity telemetry pipeline is ready to securely stream logs to the centralized <b>Ubuntu Server</b> running the <b>Wazuh SIEM Manager (10.0.2.4)</b>, which is configured to parse, correlate, and surface raw events into real-time, actionable security alerts. </p>
<p>The underlying network and collection pipeline are completely verified, rendering this <b>SOC Home Lab</b> perfectly primed for diverse adversarial testing, behavioral analysis, and live incident triage.</p>

<br>
<h2>Skills Learned</h2>
<u>
  <li><b>Hypervisor Architecture & Virtual Networking: </b>Developed hands-on proficiency in virtualization engineering by designing, provisioning, and isolating virtual machines within <b>Oracle VM VirtualBox</b>. Successfully architected a custom, multi-node <b>NAT Network (10.0.2.0/24)</b> to maintain environment isolation while ensuring structured, inter-VM network routing and connectivity.</li>
  <br><li><b>Linux System Administration & SIEM Deployment: </b>Cultivated practical Linux administration skills by deploying, configuring, and hardening an <b>Ubuntu Server</b> to act as the central repository for the lab's security infrastructure. Successfully installed the <b>Wazuh Manager</b> framework, managing core system dependencies and verifying daemon readiness.</li>
  <br><li><b>Endpoint Telemetry & Logging Architecture: </b>Gained foundational knowledge of host-level visibility and enterprise auditing by deploying <b>Microsoft System Monitor (Sysmon)</b> on a <b>Windows 10 Pro</b> endpoint. Mastered the structural installation of advanced logging binaries and endpoint-level agent services designed to transform raw OS behavior into structured telemetry.</li>
  <br><li><b>SIEM Agent Deployment & Pipeline Engineering: </b> Mastered the fundamentals of the log collection lifecycle by successfully deploying and configuring the <b>Wazuh Agent</b> on a target Windows endpoint. Successfully established secure communication between the endpoint agent and the centralized <b>Ubuntu SIEM</b> server, verifying the integrity of the ingestion pipeline.</li>
  <br><li><b>Network Infrastructure Troubleshooting: </b>Developed critical, low-level technical problem-solving skills by diagnosing and resolving hypervisor-level network connectivity issues. Successfully managed virtual interface states, negotiated IP address assignments, and validated end-to-end interface connectivity.</li>
  <br><li><b>Pragmatic Project Management & Scope Planning: </b>Demonstrated strong architectural planning and resource management by designing a phased deployment roadmap. Successfully engineered a lean, fully functional, three-node security verification pipeline optimized specifically for local hardware constraints, establishing a rock-solid foundation for future adversarial testing.</li>
</u>

<br>
<h2>Tools & Technologies Utilized</h2>
<h3>Infrastructure & Virtualization Layer</h3>
<ul>
  <li><b>Oracle VM VirtualBox: </b>Utilized as a Type-2 hypervisor to host, configure, and isolate virtual machines within a secure sandbox environment.</li>
  <br><li><b>VirtualBox NAT Networking: </b>Implemented to establish a dedicated private network (<b>10.0.2.0/24</b>), enabling secure internal inter-VM communication and controlled routing without exposing the lab directly to the physical host's network.</li>
</ul>

<h3>Defensive & Telemetry Engineering Layer</h3>
<ul>
  <li><b>Wazuh SIEM (Open-Source): </b>Deployed on an Ubuntu Server backend to act as a centralized <b>Security Information and Event Management (SIEM)</b> and <b>Extended Detection and Response (XDR)</b> platform for log aggregation, normalization, and alert generation.</li>
  <br><li><b>Wazuh Endpoint Agent: </b>Installed on the Windows target endpoint to establish a secure cryptographic channel that streams real-time local system telemetry directly to the Wazuh Manager.</li>
  <br><li><b>Microsoft System Monitor (Sysmon): </b>Integrated into the Windows host auditing subsystem to provide advanced endpoint visibility by generating high-fidelity event logs for process creation, network connections, and file modifications.</li>
</ul>

<h3>Adversarial & Simulation Layer</h3>
<ul>
  <li><b>Kali Linux: </b>Provisioned as a dedicated offensive security testing platform, fully equipped and strategically positioned within the network to simulate threat actor methodologies and execute future exploitation vectors.</li>
</ul>

<h3>Operating Systems Layer</h3>
<ul>
  <li><b>Ubuntu Server (LTS): </b>Utilized as a lightIight, high-performance Linux foundation dedicated to running core <b>Wazuh SIEM</b> management services.</li>
  <br><li><b>Windows 10 Pro: </b>Deployed as an enterprise-grade target endpoint, specifically configured for enhanced security auditing and proactive monitoring.</li>
  <br><li><b>Windows 11: </b>Serving as the physical host system, it is used to orchestrate the virtual environment and securely access the Ib-based Wazuh management dashboard for administrative verification.</li>
</ul>

<br>
<h2>Installation & Deployment Guide</h2>
<h3>A. VirtualBox</h3>
<p>I chose the vendor VirtualBox as the virtual environment (preferably Sandbox Environment). First, I go to <b>Google.com</b> and type <b>download VirtualBox</b> or <b>VirtualBox download</b> in the search bar, then press <b>Enter</b>.</p>
<p><img width="665" height="279" alt="image" src="https://github.com/user-attachments/assets/4c9f23bf-e650-4a28-b70d-fc636c642216" />
</p>
<p>Google provided different results, but I selected the first one.</p>
<p><img width="583" height="397" alt="image" src="https://github.com/user-attachments/assets/bd4115a1-c74d-4947-9b82-d37811f7e64e" />
</p>
<p>On the <b>VirtualBox</b> platform, it provided two different choices. I chose the box on the left side and selected the <b>Windows hosts</b>, since I am using Windows OS.</p>
<p><img width="829" height="381" alt="image" src="https://github.com/user-attachments/assets/260a1e46-871a-4be1-a0ce-3ed9452746d6" />
</p>
<p>After selecting the <b>Windows hosts</b>, it automatically download the application. I created a specific folder intended or dedicated only for virtual machine apps, images, and other files that are needed for this home lab setup.</p>
<p><img width="558" height="392" alt="image" src="https://github.com/user-attachments/assets/d0f1118d-df8f-48be-bd9d-ec3e95dca1e0" />
</p>
<p>After the download, I opened another browser for <b>VirusTotal.com</b> and uploaded the <b>VirtualBox</b> file, because it acts as a critical safety check to confirm the file is legitimate and free of malware. Another reason is that it prevents accidental system infections, verifies file integrity and authenticity, and catches tampered downloads.</p>
<p><img width="585" height="492" alt="image" src="https://github.com/user-attachments/assets/7f4da28d-1cdf-434b-a52d-cd2f5adc42f4" />
</p>
<p><img width="599" height="407" alt="image" src="https://github.com/user-attachments/assets/6259cc73-6bed-4284-ae9e-f29498d96ce3" />
</p>
<p><b>VirusTotal</b> checked and verifying the file.</p>
<p><img width="562" height="397" alt="image" src="https://github.com/user-attachments/assets/aaa25a2a-c65a-4fd1-b748-1eeb81ac6e66" />
</p>
<p>Based on the result, the file or installer is safe and not flagged with any anti-virus vendors; thus, I confidently installed it on my computer.</p>
<p><img width="743" height="451" alt="image" src="https://github.com/user-attachments/assets/ac870845-259d-4ce1-a9af-59a1eb927831" />
</p>
<p>I opened the folder where the installer was saved, and right-click then select <b>Open</b> to run the file.</p>
<p><img width="728" height="438" alt="image" src="https://github.com/user-attachments/assets/52aa07ed-b646-4b10-92db-123cd7db8882" />
</p>
<p>I selected <b>Next</b> to start the pre-installation.</p>
<p><img width="601" height="471" alt="image" src="https://github.com/user-attachments/assets/92be6de1-b088-47da-a9ba-7ccfd28d0033" />
</p>
<p>I selected the <b>I accept the terms of the license agreement</b> and press <b>Next</b>.</p>
<p><img width="548" height="431" alt="image" src="https://github.com/user-attachments/assets/87bad6d5-c18b-407f-b94c-bcba477d214c" />
</p>
<p>I let it as it is and selected <b>Next</b> to continue.</p>
<p><img width="568" height="446" alt="image" src="https://github.com/user-attachments/assets/95c4421d-0d31-4131-86c9-88de76a89990" />
</p>
<p>I leave it as it is and selected <b>Yes</b> to proceed.</p>
<p><img width="554" height="436" alt="image" src="https://github.com/user-attachments/assets/c9bcae26-39a7-4219-996b-3ac6078545d2" />
</p>
<p>I selected <b>Yes</b> to continue.</p>
<p><img width="572" height="456" alt="image" src="https://github.com/user-attachments/assets/ca068a30-48c1-4649-8a16-bf7c064d5f7d" />
</p>
<p>I leave it like that and selected <b>Next</b>.</p>
<p><img width="496" height="400" alt="image" src="https://github.com/user-attachments/assets/2bbabf6e-1cdf-4159-89f0-63cf4c346df7" />
</p>
<p>Lastly, I selected the <b>Install</b> to start the installation process, and I let it load up.</p>
<p><img width="507" height="401" alt="image" src="https://github.com/user-attachments/assets/23932057-7926-465b-acd4-398de76cfcbe" />
</p>
<p><img width="535" height="425" alt="image" src="https://github.com/user-attachments/assets/9cfbcea3-0707-4b08-8a52-19b35b478401" />
</p>
<p>I selected <b>Finish</b> to start the program.</p>
<p><img width="556" height="439" alt="image" src="https://github.com/user-attachments/assets/6326b0fa-4895-45ef-a5ce-34dc7993edc9" />
</p>
<p>I successfully installed the VirtualBox machine on my computer.</p>
<p><img width="644" height="385" alt="image" src="https://github.com/user-attachments/assets/1d3ad328-7157-44f2-b305-ab56856a5866" />
</p>

<br>
<h3>B. Windows 10 Pro</h3>
<p>I installed <b>Windows 10</b> as the target or victim machine. To start the process, first, I opened <b>Google.com</b> and typed <b>Microsoft windows 10 download</b> to search for the legitimate Microsoft platform.</p>
<p><img width="804" height="337" alt="image" src="https://github.com/user-attachments/assets/0b948be4-9ab7-4bd6-9c2f-401bc60c23a7" />
</p>
<p>Google provided me with some results, and I chose the first one and selected it.</p>
<p><img width="652" height="484" alt="image" src="https://github.com/user-attachments/assets/9ddc54d3-c050-4bc3-bdeb-e62f11bd27a9" />
</p>
<p>I chose the <b>Download Now</b> button to download the Windows 10 installation media.</p>
<p><img width="700" height="351" alt="image" src="https://github.com/user-attachments/assets/033539a5-1026-4213-813d-51a4388305a8" />
</p>
<p>After that, it prompted me where to save the file; thus, I selected the same folder where I saved the previous file.</p>
<p><img width="669" height="488" alt="image" src="https://github.com/user-attachments/assets/72fbdafe-4e99-4a85-82e9-6688a8fe870a" />
</p>
<p><img width="613" height="314" alt="image" src="https://github.com/user-attachments/assets/1e6e7aca-1e77-4615-98ff-0c6df7259b52" />
</p>
<p>After I downloaded the file, I verified the file using the <b>VirusTotal</b> platform to check if it is free from malware.</p>
<p><img width="771" height="356" alt="image" src="https://github.com/user-attachments/assets/33ed161c-28bf-4322-9219-f03d4f364f82" />
</p>
<p>Since the file is legit and clean, I simply opened the downloaded file, so that I can download the ISO file for VirtualBox.</p>
<p><img width="685" height="434" alt="image" src="https://github.com/user-attachments/assets/b42963eb-1594-4863-b5aa-3e056942fba1" />
</p>
<p>I selected the <b>Accept</b> button to accept the license terms.</p>
<p><img width="650" height="579" alt="image" src="https://github.com/user-attachments/assets/51bfe390-9217-4f50-8a03-40a6130f0dc8" />
</p>
<p>I selected the second one in order to create installation media, such as an ISO file. After that, I selected <b>Next</b> to continue.</p>
<p><img width="599" height="531" alt="image" src="https://github.com/user-attachments/assets/16aa2566-4868-435a-9bce-b1562cbed294" />
</p>
<p>I leave it as it is and selected <b>Next</b> to proceed.</p>
<p><img width="672" height="596" alt="image" src="https://github.com/user-attachments/assets/4e8beb70-66d3-48ce-8ee4-733754ce7f71" />
</p>
<p>I selected the <b>ISO file</b> radio button and selected the <b>Next</b> button to continue.</p>
<p><img width="602" height="524" alt="image" src="https://github.com/user-attachments/assets/81b9d69c-f31a-4441-9107-9a0a4412c58e" />
</p>
<p>It prompted me where to save the file, so I still chose the dedicated folder where I saved the other files for VirtualBox.</p>
<p><img width="703" height="444" alt="image" src="https://github.com/user-attachments/assets/15020d18-8b68-425c-9969-cb18402f3c61" />
</p>
<p>I let it download the ISO file and did not interrupt while the process was ongoing.</p>
<p><img width="975" height="289" alt="image" src="https://github.com/user-attachments/assets/ff4055de-768a-4dcd-96c9-e546a0b1beea" />
</p>
<p><img width="975" height="290" alt="image" src="https://github.com/user-attachments/assets/4ccd06bc-9abe-43dc-ab22-c3281a552221" />
</p>
<p>I selected the <b>Finish</b> button to complete the download</p>
<p><img width="604" height="531" alt="image" src="https://github.com/user-attachments/assets/d567b8ac-f13e-42d8-8ffb-de8fd91b98fb" />
</p>
<p><img width="975" height="287" alt="image" src="https://github.com/user-attachments/assets/de23d718-34d6-4eba-a15c-cf924a5f82f3" />
</p>
<p>The Windows 10 ISO file is now inside the folder and ready to ingest in VirtualBox.</p>
<p><img width="728" height="298" alt="image" src="https://github.com/user-attachments/assets/91dad945-b267-4ac1-af05-6fe96f17af68" />
</p>
<p>I opened the VirtualBox again and selected <b>New</b> to ingest the Windows 10 ISO file.</p>
<p><img width="676" height="481" alt="image" src="https://github.com/user-attachments/assets/a70f0ba9-1680-442f-bd66-0f280258413a" />
</p>
<p>In VM Name, I entered <b>Win_10</b> as the name for Windows 10. I selected the drop-down to locate the ISO image file of Windows 10.</p>
<p><img width="742" height="522" alt="image" src="https://github.com/user-attachments/assets/15156880-5103-48ef-b35b-7786c69d7e1c" />
</p>

<p><img width="721" height="507" alt="image" src="https://github.com/user-attachments/assets/d8829e09-e037-4b86-8811-8ee66ba2e13f" /></p>
<p><img width="600" height="576" alt="image" src="https://github.com/user-attachments/assets/a5e0ee64-205e-40b2-bbe1-d225447acd3b" />
</p>
<p><img width="771" height="367" alt="image" src="https://github.com/user-attachments/assets/16b4105d-2d39-427a-bdbf-adef48e0b034" />
</p>
<p>I selected <b>6 GB</b> as the Base Memory. After that, I selected <b>Next</b>.</p>
<p><img width="975" height="356" alt="image" src="https://github.com/user-attachments/assets/f6b9903a-f7d9-42b0-b4d4-7e58f17f3806" />
</p>
<p>I leave it <b>50 GB</b> as the Hard Disk File Size and selected <b>Finish</b>.</p>
<p><img width="975" height="363" alt="image" src="https://github.com/user-attachments/assets/88922015-dc82-4f27-b6b2-cce9e22f3657" />
</p>
<p>After that, the <b>Windows 10</b> machine appeared on the left pane of VirtualBox. I ran the program by selecting the <b>Start</b> button on top to start the installation of Windows 10.</p>
<p><img width="756" height="407" alt="image" src="https://github.com/user-attachments/assets/a96c24fa-e9b3-48a7-99eb-9b1bcbbd031f" />
</p>
<p>I leave everything as it is and selected the <b>Install</b> button.</p>
<p><img width="771" height="575" alt="image" src="https://github.com/user-attachments/assets/ab9b3a65-4b81-4eba-a17e-a10221cf6ef1" />
</p>
<p><img width="771" height="569" alt="image" src="https://github.com/user-attachments/assets/834eb428-8e2d-4875-9dfb-6f6af5008998" />
</p>
<p>I selected <b>I don’t have a product key</b> since I don’t have any at all</b>.</p>
<p><img width="796" height="596" alt="image" src="https://github.com/user-attachments/assets/1e69568b-5f1f-4df5-8194-b029d8126b92" />
</p>
<p>I selected the <b>Windows 10 Pro</b> and clicked on <b>Next</b> button.</p>
<p><img width="796" height="596" alt="image" src="https://github.com/user-attachments/assets/20d36cb1-9c12-4d82-8481-c9f74c3b6436" />
</p>
<p>I ticked the <b>I accept the license terms and selected the Next</b> button.</p>
<p><img width="800" height="596" alt="image" src="https://github.com/user-attachments/assets/9a262a66-1c19-489b-a664-b9e0c2b69290" />
</p>
<p>I selected the <b>Custom Install Windows only</b> to continue the process.</p>
<p><img width="790" height="415" alt="image" src="https://github.com/user-attachments/assets/ebe42f7e-9dd4-4841-8799-aa22e64137a6" />
</p>
<p>I leave everything as it is and selected the <b>Next</b> button to start the installation.</p>
<p><img width="796" height="596" alt="image" src="https://github.com/user-attachments/assets/7dd8fd43-0d3c-4b88-9d43-f38dfa3a005d" />
</p>
<p><img width="532" height="475" alt="image" src="https://github.com/user-attachments/assets/0a8a6468-e8f1-4f56-b84c-b04418b122f3" />
</p>
<p>I leave as it is and selected <b>Yes</b> button.</p>
<p><img width="814" height="574" alt="image" src="https://github.com/user-attachments/assets/c110ea7f-1226-4e27-b990-4c4e5ff79f08" />
</p>
<p>I leave as it is and selected <b>Yes</b> button.</p>
<p><img width="796" height="585" alt="image" src="https://github.com/user-attachments/assets/f1b64e9e-44ed-4e3d-987a-a1a5b22d3f0e" />
</p>
<p>I selected <b>Skip</b> button with this one.</p>
<p><img width="868" height="581" alt="image" src="https://github.com/user-attachments/assets/8d85e22f-acb1-4a66-916c-676db372d5ca" />
</p>
<p>I entered <b>Win_10</b> as the name of the PC and selected the <b>Next</b> button.</p>
<p><img width="762" height="571" alt="image" src="https://github.com/user-attachments/assets/87a1b8c0-ff2f-400c-921d-04149e945eca" />
</p>
<p>I didn’t input any password for easy access and selected the <b>Next</b> button instead.</p>
<p><img width="837" height="574" alt="image" src="https://github.com/user-attachments/assets/97857e55-2802-4d75-adaa-573eab239806" />
</p>
<p>The <b>Windows 10 Pro</b> machine is successfully installed. Later, I will be turning off all the security, which includes the Windows Defender and its anti-virus, so that I can start attacking this machine using the <b>Kali Linux</b> machine.</p>
<p><img width="714" height="539" alt="image" src="https://github.com/user-attachments/assets/8bedc995-acdc-474e-b93e-8e21770a0f62" />
</p>

<br>
<h3>C. Kali Linux</h3>
<p>I opened <b>Google.com</b> and input “<b>kali linux iso download</b>” to direct me to its Ibsite.</p>
<p><img width="975" height="448" alt="image" src="https://github.com/user-attachments/assets/a12b548d-29dc-4c24-9445-2508c5085cb8" />
</p>
<p>There are some results for <b>Kali Linux</b>, thus, I selected the first one.</p>
<p><img width="814" height="419" alt="image" src="https://github.com/user-attachments/assets/430b57b3-58f0-476a-a6ac-36e86314f2dc" />
</p>
<p>Inside the Kali Ibsite, select the <b>Virtual Machines</b> on the right-side.</p>
<p><img width="975" height="521" alt="image" src="https://github.com/user-attachments/assets/f0f235ba-a089-4e20-8b19-616977af298a" />
</p>
<p>Since I am using VirtualBox, I chose the VirtualBox option. It prompted me where to save the file, thus, I saved it in the folder where I saved the other files.</p>
<p><img width="975" height="517" alt="image" src="https://github.com/user-attachments/assets/8a089efd-de1e-431e-8b65-c6f88d60f1b2" />
</p>
<p><img width="971" height="306" alt="image" src="https://github.com/user-attachments/assets/f5094818-d849-4dba-a4cb-c97fdc7766fc" />
</p>
<p>After I downloaded the file, I extracted the file in the same folder.</p>
<p><img width="543" height="511" alt="image" src="https://github.com/user-attachments/assets/6a63a8fd-e6b9-42ba-932f-9cebfdfbf269" />
</p>
<p>After I extracted the WinRAR file, it provided two results. I double-clicked the blue one (which has <b>.vbox</b> extension).</p>
<p><img width="583" height="408" alt="image" src="https://github.com/user-attachments/assets/d2e5efd8-a065-47d0-bd67-ad737149cfd8" />
</p>
<p><img width="754" height="766" alt="image" src="https://github.com/user-attachments/assets/5a912d61-2b40-41c4-8da8-57ab155b7fa0" />
</p>
<p>It automatically imported on the <b>VirtualBox</b> .</p>
<p><img width="968" height="380" alt="image" src="https://github.com/user-attachments/assets/c7a392e6-c519-456d-a598-b089e921d0a0" />
</p>
<p>I scrolled down and found out that the <b>Username</b> and  <b>Password</b> is <b>Kali</b>.</p>
<p><img width="562" height="387" alt="image" src="https://github.com/user-attachments/assets/1f17b1e7-4e11-4689-a8da-f62a7fd8ee8c" />
</p>
<p>I selected the <b>Start</b> button on top to run Kali.</p>
<p><img width="653" height="393" alt="image" src="https://github.com/user-attachments/assets/b399155f-73bf-4a07-9c00-6d0528d78e9f" />
</p>
<p>I pressed <b>Enter</b> to start.</p>
<p><img width="460" height="449" alt="image" src="https://github.com/user-attachments/assets/9bfe1139-3861-48ed-ad8a-cd61d69a7ba0" />
</p>
<p>It prompted for Username and Password, thus, I entered <b>kali</b> and selected the <b>Log In</b> button.</p>
<p><img width="500" height="569" alt="image" src="https://github.com/user-attachments/assets/115d5a7a-bd87-4bc4-bc54-dc91f0bcb83c" />
</p>
<p><img width="726" height="404" alt="image" src="https://github.com/user-attachments/assets/1ec24ac0-0fce-46d6-a34e-583351255f87" />
</p>
<p>Inside the Kali desktop, I opened a terminal, entered a command, and pressed <b>Enter</b>;</p>
    
    sudo  apt update  &&  sudo apt upgrade  -y

<p>It prompts to enter the password and that password is <b>kali</b>.</p>
<p><img width="521" height="275" alt="image" src="https://github.com/user-attachments/assets/63771c75-38db-452e-8407-f421967cd3a7" />
</p>
<p><img width="809" height="276" alt="image" src="https://github.com/user-attachments/assets/96324a3e-0ccd-44dd-b126-65a8cfe74e5a" />
</p>
<p>After that, I rebooted Kali to finish the update.</p>
<p><img width="921" height="439" alt="image" src="https://github.com/user-attachments/assets/90c832f6-4ac9-4783-9805-6308a8e37059" />
</p>
<p>After rebooting, I entered a command that would show me its details.</p>
<p><img width="759" height="515" alt="image" src="https://github.com/user-attachments/assets/961fa5fb-35fa-4dfd-a5ef-7e7092c9f6cd" />
</p>

<br>
<h3>D. Ubuntu Server</h3>
<p>I opened the internet and typed <b>Google.com</b> in the browser. After that, I typed <b>ubuntu server download</b>.</p>
<p><img width="889" height="405" alt="image" src="https://github.com/user-attachments/assets/bc14ec2f-ee71-4b2a-afa1-d2e7db1da514" />
</p>
<p>Google provided me some results, but I chose and selected the official <b>Ubuntu</b> Ibsite.</p>
<p><img width="808" height="365" alt="image" src="https://github.com/user-attachments/assets/16bf7f83-33e8-4e54-9e1a-7c9775cb7c77" />
</p>
<p>Inside the <b>Ubuntu</b> platfrom, I clicked on the <b>Download</b> button. It prompted me where to save the file, thus, I chose where the other files intended for virtual machines are located.</p>
<p><img width="706" height="375" alt="image" src="https://github.com/user-attachments/assets/2260884e-53b7-4fdf-84e4-924a43ef6068" />
</p>
<p><img width="690" height="388" alt="image" src="https://github.com/user-attachments/assets/80a76eaf-54d6-4f8b-9f69-80e1c2e873b0" />
</p>
<p>I opened the VirtualBox and selected the <b>New</b> button on top. I entered <b>ubuntu-server as the VM Name, and selected the drop-down for ISO Image to find where the file is located</b>.</p>
<p><img width="792" height="278" alt="image" src="https://github.com/user-attachments/assets/666a1004-8e0a-4039-bf0e-b3b0f3c86b85" />
</p>
<p>I selected <b>6 GB</b> for the RAM or Base Memory with <b>2 Cores</b> for CPUs.</p>
<p><img width="794" height="242" alt="image" src="https://github.com/user-attachments/assets/2ec1bcf3-2d06-4e86-8701-339c6b4071a9" />
</p>
<p>I put <b>80 GB</b> for its Hard Disk Size, which I think is more than enough to run it.</p>
<p><img width="975" height="262" alt="image" src="https://github.com/user-attachments/assets/6395f3f0-f211-4663-a098-2cb3d1a59650" />
</p>
<p>I ran the <b>ubuntu-server</b> to start the installation process.</p>
<p><img width="653" height="358" alt="image" src="https://github.com/user-attachments/assets/72423a70-cd10-46d8-8452-9c16a372bd70" />
</p>
<p>I chose <b>English</b> as the language.</p>
<p><img width="654" height="400" alt="image" src="https://github.com/user-attachments/assets/c71f1b49-1eed-48de-9edf-25bbafc7d66e" />
</p>
<p>I let <b>English</b> for <b>Identify English</b>.</p>
<p><img width="975" height="238" alt="image" src="https://github.com/user-attachments/assets/93833ab6-c1a9-49bb-bea0-7ab2b9de0621" />
</p>
<p>I selected the <b>Ubuntu Server</b> and pressed Enter.</p>
<p><img width="733" height="454" alt="image" src="https://github.com/user-attachments/assets/078fbb06-092f-4bd1-b3f3-0cbb63c7a3aa" />
</p>
<p>I leave as it is and pressed Enter.</p>
<p><img width="975" height="218" alt="image" src="https://github.com/user-attachments/assets/adafc5d9-2d09-43c7-a4a5-5c292ba1e3f9" />
</p>
<p>I did not input any <b>Proxy address</b> and pressed Enter, then let it load up.</p>
<p><img width="975" height="154" alt="image" src="https://github.com/user-attachments/assets/9e8c9699-eaf8-4a93-a0f9-ae6ceacae721" />
</p>
<p><img width="974" height="228" alt="image" src="https://github.com/user-attachments/assets/d3f436ad-7cbd-414d-ab86-bb8caf76463a" />
</p>
<p>For storage configuration, I leave it as it is and press Enter to continue.</p>
<p><img width="975" height="390" alt="image" src="https://github.com/user-attachments/assets/c6066c6a-2295-4107-b1af-1ca4e5a03eb2" />
</p>
<p>I checked the <b>FILE SYSTEM SUMMARY</b> if everything are correct.</p>
<p><img width="661" height="506" alt="image" src="https://github.com/user-attachments/assets/c0698ea2-8cab-4412-85ae-85664dd96ca4" />
</p>
<p>For <b>Profile Configuration</b>, I input all as <b>ubuntu-server</b> with <b>kali</b> as the password.</p>
<p>I skipped upgrading to <b>Ubuntu Pro</b> and moved on.</p>
<p><img width="975" height="210" alt="image" src="https://github.com/user-attachments/assets/406a1cff-52ab-4ddf-a0d5-e185b678bd34" />
</p>
<p>I selected <b>Install OpenSSH server</b> and proceed.</p>
<p>I skipped everything and scrolled down, then selected <b>Done</b> to start to install.</p>
<p><img width="975" height="331" alt="image" src="https://github.com/user-attachments/assets/59b1e715-43ad-4554-82c6-c0fd089226cc" />
</p>
<p><img width="800" height="601" alt="image" src="https://github.com/user-attachments/assets/32d625a1-b424-4401-9ead-24df9fee5cb0" />
</p>
<p>After the installation, I rebooted it.</p>
<p><img width="711" height="717" alt="image" src="https://github.com/user-attachments/assets/4c42d01b-786f-4ed8-8057-2d4839aa77c3" />
</p>
<p>After the system rebooted, I typed a command in order to identify the OS release;</p>
            
    more /etc/os-release
<p><img width="754" height="767" alt="image" src="https://github.com/user-attachments/assets/998c8b05-a512-4f81-8c60-e07bdad3250c" />
</p>
<p><img width="862" height="329" alt="image" src="https://github.com/user-attachments/assets/5e1befb1-0491-4968-9e87-6ea0570fb476" />
</p>
<p>In order to update and upgrade the system, input the command: </p>

    sudo apt update && sudo apt upgrade -y
<p><img width="862" height="121" alt="image" src="https://github.com/user-attachments/assets/b35ee34e-9035-41fe-b708-cac8f098b778" />
</p>
<p><img width="767" height="296" alt="image" src="https://github.com/user-attachments/assets/f06223e0-b1a8-4cc0-997d-1a2430959f56" />
</p>


<br>
<br>
<h3>E. Wazuh (SIEM) </h3>
<p>Before running the <b>Ubuntu Server</b> and <b>Kali Linux</b>, I tIaked the network connections for the three VMs, so that they communicate in the same network.</p>
<p><img width="736" height="316" alt="image" src="https://github.com/user-attachments/assets/6c32d01d-9620-4244-ad93-00ed3bbfc986" />
</p>
<p>I selected the <b>Tools</b> and chose <b>Network</b>.</p>
<p><img width="694" height="549" alt="image" src="https://github.com/user-attachments/assets/c40378a7-995b-4976-94f6-5ea814819b9e" />
</p>
<p>First, I selected the <b>NAT Network</b> tab, changed the Name to <b>SOC-Home-Lab</b>, then clicked on Apply button</b>. It provided an IP range of <b>10.0.2.0/24</b>.</p>
<p><img width="835" height="448" alt="image" src="https://github.com/user-attachments/assets/67baa934-fccc-4270-907a-70e14ee038c8" />
</p>
<p>I changed the settings for each of the VMs. In the <b>Network</b>, I replaced the <b>NAT</b> with <b>NAT Network</b> and automatically selected the <b>SOC-Home-Lab</b>, then pressed the <b>OK</b> button.</p>
<p><img width="975" height="558" alt="image" src="https://github.com/user-attachments/assets/e6d6949f-55cf-4d56-816e-7406c4388c78" />
</p>
<p>I opened <b>Ubuntu Server</b> to start the installation of <b>Wazuh</b>.</p>
<p><img width="724" height="507" alt="image" src="https://github.com/user-attachments/assets/cd974bb9-d6b5-452f-b0dc-f7f04685bf2a" />
</p>
<p>While <b>Ubuntu Server</b> is running, I opened Google to look for <b>Wazuh</b> installation, thus, I typed in its search bar <b>wazuh siem</b>.</p>
<p><img width="799" height="393" alt="image" src="https://github.com/user-attachments/assets/2da0ce0e-bbec-4be8-baf4-65bcdf8b56be" />
</p>
<p>Google provided me with some results, and I selected the official website of <b>Wazuh</b>.</p>
<p><img width="933" height="344" alt="image" src="https://github.com/user-attachments/assets/7e9afcb8-07a8-496d-bd70-e606c24503ca" />
</p>
<p>Inside Wazuh's Ibsite, I clicked on <b>Install Wazuh</b> button.</p>
<p><img width="975" height="455" alt="image" src="https://github.com/user-attachments/assets/de591e32-0bd6-4636-b900-b36740004ab3" />
</p>
<p>I scrolled down and selected the <b>Quickstart</b> button.</p>
<p><img width="975" height="229" alt="image" src="https://github.com/user-attachments/assets/f2d73b0f-c135-4d3b-97ee-2738e2216c43" />
</p>
<p>After that, it provided me with a command to input in Ubuntu Server's CLI and run the said command, which is the;</p>

      curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh && sudo bash ./wazuh-install.sh -a

<p><img width="975" height="304" alt="image" src="https://github.com/user-attachments/assets/061b1a0b-8b18-4512-b36b-2887173e3acb" />
</p>
<p><img width="975" height="169" alt="image" src="https://github.com/user-attachments/assets/277d1742-3d2b-4c35-8358-6aec0ce07dd4" />
</p>
<p>After installation, it provided me with <b>User</b> and <b>Password</b> credentials.</p>
<p><img width="1011" height="203" alt="image" src="https://github.com/user-attachments/assets/5daa1651-1753-4d8a-ace4-749007d5576d" />
</p>
<p>It also provided me with the URL to input into the browser, but I need to replace the <b><wazuh-dashboard-ip></b>.</p>

    ip addr  OR  ip a

<p><img width="975" height="202" alt="image" src="https://github.com/user-attachments/assets/1e63b125-28af-4c0e-b13b-4eba60341678" />
</p>
<p>I typed the  <b>ip a</b>  command to know what the IP address would be for the Wazuh dashboard. Alternatively, I typed  <b>ip addr</b>, which gave me the same result. </p>
<p><img width="850" height="247" alt="image" src="https://github.com/user-attachments/assets/937e43d6-e9e0-481e-b2f1-74984c2e5451" />
</p>
<p>Before I started running Wazuh, I entered several commands that needed to run it seamlessly, such as: </p>

    sudo  systemctl  stop  wazuh-dashboard  wazuh-manager  wazuh-index

<p>After that, I start them back up one by one, waiting 10-15 seconds between each command;</p>

    sudo  systemctl  start  wazuh-indexer
    sudo  systemctl  start  wazuh-manager
    sudo  systemctl  start  wazuh-dashboard

<p><img width="946" height="147" alt="image" src="https://github.com/user-attachments/assets/438e55fc-6ca8-4e57-85ef-472a82d91c68" />
</p>

<p>Or, simply this instead:</p>

    sudo systemctl start wazuh-indexer wazuh-manager wazuh-dashboard
<p><img width="762" height="57" alt="image" src="https://github.com/user-attachments/assets/471dd009-a1f8-4642-82b6-52e3f7cff075" />
</p>



<p>Now, I verified the API daemon is active by checking if the manager and backend API are running properly using the command:</p>

    sudo  systemctl  status  wazuh-manager
    
<p>Since it says <b>active (running)</b>, tail the API log file to make sure there are no internal credentials or structural errors blocking the link by typing:</p>

    sudo  tail  -n  20  /var/ossec/logs/api.log
    
<p><img width="780" height="467" alt="image" src="https://github.com/user-attachments/assets/69912a94-6a4d-41fa-841b-8ed8494d2749" />
</p>
<p><b>Wazuh</b> Wazuh is highly resource-intensive. My Ubuntu VM has <b>6 GB</b> of RAM allocated; the API daemon will crash silently under an <b>Out of Memory (OOM)</b> exception. I cleared the RAM cache immediately using:</p>

      sudo  sync;  echo  3  |  sudo  tee  /proc/sys/vm/drop_caches
      
<p>Lastly, I also checked how much RAM is consumed and remaining by typing:</p>

    free -h
<p>
</p>
<p> For me to open the dashboard, I launched a <b>Kali Linux</b> machine where I can use <b>Mozilla Firefox</b> for the internet and input the URL with the IP to test if it will launch the <b>Wazuh Dashboard</b>. I preferred to use Kali Linux because it consumes less RAM than running Wazuh in Windows 10; however, Wazuh can run in Windows 10 as well. </p>
<p><img width="975" height="463" alt="image" src="https://github.com/user-attachments/assets/c9a9cee7-8f6d-4c00-b3f0-c07bac3016dd" />

</p>
<p><img width="540" height="340" alt="image" src="https://github.com/user-attachments/assets/ab2b551f-6c5d-42df-940d-134d6bf3762a" />

</p>
<p><img width="702" height="409" alt="image" src="https://github.com/user-attachments/assets/e6e91b60-da49-4f38-a4bd-f83211e2d547" />
</p>
<p><img width="765" height="239" alt="image" src="https://github.com/user-attachments/assets/4e040e19-c256-438e-abe0-54c627b9d3d7" />
</p>
<p>I entered the credentials given from the Ubuntu Server earlier and selected <b>Log In</b> and let it load up.</p>
<p><img width="426" height="359" alt="image" src="https://github.com/user-attachments/assets/36206c4d-64f0-4e9e-90e7-81187df990cc" />
</p>
<p><img width="601" height="354" alt="image" src="https://github.com/user-attachments/assets/90eb6575-9fe5-4abe-be94-ff959ae7805f" />
</p>
<p><img width="975" height="502" alt="image" src="https://github.com/user-attachments/assets/c45f5302-bf3a-4a48-8975-e5b11167e06e" />
</p>
<p> If I shut down the VMs, both <b>Kali Linux</b> (where I opened the Wazuh dashboard) and <b>Ubuntu Server</b> (to start running Wazuh), and want to run Wazuh again, I typed this command to see if the services are running on their own:</p>

    sudo systemctl status wazuh-manager wazuh-indexer wazuh-dashboard
    
<p>If I see <b>active (running)</b> in green for all three, I can immediately type the HTTPS URL into the Kali Linux browser.</p>
<p>If the status command shows that the services are <b>inactive</b> or <b>stopped</b>, I would run this command on my Ubuntu Server to force them to start:</p>

    sudo systemctl start wazuh-indexer wazuh-manager wazuh-dashboard

<p>To exit from the status, simply press <b><i>q</i></b> key to exit</p>
<br>
<br>
<p><b>NOTE #1:</b>  If you wanted to move from a regular user into root privileges, type:</p>

    sudo su -
<p><img width="975" height="97" alt="image" src="https://github.com/user-attachments/assets/888d5bc7-9df4-4f08-a317-a1e817c528f3" /></p>

<br>
<br>
<p><b>NOTE #2:</b> If you forgot your password or wanted to know about the credentials of the Ubuntu Server (which you will be using to access Wazuh), type the command:</p>

    ls
<p><img width="750" height="84" alt="image" src="https://github.com/user-attachments/assets/e3c4b517-a600-49d8-a0de-fb63ccf93cb3" /></p>

<p>In order to extract the <b><i>wazuh-install-files.tar</i></b>  file, type the command:</p>

    sudo tar -xf wazuh-install-files.tar
<p><img width="884" height="71" alt="image" src="https://github.com/user-attachments/assets/04b22d74-91c5-41de-8bb6-142b41e92440" /></p>

<p>Open the  <b><i>wazuh-install-files</i></b>  by typing:</p>

    cat  wazuh-install-files
<p><img width="975" height="131" alt="image" src="https://github.com/user-attachments/assets/4aa519af-3c91-482b-9acb-66b150b32d12" /></p>

<p>Now, open the  <b><i>wazuh-passwords.txt</i></b>  by typing:</p>

    sudo  cat  wazuh-passwords.txt
<p><img width="747" height="507" alt="image" src="https://github.com/user-attachments/assets/efaf72d6-e18c-49bf-8174-4422cc755005" /></p>

<br>
<br>
<p><b>Note #3:</b> By default, Wazuh only indexes events that trigger security alerts to save disk space. Enabling the archive feature provides a complete, unmodified history of your environment's log data.</p>
<p>Wazuh archive is used to automatically store all security events and logs received by the Wazuh server, regardless of whether they trigger an alert or trip a specific rule. It essentially allows Wazuh to monitor and capture all the telemetry that I throw at it.</p>
<h4>Procedures:</h4>
<ul>
  <li>I want to configure the <b><i>ossec.conf</i></b> file.</li>
  <li>In order to find that file, it is located under the <b><i>/var/ossec</i></b> directory</li>

      sudo ls -la /var/ossec
  <p><img width="819" height="397" alt="image" src="https://github.com/user-attachments/assets/5b946534-e7a5-40a2-b7fa-178ac8e98cf2" /></p>

 <li>I changed into root privileges</li>

     sudo su -

  <li>I opened the <b><i>/var/ossec/etc</i></b> and I should see the file <b><i>ossec.conf</i></b></li>
  
    cd /var/ossec/etc
  <p><img width="907" height="90" alt="image" src="https://github.com/user-attachments/assets/0c29df53-ca60-48d3-9782-ae8dc6573782" /></p>

<li>This time, I opened the <b><i>ossec.conf</i></b> file.</li>

    nano ossec.conf
<p><img width="832" height="92" alt="image" src="https://github.com/user-attachments/assets/5ac97a49-725c-4012-a6e7-2068deeebf77" /></p>
<p><img width="742" height="760" alt="image" src="https://github.com/user-attachments/assets/f3f86370-775d-444d-8823-0fd7eaf668e7" />
</p>

<li>I changed the <b><i>logall</i></b> and <b><i>logall_json</i></b>, from <b><i>no</i></b> into <b><i>yes</i></b>. Save it by holding the CTRL+X, press Y to save, and press Enter.</li>
<p><img width="615" height="382" alt="image" src="https://github.com/user-attachments/assets/235ba3e7-3547-4885-bc2c-9155139e2083" />
</p>

<li>After that, restart the manager by typing:</li>

    systemctl restart wazuh-manager.service

<li>The next thing to do is to modify the <b>filebeat configuration</b>. I need to change the directory to <b><i>/etc/filebeat/</i></b>.</li>

    cd /etc/filebeat
<p><img width="497" height="40" alt="image" src="https://github.com/user-attachments/assets/eb39d735-8816-4c86-b719-1bb62ba1341f" /></p>

<li>Open the <b><i>/etc/filebeat/</i></b> by typing:</li>

    ls -la
<p><img width="567" height="186" alt="image" src="https://github.com/user-attachments/assets/7d8596ab-89dc-4961-a439-62e574abe216" /></p>

<li>Now, open the <b><i>filebeat.yml</i></b></li>

    nano filebeat.yml
<p><img width="652" height="52" alt="image" src="https://github.com/user-attachments/assets/1b08784f-bc2b-4271-945e-7f1b78b54dd1" /></p>
<p><img width="580" height="720" alt="image" src="https://github.com/user-attachments/assets/3c182765-d532-4096-8f78-da46e4922bf4" />
</p>

<li>Change the <b><i>archives</i></b> from <b><i>false</i></b> into <b><i>true</i></b>. Save it by holding CTRL+X, press Y to save, and press Enter.</li>
<p><img width="412" height="127" alt="image" src="https://github.com/user-attachments/assets/53a160da-c812-49fc-999f-86d2fe2a1cda" />
</p>

<li>Restart the <b>Filebeat service</b> by typing:</li>

    systemctl restart filebeat.service

<p><img width="587" height="50" alt="image" src="https://github.com/user-attachments/assets/9252845d-0a9d-4086-b292-554a67e6f0d2" /></p>

<li>Now, go back to the Wazuh dashboard and head over to the hamburger icon, scroll down to select <b><i>Dashboard Management</i></b>, then select <b><i>Index patterns</i></b>.</li>
<p><img width="660" height="406" alt="image" src="https://github.com/user-attachments/assets/ab066f37-af97-42d1-b1f2-d424e34fb637" /></p>
<p><img width="448" height="771" alt="image" src="https://github.com/user-attachments/assets/fb197700-0511-4e5b-aa4f-ea50903b5c6d" />
</p>
<p><img width="954" height="287" alt="image" src="https://github.com/user-attachments/assets/b6473007-9e74-4a4d-93ce-f01d68e8e043" />
</p>

<li>Inside the <b>Index patterns</b>, select the <b><i>Create index pattern</i></b> button.</li>
<p><img width="955" height="187" alt="image" src="https://github.com/user-attachments/assets/bac14b7a-3c6e-400c-a829-f601ae952f2c" />
</p>

<li>Inside <b><i>Create index pattern</i></b>, type in the search bar, <b><i>wazuh-archives</i></b>. I should see the <b><i>wazuh-archives</i></b> result at the bottom. After that, press the <b>Next step</b> button</li>
<p><img width="937" height="497" alt="image" src="https://github.com/user-attachments/assets/7ac39bde-5fbd-4726-ab68-d354121e79c8" />
</p>

<li>On the <b><i>Time field</i></b>, dropdown and select <b><i>timestamp</i></b>, and select the <b><i>Create index pattern</i></b> button.</li>
<p><img width="952" height="547" alt="image" src="https://github.com/user-attachments/assets/3cc80c29-5255-4a83-88e1-93b23e9f2e2e" /></p>
<p><img width="960" height="760" alt="image" src="https://github.com/user-attachments/assets/19cc2f87-e2d2-4e93-a134-becec519295b" />
</p>

<li>Go back to hamburger icon, select <b>Discover</b>, select <b>Explore</b>, select the dropdown and I should see the <b><i>wazuh-archives</i></b>.</li>
<p><img width="960" height="189" alt="image" src="https://github.com/user-attachments/assets/ef9231d8-895d-4ae4-912a-0c1f3c5ecacc" />
</p>
<p><img width="522" height="437" alt="image" src="https://github.com/user-attachments/assets/13caddb9-17ed-413d-8a31-559cdbd7c436" />
</p>
<p><img width="957" height="277" alt="image" src="https://github.com/user-attachments/assets/8cada3e2-f8a9-41a5-a58a-d08845eb4435" />
</p>
<p><img width="947" height="741" alt="image" src="https://github.com/user-attachments/assets/45d40d30-611f-4f00-8bbd-8f16ed4292d3" />
</p>


<li>On the <b>Wazuh server</b>, I increased the <b><i>timeout</i></b> by typing, <b><i>sudo su -</i></b> to change into root user and locate the <b><i>wazuh.yml</i></b> by typing:</li>

    cd /usr/share/wazuh-dashboard/data/wazuh/config/
    ls
    nano wazuh.yml

<p><img width="809" height="150" alt="image" src="https://github.com/user-attachments/assets/b2e7d946-4aa5-4776-a8e7-6d226cb02766" />
</p>
<p>After that, I modified the <b><i>timeout</i></b> limit from <b>20000ms</b> into <b>90000ms</b> and saved.</p>
<p><img width="859" height="277" alt="image" src="https://github.com/user-attachments/assets/2dcd4eaa-3e05-49d2-932d-02444beef4bc" />
</p>

<li>Lastly, I selected the <b>Machine</b> tab, select <b><i>Take Snapshot...</i></b>, rename it of your choice, and press the <b>OK</b> button. The description is optional.</li>
<p><img width="605" height="347" alt="image" src="https://github.com/user-attachments/assets/8d936543-821a-4f8f-8725-81e822206ca7" />
<p><img width="496" height="447" alt="image" src="https://github.com/user-attachments/assets/88e732c8-1260-414f-8854-72e98cc30872" />
</p>
</p>
</ul>

<br>   
<br>
<h3>F. Deploying Wazuh Agents on Windows Endpoints</h3>
<p>I let Ubuntu Server with Wazuh up and running to check if the Wazuh Agent would run successfully using the graphical user interface (GUI), which I needed to download. I opened the Windows 10 machine and used Internet Explorer to download the agent.</p>
<p><img width="752" height="602" alt="image" src="https://github.com/user-attachments/assets/58dacc18-469a-4862-b148-69d97b360a54" />
</p>
<p>In the Internet Explorer's browser, I input <b>Google.com</b>. On Google's website, I entered <b>wazuh agent gui</b>.</p>
<p><img width="975" height="411" alt="image" src="https://github.com/user-attachments/assets/7b73adbe-b464-42f8-ab7e-621eef23e2a3" />
</p>
<p>I selected the official Ibsite, which leads me to its platform.</p>
<p><img width="975" height="340" alt="image" src="https://github.com/user-attachments/assets/f360aadb-345e-4c55-be27-f53b1c49fe69" />
</p>
<p>Inside Wazuh's Ibsite, there are two choices, <b>CLI</b> or <b>GUI</b>. I chose the GUI tab, then downloaded the installer using the provided link.</p>
<p><img width="525" height="369" alt="image" src="https://github.com/user-attachments/assets/53946e6e-fea7-42cf-b139-cfea908237aa" />
</p>
<p>It prompted me to start the installation process and follow along.</p>
<p><img width="517" height="369" alt="image" src="https://github.com/user-attachments/assets/6377834a-dccf-40ae-8b43-4c1249634c63" />
</p>
<p>I ticked the box before pressing the <b>Finish</b> button, so that the Wazuh Agent app runs.</p>
<p><img width="522" height="370" alt="image" src="https://github.com/user-attachments/assets/f750fc2e-4245-4dc5-9a2c-2ff7e2d20eb7" />
</p>
<p>I input Wazuh's IP address and pressed <b>Save</b> button.</p>
<p><img width="825" height="520" alt="image" src="https://github.com/user-attachments/assets/7032e6d9-bdfd-4e60-b9f4-d729fbcd83e8" />
</p>
<p>I clicked the <b>Manage</b> button at the top and selected <b>Start</b> to start the Wazuh Agent to communicate back to its dashboard. After that, I pressed the <b>OK</b> button.</p>
<p><img width="975" height="587" alt="image" src="https://github.com/user-attachments/assets/9b49c12a-77b8-43cb-9465-ef685505a2c7" />
</p>
<p><img width="968" height="591" alt="image" src="https://github.com/user-attachments/assets/e17a5757-5400-4e88-a360-629eadedb82c" />
</p>
<p>Going back to the Wazuh Dashboard and refreshing, the Wazuh Agent successfully installed and did its job, and registered the Windows 10 machine in the dashboard.</p>
<p><img width="975" height="693" alt="image" src="https://github.com/user-attachments/assets/ac103e72-30f8-4fac-9c7b-fa468413a97d" />
</p>
<p>In the <b>Agent’s Summary</b> section, I selected <b>Active</b>, and it led me to more information about Windows 10’s system in real-time.</p>
<p><img width="975" height="476" alt="image" src="https://github.com/user-attachments/assets/1b09eac0-fa3a-4c1a-ad0e-b7cd5c9615c0" />
</p>
<p>Based on the result, I clicked on the <b>Operating system</b> at the bottom and showed more specific information.</p>
<p><img width="706" height="501" alt="image" src="https://github.com/user-attachments/assets/7856480f-65f2-4327-89ac-7c57f58a904d" />
</p>

<br>
<h3>G. Sysmon</h3>
<p>Using the Windows 10 machine, I opened Internet Explorer to access Google to search <b>Microsoft Sysmon</b>.</p>
<p><img width="568" height="469" alt="image" src="https://github.com/user-attachments/assets/648e8b6f-7287-42ce-93ae-88643a96cede" />
</p>
<p>Inside the Google Ibsite, I entered <b>Microsoft sysmon download</b> in the search bar.</p>
<p><img width="903" height="387" alt="image" src="https://github.com/user-attachments/assets/86525b5c-e338-444d-b7c8-ac285cce2c00" />
</p>
<p>I selected the official Ibsite of Microsoft to download the app. </p>
<p><img width="940" height="446" alt="image" src="https://github.com/user-attachments/assets/a1ff9aba-11f9-4322-a996-e352e5911c27" />
</p>
<p>I clicked on the link and automatically downloaded the file.</p>
<p><img width="773" height="625" alt="image" src="https://github.com/user-attachments/assets/d8f00695-e71f-49c2-a303-ea818a5879fb" />
</p>
<p>After downloading the Sysmon app, I opened another browser for the module and typed: </p>

    github.com/olafhatong/sysmon-modular/blob/master/sysmonconfig.xml
    
<p><img width="975" height="262" alt="image" src="https://github.com/user-attachments/assets/7e5fc92e-2495-4739-b155-df92f22dedd3" />
</p>
<p>After being directed to the website, I selected the <b>raw</b>button and right-clicked the page to download it by selecting <b>Save as</b>. I changed the name to <b>sysmonconfig</b> and chose <b>xml</b> as the type of the file.</p>
<p><img width="975" height="444" alt="image" src="https://github.com/user-attachments/assets/2e4fd378-9172-432a-aa80-ca6318c9919f" />
</p>
<p>I preferred to save in <b>Downloads</b>, renamed it to <b>sysmonconfig</b> and I make sure that the file would be <b>xml</b>, and pressed the <b>Save</b> button.</p>
<p><img width="764" height="584" alt="image" src="https://github.com/user-attachments/assets/1692dd19-0c7a-456e-837d-3cc05a13adee" />
</p>
<p>The next thing I did was to extract the <b>Sysmon</b> zip file and save it to the same folder, but housed in a new folder named <b>Sysmon</b>.</p>
<p><img width="789" height="464" alt="image" src="https://github.com/user-attachments/assets/036328db-b6e7-452e-bee9-a21ed530242d" />
</p>
<p><img width="752" height="590" alt="image" src="https://github.com/user-attachments/assets/782bdf54-a201-48d4-a840-7de4badd37f7" />
</p>
<p><img width="975" height="330" alt="image" src="https://github.com/user-attachments/assets/f6301039-277a-48b4-9297-a6c31143850a" />
</p>
<p>Instead of executing the file after the extraction, I opened <b>Windows PowerShell (Admin)</b> instead.</p>
<p><img width="712" height="699" alt="image" src="https://github.com/user-attachments/assets/6a2b3abd-a66d-4cbc-8a06-d1c2bf269eba" />
</p>
<p>I copied the extracted file's location and pasted it into the PowerShell command line, then pressed Enter. In the PowerShell CLI, it should show the current location.</p>
<p><img width="975" height="441" alt="image" src="https://github.com/user-attachments/assets/9a5f9ba9-0519-4f14-b101-bbd7900f3562" />
</p>
<p><img width="805" height="197" alt="image" src="https://github.com/user-attachments/assets/ac506537-a674-4975-bbf5-272b53ae4515" />
</p>
<p><img width="860" height="226" alt="image" src="https://github.com/user-attachments/assets/ea29abcd-2c18-45f6-aab8-35cc67f69033" />
</p>
<p>I cut the <b>sysmonconfig</b> file and pasted in the same folder where the extracted files are located.</p>
<p><img width="656" height="377" alt="image" src="https://github.com/user-attachments/assets/4a9c3a03-b0b2-4422-ad18-ef2f4160960f" />
</p>
<p>I opened the PoIrShell CLI again then typed, <b>ls</b>  command to make sure everything are intact.</p>
<p><img width="650" height="352" alt="image" src="https://github.com/user-attachments/assets/a769a0f2-0dd9-47cb-8cf9-aaa6948dc013" />
</p>
<p>Based on the result, there are a couple of executable files; thus, I chose and executed the <b>Sysmon64.exe</b> file in PoIrShell.</p>
<p><img width="601" height="337" alt="image" src="https://github.com/user-attachments/assets/56f71dea-cee4-4bab-a889-a74ab80656a6" />
</p>
<p>The result should show information on how to do installation and update; thus, I installed the <b>Sysmon64.exe</b> and <b>sysmonconfig.xml</b> by typing: </p>

    .\Sysmon64.exe  -i  .\sysmonconfig.xml
    
<p><img width="975" height="682" alt="image" src="https://github.com/user-attachments/assets/98d30245-7c67-4e09-9756-e476abfc1257" />
</p>
<p><img width="827" height="252" alt="image" src="https://github.com/user-attachments/assets/6846ad7a-1c04-460c-9ea4-d0bdd23bd846" />
</p>
<p>It prompted me to agree to the license of Sysmon Monitor and selected the <b>Agree</b> button, then let it load up.</p>
<p><img width="975" height="842" alt="image" src="https://github.com/user-attachments/assets/b0890607-d2a9-4f0c-8868-f283bf5052af" />
</p>
<p><img width="802" height="344" alt="image" src="https://github.com/user-attachments/assets/a2fe4c47-d58f-4bd9-8d0d-2e1dfcf94432" />
</p>
<p>Now, I opened <b>Services</b> in Windows 10 if it successfully executed by typing <b>services</b> in search bar, then select the <b>Services App</b> result.</p>
<p><img width="699" height="630" alt="image" src="https://github.com/user-attachments/assets/6e50b906-4fa2-4c66-8e56-f5236318ccac" />
</p>
<p>After I opened <b>Services</b> app, I located the <b>Sysmon </b> if it is installed in the said app. Luckily, <b>Sysmon </b>has been installed successfully.</p>
<p><img width="975" height="723" alt="image" src="https://github.com/user-attachments/assets/1e61b78e-69dd-4cb0-8314-329def7fd1d3" />
</p>
<p<img width="975" height="648" alt="image" src="https://github.com/user-attachments/assets/48e861c6-9f68-46c6-a95b-5a10abea6e1b" />
></p>
<p>This time, I entered <b>Event VieIr</b> in the search bar to check if <b>Sysmon</b> installed and saved from there.</p>
<p><img width="792" height="841" alt="image" src="https://github.com/user-attachments/assets/3805d84b-4ada-448e-9237-d0cde9fd9391" />
</p>
<p>Inside the <b>Event VieIr</b>, I dropped down the <b>Application and Services Logs</b>, selected <b>Microsoft</b>, selected <b>Windows</b>, then scrolled-down to check if the folder of <b>Sysmon</b> is there. So, the folder of <b>Sysmon</b> is there and fully functional, which provides information or telemetry in real-time on the system.</p>
<p><img width="922" height="434" alt="image" src="https://github.com/user-attachments/assets/c091ea9f-45b4-4f5c-9211-49306448f9aa" />
</p>
<p><img width="975" height="758" alt="image" src="https://github.com/user-attachments/assets/64109602-36bc-4acd-86eb-0b152e5a6b23" />
</p>

<br>
<h3>H. Wazuh Agent & Sysmon Connection</h3>
<p>On the left pane, the <b>Available Fields</b>, i selected the <b>agent.name</b>, and selected <b>Windows 10</b>.</p>
<p><img width="890" height="437" alt="image" src="https://github.com/user-attachments/assets/76c8b95b-82fb-4d1d-8868-e4eaf37212a5" />
</p>
<p><img width="715" height="325" alt="image" src="https://github.com/user-attachments/assets/5a2c13b4-0df6-4e5c-b020-df97db95477b" />
</p>
<p><img width="785" height="432" alt="image" src="https://github.com/user-attachments/assets/344eb7c1-4b4b-42c9-ab39-522d6fedf104" />
</p>
<p>I typed in the search bar for <b>Sysmon</b> but it shows no result. I found <b>397 hits</b>, but that is coming from our Sysmon service, rather than events generating from Sysmon</p>
<p><img width="965" height="640" alt="image" src="https://github.com/user-attachments/assets/62fb6bb9-805c-4e77-ab57-c813a60b1a46" />
</p>
<p>I don’t see any events sourced from Sysmon yet; it’s because, in Wazuh and even in any other SIEM, I need to configure its settings to instruct the agent to push Sysmon data.</p>
<p><img width="975" height="288" alt="image" src="https://github.com/user-attachments/assets/4e8ffd19-b531-4a54-b124-de9c923d8b41" />
</p>
<p>I opened Notepad and selected the <i>Run as administrator</i>.</p>
<p><img width="600" height="495" alt="image" src="https://github.com/user-attachments/assets/289987e2-f772-449c-bf4c-bc166334503c" />
</p>
<p>I selected <b>File</b> and chose <b>Open.</b> The reason for this is to find the Wazuh agent configuration settings.</p>
<p><img width="554" height="284" alt="image" src="https://github.com/user-attachments/assets/c3242038-6596-4d85-ab3b-9b3c5f4d5da8" />
</p>
<p>I selected the <b>This PC</b> on the left pane and the <b>C:</b> drive.</p>
<p><img width="726" height="414" alt="image" src="https://github.com/user-attachments/assets/a0a74c80-c6a8-4977-ab2b-88753c3abc0a" />
</p>
<p>I selected the <b>Program Files (x86)</b>.</p>
<p><img width="740" height="446" alt="image" src="https://github.com/user-attachments/assets/3d3ff48a-f70d-4e16-90df-2772eb00b6bd" />
</p>
<p>I selected the <b>ossec-agent</b>.</p>
<p><img width="744" height="450" alt="image" src="https://github.com/user-attachments/assets/79c480d5-f627-4547-8dfb-1b423c79b8ae" />
</p>
<p>Inside the ossec-agent folder, I selected <b>All Files</b> at the bottom right to show all results, in order to find the <b>ossec.conf</b> file and select it.</p>
<p><img width="739" height="451" alt="image" src="https://github.com/user-attachments/assets/f1627357-0377-4a56-8783-28f1caf6acd6" />
</p>
<p><img width="740" height="457" alt="image" src="https://github.com/user-attachments/assets/aedd696e-56a9-436d-bcfa-3f14ddb20479" />
</p>
<p>And this is how the <b>ossec configuration</b> would look like.</p>
<p><img width="975" height="513" alt="image" src="https://github.com/user-attachments/assets/6b5e2679-a337-4ddd-b650-f268fc0889ae" />
</p>
<p>Now, I copied the <b>Application</b> log file and pasted it next to it and replaced the word <b><i>Application</i></b> later on, in order to point to Sysmon.</p>
<p><img width="975" height="771" alt="image" src="https://github.com/user-attachments/assets/b5ddaf8b-1cc5-43e5-9a6c-8d4980852ab0" />
</p>
<p><img width="975" height="812" alt="image" src="https://github.com/user-attachments/assets/5bb60127-877a-41ed-98af-441c7e7b2362" />
</p>
<p>Next, I opened <b>Event Viewer</b>, selected <b>Applications and Services Logs</b>, selected <b>Microsoft</b>, dropped down Windows, and scrolled down to find Sysmon.</p>
<p><img width="975" height="534" alt="image" src="https://github.com/user-attachments/assets/b3032e5f-bf13-4d7f-9f37-a8541a9a9a2e" />
</p>
<p><img width="975" height="684" alt="image" src="https://github.com/user-attachments/assets/ec210255-9e71-4b5d-b369-e70bf06ba912" />
</p>
<p><img width="975" height="680" alt="image" src="https://github.com/user-attachments/assets/6a087a38-49a8-4477-b4b7-c1f2fc4f253e" />
</p>
<p><img width="621" height="509" alt="image" src="https://github.com/user-attachments/assets/56b13c7b-7be7-47ac-9c30-45e9e996cd21" />
</p>
<p>After that, I dropped down <b>Sysmon</b>, and the <b>Operational</b> event log showed up. I right-clicked on it and selected <b>Properties.</b></p>
<p><img width="975" height="589" alt="image" src="https://github.com/user-attachments/assets/7dba597d-b7e1-47d7-a203-a1170a54c140" />
</p>
<p><img width="700" height="652" alt="image" src="https://github.com/user-attachments/assets/4c2805c9-8937-4d4c-bf78-47a248b49ec7" />
</p>
<p>I copied the <i>Full Name</i> (<b>Microsoft-Windows-Sysmon/Operational</b>), pasted the copied log file into Notepad, then replaced <b><i>Operational</i></b> with <b><i>Microsoft-Windows-Sysmon/Operational</i></b>  and saved.</p>
<p><img width="787" height="537" alt="image" src="https://github.com/user-attachments/assets/abc22c3a-d60a-4ad0-a96d-4a52701eb4de" />
</p>
<p><img width="789" height="414" alt="image" src="https://github.com/user-attachments/assets/95b3fd90-2610-4736-85f5-b3e93ee2f791" />
</p>
<p><img width="975" height="585" alt="image" src="https://github.com/user-attachments/assets/2abf58dc-7004-4246-a9da-ea6dcaa6f7bb" />
</p>
<p><img width="975" height="606" alt="image" src="https://github.com/user-attachments/assets/59d31bfc-c7f7-4504-9eb9-991e8b6ab586" />
</p>
<p><img width="872" height="421" alt="image" src="https://github.com/user-attachments/assets/1116d1a9-b4f2-4a15-bf1a-37a014cb97ec" />
</p>
<p>After that, I opened the <b>Services</b> and selected Wazuh, then restarted its service.</p>
<p><img width="975" height="633" alt="image" src="https://github.com/user-attachments/assets/4150ec48-7669-4f49-b6ef-8cb188a43aa5" />
</p>
<p><img width="975" height="638" alt="image" src="https://github.com/user-attachments/assets/21d79fbd-3035-4d33-862e-5f7ddead4263" />
</p>
<p>Going back to the Wazuh dashboard, I restarted or refreshed it as well.</p>
<p><img width="694" height="527" alt="image" src="https://github.com/user-attachments/assets/16a8e101-4a73-41e2-96e2-4af5fc0cb5af" />
</p>
<p>As you can see, there are <b>740 hits</b> now. Not only that, it is now sourcing from Sysmon because when I dropped down and expanded the <b>Event</b> and scrolled down, it shows up that it came from <b>Microsof-windows-Sysmon/Operational</b>.</p>
<p><img width="950" height="471" alt="image" src="https://github.com/user-attachments/assets/21a18d0f-bcc1-4c57-b7e5-073aeafe09c7" />
</p>


<br>
<h3>I. Generate & Read Telemetry</h3>
<p>In order to test and generate telemetry, I opened the command prompt on the Windows machine.</p>
<p><img width="827" height="737" alt="image" src="https://github.com/user-attachments/assets/327b0f40-8bef-4b29-9ec9-bc44e5398713" />
</p>
<p>I added a user named “<b><i>TestUser</i></b>”  and the password  “<b><i>pass123</i></b>” by typing:</p>

    net user TestUser pass123 /add
<p><img width="502" height="237" alt="image" src="https://github.com/user-attachments/assets/1c1fb83b-afcb-4182-8939-3bfc80c8155f" />
</p>

<p>After that, I added the new user to the local group of administrators by typing:</p>

    net  localgroup  administrators  TestUser  /add
<p><img width="584" height="177" alt="image" src="https://github.com/user-attachments/assets/1e3e5a2a-147c-4a1a-b47d-cce09b8e07d9" />
</p>
<p>In order to check and see if the new user was added, I typed:</p>

    net  localgroup  administrators
<p><img width="802" height="312" alt="image" src="https://github.com/user-attachments/assets/7eb10343-02c1-42c0-88b3-925883e3e7cd" />
</p>
<p>To delete the new user for some reason, I typed:</p>

    net user TestUser /delete
<p><img width="434" height="171" alt="image" src="https://github.com/user-attachments/assets/17834eac-c4fc-4185-8d8b-14cc5ee7f5a1" />
</p>
<p>By running all of these commands on the Windows VM, these should be tracked in the Wazuh dashboard.</p>
<p><img width="975" height="440" alt="image" src="https://github.com/user-attachments/assets/9191c689-9494-49e4-8a7f-d49ebd81ed2a" />
</p>
<p>I changed the time by at least 15 minutes in order to cut the noise.</p>
<p><img width="975" height="148" alt="image" src="https://github.com/user-attachments/assets/05b107ab-66d5-4310-87db-db662b2a014c" />
</p>
<p><img width="975" height="301" alt="image" src="https://github.com/user-attachments/assets/03fe1563-2d8f-40fe-a608-8a923ead4c8c" />
</p>
<p><img width="975" height="465" alt="image" src="https://github.com/user-attachments/assets/633009ab-6a1c-4d9c-a9cd-1fb4ea946cd7" />
</p>
<p>I expanded the first event.</p>
<p><img width="972" height="365" alt="image" src="https://github.com/user-attachments/assets/d81bce04-d068-463f-959f-7de339861e18" />
</p>
<p>There is this Windows event ID “<b><i>4726</i></b>”. </p>
<p><img width="712" height="387" alt="image" src="https://github.com/user-attachments/assets/f231bc79-2ec2-47ae-aa54-6ec17ffceb17" />
</p>
<p>I researched what does the Windows Event ID 4726 means. This means that “<i>A user account was deleted</i>”, which is the activity what I did from the Windows VM, deleting the new user.</p>
<p><img width="975" height="291" alt="image" src="https://github.com/user-attachments/assets/6c981b4a-c90a-4243-88a6-488521b7c785" />
</p>
<p>I scrolled down for more information. Under the system message, it was indeed the new user was deleted. There are other information , such as the account name who made and delete the new user along with its Relative Identifier (RID), and the account name of the user itself with its Relative Identifier (RID) as well.</p>
<p><img width="959" height="340" alt="image" src="https://github.com/user-attachments/assets/f4622d01-9114-493d-bdbb-33bfc39240ce" />
</p>
<p>Again, I researched online what the event ID is for a user account creation, which I will be using to search in Wazuh.</p>
<p><img width="975" height="131" alt="image" src="https://github.com/user-attachments/assets/8ef3b708-eddf-483b-aa44-2d40e3fdd74d" />
</p>
<p>Using the information I found online, I typed the event ID 4720 on the search bar and found <b>84</b> hits.</p>
<p><img width="975" height="172" alt="image" src="https://github.com/user-attachments/assets/24d7ea34-ba60-4760-a586-855433a160db" />
</p>
<p><img width="975" height="508" alt="image" src="https://github.com/user-attachments/assets/99589608-9b2c-4ba9-86ff-dd825df85b70" />
</p>
<p>Another way to find the 4720, which provides the same result, is to type the field name of the event ID in the search bar:</p>

    data.win.system.eventID: 4720
<p><img width="975" height="499" alt="image" src="https://github.com/user-attachments/assets/36552c5f-d2bf-493d-b51e-bb82bd409a5c" />
</p>
<p><img width="975" height="726" alt="image" src="https://github.com/user-attachments/assets/88a71890-d686-4ae1-9990-978635fda7b5" />
</p>
<p>Now, I locked the Windows machine for security reasons and to test, then logged in by entering the password, in order to generate event ID 4624 on Wazuh.</p>
<p><img width="546" height="481" alt="image" src="https://github.com/user-attachments/assets/f0d397f1-ecaf-447d-ac08-e159e887d5ae" />
</p>
< p> In the search bar, I typed:</p>

    data.win.system.eventID: 4624
<p><img width="975" height="148" alt="image" src="https://github.com/user-attachments/assets/2c4beebb-7cc1-4f32-8a86-8620c03ff05f" />
</p>
<p>It generated the list of event ID 4624 from logging in on a Windows machine. On the first result, I dropped down to look for the system’s message. </p>
<p><img width="975" height="738" alt="image" src="https://github.com/user-attachments/assets/9c663f4b-37b7-4ebc-9446-4b8ac1aec1ef" />
</p>
<p>Once found, the description says, “<i>An account was successfully logged on</i>”, which means it successfully captured the logged-in activity in real-time. There are other information that can be found if scrolled down.</p>
<p><img width="870" height="389" alt="image" src="https://github.com/user-attachments/assets/d64fd488-1481-44e7-bb3a-dfebdc8fbd19" />
</p>
<p>I noticed that there is this Logon Information section, which is Logon Type: 2. I researched online what it means, and that is <b><i>Interactive</i></b>, which basically means logging on locally from the Windows machine. As an aspiring SOC Analyst, the other Logon Type numbers are also essential to identify so that in the real world cases and are helpful reference to any type of activities that are or will occur.</p>
<p><img width="814" height="802" alt="image" src="https://github.com/user-attachments/assets/5c090629-604b-4813-b6b9-fcc0485b8c26" />
</p>
<p>I identified the Windows event ID where I added the new user on the local group of administrators by researching online and found out that it is event ID <b>4732.</b></p>
<p><img width="975" height="99" alt="image" src="https://github.com/user-attachments/assets/0ba4727b-5dfd-41d0-9a7f-f8618bbd2d7c" />
</p>
<p>After that, I entered it in the search bar by typing:</p>

    data.win.system.eventID: 4732
<p><img width="975" height="640" alt="image" src="https://github.com/user-attachments/assets/c6d0a553-8a54-4b34-b363-fc0d035d868b" />
</p>
<p>On the first result, I scrolled down and looked for the system’s message, and its description says, “<i>A member was added to a security-enabled local group</i>”, which means that it captured the addition of the new user to the local group.</p>
<p><img width="869" height="377" alt="image" src="https://github.com/user-attachments/assets/d5b46b91-19f9-4aa4-b490-39fc98fa97e3" />
</p>
<p>I noticed that the new user’s account name did not appear in the Member section; thus, I copied its Security ID and pasted on the search bar in order to search for it.</p>
<p><img width="865" height="334" alt="image" src="https://github.com/user-attachments/assets/d02f7f1f-703a-440c-bf11-fb3eeb43c4e2" />
</p>
<p><img width="975" height="472" alt="image" src="https://github.com/user-attachments/assets/9403f657-0dc1-4d64-9852-098bad5b5c85" />
</p>
<p>I selected the first result, expanded, and scrolled it down. It confirmed that it is the target’s username or the new user’s account name.</p>
<p><img width="971" height="404" alt="image" src="https://github.com/user-attachments/assets/fc1bc928-b9e3-463f-92aa-56b0dd21b2db" />
</p>
<p><img width="882" height="365" alt="image" src="https://github.com/user-attachments/assets/6b5483d4-b8cf-47de-9cb1-e3836db61f87" />
</p>

<br>
<br>
<h3>J. Wazuh Custom Rules</h3>
<p>Inside the Wazuh dashboard, I headed over to the hamburger icon in the upper-left corner.</p>
<p><img width="975" height="392" alt="image" src="https://github.com/user-attachments/assets/1e1e95ed-d59b-45db-9b0a-24002b58adad" />
</p>
<p>After clicking the icon, I selected and expanded <b>Server management</b> and selected the <b><i>Rules</i></b>.</p>
<p><img width="626" height="619" alt="image" src="https://github.com/user-attachments/assets/59280efa-15e9-43de-ae8a-0e6873d125de" />
</p>
<p>I selected the <b><i>wazuh-archive*</i></b> as the <b>Index pattern</b>. After that, I typed the <b><i>local_rules.xml</i></b> in the search bar and searched for it.</p>
<p><img width="975" height="394" alt="image" src="https://github.com/user-attachments/assets/64cad516-0307-4332-81e7-e7b6dab951b6" />
</p>
<p>There are two ways to customize the <b><i>local_rules.xml</i></b>: either on the dashboard or on the <b>Ubuntu server</b> itself. If I use the Ubuntu server, I have to change the regular user first into a root user by typing: </p>

    sudo su -
<p><img width="659" height="121" alt="image" src="https://github.com/user-attachments/assets/2646a9a2-2c66-4de1-bd81-11a38ae590b1" />
</p>
<p>After becoming the root user, I have to locate the rules directory where the <b><i>local_rules.xml</i></b> is located by typing: </p>

    cd /var/ossec/etc/rules
<p><img width="615" height="181" alt="image" src="https://github.com/user-attachments/assets/15ba1b75-308d-4710-a25e-a1ab714cfab3" />
</p>
<p>After changing the directory and locating the XML file, I can modify the inside of the file and input the custom rules that I have prepared by typing: </p>

    nano local_rules.xml
<p><img width="975" height="605" alt="image" src="https://github.com/user-attachments/assets/bf046e9c-9b88-4365-91e2-8df207035c2b" />
</p>
<p>The only difference is that using this method, I have to type each rule one by one, which may take some time to finish. On the other hand, I preferred to use the dashboard instead because it’s easy and fast to input the desired custom rules, which, in the end, have the same results.</p>
<p> I selected the <b><i>local_rules.xml</i></b> based from the result.</p>
<p><img width="975" height="180" alt="image" src="https://github.com/user-attachments/assets/27efc6fc-fc95-47f6-bd1a-db2591d13380" />
</p>
<p><img width="905" height="327" alt="image" src="https://github.com/user-attachments/assets/7a6bad0f-bd82-4ea6-924d-912e940c9c55" />
</p>
<p>After pasting the custom rules, I saved the file, then pressed reload to refresh and activate the rules</p>
<p><img width="975" height="122" alt="image" src="https://github.com/user-attachments/assets/274c2cf7-74b0-4d4a-8596-916d20267cae" />
</p>
<p><img width="975" height="124" alt="image" src="https://github.com/user-attachments/assets/3c443353-9363-4a60-a845-00af08aaf50f" />
</p>
<p>I can also click the <b><i>Custom rules</i></b> button, where I can easily find the customized and newly added rules.</p>
<p><img width="975" height="351" alt="image" src="https://github.com/user-attachments/assets/35f5ff39-3b32-4fdb-8cf5-a62769b61097" />
</p>


<br>
<br>
<h3>K. Active Response</h3>
<p>I configured the Active Response so that Wazuh can perform some automated actions. I headed over to Aazuh manager or ubuntu server and typed:</p>

    sudo nano /var/ossec/etc/ossec.conf

<p><img width="669" height="100" alt="image" src="https://github.com/user-attachments/assets/86db568e-434f-414a-a220-923de2be87f6" />
</p>

<p>After that, I scrolled down until I reached the <b><i>Active Response</i></b> section.</p>
<p><img width="845" height="570" alt="image" src="https://github.com/user-attachments/assets/c6e94fb9-7b60-4de8-a7ad-2915aad8479d" />
</p>

<p>I removed the comments symbols from <b>active-response</b> and replaced the a<b><i>ctive-response options here</i></b> the following commands, such as:</p>
<ul>
	     <li> Disable: no</li>
	     <li> Command: firewall-drop</li>
	     <li> Location: local </li>
	     <li> Rules ID: 100101 </li> (which is for the multiple failed login attempts)
	</ul>

<p><img width="715" height="372" alt="image" src="https://github.com/user-attachments/assets/a99c5f7a-1b5d-4186-aff3-96112d43aa61" />
</p>
<p><img width="665" height="314" alt="image" src="https://github.com/user-attachments/assets/96fb7e2f-2878-4d15-9838-8ca6ea4dc53b" />
</p>
<p><img width="975" height="188" alt="image" src="https://github.com/user-attachments/assets/48e16ba2-6413-49e5-b211-3bc57dcbccfa" />
</p>
<p><img width="975" height="302" alt="image" src="https://github.com/user-attachments/assets/e2edd5a6-daf1-468e-8cab-b7de3454d83e" />
</p>
<p><img width="975" height="277" alt="image" src="https://github.com/user-attachments/assets/726b9325-80fe-46ed-b08d-facf31963553" />
</p>
<p><img width="469" height="269" alt="image" src="https://github.com/user-attachments/assets/a83fe3fa-e00e-4662-a72d-9833d22b7f57" />
</p>
<p>After I saved it, I restarted the Wazuh manager by typing:</p>

    sudo systemctl restart wazuh-manager.service
<p><img width="771" height="87" alt="image" src="https://github.com/user-attachments/assets/237342b2-1604-4362-950c-e4f0769fb3ff" />
</p>
<p>I verified that it’s been activated by changing the user from regular user into root account by typing:</p>

    sudo su -

<p><img width="415" height="75" alt="image" src="https://github.com/user-attachments/assets/aaeee8a7-5dea-475d-af0d-733e771d5c16" />
</p>

<p>The binary of interest is in:</p>

    /var/ossec/bin/agent_control -L

<p><img width="582" height="146" alt="image" src="https://github.com/user-attachments/assets/92b5d256-aec7-48af-bdac-d8607f7f08ba" />
</p>
<p>To restore the connectivity, I moved from root account into regular user by typing <b>exit</b>, then typed:</p>

    sudo iptables –L –n –line-numbers

<p><img width="845" height="270" alt="image" src="https://github.com/user-attachments/assets/7353f14d-ebf7-4898-a0c7-68df837d68dc" />
</p>

<p>I removed the <b>target</b> and <b><i>source ip</i></b> by typing:</p>

    sudo iptables –D INPUT 1
    sudo iptables –D FORWARD 1

<p>I verified that it’s all cleared by retyping the command:</p>

    sudo iptables –L –n –line-numbers

<p><img width="650" height="209" alt="image" src="https://github.com/user-attachments/assets/d747458a-d83a-453e-923a-a94482fd1e98" />
</p>

<br>
<h2>Lessons Learned</h2>
<p>Engineering this infrastructure from the ground up highlighted the critical reality that elite defensive monitoring relies entirely on the precision of architecture and telemetry configuration rather than unlimited hardware resources. By navigating local physical resource constraints, I developed a deep practical understanding of the log ingestion lifecycle—specifically how to successfully bridge endpoints and central management utilities across an isolated network.</p>
<p>True security engineering requires a meticulous approach to filtering, parsing, and baseline standardization to ensure that when an attack eventually occurs, the resulting telemetry contains highly relevant, MITRE ATT&CK-mapped data that is instantly actionable for an investigation.</p>

<br>
<h2>Organizational Value</h2>
<p>For an enterprise or security organization, this project demonstrates a foundational mastery of cost-effective security engineering, proactive visibility optimization, and infrastructure scalability. By utilizing open-source frameworks like the Wazuh SIEM alongside targeted Microsoft Sysinternals tooling, this deployment models how businesses can successfully architect high-fidelity detection pipelines without relying on prohibitively expensive commercial licenses.</p>
<p>Furthermore, the deliberate design choices implemented in this lab—such as reducing endpoint event noise while explicitly preparing a structured pipeline to ingest complex telemetry like Active Directory authentication vectors—directly translate to real-world corporate environments.</p>
<p>An organization benefits from a professional who understands not just how to look at an analyst dashboard, but how to deploy lightweight, resource-optimized endpoint configurations that minimize operational overhead while maximizing defensive visibility across the enterprise footprint.</p>

<br>
<h2>Value to an Aspiring SOC Analyst & Enthusiast</h2>
<p>As an aspiring security professional and enthusiast, constructing this lab environment bridges the gap between theoretical knowledge and practical, enterprise-grade engineering. It transforms abstract concepts learned from textbooks into a tangible, multi-node playground where I am in absolute control of the security stack.</p>
<p>By executing the full installation, managing virtual network configurations, and binding endpoint agents to a centralized SIEM manager, I have cultivated the precise technical confidence required to navigate real-world corporate infrastructures.</p>
< p> This project completely shifts my perspective from a passive observer to an active infrastructure designer, establishing a rock-solid operational foundation. It ensures that as I move forward into live adversarial testing and incident verification, I am approaching threat hunting with an intimate, firsthand understanding of the underlying pipelines that generate the alerts.</p>















