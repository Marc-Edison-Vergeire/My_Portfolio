<h1>Phishing Email Investigation & Incident Response — Microsoft Impersonation, Malicious URL Analysis, and Credential Harvesting</h1>

<br>
<p><b>Role:</b> SOC Analyst / Incident Response Analyst</p>
<p><b>Environment:</b> Windows 10 Workstation → Gmail → Isolated VM → Web Browser → VirusTotal → OSINT Tools</p>
<p><b>Attack:</b> Credential Harvesting/Phishing Attack</p>
<p><b>Target:</b> Company Employee — “John D. Victim”</p>
<p><b>Attacker:</b> Unknown / Simulated Threat Actor</p>
<p><b>Target Service:</b> Microsoft Account / Microsoft-Branded Authentication</p>
<p><b>Detection:</b> Phishing Indicators + Email/Header Analysis</p>
<p><b>Response:</b> Containment + IoC Blocking/Monitoring + User Awareness</p>
<p><b>Investigation:</b> Email Analysis + Header Analysis + URL Analysis + VM Detonation + Threat Hunting</p>
<p><b>Framework:</b> NIST Cybersecurity Framework and MITRE ATT&CK</p>

<br>
<h2>Executive Summary</h2>
<p>On September 7, 2026, a simulated phishing attack targeted a company employee through a fraudulent Microsoft-themed email designed to harvest user credentials. The attack used social-engineering techniques, including impersonation, typosquatting, urgency, and a shortened malicious URL that redirected the user to a fraudulent Microsoft login page. The employee recognized the email as suspicious due to prior security-awareness training and reported it without submitting any credentials, preventing account compromise.</p>
<p>A subsequent SOC investigation confirmed multiple indicators of malicious activity, including the suspicious sender identity, malicious URL reputation, and credential-harvesting behavior observed in an isolated environment. Although SPF, DKIM, and DMARC checks passed, the investigation demonstrated that email authentication results alone are not sufficient to determine legitimacy. The incident was successfully contained by removing and blocking the malicious email and associated indicators, notifying the affected user, escalating and documenting the incident, and conducting follow-up monitoring. No legitimate user credentials were compromised, demonstrating the effectiveness of security awareness and timely SOC intervention in reducing the potential impact of a phishing attack.</p>

<br>
<h2>Objectives</h2>
<p>The objective is to simulate and analyze a complete phishing attack scenario from both the threat actor's and SOC Analyst's perspectives, demonstrating how a phishing email can be crafted to impersonate a legitimate organization and used to harvest user credentials. The exercise aims to evaluate the effectiveness of security-awareness training in enabling users to recognize and report suspicious emails, while demonstrating the SOC Analyst's ability to investigate potential phishing indicators, including sender identity, email authentication results, email headers, IP addresses, URLs, redirects, and fraudulent login pages.</p>
<p>It also aims to demonstrate the application of threat-intelligence and analysis tools within an isolated environment, assess the potential impact of credential compromise, and apply appropriate incident-response actions such as containment, user notification, escalation, documentation, and continued monitoring. Ultimately, the exercise demonstrates the importance of a layered cybersecurity approach in detecting and preventing phishing attacks before they result in credential theft or further compromise of organizational systems.</p>

<br>
<h2>Scenario</h2>
<p>On September 7, 2026, at approximately 9:35 AM, a simulated company employee, <b>John D. Victim</b>, received an email claiming that his Microsoft account had experienced unusual activity and required immediate attention. The message employed an urgent account-security narrative and instructed the recipient to follow an embedded hyperlink to address the alleged issue. Recognizing several suspicious characteristics, John did not interact with the link or submit any credentials and instead reported the email to the Security Operations Center (SOC) for investigation.</p> <p>Acting as the SOC Analyst, I preserved the original message and conducted a structured investigation to determine its legitimacy and potential security impact. The investigation included examination of the sender identity, email headers, authentication results, embedded hyperlinks, URL reputation, and associated network indicators. Initial analysis identified multiple warning signs, including a suspicious sender address, an apparent impersonation of the Microsoft brand, and a typographical variation intended to make the sender appear legitimate.</p> <p>Further investigation determined that the embedded hyperlink did not lead to legitimate Microsoft infrastructure. Instead, the shortened URL redirected to a fraudulent Microsoft-style authentication page within the controlled laboratory environment. The simulated page was capable of capturing credentials submitted by a user, confirming that the email represented a credential-phishing attempt. The incident was subsequently treated as a security event, prompting appropriate containment, notification, documentation, and monitoring activities to prevent potential credential compromise and identify any related malicious activity.</p>

