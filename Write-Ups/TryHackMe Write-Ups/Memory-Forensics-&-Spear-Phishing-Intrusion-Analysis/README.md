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
  <li><b>Volatility:</b> An open-source advanced memory forensics framework used to analyze and extract critical digital artifacts, trace anomalous process trees, and uncover hidden implants from volatile memory (RAM) samples.</li>
  <li><b>Olevba: </b>A specialized script-analysis tool utilized to automatically parse, extract, and analyze embedded Visual Basic for Applications (VBA) macros within the weaponized Microsoft Office document to decode the initial execution payload.</li>
  <li><b>Evolution Mail: </b>A Linux-based email client and information management framework utilized to safely inspect raw email headers, body content, and attached artifacts to isolate the initial spear-phishing vector without risking accidental execution.</li>
  <li><b>Virustotal: </b>A cloud-based threat intelligence platform used to aggregate scanning data from dozens of antivirus engines and datasets to validate extracted file hashes, cross-reference external C2 IP addresses, and identify known advanced persistent threat (APT) campaign indicators.</li>
</ul>

<br>
<h2>Artifacts Analyzed</h2>
<ul>
  <li><b>Resume - Application for Junior IT Analyst Role[.]eml (Phishing Email): </b>A copy of the raw phishing email used to target the Human Resources department. It was inspected to extract sender transport headers, source IP addresses, and the specific delivery context used by the adversary.</li>
  <li><b>Resume_WesleyTaylor[.]doc (Weaponized Resume Attachment): </b>The malicious resume submitted by the threat actor, which contained the embedded, deobfuscated VBA macro code responsible for initiating the first-stage download and executing the initial workstation compromise.</li>
  <li><b>WKSTN-2961[.]raw (Volatile Memory Dump): </b>A complete, raw memory capture of the victim's workstation acquired immediately following the alert. This artifact served as the primary source for memory forensics, allowing the extraction of active network connections, process trees, and in-memory implants.</li>
</ul>

