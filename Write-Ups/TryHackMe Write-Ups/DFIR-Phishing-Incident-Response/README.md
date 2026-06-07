<h1>DFIR Phishing Incident Response</h1>

<h2>(Enterprise Email Forensics Case)</h2>

<h3>Executive Summary</h3>
	<p>
		This incident response case study documents the end-to-end investigation of a targeted phishing campaign that led to the compromise of a finance workstation within a logistics enterprise.
	</p>
	<p>
		The attack initiated via a sophisticated email lure utilizing typosquatted infrastructure to deliver a weaponized Windows shortcut (<b>.lnk</b>) file. Upon execution, the payload initiated a hidden PowerShell download cradle to establish command-and-control (C2) communication. Host log analysis revealed that the adversary successfully engaged in defense evasion by deploying a masqueraded database utility (<b>sq3.exe</b>) to harvest unencrypted user credentials from local Windows Sticky Notes.
	</p>
	<p>
		Furthermore, the attacker located an enterprise password vault (<b>protected_data.kdbx</b>) and exfiltrated the sensitive asset using hex-encoded DNS tunneling. By cross-correlating endpoint JSON logs with network packet captures, the complete intrusion timeline was reconstructed, the C2 server infrastructure was mapped, and the exfiltrated password database was forensically recovered and decrypted.
	</p>

<br>
<h3>Objective</h3>
	<p>
		The objective of this incident response case study is to perform a comprehensive, end-to-end forensic investigation of a targeted phishing intrusion within an enterprise network. By conducting detailed email header analysis, de-obfuscating malicious PowerShell execution artifacts, and utilizing host and network telemetry (JSON event logs and PCAP files), this analysis aims to reconstruct the complete adversarial timeline. Ultimately, the investigation serves to identify host-based defense evasion tactics, isolate covert network exfiltration channels, and extract actionable Indicators of Compromise (IoCs) to formulate strategic, data-driven remediation recommendations for enterprise defense.
	</p>

<br>
<h3>Scenario</h3>
	<p>
		A finance employee at a logistics firm received a highly targeted follow-up email regarding an unpaid invoice from a known packaging business partner. Unbeknownst to the employee, this was a sophisticated phishing attack containing a weaponized attachment that compromised the host or workstation upon execution.
	</p>
	<p>
		As the responding SOC Analyst, I flagged the anomalous execution of the attachment, correlating it with corresponding phishing reports submitted by other personnel within the finance division. Threat intelligence and TTP (Tactics, Techniques, and Procedures) mapping indicate that the initial delivery mechanisms align directly with an emerging threat group actively targeting the logistics sector.
	</p>

<br>
<h3>Skills Learned</h3>
	<ul>
		<li>Email header & Forensic analysis</li>
		<li>Windows artifact forensics</li>
		<li>Log triage & Structured parsing</li>
		<li>Network traffic reconstruction</li>
		<li>Malware TTP identification</li>
	</ul>

<br>
<h3>Tool Utilized</h3>
	<ul>
		<li><b>Thunderbird</b> (free and open-source cross-platform email client)</li>
		<li><b>mha.azurewebsites.net</b> (Online email analyzer)</li>
		<li><b>lnkparse / LINKParse3 </b>(LNK parsing tool in CLI)</li>
		<li><b>Cyberchef.com </b>(intuitive web-based application)</li>
		<li><b>Wireshark</b> (Packet analyzer GUI)</li>
		<li><b>TShark </b> (Wireshark’s command-line)</li>
	</ul>

<br>
<h3>Artifacts Analyzed</h3>
	<ul>
		<li><b>dump[.]eml</b> (Copy from the phishing email)</li>
		<li><b>powershell.json </b>(Powershell Logs from the finance employee’s host or workstation)</li>
		<li><b>capture.pcapng </b>(Packet capture from the same workstation)</li>
	</ul>

