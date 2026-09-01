<h1>SOC/Blue Team Lab: End-to-End SSH Brute-Force Attack Detection, Investigation, Monitoring, and Incident Response Using Wazuh SIEM</h1>


<br>
<p><b>Role:</b> SOC Analyst / Blue Team</p>
<p><b>Environment: </b>Kali Linux → Ubuntu Server → Wazuh SIEM</p>
<p><b>Attack: </b>SSH Brute Force / Password Guessing</p>
<p><b>Target: </b>10.0.2.12</p>
<p><b>Attacker: </b>10.0.2.3</p>
<p><b>Target Service: </b>SSH / TCP 22</p>
<p><b>Detection: </b>Wazuh Custom Rules</p>
<p><b>Response: </b>Wazuh Active Response</p>
<p><b>Investigation: </b>Discover + Threat Hunting</p>
<p><b>Framework: </b>MITRE ATT&CK</p>


<br>
<h2>Executive Summary</h2>
<p>This case study demonstrates the end-to-end detection, investigation, and response process for an SSH brute-force attack within a controlled virtualized cybersecurity lab environment. The attack was simulated from a Kali Linux machine against an Ubuntu Server hosting an SSH service. Initial connectivity testing confirmed that the target server was responsive, followed by Nmap reconnaissance to identify the availability of TCP port 22. After confirming that SSH was exposed, multiple failed authentication attempts were generated against the target account to simulate brute-force activity.</p>
<p> From the defensive perspective, Wazuh was used as the Security Information and Event Management (SIEM) platform to monitor authentication events, generate alerts, correlate repeated login failures, and trigger an Active Response. Investigation through the Wazuh Discover and Threat Hunting interfaces identified the attacking source IP address as 10.0.2.3 and confirmed repeated failed SSH authentication attempts against the Ubuntu Server. The exercise demonstrates practical SOC capabilities across network reconnaissance, security monitoring, alert triage, event analysis, threat hunting, attack validation, and automated response.</p>


<br>
<h2>Objective</h2>
<p>The primary objective of this project was to simulate an SSH brute-force attack against an Ubuntu Server and evaluate the ability of Wazuh to detect, alert on, investigate, and respond to repeated SSH authentication failures. The exercise was designed to replicate a realistic SOC workflow in which an analyst receives security telemetry, validates the significance of an alert, identifies the source of malicious activity, examines supporting evidence, and determines whether the observed behavior represents an actual attack. A secondary objective was to gain practical experience connecting offensive security techniques with defensive monitoring and demonstrating how SIEM telemetry can be used to identify authentication-based threats.</p>


<br>
<h2>Scenario</h2>
<p>A controlled enterprise-like lab environment was established using Kali Linux as the simulated adversary and an Ubuntu Server as the target system. The Ubuntu Server was monitored by Wazuh to provide security visibility into authentication activity. The simulated attacker first verified connectivity to the target and performed network reconnaissance to determine whether the SSH service was accessible. After confirming that TCP port 22 was open, the attacker generated multiple incorrect SSH authentication attempts against the target account.</p> 
<p>Acting as the SOC analyst on duty, the resulting security events were investigated through the Wazuh dashboard. The analyst reviewed the generated alerts, examined relevant fields including the rule ID, rule description, source IP address, and agent name, and performed additional investigation through Threat Hunting. The investigation ultimately identified the repeated authentication failures originating from <b>10.0.2.3</b>, supporting the conclusion that the activity represented an SSH brute-force attack.</p>


<br>
<h2>Skills Learned</h2>
<ul>
    <li>Network connectivity validation</li>
    <li>Nmap reconnaissance</li>
    <li>SSH security testing</li>
    <li>Brute-force attack simulation</li>
    <li>SIEM monitoring</li>
    <li>Wazuh alert analysis</li>
    <li>Security event investigation</li>
    <li>Log analysis</li>
    <li>Threat hunting</li>
    <li>Source IP identification</li>
    <li>Custom Wazuh rule analysis</li>
    <li>Active Response validation</li>
    <li>Incident triage</li>
    <li>Attack-to-alert correlation</li>
    <li>SOC investigation workflow</li>
</ul>


<br>
<h2>Tools Utilized</h2>
<ul>
    <li><b>Kali Linux:</b> Attack simulation and reconnaissance</li>
    <li><b>Ubuntu Server:</b> SSH target system</li>
    <li><b>Wazuh: </b>SIEM, detection, investigation, monitoring, and incident response</li>
    <li><b>Nmap:</b> Network and port scanning</li>
    <li><b>Wazuh Discover: </b>Security event analysis</li>
    <li><b>Wazuh Threat Hunting: </b>Investigative analysis</li>
