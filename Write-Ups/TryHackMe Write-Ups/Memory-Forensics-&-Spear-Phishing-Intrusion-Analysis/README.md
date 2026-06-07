<h1>Memory Forensics & Spear Phishing Intrusion Analysis</h1>

<br>
<h2>Executive Summary</h2>
<p>An advanced persistent threat (APT) incident was successfully detected and analyzed involving a targeted spear-phishing attack that resulted in host compromise and deep-system persistence. The intrusion began when an internal employee executed a malicious Microsoft Word document weaponized with an embedded Visual Basic for Applications (VBA) macro, which initiated an out-of-band network request to an external Command and Control (C2) infrastructure to download a secondary payload. Comprehensive memory forensics and artifact analysis revealed that the initial  <b>.exe</b>  file  process spawned an anomalous in-memory implant that maintained active beaconing back to the adversary's server. To ensure long-term persistence across system reboots, the malware automatically registered an unauthorized Scheduled Task on the endpoint, positioning the threat actor for potential lateral movement and domain escalation.</p>

<br>
<h2>Objective</h2>
<p>As a SOC Analyst tasked with analyzing and assessing the impact of this compromise, my objective is to perform a comprehensive, end-to-end incident response and memory forensics investigation to uncover the full scope of this sophisticated spear-phishing intrusion. I will reconstruct the adversary's attack lifecycle by inspecting email artifacts to isolate the initial access vector and weaponized attachment, and then delve into volatile memory dumps to trace anomalous process trees, extract Command and Control (C2) indicators, and dissect the exact persistence mechanisms established on the host. By evaluating these artifacts, I aim to map the advanced threat actor behaviors, validate critical indicators of compromise (IoCs), and determine the precise depth of the breach to formulate effective isolation and remediation strategies that minimize organizational impact.</p>

<br>
<h2>Scenario</h2>
<p>A Human Resource Specialist at the logistics company reviewed incoming job applications and received an email regarding one of the organization's open positions. Unknowingly, the employee opened the attached resume, which was heavily weaponized and successfully compromised its workstation. The Security Operations Center (SOC) promptly flagged a series of anomalous commands executed on the infected host, which immediately triggered this forensic investigation.</p>
<br>
<img width="975" height="698" alt="image" src="https://github.com/user-attachments/assets/6641e649-9263-4e96-bbc5-0d48bfb909b1" />

<br><br>
<h2>Skills Learned</h2>
<ul>
  <li><b>Advanced Volatile Memory Forensics: </b>Gained hands-on experience utilizing memory analysis tools to parse volatile memory dumps, reconstruct process injection techniques, and isolate hidden or unlinked malicious structures.</li>
  <li><b>Process Tree Hierarchy Reconstruction: </b>Mastered the capability to map process execution to pinpoint parent-child relationships and identify unauthorized execution paths.</li>
  <li><b>C2 Infrastructure Identification: </b>Refined techniques for extracting network artifacts from system memory to pinpoint active Command and Control (C2) domains, remote IP addresses, and unique beaconing profiles utilized by advanced persistent threats.</li>
  <li><b>Host-Based Persistence Tracking: </b>Enhanced the ability to hunt for and identify defensive evasion and persistence mechanisms within endpoint environments, with a direct focus on locating and analyzing unauthorized Scheduled Tasks.</li>
  <li><b>Incident Response & Impact Assessment: </b>Cultivated the core blue-team methodologies required to fully assess host compromise, validate complex Indicators of Compromise (IoCs), and formulate actionable containment strategies like network isolation and credential revocation.</li>
</ul>

<br>
<h2>Tools Utilized</h2>
<ul>
  <li><b></b></li>
  <li><b></b></li>
  <li><b></b></li>
  <li><b></b></li>
</ul>