<br>
<h3>Findings</h3>
	<ul>
		<li><b>Phase 1:</b> (Phishing) Email Analysis/Forensics</li>
			<br>
			<p>To understand how this <b>.eml</b>  artifact was acquired, I flagged the anomalous endpoint execution on the employee’s workstation, and responded by using automated containment playbooks to run an enterprise-wide search. I locate the specific message ID within the employee’s mailbox and exported the message directly as a standard <b>.eml</b> forensic artifact to investigate the initial access vector. In this case, Thunderbird was utilized to parse and open the EML file from the phishing email.
			</p>
			<p>
			<img width="975" height="169" alt="image" src="https://github.com/user-attachments/assets/0e3df460-713c-4949-820b-bd9f48447939" />
			</p>
			<p>
			<img width="975" height="472" alt="image" src="https://github.com/user-attachments/assets/1120b75c-40e4-42fb-96b6-c81ab5824a7a" />
			</p>
			<p>
			<img width="975" height="469" alt="image" src="https://github.com/user-attachments/assets/759b11ea-c297-4d74-a166-dce2a3cd2576" />
			</p>
			<p>
				Based on the email content, I took note of the email address used to send the phishing email and that is<b><u> agriffin@bpakcaging[.]xyz</u></b>. Aside from that, I noticed that there’s also a typosquatting, which is a red flag already to me. Instead of using the word, “<u>packaging</u>”, the attacker used a misspelled word, and that is “<u>pakcaging</u>”, which serves as a primary indicator of deceptive infrastructure.
				</p>
			<p>
				After that, I downloaded the <b>Invoice.zip</b> and extract using the terminal or command-line interface (CLI), at the same time, input the password, which is the <b>Invoice2023!</b> that has been provided inside the email content. After the file unzipped, it appeared as <b>Invoice_20230103.lnk</b>.
			</p>
			<p>
			<img width="975" height="403" alt="image" src="https://github.com/user-attachments/assets/92c3fec1-612c-4952-a846-ecc2eafa652e" />
			</p>
			<p>
				I used a lnkparse tool against <b>Invoice_20230103.lnk</b>  file, in order for me to find out the encoded payload Command-line arguments.
			</p>
			<p>
			<img width="975" height="487" alt="image" src="https://github.com/user-attachments/assets/80172800-14ba-457a-a98e-fc443154b6e9" />
			</p>
			<p>
			<img width="975" height="457" alt="image" src="https://github.com/user-attachments/assets/66c59f53-0e82-4fb0-a0c8-3cdd2a99b426" />
			</p>
			<p>
				To decode this Command-line arguments, I used Cyberchef tool. Applying standard cryptographic decoding techniques, the string was successfully de-obfuscated using a <b>From Base64</b> recipe.
			</p>
			<p>
			<img width="975" height="264" alt="image" src="https://github.com/user-attachments/assets/db6d8dfe-2675-4b3f-9a9f-4dc18f7f5921" />
			</p>
			<p>
				The output result is an example of a C2 "cradle" or downloader. While the DownloadString method itself is a legitimate administrative tool created by Microsoft, the specific way it is packaged in the string—hidden inside a Base64-encoded PowerShell command—is a classic indicator of malicious C2 activity.
			</p>
			<p>
				In order for me to find the name of the third-party mail relay serviced used by the attacker based on the DKIM-Signature and List-Unsubscribe headers, I checked on the View Source first of the said email.
			</p>
			<p>
			<img width="975" height="580" alt="image" src="https://github.com/user-attachments/assets/a19a9885-a544-480e-91c4-041f38873268" />
			</p>
			<p>
			<img width="975" height="762" alt="image" src="https://github.com/user-attachments/assets/03f298cd-9fd3-4ffb-b2f3-a9d107c41fc0" />
			</p>
			<p>
				To make this easy to analyze the third-party mail, I used the online mail header tool, <b>mha.azurewebsites.net</b>. From there, I found the third-party mail relay service used was <b>elasticmail</b>.
			</p>
			<p>
			<img width="975" height="444" alt="image" src="https://github.com/user-attachments/assets/c03b92d4-5fb7-4e73-a86c-ff4ac9c98c16" />
			</p>

