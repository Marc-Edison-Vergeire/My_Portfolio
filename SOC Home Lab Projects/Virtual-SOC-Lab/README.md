<h1>Complete- Virtual-Cybersecurity-Lab (SOC-Home-Lab)</h1>
<p><img width="975" height="531" alt="image" src="https://github.com/user-attachments/assets/6bcf8367-69d8-4468-9e4b-251f42660c3c" />
</p>
<p><i>Virtual Cybersecurity (SOC) Lab Network Topology</i></p>

<br>
<h2>Executive Summary</h2>
<p>This environment serves as a rigorous testing ground where an adversarial <b>Kali Linux</b> platform (<b>10.0.2.3</b>) executes diverse attack vectors—including SSH brute-forcing, unauthorized RDP access, and other tactical exploits—against a hardened <b>Windows 10 Pro</b> target machine (<b>10.0.2.15</b>). Advanced endpoint visibility is achieved via <b>Microsoft System Monitor (Sysmon)</b>, which captures detailed behavioral events and safely ships them alongside core system logs to a centralized <b>Ubuntu Server</b> running <b>Wazuh Manager</b> (<b>10.0.2.4</b>). </p>
<p>By analyzing live telemetry and managing incident alerts, this project successfully validates my hands-on technical proficiency in <b>SIEM</b> engineering, log parsing, and detection validation—proving that elite, defensive analysis requires critical problem-solving and architectural agility far more than unlimited hardware.</p>

<br>
<h2>Project Objective</h2>
<p>This project represents <b>Phase 1</b> of my <b>SOC Home Lab</b>, where my primary objective was to establish a fully functional, high-fidelity endpoint telemetry pipeline using <b>Sysmon</b> and <b>Wazuh</b>. Given my current laptop hardware limitations, I chose to focus intensely on perfecting single-host endpoint logging and behavioral detection methodologies first. </p>
<p>Looking forward, <b>Phase 2</b> of my roadmap includes scaling my infrastructure to introduce a <b>Windows Server Domain Controller</b>, allowing me to monitor <b>Active Directory</b>-specific attack vectors such as <b>Kerberoasting</b> and <b>Golden Ticket</b> techniques.</p>

<br>
<h2>Lab Overview</h2>
<p><img width="704" height="460" alt="image" src="https://github.com/user-attachments/assets/e039be25-b125-4a3d-8751-87a77a5cafa0" />
<p><i>Basic Network Topology Layout</i></p>
</p>
<p>To replicate the daily workflows of a <b>SOC Analyst</b> under local hardware constraints, this lab features a targeted deployment of three core virtual machines within a custom network: a <b>Kali Linux</b> attacker platform, a <b>Windows 10 Pro</b> endpoint equipped with <b>Sysmon</b> telemetry, and a centralized <b>Ubuntu Server</b> hosting the <b>Wazuh SIEM</b>. While an enterprise-grade <b>Active Directory</b> infrastructure was intentionally omitted to optimize system performance, this environment successfully simulates end-to-end, real-world attack investigations, detection engineering, and live log monitoring.</p>

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
  <li><b>Ubuntu Server (LTS): </b>Utilized as a lightweight, high-performance Linux foundation dedicated to running core <b>Wazuh SIEM</b> management services.</li>
  <br><li><b>Windows 10 Pro: </b>Deployed as an enterprise-grade target endpoint, specifically configured for enhanced security auditing and proactive monitoring.</li>
  <br><li><b>Windows 11: </b>Serving as the physical host system, it is used to orchestrate the virtual environment and securely access the web-based Wazuh management dashboard for administrative verification.</li>
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
<p>I opened <b>Google.com</b> and input “<b>kali linux iso download</b>” to direct me to its website.</p>
<p><img width="975" height="448" alt="image" src="https://github.com/user-attachments/assets/a12b548d-29dc-4c24-9445-2508c5085cb8" />
</p>
<p>There are some results for <b>Kali Linux</b>, thus, I selected the first one.</p>
<p><img width="814" height="419" alt="image" src="https://github.com/user-attachments/assets/430b57b3-58f0-476a-a6ac-36e86314f2dc" />
</p>
<p>Inside the Kali website, select the <b>Virtual Machines</b> on the right-side.</p>
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
<p>Google provided me some results, but I chose and selected the official <b>Ubuntu</b> website.</p>
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
<p>In order to update and upgrade the system, input the command;</p>

    sudo apt update && sudo apt upgrade -y