</ul>


<br>
<h2>Artifacts</h2>
<ul>
    <li>Network connectivity test results</li>
    <li>Nmap scan results</li>
    <li>SSH authentication failure events</li>
    <li>Wazuh security alerts</li>
    <li>Custom Wazuh rule IDs and descriptions</li>
    <li>Wazuh Discover investigation</li>
    <li>Source IP identification</li>
    <li>Wazuh Active Response event</li>
    <li>Threat Hunting results</li>
    <li>Attack timeline</li>
    <li>Investigation screenshots</li>
    <li>Detection and response evidence</li>
</ul>


<br>
<h2>Findings</h2>
<h3>Phase 1: Target Connectivity Validation</h3>
<p>The investigation began by validating communication between the Kali Linux attack machine and the Ubuntu Server. A ping request was sent to the Ubuntu Server to determine whether the target was reachable and responsive within the lab network.</p>

<p>The successful connectivity test established that the target was accessible and allowed the assessment to proceed to network reconnaissance.</p>

<p><b>Finding:</b> The Ubuntu Server was reachable from the Kali Linux machine, confirming basic network connectivity between the simulated attacker and target.</p>

<p><img width="653" height="347" alt="image" src="https://github.com/user-attachments/assets/d68be0d4-aed5-47cf-aa22-557ef0b4eaed" />
</p>

<br>
<h3>Phase 2 — Network Reconnaissance</h3>
<p>After confirming connectivity, Nmap was used to scan the Ubuntu Server at <b>10.0.2.12</b>. The purpose of the scan was to identify exposed services and determine whether the SSH service was accessible.</p>

<p>The scan confirmed that <b>TCP port 22</b>, commonly used by SSH, was open on the target system. This established that the SSH authentication service was accessible from the simulated attacker's position within the lab network.</p>

<p><b>Finding:</b> TCP/22 was open, identifying SSH as an accessible attack surface on the Ubuntu Server.</p>

<p><img width="657" height="465" alt="image" src="https://github.com/user-attachments/assets/0439d5ec-d81c-4d53-aa5f-b607e38ce382" />
</p>

<br>
<h3>Phase 3 — SSH Brute-Force Attack Simulation</h3>
<p>With SSH confirmed as an exposed service, multiple unsuccessful authentication attempts were generated against the target account using SSH. The attack simulation intentionally used incorrect credentials to reproduce the characteristics of an SSH password-guessing or brute-force attack.</p>

<p>The repeated authentication failures generated the security telemetry necessary to evaluate whether the Wazuh monitoring environment could detect, correlate, and respond to authentication-based attack activity.</p>

<p>The activity was not intended to compromise the Ubuntu Server. Instead, the objective was to generate a recognizable pattern of repeated authentication failures and validate the effectiveness of the configured defensive controls.</p>

<p><b>Finding:</b> Multiple failed SSH authentication attempts were successfully generated, creating the behavioral pattern associated with SSH brute-force/password-guessing activity.</p>

<p><img width="652" height="340" alt="image" src="https://github.com/user-attachments/assets/b03aec97-01ea-4d14-93fe-edc131b61cda" />
</p>

<br>
<h3>Phase 4 — SIEM Alert Detection</h3>
<p>From the perspective of the SOC analyst, the investigation moved to the Wazuh dashboard to determine whether the simulated attack had been detected.</p>

<p>Within the Wazuh interface, the analyst navigated to Explore → Discover and configured the investigation view to focus on relevant security telemetry. The investigation included fields such as:</p>

<ul>
    <li>wazuh-alerts-*</li>
    <li>rule.id</li>
    <li>rule.description</li>
    <li>data.srcip</li>
    <li>agent.name</li>
    <li>data.parameters.alert.rule.description</li>
</ul>

<p>The <b>agent.name</b> filter was restricted to <b>wazuh-server</b> to focus the investigation on the relevant monitored Ubuntu Server.</p>

<p>The resulting events showed that Wazuh detected multiple failed SSH authentication attempts and generated an alert based on the configured detection logic. The activity matched the behavior defined by the custom detection rule, which was designed to identify repeated SSH authentication failures associated with brute-force/password-guessing behavior.</p>

<p>The alert was generated by <b>custom Wazuh Rule ID 100101</b>.</p>