<br>
		<li><b>Phase 2: Host Execution & Artifact Forensic Analysis</b></li>
			<br>
			<p>
				Now, on the initial findings, I discovered how the malicious attachment compromised the employee’s workstation; through the execution of PowerShell command, as well as, decoding the payload, which reveals the starting point of endpoint activities.
			</p>
			<p>
				With these discoveries, I proceed analyzing the PowerShell logs (Powershell.json) to uncover the potential impact of the attack. I can start to analyze by searching the execution of the initial payload in the PowerShell logs.
			</p>
			<p>
				To efficiently manipulate the structured JSON event log data, the <b>jq</b> command-line utility was integrated into the parsing pipeline. I used <b>jq</b> and other various commands.
			</p>
			<p>
			<img width="975" height="625" alt="image" src="https://github.com/user-attachments/assets/6ba91759-be51-4061-9cfd-91c38369cbc3" />
			</p>
			<p>
				I used a command that will filter only the fields in the file, which can be helpful in this investigation.
			</p>
			<p>
			<img width="975" height="492" alt="image" src="https://github.com/user-attachments/assets/1af0172e-8776-4e42-a836-a5f226da53d7" />
			</p>
			<p>
				I sorted the logs based on their Timestamp and printed multiple field values by using <b>ScriptBlockText</b> as the field text.
			</p>
			<p>
				<img width="975" height="49" alt="image" src="https://github.com/user-attachments/assets/190ecbfd-def7-4cec-af9c-67e11eb49f35" />
			</p>
			<p>
				Based on the result, the domains used by the attacker for file hosting and command-and-control (C2) are <b>cdn[.]bpakcaging[.]xyz</b> and <b>files[.]bpakcaging[.]xyz</b>. Aside from that, I found out that the name of the enumeration tool downloaded by the attacker is <b>Seatbelt</b>.
			</p>
			<p>
			<img width="975" height="373" alt="image" src="https://github.com/user-attachments/assets/63d9f37b-a6ce-4007-ab2a-fbd55012d017" />
			</p>
			<p>
				Using the same command, I added grep to help me to locate the full file path easily, which accessed by the attacker using the downloaded <b>sq3[.]exe</b> binary, a legitimate command-line tool used to view and manage database files. The full file path is 
			</p>
	
   		C:\\Users\\j[.]westcott\\AppData\\Local\\Packages\\Microsoft[.]MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum[.]sqlite.

<p>
	Another thing is that, <b>Microsoft Sticky Notes</b> is the software that uses the file.
</p>
<p>
	<img width="975" height="172" alt="image" src="https://github.com/user-attachments/assets/2859b222-7287-4b31-bdf4-03a8cda05ea8" />
</p>
<p>
	The name of the exfiltrated file by the attacker was <b>protected_data[.]kdbx</b>. 
</p>
<p>
	<img width="975" height="172" alt="image" src="https://github.com/user-attachments/assets/5e0f449a-e7e7-430d-8143-c96a62d92fdb" />
</p>
<p>
	Based on the result, I researched online if what file, application or software uses the <b>.kdbx</b> file extension. The result shows that it is the KeePass 2 application.
</p>
<p>
	<img width="975" height="317" alt="image" src="https://github.com/user-attachments/assets/f1472a6d-769c-48db-88ff-d965e0897a05" />
</p>
<p>
	The encoding used by the attacker during the exfiltration attempt of the sensitive file was <b>hex</b> and the tool used for exfiltration was <b>nslookup</b>.
</p>
<p>
	<img width="975" height="153" alt="image" src="https://github.com/user-attachments/assets/559faf0b-192b-468f-9e9c-fffc1504f7e3" />
</p>

<br>
<li><b>Phase 3:</b> Network Traffic Analysis & Exfiltration Identification/Triage</li>

<br>
<p>
	Based on the PowerShell logs investigation, I now have seen the full impact of the attack, such as the threat actor was able to read and exfiltrate two potentially sensitive files <b>(protected_data[.]kdbx & plum[.]sqlite)</b>, and the domains and ports used for network activity were discovered <b>(cdn[.]bpakcaging[.]xyz[:]8080</b> and <b>files[.]bpakcaging[.]xyz)</b>, which also includes the tool used by the threat actor for exfiltration.
</p>
<p>
	I utilized the packet capture <b>(capture[.]pcapng)</b> and opened it with Wireshark. By searching for <b>sq3[.]exe</b>, I investigated on what software was used by the attacker to host its presumed file or payload server through the input of <b>files[.]bpakcaging[.]xyz</b> on the search bar. I found out that the attacker was using <b>Python</b>.
</p>
<p>
	<img width="975" height="254" alt="image" src="https://github.com/user-attachments/assets/0af0ba53-9e4f-46d5-9cb7-d03838e8e178" />
</p>
<p>
	<img width="975" height="305" alt="image" src="https://github.com/user-attachments/assets/5653dce2-728e-4aad-87f2-85b5d4165473" />
</p>
<p>
	<img width="975" height="395" alt="image" src="https://github.com/user-attachments/assets/e97259cc-7794-430f-aa75-f0a39b0bbbf0" />
</p>
<p>
	<img width="975" height="243" alt="image" src="https://github.com/user-attachments/assets/2f438c30-ab5f-4d37-892b-3a112f6bbcff" />
