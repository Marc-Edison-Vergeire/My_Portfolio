<h1>DFIR Phishing Incident Response</h1>

<h2>(Enterprise Email Forensics Case)</h2>

<h3>Objective</h3>
	<p>Analyze an enterprise workstation compromise by performing forensic triage on malicious email headers, decoding obfuscated execution artifacts, and correlating host and network logs to establish a chronological intrusion timeline.</p>

<h3>Scenario</h3>
	<p>A finance employee at a logistics firm received a highly targeted follow-up email regarding an unpaid invoice from a known packaging business partner. Unbeknownst to the employee, this was a sophisticated phishing attack containing a weaponized attachment that compromised the host or workstation upon execution.</p>
	<p>As the responding SOC Analyst, I flagged the anomalous execution of the attachment, correlating it with corresponding phishing reports submitted by other personnel within the finance division. Threat intelligence and TTP mapping indicate that the initial delivery mechanisms align directly with an emerging threat group actively targeting the logistics sector.</p>

<h3>Skills Learned</h3>
	<ul>
		<li>Email header & Forensic analysis</li>
		<li>Windows artifact forensics</li>
		<li>Log triage & Structured parsing</li>
		<li>Network traffic reconstruction</li>
		<li>Malware TTP identification</li>
	</ul>

<h3>Tool Used</h3>
	<ul>
		<li><b>Thunderbird</b> (free and open-source cross-platform email client)</li>
		<li><b>mha.azurewebsites.net</b> (Online email analyzer)</li>
		<li><b>lnkparse / LINKParse3 </b>(LNK parsing tool in CLI)</li>
		<li><b>Cyberchef.com </b>(intuitive web-based application)</li>
		<li><b>Wireshark</b> (Packet analyzer GUI)</li>
		<li><b>TShark </b> (Wireshark’s command-line)</li>
	</ul>

<h3>Artifacts</h3>
	<ul>
		<li><b>dump.eml</b> (Copy from the phishing email)</li>
		<li><b>powershell.json </b>(Powershell Logs from the finance employee’s host or workstation)</li>
		<li><b>capture.pcapng </b>(Packet capture from the same workstation)</li>
	</ul>

<h3>Phases</h3>
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
				Based on the email content, I took note of the email address used to send the phishing email and that is<b><u> agriffin@bpakcaging.xyz</u></b>. Aside from that, I noticed that there’s also a typosquatting, which is a red flag already to me. Instead of using the word, “<u>packaging</u>”, the attacker used a misspelled word, and that is “<u>packaging</u>”, which serves as a primary indicator of deceptive infrastructure.
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
<li><b></b></li>
   <li><b></b></li>
 </ul>












