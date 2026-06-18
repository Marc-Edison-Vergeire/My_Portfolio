<img width="975" height="289" alt="image" src="https://github.com/user-attachments/assets/3c96d8f2-4e12-453b-a0ad-57837f936e55" /><h1>Complete Virtual Cybersecurity Lab (SOC Home Lab)</h1>
<p><img width="950" height="531" alt="image" src="https://github.com/user-attachments/assets/bd6b6a12-26e3-4624-8f1a-194ac2b027b9" />
</p>
<p text-align="center"><i>Virtual Cybersecurity (SOC) Lab Network Topology</i></p>

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
<img width="721" height="507" alt="image" src="https://github.com/user-attachments/assets/d8829e09-e037-4b86-8811-8ee66ba2e13f" />
