</p>
<p>
	Based from the previous result from Phase 2, the HTTP method used by the C2 for the output of the commands executed by the attacker was <b>POST</b> method.
</p>
<p>
	<img width="975" height="149" alt="image" src="https://github.com/user-attachments/assets/f5c09541-b7da-4327-8195-1788538297a3" />
</p>
<p>
	In order to identify what was the password of the exfiltrated file, I investigated using Wireshark through the input of <b>sq3.exe</b>.
</p>
<p>
	<img width="975" height="392" alt="image" src="https://github.com/user-attachments/assets/ba94a09c-cf99-4f5b-a498-5fd0a2f1a480" />
</p>
<p>
	<img width="975" height="711" alt="image" src="https://github.com/user-attachments/assets/8d661885-d21b-4d1e-8057-826a74a3e9bc" />
</p>
<p>
	I analyzed the sequential TCP streams, shifting from stream 749 to stream 750, to isolate the raw data payloads transmitted during the session. The payload stream revealed a massive array of decimal values, which were extracted for forensic decoding.
</p>
<p>
	<img width="975" height="714" alt="image" src="https://github.com/user-attachments/assets/0343c384-4b0f-4d0e-a90f-ed27d766cf4e" />
</p>
<p>
	I used “<b>Magic</b>” to initially identify what type of characters they were.
</p>
<p>
	<img width="975" height="475" alt="image" src="https://github.com/user-attachments/assets/23d79213-a148-48c2-b302-90c9456a6b06" />
</p>
<p>
	By clicking or selecting “<b>From_Decimal</b>” from Recipe section, the master password for the exfiltrated file is now retrieved.
</p>
<p>
	<img width="975" height="435" alt="image" src="https://github.com/user-attachments/assets/ed158a21-cf73-4f98-bbc7-8c5b34894878" />
</p>
<p>
	Another important and sensitive information is the Account Number, which was stored inside the exfiltrated file. I did a lot of research online until I ended up in combining with different commands, thus, TShark was leveraged via the command-line to rebuild the payload.
</p>
<p>
	Command:
</p>

	tshark –r capture.pcapng –Y “ip.dst==167[.]71[.]211[.]113 and dns” –T fields –e dns[.]qry[.]name | grep –E ‘[A-F0-9]+[.]bpakcaging[.]xyz $’ | cut –d’-‘ –f1 | tr –d ‘\n’ | xxd –p –r > protected_data[.]kdbx

<p>
	<img width="975" height="141" alt="image" src="https://github.com/user-attachments/assets/1e77a6bb-330c-4caf-9424-776857ff6a9d" />
</p>
<p>
	Now, let me explain each of these commands. This command is a classic example of <b>DNS tunneling data exfiltration</b>. The attacker encoded a hidden file (a <b>.kdbx</b> KeePass password database) into the subdomains of DNS queries, and this pipeline piece them back together.
</p>
<p>
	Here is the breakdown of what each part does:
	<ul>
		<li><b>tshark -r capture[.]pcapng -Y "ip.dst==167[.]71[.]211[.]113 and dns" -T fields -e dns[.]qry[.]name</b></li>
			<p>
				This command extracts the requested domain names from a network capture.
			</p>
		<li><b>grep -E '[A-F0-9]+[.]bpakcaging[.]xyz $ '</b></li>
			<p>
				This command filters the list to ensure it only processes the attacker’s specific data-carrying domains.	
			</p>
		<li><b>cut -d'.' -f1</b></li>
			<p>
				This command strips away the domain name, leaving only the encoded data.
			</p>
		<li><b>tr -d '\n'</b></li>
			<p>
				This command merges all the separate lines into one single, continuous string.
			</p>
		<li><b>xxd -p -r > protected_data[.]kdbx</b></li>
			<p>
				This command converts the giant hex string back into its original binary file format.
			</p>
	</ul>

<p>
	I opened the <b>artefacts</b> folder and found the <b>protected_data[.]kdbx</b>, then run it.
</p>
</p>
<p>
	<img width="975" height="366" alt="image" src="https://github.com/user-attachments/assets/cec64c0f-a6ed-4d92-98d9-8b8b145957e8" />
</p>
<p>
	The KeePass banner appeared and asked for the Master Password (<b>%p9^3!lL^Mz47E2GaT^y</b>, which I acquired earlier), then I input those.
</p>
<p>
	<img width="825" height="409" alt="image" src="https://github.com/user-attachments/assets/37c0c255-9677-4869-aeb7-501d5312c673" />