<p><b>Rule 100101</b> detected a repeated pattern of failed SSH authentication attempts against the monitored Ubuntu Server. Rather than treating each failed login as an isolated event, the rule was used to identify a pattern of repeated authentication failures indicative of potential SSH brute-force or password-guessing activity.</p>

<p>The configured detection threshold was <b>three or more matching failed SSH authentication attempts within the rule's configured correlation conditions</b>. This threshold enabled Wazuh to distinguish repeated authentication failures from a single or occasional unsuccessful login.</p>

<p>The corresponding rule ID and rule description provided additional context for the analyst and helped establish why the event had been classified as suspicious.</p>

<p><b>Finding:</b> Wazuh successfully detected the repeated SSH authentication failures using custom <b>Rule ID 100101</b>, demonstrating that the SIEM was capable of identifying the simulated brute-force behavior based on a defined detection threshold.</p>

<p><img width="692" height="295" alt="image" src="https://github.com/user-attachments/assets/00f72214-9882-4f16-aadb-812b652054a5" />
</p>

<br>
<h3>Phase 5 — Alert Correlation and Active Response</h3>
<p>Further examination of the Wazuh events showed that the authentication failures occurred repeatedly within the observed timeframe. The detection was associated with <b>Rule ID 100101</b>, confirming that the activity matched the configured SSH brute-force detection logic.</p>

<p>The Wazuh environment was also configured to initiate an <b>Active Response</b> when Rule 100101 was triggered. For this investigation, the Active Response was not disabled; instead, its configuration and execution were examined as part of the response validation.</p>

<p>The configured Active Response used the <b>firewall-drop</b> command with the execution location set to <b>local</b> and was associated with <b>Rule ID 100101</b>. This configuration instructs the Wazuh agent on the monitored endpoint to execute the firewall-based response locally when the associated detection rule is triggered.</p>

<p>When Rule 100101 was triggered, Wazuh invoked the configured firewall-drop Active Response locally. The purpose of this response was to initiate a firewall-based blocking action against the source IP associated with the detected SSH brute-force activity.</p>

<p>The Active Response event was recorded at approximately <b>12:31 PM</b>, providing a timestamp that could be correlated with the corresponding security alert and authentication events.</p>

<p>The Wazuh telemetry confirmed that the Active Response was <b>triggered against the identified source IP, 10.0.2.3</b>. However, an Active Response event confirms that Wazuh invoked the response command; it does not, by itself, provide definitive proof that the firewall successfully enforced the block. To conclusively verify the block, the analyst would need to validate the host firewall state or review the corresponding firewall logs.</p>

<p>This distinction is important because it separates <b>response execution</b> from <b>response effectiveness</b>.</p>

<p>Finding: Wazuh successfully correlated the repeated authentication failures with <b>Rule ID 100101</b> and invoked the configured local <b>firewall-drop Active Response</b> , demonstrating an automated detection-and-response workflow.</p>

<p><img width="675" height="434" alt="image" src="https://github.com/user-attachments/assets/1e068d24-99e9-4281-bddb-69b2d3f334ea" />
</p>

<p><img width="975" height="207" alt="image" src="https://github.com/user-attachments/assets/d86b3b50-0ede-46f2-b955-73b9b21937db" />
</p>

<p><img width="975" height="360" alt="image" src="https://github.com/user-attachments/assets/fd807b06-bfe7-4243-818c-b2b64a8a40a9" />
</p>

<br>
<h3>Phase 6 — Source IP Identification and Investigation</h3>
<p>The analyst expanded the relevant Wazuh event details and reviewed the underlying telemetry to determine the origin of the suspicious authentication attempts.</p>

<p>The investigation identified <b>10.0.2.3</b> as the source IP associated with the repeated failed SSH authentication attempts. The frequency and repetitive nature of the authentication failures, combined with the Wazuh detection, provided strong evidence that the activity originated from the simulated attacker system.</p>

<p>This step was particularly important from a SOC perspective because identifying the source IP allows an analyst to establish the attack path, correlate activity across security telemetry, and determine appropriate containment or response actions.</p>

<p>The security events used for the detection originated from the <b>Ubuntu Server</b>, which had the <b>Wazuh agent installed and running</b>. The agent monitored relevant authentication activity on the endpoint and forwarded the collected security telemetry to the Wazuh server for analysis.</p>

<p>The SSH authentication-related events provided the underlying evidence of the repeated failed login attempts. Wazuh then evaluated those events against the configured detection logic associated with <b>Rule ID 100101</b> and generated the corresponding security alert.</p>
<p>The alert was generated from <b>SSH authentication-related events collected by the Wazuh agent on the Ubuntu Server</b>. The endpoint agent provided Wazuh with visibility into the authentication failures, allowing the SIEM to analyze the events and apply the configured detection rule.</p>