<br>
<h2>Skills Learned</h2>
<ul>
    <li>Phishing and social engineering analysis</li>
    <li>Threat actor and attack behavior analysis</li>
    <li>Phishing email and sender identification</li>
    <li>SPF, DKIM, DMARC, and email header analysis</li>
    <li>IP address and reputation investigation</li>
    <li>Threat intelligence and Indicator of Compromise (IoC) analysis</li>
    <li>URL, redirect, and malicious link investigation</li>
    <li>Isolated environment and virtual machine analysis</li>
    <li>Incident triage, containment, and remediation</li>
    <li>SOC investigation, documentation, escalation, and response</li>
</ul>

<br>
<h2>Tools Utilized</h2>
<ul>
    <li><b>Zphisher: </b>Phishing simulation and credential-harvesting demonstration</li>
    <li><b>TinyURL:</b> URL shortening and redirect analysis</li>
    <li><b>MaskPhish: </b>URL obfuscation demonstration</li>
    <li><b>VirusTotal: </b>URL, IP, and threat-intelligence analysis</li>
    <li><b>IPinfo: </b>IP address and geolocation investigation</li>
    <li><b>Cisco Talos: </b>IP reputation and threat intelligence</li>
    <li><b>IPLocation: </b>IP geolocation analysis</li>
    <li><b>Robtex: </b>IP, DNS, and network intelligence</li>
    <li><b>AbuseIPDB: </b>IP reputation and abuse investigation</li>
    <li></li><b>WhatIsMyIP: </b>IP and geolocation analysis</li>
    <li></li><b>WhatIsMyIPAddress: </b>IP information lookup</li>
    <li><b>MXToolbox: </b>Email header and DNS analysis</li>
    <li><b>Google Admin Toolbox: </b>Email header analysis</li>
    <li><b>Kali Linux: </b>Security testing and investigation environment</li>
    <li><b>Windows 10: </b>Simulated endpoint environment</li>
    <li><b>MHA (Message Header Analyzer): </b>Email header analysis</li>
    <li><b>Gmail: </b>Email delivery and authentication analysis
</li>
    <li><b>Virtual Machine (VM)/Sandbox: </b>Isolated malware/phishing analysis environment</li>
    <li><b>VPN: </b>Simulated network-location obfuscation</li>
</ul>

<br>
<h2>Artifacts</h2>
    <ul>
       <li><b>Victim email:</b> victimjohn[.]windows10@gmail[.]com</li>
       <li><b>Phishing email:</b> !! Microsoft account unusual sign-in activity</li>
       <li><b>Spoofed sender:</b> support[.]microsorft@gmail[.]com / typosquatted <i>microsorft</i></li>
       <li><b>Spoofed Microsoft branding/logo</b></li>
       <li><b>Malicious shortened URL:</b> https[:]//tinyurl[.]com/6cjrcydx</li>
       <li><b>Payload/fake login URLs: </b>https[:]//127[.]0[.]0[.]1[:]5555 / http[:]//127[.]0[.]0[.]1[:]5555/login[.]html</li>
       <li><b>Sender IP address: </b>209[.]85[.]220[.]41</li>
       <li><b>Email authentication and header results:</b> SPF, DKIM, DMARC, and header analysis</li>
       <li><b>Threat-intelligence evidence: </b>VirusTotal URL/IP findings and URL redirection results</li>
       <li><b>Incident evidence and response: </b>credential-harvesting evidence, VM analysis, screenshots, containment, and documentation</li>
    </ul>

<br>
<h2>Findings</h2>
<h3>Threat Actor's Perspective</h3>
<p>On the threat actor's end, I demonstrated how a threat actor could craft a phishing link. One of the most common tools that can be found online is called <b>Zphisher</b>. This tool provides more than 30 different platforms to choose from. For this demonstration, I selected <b>option 4</b>, which represents <b>Microsoft</b>, as the platform that would be used to target a company employee.</p>
<p>After selecting Microsoft as the platform, the tool provided three different choices for generating a payload link. I selected <b>option 1</b>, <b>Localhost</b>, which would return information such as the credentials entered by the target. I then selected "Yes" to create a custom port, using port number <b>5555</b>.</p>
<p>The tool subsequently generated the following payload link:</p>
        https[:]//127[.]0[.]0[.]1[:]5555
