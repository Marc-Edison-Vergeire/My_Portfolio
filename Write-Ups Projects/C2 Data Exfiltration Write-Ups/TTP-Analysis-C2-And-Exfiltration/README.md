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