<br>
<h2>Findings</h2>
<h3>Phase 1: Initial Triage and Phishing Analysic</h3>
<p>Following an alert flagging anomalous endpoint execution on an employee's workstation, I deployed automated containment playbooks to execute an enterprise-wide search. The specific message ID was successfully located within the employee's mailbox, allowing the direct export of the raw <b>.eml</b> file to investigate the initial access vector. In this case, I utilized Evolution Mail to parse and open the EML file from the phishing email, just to see the content of the email.</p>
<p><img width="975" height="568" alt="image" src="https://github.com/user-attachments/assets/3ab39c6c-89a1-4f51-85af-02b318ec99b8" /></p>
<p><img width="975" height="514" alt="image" src="https://github.com/user-attachments/assets/a7f3dcc0-fb83-46bf-8229-add3ecbc0d16" /></p>
<p><img width="975" height="620" alt="image" src="https://github.com/user-attachments/assets/2a208a05-696b-4ba5-8a03-8e7f84f8ff13" /></p>
<p><img width="975" height="375" alt="image" src="https://github.com/user-attachments/assets/d5f949ef-f6c8-4ca0-b8b7-bbf01b6823b4" /></p>
<p>Based from the content, the email was used to send the phishing email was <b>westaylor23@outlook[.]com</b>, and the email of the victim employee was <b>maxine[.[beck@quicklogisticsorg[.]onmicrosoft[.]com</b>.</p>

<p>The attached file at the bottom of the email content, the name of the attached malicious document was <b>Resume_WesleyTaylor[.]doc<b/>.</p>
<p><img width="975" height="380" alt="image" src="https://github.com/user-attachments/assets/15d4fa8d-55a5-41d9-96f3-b9c2ea0851b7" />
</p>
<p>I downloaded the malicious attachment to investigate.</p>
<p><img width="975" height="390" alt="image" src="https://github.com/user-attachments/assets/cb6fc9eb-6cad-4e16-886d-cb265d60075f" />
</p>
<p><img width="975" height="475" alt="image" src="https://github.com/user-attachments/assets/f9e2cb46-460c-4c80-9ccf-4cc5b9d63864" />
</p>
<p><img width="975" height="513" alt="image" src="https://github.com/user-attachments/assets/0d9fc52f-41fd-4142-af09-a6729d415ba1" />
</p>
<p><img width="964" height="489" alt="image" src="https://github.com/user-attachments/assets/78a762ad-651a-448c-93f7-864bb7c6d9e2" />
</p>

<br>
<h3>Phase 2: Static Malware Analysis & Threat Intelligence</h3>
<p>I investigated what is the MD5 hash of the malicious attachment by opening a terminal in the Artefact folder</p>
<p><img width="975" height="752" alt="image" src="https://github.com/user-attachments/assets/f0cac0e8-6fb7-4ad9-baec-bf9ee974fca8" />
</p>
<p>Inside the terminal, I typed the two commands to get the hash value of the malicious attachment, such as:</p>

    ls  & md5sum  Resume_WesleyTaylor[.]doc

<p><img width="975" height="246" alt="image" src="https://github.com/user-attachments/assets/a36a9fc7-3ea9-4560-a345-6561044e7af8" />
</p>
<p><img width="975" height="276" alt="image" src="https://github.com/user-attachments/assets/fca77255-01f3-4235-bda4-0ac787e6969e" />
</p>
<p><img width="974" height="320" alt="image" src="https://github.com/user-attachments/assets/5972095a-3f01-456a-b3af-2539ee44841d" />
</p>
<p>I copied the hash value and input in Virustotal to analyze and  gathered more information about the file.</p>
<p><img width="975" height="394" alt="image" src="https://github.com/user-attachments/assets/cf519b90-a95d-4d17-b622-210d68c2333e" />
</p>
<p>Based from the result, 39/62 security vendors flagged this file as malicious. There are a lot of details I found from the details, relations, behavior, and community.</p>
<p><img width="975" height="175" alt="image" src="https://github.com/user-attachments/assets/341bac60-e6c3-45ad-99e5-13a07187a00c" />
</p>

<br>
<h3>Phase 3: Volatility Memory Forensics & Process Triage</h3>
<p>Upon further investigation, I utilized the Olevba command against the malicious attachment, thus, the URL is used to download the stage 2 payload based on the document’s macro is <b>https[:]//files[.]boogeymanisback[.]lol/aa2a9c53cbb80416d3b47d85538d9971/update[.]png</b></p>
<p><img width="814" height="339" alt="image" src="https://github.com/user-attachments/assets/35d6e1e4-3862-4863-a0da-8f2b88d76fc1" />
</p>
<p><img width="975" height="892" alt="image" src="https://github.com/user-attachments/assets/80b38e8b-9a7a-4266-9f15-93905a5e40f4" />
</p>
<p>Based on this result, the name of the process that executed the newly downloaded stage 2 payload is <b>wscript[.]exe</b>. At the same time, the full file path of the malicious stage 2 payload is <b>C[:]\ProgramData\update[.]js</b>.</p>
<p><img width="890" height="627" alt="image" src="https://github.com/user-attachments/assets/62696abe-cd6f-452a-880b-9ca3c652a705" />
</p>
<p>I identified the PID of the process that executed the stage 2 payload (<b>wscript[.]exe</b>) and utilized the Volatility by entering the syntax command:</p>

    vol  -f  WKSTN-2961.raw  windows.pslist

<p><img width="975" height="439" alt="image" src="https://github.com/user-attachments/assets/b54cccb4-117b-406e-9782-d551e4b9cda0" />
</p>
<p>In order for me to spot the PID easier and faster, I added the command,  <b>| grep “wscript[.]exe”</b>. Therefore, the PID is <b>4260</b>.</p>
<p><img width="975" height="303" alt="image" src="https://github.com/user-attachments/assets/45404d3d-18f1-4465-bd39-e757b096ea21" />
</p>

<br>
<h3>Phase 4: Network Analysis & Infrastructure Mapping</h3>
<p>This time, I identified what is the parent PID of the process that executed the stage 2 payload and that is <b>1124</b>, by using the syntax command:</p>

    vol  -f  WKSTN-2961.raw  windows.pstree  |  grep  "4260"

<p><img width="975" height="228" alt="image" src="https://github.com/user-attachments/assets/cfd788cd-2172-4f38-b588-e63e18f5bed6" />
</p>
<p>I investigated about the URL used to download the malicious binary executed by the stage 2 payload and that is <b>https[:]//files[.]boogeymanisback[.]lol/aa2a9c53cbb80416d3b47d85538d9971/update[.]exe</b>, I entered the syntax command again:</p>

    olevba  Resume_WeslyTaylor[.]doc



