<p>This payload link could theoretically be delivered to a particular target through various methods, such as email, a file stored on a USB or flash drive, or other delivery methods depending on the threat actor's approach.</p>
<p>To make the payload link less obvious and appear more legitimate, threat actors may use URL-shortening platforms such as <b>Bitly</b> or <b>TinyURL</b> to conceal the original link generated by Zphisher. In this demonstration, the URL was changed from:</p>
        https[:]//127[.]0[.]0[.]1[:]5555
<p>to:</p>
        https[:]//tinyurl[.]com/6cjrcydx
<p>More skilled threat actors may use additional techniques to make the shortened URL appear more legitimate. One example is <b>MaskPhish</b>, which can be used to modify the appearance of a URL. However, for this demonstration, I used the shortened payload link and incorporated it into the crafted phishing email.</p>
<p>This resulted in the final phishing email, which was designed to appear as genuine and convincing as possible in an attempt to persuade the recipient, <b>victimjohn[.]windows10@gmail[.]com</b>, to click the link. To make the demonstration more realistic, I also used a VPN to simulate an attempt by the threat actor to conceal the originating network location.</p>

<br>
<h3>Target/Victim Perspective</h3>
<p>On the target or victim's end, <b>John D. Victim</b>, a company employee, received the email on his Windows 10 workstation. He opened an unusual email claiming that his Microsoft account was about to expire due to inactivity and required immediate attention because of the urgency of the situation. The email also provided a specific deadline of <b>October 21, 2026</b>.</p>
<p>John regularly uses his Microsoft account for work-related activities. Fortunately, the company conducts monthly security-awareness training covering topics such as phishing emails, social engineering, and other cybersecurity threats.</p>
<p>As a result of this training, John became suspicious of the email and asked me to investigate it. This is where I, acting as a SOC Analyst, became involved. I began investigating and verifying the contents of the email to determine whether it was a phishing attempt or a legitimate communication.</p>
<p>Since John did not click the link provided in the email, I was able to safely conduct the investigation using multiple online tools and resources before reaching a conclusion.</p>
<p>At approximately <b>9:35 AM on September 7, 2026</b>, John received the email in his Gmail inbox. The subject line was:</p>
        "!! Microsoft account unusual sign-in activity"
<p>John opened the email because he was concerned about the urgent nature of the message and wanted to understand why immediate action was required.</p>


<br>
<h3>Phase 1: Sender Investigation</h3>
<p>Upon investigation, the sender appeared to be Microsoft Teams, with the following email address:</p>
        support[.]microsorft@gmail[.]com
<p>Several issues were immediately identified.</p>
<p>The sender's email address was a significant red flag because it appeared to impersonate Microsoft while using a Gmail domain. In addition, the word "<b><i>microsorft</i></b>" was misspelled and should have been "<b><i>microsoft</i></b>."</p>
<p>This is an example of a <b>typosquatting technique</b>, in which an attacker uses a domain name, email address, or other identifier that closely resembles a legitimate one in an attempt to deceive the recipient.</p>
<p>A legitimate Microsoft communication would not normally be expected to originate from a random Gmail address. Therefore, the sender's address provided an important indication that the email was potentially malicious.</p>
<p>I then opened the original message and examined the complete contents of the email.</p>



<br>
<h3>Phase 2: Email Authentication Investigation</h3>
<p>Although the <b>SPF</b>, <b>DKIM</b>, and <b>DMARC</b> checks displayed in Gmail indicated <b>PASS</b>, I continued the investigation rather than considering the email legitimate solely based on these results.</p>
<p>I investigated the sender's email address using several online email-verification and checking services.</p>
<p>Based on the information gathered from these tools and resources, the sender's email address presented several inconsistencies and could not be reliably associated with a legitimate Microsoft platform.</p>
<p>Therefore, the authentication results alone were not sufficient to establish that the email was legitimate.</p>


