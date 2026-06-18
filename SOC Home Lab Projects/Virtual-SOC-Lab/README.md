<h1>Complete Virtual Cybersecurity Lab (SOC Home Lab)</h1>
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
<h3>VirtualBox</h3>
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
<p></p>






