<p>This demonstrates the role of the Wazuh agent in the detection architecture: security telemetry is collected directly from the monitored endpoint and forwarded to the Wazuh platform, where detection logic can be applied and alerts generated.</p>

<p><b>Finding:</b> The source of the observed SSH authentication attack was identified as <b>10.0.2.3</b>, while the Wazuh agent on the Ubuntu Server supplied the authentication telemetry used to detect the repeated failed login activity.</p>

<p><img width="975" height="331" alt="image" src="https://github.com/user-attachments/assets/058f4d6a-3153-445a-b970-a4757368d940" />
</p>

<p><img width="975" height="478" alt="image" src="https://github.com/user-attachments/assets/b3bb8dd6-5f14-4601-b0c7-c59346a5ca65" />
</p>

<br>
<h3>Phase 7 — Threat Hunting and Validation</h3>
<p>Following the initial alert investigation, the analysis was extended to the Wazuh <b>Threat Hunting</b> functionality. The purpose was to independently examine the available security telemetry and determine whether additional evidence supported the initial alert.</p>

<p>The Threat Hunting results were consistent with the Discover investigation, showing the same pattern of repeated SSH authentication failures and confirming the previously identified source IP of <b>10.0.2.3</b>.</p>

<p>The consistency between the initial alert, event-level investigation, and Threat Hunting results increased confidence in the assessment and demonstrated that the observed activity represented a repeated attack pattern rather than an isolated authentication failure.</p>

<p>The analyst also reviewed the Wazuh events associated with the Active Response to determine whether the automated response mechanism had been invoked.</p>

<p>The Wazuh event data confirmed that the configured <b>Active Response was invoked</b> in association with <b>Rule ID 100101</b> at approximately <b>12:31 PM</b>. This verified that Wazuh executed the configured response action.</p>

<p>However, the investigation distinguishes between <b>verification that the Active Response was triggered and verification that the firewall successfully blocked the attacker IP</b>. The former was confirmed through Wazuh telemetry, while definitive verification of firewall-level blocking would require additional evidence from the Ubuntu Server, such as firewall status information or corresponding firewall logs.</p>

<p>This distinction provides a more accurate assessment of the response outcome and avoids treating the execution of a response command as automatic proof of successful containment.</p>

<p><b>Finding:</b> Threat Hunting corroborated the initial Wazuh alert investigation, while the Active Response event confirmed that the configured local firewall-drop response associated with Rule 100101 was invoked against the identified source.</p>

<p><img width="771" height="345" alt="image" src="https://github.com/user-attachments/assets/642634bf-d6c7-4982-a414-b176c14e4df5" />
</p>

<p><img width="975" height="165" alt="image" src="https://github.com/user-attachments/assets/aaabb547-196a-48bc-8b78-334db2deacb7" />
</p>

<br>
<h3>Phase 8 — Final Assessment</h3>
<p>The combined evidence from network reconnaissance, SSH authentication logs, Wazuh alerts, custom detection rules, source IP analysis, Active Response, and Threat Hunting established a clear attack narrative.</p>
<p>The simulated attacker at<b> 10.0.2.3</b> targeted the Ubuntu Server at <b>10.0.2.12</b> through the exposed SSH service on TCP/22. Multiple unsuccessful authentication attempts were generated and subsequently detected by Wazuh through <b>custom Rule ID 100101</b>. The detection logic identified the repeated authentication failures as behavior consistent with SSH brute-force/password-guessing activity.</p>
<p>The corresponding detection alert and Active Response event were recorded at approximately <b>12:31 PM</b>. Once Rule 100101 was triggered, Wazuh invoked the configured local <b>firewall-drop</b> Active Response to initiate a firewall-based blocking action against the identified source IP.</p>
<p>The investigation verified through Wazuh telemetry that the Active Response was invoked. However, definitive confirmation that the firewall successfully enforced the block would require additional host-level firewall evidence. This distinction ensures that the final assessment remains based on directly observed evidence.</p>
<p>The investigation also demonstrated the value of endpoint-based security telemetry. Because the Ubuntu Server was monitored by a Wazuh agent, SSH authentication events could be collected, forwarded to the Wazuh platform, evaluated against custom detection logic, and correlated with the source IP and automated response.</p>
<p><b>Final Finding:</b> The investigation confirmed that the observed activity was consistent with an <b>SSH brute-force/password-guessing attack</b> originating from <b>10.0.2.3</b> against the Ubuntu Server at <b>10.0.2.12</b>. Wazuh successfully detected the repeated authentication failures through <b>Rule ID 100101</b>, supported analyst investigation and threat hunting, and invoked the configured local <b>firewall-drop Active Response</b> at approximately <b>12:31 PM</b>. The exercise validated an end-to-end SOC workflow encompassing <b>security monitoring, detection, alert triage, investigation, threat hunting, source identification, and automated response</b> within a controlled laboratory environment.</p>