<br>
<h3>Phase 3: Sender IP Investigation</h3>
<p>I then investigated the sender's IP address:</p>
        209[.]85[.]220[.]41
<p>I used several security and threat-intelligence platforms to investigate the IP address and its associated activity.</p>
<p>On <b>VirusTotal</b>, the IP address itself did not initially appear to be blacklisted. However, after conducting further investigation within the platform, I found that three detected files had communicated with the IP address. This indicated an association with potentially malicious activity, even though the IP address itself was not directly classified as malicious.</p>
<p>I also investigated the geographical location associated with the IP address.</p>
<p>Several platforms, including <b>VirusTotal</b>, <b>IPinfo</b>, <b>Cisco Talos</b>, <b>IPLocation</b>, <b>Robtex</b>, <b>AbuseIPDB</b>, <b>WhatIsMyIP</b>, and <b>WhatIsMyIPAddress</b>, returned different geographical results.</p>
<p>Some platforms identified <b>Mountain View, California, USA</b>, while others identified <b>Utica, New York, USA</b>.</p>
<p></p>

<br>
<h3>Phase 4: Email Header Investigation</h3>
<p>I copied the raw email headers and analyzed them using several email-header analysis platforms, including <b>mha.azurewebsites.net</b>, <b>MXToolbox</b>, and <b>Google's Toolbox</b>.</p>
<p>Based on the results generated by these platforms, the email headers did not immediately identify the message as malicious.</p>
<p>However, this did not eliminate the possibility that the email was a phishing attempt. The sender's identity, email content, hyperlink, and destination still required further investigation.</p>

<br>
<h3>Phase 5: Microsoft Logo Investigation</h3>
<p>I hovered over the Microsoft logo displayed next to the sender's name and copied the associated URL to determine where the image was being retrieved from.</p>
<p>This was relevant because an attacker could potentially obtain, copy, or download a legitimate Microsoft logo from publicly available sources and reuse it in a phishing email to make the message appear more authentic.</p>
<p>Therefore, the presence of the Microsoft logo was not considered sufficient evidence that the email was legitimate.</p>

<br>
<h3>Phase 6: Hyperlink Investigation</h3>
<p>I investigated the email content again by examining the original message and identifying the hyperlink associated with the word "<b>here</b>."</p>
<p>The purpose of this investigation was to determine whether the hyperlink directed the recipient to a legitimate Microsoft website or to a spoofed or malicious destination designed to impersonate Microsoft.</p>
<p>The investigation revealed that the hyperlink did not point to a legitimate Microsoft URL. Instead, it used the following shortened URL:</p>
      https[:]//tinyurl[.]com/6cjrcydx  
<p>At this point, the shortened URL was identified as a significant indicator that the email was suspicious.</p>
<p>I then submitted the URL to <b>VirusTotal</b> for further analysis to determine whether it had been associated with malicious activity.</p>
<p>The results indicated that the URL was associated with <b>phishing and malicious activity</b>.</p>
<p>I also investigated the IP address associated with the URL; however, the IP address itself did not initially appear to be malicious.</p>
<p>This demonstrated the importance of investigating the complete URL and redirect chain rather than relying solely on the reputation of an individual IP address.</p>

<br>
<h3>Phase 7: Isolated Environment Investigation</h3>
<p>To safely investigate the behavior of the URL, I used a virtual machine in an isolated environment.</p>
<p>I opened a browser within the virtual machine and entered the URL to determine whether it redirected to a suspicious or malicious destination.</p>
<p>The URL redirected to a fake Microsoft login page designed to resemble a legitimate Microsoft authentication page. A potential victim could enter their credentials into the fraudulent page, after which the credentials could be transmitted to the threat actor's infrastructure.</p>
<p>This behavior represents a <b>credential-harvesting technique</b>, in which an attacker impersonates or imitates a legitimate service to deceive a victim into submitting sensitive authentication information.</p>
<p>The fraudulent page used the following URL:</p>
        http[:]//127[.]0[.]0[.]1[:]5555/login[.]html