<p><img width="862" height="121" alt="image" src="https://github.com/user-attachments/assets/b35ee34e-9035-41fe-b708-cac8f098b778" />
</p>
<p><img width="767" height="296" alt="image" src="https://github.com/user-attachments/assets/f06223e0-b1a8-4cc0-997d-1a2430959f56" />
</p>

<br>
<h3>E. Wazuh (SIEM)</h3>
<p>Before running the <b>Ubuntu Server</b> and <b>Kali Linux</b>, I tweaked the network connections for the three VMs, so that they communicate in the same network.</p>
<p><img width="736" height="316" alt="image" src="https://github.com/user-attachments/assets/6c32d01d-9620-4244-ad93-00ed3bbfc986" />
</p>
<p>I selected the <b>Tools</b> and chose <b>Network</b>.</p>
<p><img width="694" height="549" alt="image" src="https://github.com/user-attachments/assets/c40378a7-995b-4976-94f6-5ea814819b9e" />
</p>
<p>First, I selected the <b>NAT Network</b> tab, changed the Name to <b>SOC-Home-Lab, then clicked on Apply button</b>. It provided an IP range of <b>10.0.2.0/24</b>.</p>
<p><img width="835" height="448" alt="image" src="https://github.com/user-attachments/assets/67baa934-fccc-4270-907a-70e14ee038c8" />
</p>
<p>I changed the settings for each of the VMs. In the <b>Network</b>, I replaced the <b>NAT</b> with <b>NAT Network</b> and automatically selected the <b>SOC-Home-Lab, then pressed the <b>OK</b> button.</p>
<p><img width="975" height="558" alt="image" src="https://github.com/user-attachments/assets/e6d6949f-55cf-4d56-816e-7406c4388c78" />
</p>
<p>I opened <b>Ubuntu Server</b> to start the installation of <b>Wazuh</b>.</p>
<p><img width="724" height="507" alt="image" src="https://github.com/user-attachments/assets/cd974bb9-d6b5-452f-b0dc-f7f04685bf2a" />
</p>
<p>While <b>Ubuntu Server</b> is running, I opened Google to look for <b>Wazuh</b> installation, thus, I typed in its search bar <b>wazuh siem</b>.</p>
<p><img width="799" height="393" alt="image" src="https://github.com/user-attachments/assets/2da0ce0e-bbec-4be8-baf4-65bcdf8b56be" />
</p>
<p>Google provided me some results, and I selected the official website of <b>Wazuh</b>.</p>
<p><img width="933" height="344" alt="image" src="https://github.com/user-attachments/assets/7e9afcb8-07a8-496d-bd70-e606c24503ca" />
</p>
<p>Inside Wazuh's website, I clicked on <b>Install Wazuh</b> button.</p>
<p><img width="975" height="455" alt="image" src="https://github.com/user-attachments/assets/de591e32-0bd6-4636-b900-b36740004ab3" />
</p>
<p>I scrolled down and selected the <b>Quickstart</b> button.</p>
<p><img width="975" height="229" alt="image" src="https://github.com/user-attachments/assets/f2d73b0f-c135-4d3b-97ee-2738e2216c43" />
</p>
<p>After that, it provided me a command to input in Ubuntu Server's CLI and run the said command, which is the;</p>

      curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh && sudo bash ./wazuh-install.sh -a