</p>
<p>
	I investigated the application to find the Account Number, thus, I selected the <b>Card Number</b> if the sensitive information would appear, and so it did.
</p>
<p>
	<img width="975" height="609" alt="image" src="https://github.com/user-attachments/assets/77ff5d70-d961-45cd-b9d3-284e04548717" />
</p>

<br>
<h3>MITRE ATT&CK</h3>
<ul>
	<li><b>Phishing:</b> Malicious Attachment (T1566.001)</li>
	<li><b>Command and Scripting Interpreter:</b> PowerShell (T1059.001)</li>
	<li><b>System Information Discovery (T1082)</b></li>
	<li><b>Credentials from Password Stores (T1555)</b></li>
	<li><b>Exfiltration Over Alternative Protocol:</b> DNS Tunneling (T1048.003)</li>
</ul>

<br>
<h3>Indicators of Compromise (IoC)</h3>
<p>
	During the investigation, the following technical indicators were identified and extracted to facilitate enterprise-wide blocklisting, threat hunting, and perimeter containment:
</p>
<ul>
<li><h4>Network & Infrastructure Indicators</h4></li>
	<ul>
		<li><b>Phishing Sender Address:</b> agriffin@bpakcaging[.]xyz</li>
		<li><b>Command & Control (C2) / Payload Hosting Domain:</b> files[.]bpakcaging[.]xyz</li>
		<li><b>Content Delivery Network (CDN) Domain:</b> cdn[.]bpakcaging[.]xyz</li>
		<li><b>Exfiltration Destination IP Address:</b> 167[.]71[.]211[.]113</li>
	</ul>

<li><h4>Host & File Indicators</h4></li>
	<ul>
		<li><b>Malicious Loader File:</b> Invoice_20230103[.]lnk</li>
		<li><b>Masquerade Binary:</b> sq3[.]exe</li>
		<li><b>Targeted Financial Credential Repositories:</b>
			<ul>
				<li><b>Windows Sticky Notes Database</b></li>
														
				C:\Users\j[.]westcott\AppData\Local\Packages\Microsoft[.]MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum[.]sqlite
			
<li><b>KeePass Password Vault</b></li>
		</li>			 				
	
	protected_data[.]kdbx 		
</ul>
</ul>

<br>
<h3>Lesson Learned</h3>
<p>
	This incident underscores the critical necessity of a defense-in-depth security posture, beginning with continuous user awareness training to mitigate sophisticated, targeted phishing vectors. From a technical perspective, the investigation highlights the importance of implementing robust Endpoint Detection and Response (EDR) telemetry to catch "Living off the Land" techniques, such as administrative tool masquerading and unauthorized PowerShell execution. Finally, this compromise demonstrates that standard network perimeters are insufficient without proactive protocol auditing; implementing strict DNS monitoring and behavioral analysis is paramount to identifying and blocking covert data exfiltration channels before assets leave the enterprise boundary.
</p>

<br>
<h3>Recommendations</h3>
<p>
	To comprehensively mitigate the architectural vulnerabilities exploited during this intrusion, the enterprise must immediately execute a multi-layered defense-in-depth remediation strategy across email, endpoint, and network boundaries. 
</p>
<p>
	First, perimeter security must be reinforced by implementing aggressive email filtering to block typosquatted infrastructure, enforcing strict DKIM and SPF verification, and delivering targeted user awareness training to high-risk business units
</p>
<p>
	Second, the internal endpoint footprint must be hardened by deploying robust Endpoint Detection and Response (EDR) telemetry to flag obfuscated PowerShell execution cradles, enforcing strict application whitelisting to block masqueraded utilities like <b>sq3.exe</b> from user-writable directories, and mandating a zero-tolerance policy for plaintext corporate credential storage. 
</p>
<p>
	Finally, to eliminate covert exfiltration vectors, the security team must deploy behavioral network analysis rules capable of detecting high-frequency DNS tunneling, while restricting local workstations from querying public nameservers directly, forcing all outbound internal requests through a secure, monitored DNS proxy.
</p>

<br>
<h3>References & Acknowledgement</h3>
<p>
	This incident response case study was conducted using <b>Boogeyman 1</b>, an educational environment provided by the <b>TryHackMe platform</b>. All logs, artifacts, and network captures analyzed herein originate from their defensive security training curriculum. This controlled simulation was completed to enhance tactical awareness, technical knowledge, and practical skills that can be directly applied to protect enterprise environments. 
</p>

</ul>