<br>
<h3>Potential Impact on the Victim</h3>
<p>If John had clicked the link and entered valid credentials, the threat actor could potentially have captured those credentials.</p>
<p>The attacker could then attempt to use the stolen credentials to gain unauthorized access to John's account. Depending on the account's security controls and privileges, the attacker could potentially attempt to change the account password, lock the legitimate user out of the account, access sensitive information, or use the compromised account to conduct additional attacks.</p>
<p>A compromised account could also potentially be used as an entry point for <b>lateral movement</b> within the organization's environment.</p>
<p>If the attacker successfully gained access to additional systems or sensitive information, the incident could potentially affect not only John but also the organization's systems, data, operations, employees, and reputation.</p>

<br>
<h3>Threat Actor's Credential-Harvesting View</h3>
<p>I also examined the simulated threat actor's perspective to understand how credentials submitted by a victim could appear on the attacker's side.</p>
<p>During the demonstration, the following test credentials were captured:</p>
        Username: wrong_email@gmail.com
        Password: Password
<p>These were demonstration credentials and were not the legitimate credentials of the affected employee.</p>
<p>This demonstrated how credentials entered into a fraudulent login page could potentially be transmitted to infrastructure controlled by the threat actor. If legitimate credentials had been entered, the attacker could potentially attempt to use them to gain unauthorized access to the victim's account.</p>


<br>
<h3>Incident Response</h3>
<p>Finally, I initiated the appropriate response actions by blocking and deleting the malicious email and blocking the identified malicious indicators where applicable.</p>
<p>I informed John about the incident and provided guidance on how to identify and avoid similar phishing attempts in the future.</p>
<p>I then reported the incident to the appropriate team and manager and documented the investigation, findings, indicators, and response actions.</p>
<p>Following containment, I continued monitoring the environment and followed up for any additional signs of compromise or related malicious activity.</p>

<br>
<h3>Conclusion</h3>
<p>Based on the investigation, the email was determined to be a <b>phishing attempt</b> designed to harvest user credentials.</p>
<p>Although the email passed SPF, DKIM, and DMARC checks, these results alone did not establish its legitimacy. Multiple additional indicators, including the suspicious sender address, typosquatting, use of a shortened URL, malicious URL reputation, and redirection to a fraudulent Microsoft login page, supported the conclusion that the email was malicious.</p>
<p>The incident was successfully identified before the victim submitted legitimate credentials. The malicious email and associated indicators were contained, the affected user was informed, the incident was escalated and documented, and continued monitoring was performed to identify any additional signs of compromise.</p>


<br>
<h2>MITRE ATT&CK Mapping</h2>
<ul>
    <li><b>T1566.002 – Phishing: Spearphishing Link</b> - Malicious link delivered through a phishing email.</li>
    <li><b>T1036.005 – Masquerading: Match Legitimate Name or Location</b> - Attacker impersonated Microsoft and used Microsoft branding.</li>
    <li><b>T1583.001 – Acquire Infrastructure: Domains</b> - Use of a shortened URL to facilitate phishing activity.</li>
    <li><b>T1608.005 – Stage Capabilities: Link Target</b> - Phishing infrastructure prepared to redirect victims to a fake login page.</li>
    <li><b>T1056.002 – Input Capture: GUI Input Capture</b> - Fake Microsoft login page designed to capture submitted credentials.</li>
    <li><b>T1078 – Valid Accounts</b> - Stolen credentials could potentially be used for unauthorized account access.</li>
    <li><b>T1589.002 – Gather Victim Identity Information: Email Addresses</b> - Targeting of a specific employee through their email address.</li>
    <li><b>T1566 – Phishing</b> - Overall attack technique involving deceptive email-based delivery.</li>
</ul>
<h4>Primary Techniques Demonstrated</h4>
<ul>
    <li><b>T1566.002 – Spearphishing Link</b></li>
    <li><b>T1056.002 – Input Capture:</b> GUI Input Capture</li>
    <li><b>T1036.005 – Masquerading</b></li>
    <li><b>T1078 – Valid Accounts</b></li>
</ul>