<p><img width="975" height="304" alt="image" src="https://github.com/user-attachments/assets/061b1a0b-8b18-4512-b36b-2887173e3acb" />
</p>
<p><img width="975" height="169" alt="image" src="https://github.com/user-attachments/assets/277d1742-3d2b-4c35-8358-6aec0ce07dd4" />
</p>
<p>After installation, it provided me with <b>User</b> and <b>Password</b> credentials.</p>
<p><img width="1011" height="203" alt="image" src="https://github.com/user-attachments/assets/5daa1651-1753-4d8a-ace4-749007d5576d" />
</p>
<p>It also provided me with the URL to input inside the browser, but I need to replace the <b><wazuh-dashboard-ip></b>.</p>

    ip addr  OR  ip a

<p><img width="975" height="202" alt="image" src="https://github.com/user-attachments/assets/1e63b125-28af-4c0e-b13b-4eba60341678" />
</p>
<p>I typed the  <b>ip a</b>  command to know what the IP address would be for the Wazuh dashboard. Alternatively, I typed  <b>ip addr</b>, which gave me the same result. </p>
<p><img width="975" height="619" alt="image" src="https://github.com/user-attachments/assets/e022eab0-b583-46df-b0a5-bfc20fe56fb5" />
</p>
<p>Before I start running Wazuh, I entered several commands that needed to run it seamlessly, such as: </p>

    sudo  systemctl  stop  wazuh-dashboard  wazuh-manager  wazuh-index

<p>After that, I start them back up one by one, waiting 10-15 seconds between each command;</p>

    sudo  systemctl  start  wazuh-indexer
    sudo  systemctl  start  wazuh-manager
    sudo  systemctl  start  wazuh-dashboard
    
<p><img width="946" height="147" alt="image" src="https://github.com/user-attachments/assets/438e55fc-6ca8-4e57-85ef-472a82d91c68" />
</p>
<p>Now, I verified the API daemon is active by checking if the manager and backend API are running properly using the command:</p>

    sudo  systemctl  status  wazuh-manager
    
<p>Since it says <b>active (running)</b>, tail the API log file to make sure there are no internal credentials or structural errors blocking the link by typing:</p>

    sudo  tail  -n  20  /var/ossec/logs/api.log
    
<p><img width="780" height="467" alt="image" src="https://github.com/user-attachments/assets/69912a94-6a4d-41fa-841b-8ed8494d2749" />
</p>
<p><b>Wazuh</b> Wazuh is highly resource-intensive. My Ubuntu VM has <b>6 GB</b> of RAM allocated, the API daemon will crash silently under an <b>Out of Memory (OOM)</b> exception. I cleared the RAM cache immediately using:</p>

      sudo  sync;  echo  3  |  sudo  tee  /proc/sys/vm/drop_caches
      
<p>Lastly, I also checked how much RAM is consumed and remaining by typing:</p>

    free -h
<p>
</p>
<p> For me to open the dashboard, I launched a <b>Kali Linux</b> machine where I can use <b>Mozilla Firefox</b> for the internet and input the URL with the IP to test if it will launch the <b>Wazuh Dashboard</b>. I preferred to use Kali Linux because it consumes less RAM than running Wazuh in Windows 10; however, Wazuh can run in Windows 10 as well.</p>
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
<p> If I shut down the VMs, both <b>Kali Linux</b> (where I opened the Wazuh dashboard) and <b>Ubuntu Server</b> (to start running Wazuh), and want to run Wazuh again, I will type this command to see if the services are running their own:</p>

    sudo systemctl status wazuh-manager wazuh-indexer wazuh-dashboard
    
<p>If I see <b>active (running)</b> in green for all three, I can immediately type the HTTPS URL into the Kali Linux browser.</p>
<p>If in case the status command shows that the services are <b>inactive</b> or <b>stopped</b>, I would run this command on my Ubuntu Server to force them to start:</p>

    sudo systemctl start wazuh-indexer wazuh-manager wazuh-dashboard
    
<br>
<h3>F. Deploying Wazuh Agents on Windows Endpoints</h3>
<p></p>















