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
<p>With the core engineering phase complete, this deployment stands fully operational and optimized for defensive validation. As future simulations trigger malicious executions or privilege escalation techniques, <b>Microsoft System Monitor (Sysmon)</b> stands active on the target machine to capture granular, low-level behavioral event logs. This high-fidelity telemetry pipeline is ready to securely stream logs to the centralized <b>Ubuntu Server</b> running the <b>Wazuh SIEM Manager (10.0.2.4)</b>, which is configured to parse, correlate, and surface raw events into real-time, actionable security alerts. </p>
<p>The underlying network and collection pipeline are completely verified, rendering this <b>SOC Home Lab</b> perfectly primed for diverse adversarial testing, behavioral analysis, and live incident triage.</p>

<br>
<h2>Skills Learned</h2>
<u>
  <li><b>Hypervisor Architecture & Virtual Networking: </b>Developed hands-on proficiency in virtualization engineering by designing, provisioning, and isolating virtual machines within <b>Oracle VM VirtualBox</b>. Successfully architected a custom, multi-node <b>NAT Network (10.0.2.0/24)</b> to maintain environment isolation while ensuring structured, inter-VM network routing and connectivity.</li>
  <br><li><b>Linux System Administration & SIEM Deployment: </b>Cultivated practical Linux administration skills by deploying, configuring, and hardening an <b>Ubuntu Server</b> to act as the central repository for the lab's security infrastructure. Successfully installed the <b>Wazuh Manager</b> framework, managing core system dependencies and verifying daemon readiness.</li>
  <br><li><b>Endpoint Telemetry & Logging Architecture: </b>Gained foundational knowledge of host-level visibility and enterprise auditing by deploying <b>Microsoft System Monitor (Sysmon)</b> on a <b>Windows 10 Pro</b> endpoint. Mastered the structural installation of advanced logging binaries and endpoint-level agent services designed to transform raw OS behavior into structured telemetry.</li>
  <br><li><b>SIEM Agent Deployment & Pipeline Engineering: </b> Mastered the fundamentals of the log collection lifecycle by successfully deploying and configuring the <b>Wazuh Agent</b> on a target Windows endpoint. Successfully established secure communication between the endpoint agent and the centralized <b>Ubuntu SIEM</b> server, verifying the integrity of the ingestion pipeline.</li>
  <br><li><b>Network Infrastructure Troubleshooting: </b>Developed critical, low-level technical problem-solving skills by diagnosing and resolving hypervisor-level network connectivity issues. Successfully managed virtual interface states, negotiated IP address assignments, and validated end-to-end interface connectivity.</li>
  <li><b>Pragmatic Project Management & Scope Planning: </b>Demonstrated strong architectural planning and resource management by designing a phased deployment roadmap. Successfully engineered a lean, fully functional, three-node security verification pipeline optimized specifically for local hardware constraints, establishing a rock-solid foundation for future adversarial testing.</li>
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