<br>
<h2>Indicators of Compromise (IoC)</h2>
<ul>
    <li><b>Suspicious/Phishing sender: </b>support[.]microsorft@gmail[.]com</li>
    <li><b>Sender IP address observed:</b> 209[.]85[.]220[.]41</li>
    <li><b>Shortened Malicious URL:</b> https[:]//tinyurl[.]com/6cjrcydx</li>
    <li><b>Fraudulent/Payload Login URL:</b> http://127[.]0[.]0[.]1[:]5555/login[.]html</li>
    <li><b>Brand impersonation:</b> Microsoft</li>
    <li><b>Typosquatting:</b> <b><i>microsorft</i></b> instead of <b><i>microsoft</i></b></li>
    <li><b>Attack Technique: </b>Credential harvesting</li>
    <li><b>Malicious artifact:</b> Fraudulent Microsoft login page</li>
    <li><b>Targeted service:</b> Microsoft account authentication</li>
    <li><b>URL Shortener:</b> TinyURL</li>
    <li><b>Phishing Subject: </b>!! Microsoft account unusual sign-in activity</li>
    <li><b>Associated Files:</b> 3 files observed communicating with 209[.]85[.]220[.]41</li>
</ul>

<br>
<h2>Investigation Timeline</h2>
<p></p>


<br>
<h2>Lessons Learned</h2>
<p>This incident demonstrated that effective phishing detection requires a combination of technical analysis, user awareness, and a structured incident-response process rather than reliance on a single security control. One of the key lessons learned was that SPF, DKIM, and DMARC passing results do not automatically confirm that an email is legitimate, particularly when attackers can use legitimate email services or compromised infrastructure. Careful examination of the sender address, typosquatting indicators, email content, hyperlinks, URL reputation, redirect behavior, and the final destination was essential in identifying the phishing attempt.</p>
<p>The investigation also highlighted the importance of security-awareness training, as the user's knowledge of phishing and social-engineering techniques prevented the submission of legitimate credentials and allowed the incident to be reported promptly. Furthermore, conducting URL and malware analysis within an isolated environment reduced the risk of exposure while allowing the suspicious behavior to be safely examined. Finally, the incident reinforced the importance of timely containment, indicator blocking, user notification, escalation, documentation, and continuous monitoring. Overall, the exercise demonstrated that a strong cybersecurity defense depends on multiple layers of protection working together, with both technical controls and informed users playing critical roles in preventing credential theft and limiting the potential impact of phishing attacks.</p>

<br>
<h2>Recommendations</h2>
<p>Based on the findings of this investigation, the organization should strengthen its overall phishing-defense strategy through a combination of technical controls, employee awareness, and continuous monitoring. Regular security-awareness training and phishing simulations should be conducted to ensure employees can recognize suspicious sender addresses, typosquatting, shortened URLs, social-engineering techniques, and fraudulent login pages. The organization should also enforce strong email-security controls, including effective SPF, DKIM, and DMARC policies, URL and attachment scanning, anti-phishing and threat-intelligence capabilities, and appropriate blocking of known malicious domains and indicators. </p>
<p>Multi-factor authentication (MFA), preferably using phishing-resistant authentication methods, should be implemented to reduce the impact of compromised credentials. Employees should be encouraged to report suspicious emails immediately rather than interacting with embedded links, and security teams should maintain clear procedures for investigating, containing, documenting, and escalating reported phishing incidents. Finally, the organization should continuously monitor authentication activity, endpoint telemetry, and network traffic for indicators of credential compromise or account misuse, while regularly reviewing and updating security controls to address emerging phishing techniques and reduce the likelihood and potential impact of future attacks.</p>

<br>
<h2>References & Acknowledgment</h2>
<p>This investigation and demonstration were developed with reference to publicly available cybersecurity resources, threat-intelligence platforms, email-analysis tools, URL-analysis services, and security-awareness materials used to support the identification, analysis, and response to phishing activity. Resources and platforms consulted during the investigation included VirusTotal, MXToolbox, Google Admin Toolbox, IPinfo, Cisco Talos, IPLocation, Robtex, AbuseIPDB, WhatIsMyIP, and other publicly available security resources, while Zphisher and related phishing-simulation techniques were examined strictly within an isolated and controlled environment for educational and cybersecurity-awareness purposes. </p>
<p>I acknowledge the developers and providers of these tools and resources for making information and analytical capabilities available to security practitioners and learners. All credentials, accounts, URLs, and other potentially sensitive information presented in this demonstration were simulated or used solely for educational purposes, and no legitimate user credentials were intentionally collected or compromised. The purpose of this work is to demonstrate the methods used to identify, investigate, contain, and respond to phishing threats and to reinforce the importance of security awareness, verification, and responsible cybersecurity practices.</p>