<br>
<h2>MITRE ATT&CK</h2>
<p>The observed activity can be mapped to the following <b>MITRE ATT&CK</b> techniques:</p>
<ul>
    <li><b>T1046 — Network Service Scanning:</b> Nmap scanning to identify exposed SSH services.</li>
    <li><b>T1110 — Brute Force:</b> Repeated failed authentication attempts against SSH.</li>
    <li><b>T1110.001 — Password Guessing:</b> Incorrect password attempts against the SSH account.</li>
    <li><b>T1021.004 — Remote Services (SSH): </b>SSH was used as the remote access protocol targeted during the simulation.</li>
    <li><b>T1059 — Command and Scripting Interpreter: </b>Command-line utilities were used during the attack simulation.</li>
</ul>


<br>
<h2>Indicators of Compromise (IoC)</h2>
<ul>
    <li><b>Source IP: </b>10.0.2.3</li>
    <li><b>Target IP: </b>10.0.2.12</li>
    <li><b>Target Service: </b>SSH</li>
    <li><b>Target Port: </b>TCP/22</li>
    <li><b>Protocol: </b>SSH</li>
    <li><b>Activity: </b>Repeated failed authentication attempts</li>
    <li><b>Detection Platform: </b>Wazuh</li>
    <li><b>Detection Source: </b>Wazuh security alerts</li>
    <li><b>Response:</b> Wazuh Active Response</li>
    <li><b>Relevant Evidence: </b>SSH authentication failure events</li>
    <li><b>Attack Type: </b>SSH brute-force / password-guessing activity</li>
</ul>


<br>
<h2>Lesson Learned</h2>
<p>This project demonstrated that effective cybersecurity defense requires more than identifying whether a port is open or whether an attack can be successfully executed. The most valuable capability is being able to connect attacker behavior with defensive telemetry and translate raw events into actionable security findings. </p>
<p>The exercise provided practical experience in following a SOC investigation lifecycle: validating the initial activity, analyzing security events, identifying the source of suspicious behavior, correlating multiple pieces of evidence, validating findings through threat hunting, and observing an automated response. It also reinforced the importance of properly configured detection rules because repeated authentication failures can appear as isolated events unless they are appropriately correlated and escalated. Most importantly, the project demonstrated how offensive security techniques can be used in a controlled environment to validate and improve defensive detection capabilities.</p>


<br>
<h2>Recommendations</h2>
<p>Organizations should implement layered defenses to reduce the risk associated with SSH brute-force attacks. SSH access should be restricted to trusted networks or management hosts wherever possible, while unnecessary internet-facing SSH exposure should be eliminated. Strong authentication mechanisms, particularly <b>SSH key-based authentication and multi-factor authentication where supported</b>, should be prioritized over password-only access. Account lockout or rate-limiting controls can further reduce the effectiveness of repeated password-guessing attempts. </p>
<p>From a monitoring perspective, organizations should maintain centralized authentication logging and establish SIEM detection rules capable of identifying repeated failures, abnormal authentication patterns, and suspicious source addresses. Wazuh Active Response or equivalent automated controls can be used to temporarily block confirmed malicious sources when appropriate. Finally, detection rules should be regularly tested through controlled attack simulations to ensure that alerts are generated reliably and that automated response mechanisms operate as intended.</p>


<br>
<h2>References & Acknowledgement</h2>
<p>This project was conducted in a controlled cybersecurity laboratory environment for educational and defensive security purposes. The investigation methodology was based on practical SOC monitoring and incident-response concepts, with <b>Wazuh</b> serving as the primary security monitoring and detection platform, <b>Nmap</b> being used for network reconnaissance, <b>SSH</b> for authentication testing, and <b>MITRE ATT&CK</b> providing the framework for adversary behavior classification. The project also acknowledges the value of security telemetry, custom detection rules, threat hunting, and automated response in developing a practical defensive security capability. All attack activity described in this case study was performed against intentionally configured laboratory systems rather than unauthorized production infrastructure.</p>
