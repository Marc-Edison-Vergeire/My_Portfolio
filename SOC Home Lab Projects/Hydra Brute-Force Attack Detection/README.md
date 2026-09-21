<h1>SOC Incident Response: SSH Brute-Force Attack Detection, Investigation & Automated Containment with Wazuh SIEM</h1>

<br>
<p><b>Role:</b> SOC Analyst / Blue Team Analyst</p>
<p><b>Environment:</b> Ubuntu Server, Kali Linux, Wazuh SIEM</p>
<p><b>Attack: </b>SSH Credential Brute Force / Password Guessing (Tool: Hydra)</p>
<p><b>Target:</b> Ubuntu Server — 10[.]0[.]2[.]6</p>
<p><b>Attacker: </b>Internal source host — 10[.]0[.]2[.]15</p>
<p><b>Target Service: </b>OpenSSH — TCP/22</p>
<p><b>Detection:</b>Wazuh SIEM — Rules 5503, 5551, 100101, and 651</p>
<p><b>Response</b> Wazuh Active Response — firewall-drop</p>
<p><b>Investigation:</b> Authentication-event analysis, alert correlation, source/destination validation, threat hunting, and containment verification</p>
<p><b>Framework:</b> <b>MITRE ATT&CK</b> — T1110: Brute Force / Credential Access</p>

<br>
<h2>Executive Summary</h2>
<p>A simulated SSH brute-force attack was conducted against an Ubuntu Server at <b>10[.]0[.]2[.]6</b> from <b>10[.]0[.]2[.]15</b>, targeting the SSH service on TCP/22. Reconnaissance identified the exposed SSH service, after which Hydra was used to perform credential-guessing activity and identify a weak password. The resulting authentication failures generated multiple Wazuh alerts, which were investigated and correlated across rules <b>5503</b>, <b>5551</b>, and <b>100101</b> and mapped to <b>MITRE ATT&CK T1110 — Brute Force</b>. Wazuh Active Response, configured against rule <b>651</b>, automatically executed a <b>firewall-drop</b> action to block the source IP and terminate further connection attempts. The incident demonstrates an end-to-end SOC workflow encompassing detection, triage, investigation, correlation, automated containment, threat hunting, and security-control improvement.</p>

<br>
<h2>Objective</h2>
<p>The objective of this case study was to demonstrate the ability to detect, investigate, correlate, and contain an SSH brute-force attack using a SIEM-driven SOC workflow. The exercise specifically evaluates authentication monitoring, network reconnaissance analysis, credential-attack identification, MITRE ATT&CK mapping, custom detection logic, automated response, and post-containment threat hunting. It also demonstrates how proactive SIEM and response configuration can reduce attacker dwell time and limit repeated unauthorized authentication attempts.</p>

<br>
<h2>Scenario</h2>
<p>An attacker with knowledge of the Ubuntu Server's IP address and username performed reconnaissance against <b>10[.]0[.]2[.]6</b> and identified SSH as an exposed service. The attacker subsequently used Hydra to conduct password guessing against the SSH account and identified the weak password <b>"kali."</b> The attacker then attempted initial access through SSH, generating authentication failures visible to Wazuh. A SOC Analyst investigated the resulting alerts, correlated multiple authentication-failure events, assessed the activity as consistent with <b>MITRE ATT&CK T1110</b>, and relied on a preconfigured Wazuh Active Response to automatically block the attacker's source IP. The Analyst subsequently performed threat hunting to identify additional related activity.</p>

<br>
<h2>Skills Learned</h2>
<ul>
    <li>SOC alert triage</li>
    <li>SIEM investigation</li>
    <li>Linux authentication analysis</li>
    <li>SSH security monitoring</li>
    <li>Network reconnaissance analysis</li>
    <li>Brute-force detection</li>
    <li>Alert correlation</li>
    <li>Detection-rule analysis</li>
    <li>MITRE ATT&CK mapping</li>
    <li>Incident containment</li>
    <li>Automated response</li>
    <li>Threat hunting</li>
    <li>IOC identification</li>
    <li>Incident documentation</li>
</ul>

<br>
<h2>Tools Utilized</h2>
<ul>
    <li><b>Wazuh </b>— SIEM, detection & response</li>
    <li><b>Hydra </b>— Credential-attack simulation</li>
    <li><b>Nmap </b>— Network/service discovery</li>
    <li><b>Ping </b>— Connectivity validation</li>
</ul>

<br>
<h2>Artifacts</h2>
<ul>
    <li>Ping/connectivity results</li>
    <li>Nmap scan results</li>
    <li>Hydra attack output</li>
    <li><b>Wazuh rule IDs (alerts):</b> 5503, 5551, 100101, 651</li>
    <li><b>Source IP:</b> 10[.]0[.]2[.]15</li>
    <li><b>Target IP:</b> 10[.]0[.]2[.]6</li>
    <li><b>Target port:</b> TCP/22</li>
    <li>Wazuh Active Response</li>
    <li>Firewall-drop response evidence</li>
    <li>Threat Hunting events</li>
    <li>MITRE ATT&CK mapping</li>
</ul>

<br>
<h2>Findings</h2>
<h3>Phase 1 — Target Identification and Reconnaissance (Attacker's Perspective)</h3>
<p>The attacker begins with information already available about the target, specifically the target IP address <b>(10[.]0[.]2[.]6)</b> and username (ubuntu-server).</p>
<p>The attacker first verifies whether the target is reachable by sending a ping request:</p>

    ping 10.0.2.6

<p><img width="620" height="195" alt="image" src="https://github.com/user-attachments/assets/180ea202-d1d5-408a-9527-0970acd41cdf" />
</p>

<p>After receiving a response, the attacker performs an Nmap scan to identify possible open ports and services:</p>

    nmap -sS 10.0.2.6

<p><img width="675" height="300" alt="image" src="https://github.com/user-attachments/assets/9b372405-3d41-4858-913a-231cf65eb165" />
</p>

<p>The scan identifies port 22/TCP as open, with SSH running as the associated service.</p>
<p><b>Objective:</b> Determine whether the target is reachable and identify accessible services that could potentially be targeted.</p>

<br>
<h3>Phase 2 — Credential Access / Brute-Force Atta</h3>
<p>After discovering that SSH is available on port 22, the attacker attempts to obtain the target's credentials using Hydra. The attacker executes:</p>

    hydra -l Ubuntu-server -P /usr/share/wordlists/rockme.txt

<p><img width="975" height="145" alt="image" src="https://github.com/user-attachments/assets/766f68d0-86ea-429d-ac1a-2ca2426b375c" />
</p>

<p>The attacker performs a brute-force attack against the account and successfully identifies the password as "kali", which represents a weak password.</p>
<p><b>Objective:</b> Obtain valid credentials that can potentially be used to access the target system.</p>

<br>
<h3>Phase 3 — Attempted Initial Access</h3>
<p>With the SSH service exposed and credentials obtained, the attacker attempts to use the discovered credentials to access the Ubuntu Server.</p>
<p>The relevant information identified during this phase includes:</p>

    Target IP: 10.0.2.6

    Service: SSH

    Port: 22/TCP

    Username: ubuntu-server

    Password: kali

<p>The authentication attempts generate multiple failed login events that are subsequently detected by the Wazuh SIEM.</p>
<p><b>Objective:</b> Gain unauthorized access to the Ubuntu Server using the obtained credentials</p>

<br>
<h3>Phase 1 — Security Monitoring and Detection (SOC Analyst Perspective)</h3>
<p>From the SOC Analyst's perspective, the Analyst begins their shift and opens the Wazuh SIEM to investigate the environment</p>
<p>At approximately 11:26 PM (23:26) on September 14, 2026, the Analyst notices multiple alerts indicating failed login attempts.</p>

<p><img width="865" height="494" alt="image" src="https://github.com/user-attachments/assets/49485bb0-7afa-4625-b124-e605baf3469c" />
</p>

<p><img width="709" height="284" alt="image" src="https://github.com/user-attachments/assets/5ebc70d2-bc02-4d17-88b6-8c17cd319598" />
</p>

<p>The Analyst suspects that the activity could be related to:</p>

    A Hydra brute-force attack, or

    A password-spraying attack.

<p>Because there is considerable noise in the Event dashboard, the Analyst filters the events using:</p>

    rule.id

    rule.description

<p>The Analyst focuses on the following rule IDs:</p>

    5503

    5551

    100101

    651

<p><img width="975" height="590" alt="image" src="https://github.com/user-attachments/assets/0f731a40-8ac7-4142-a9c7-72b562d06230" />
</p>

<p>The investigation begins with rule ID 5503.</p>
<p><b>Objective:</b> Detect suspicious authentication activity and identify potentially malicious login attempts.</p>
<p>The Analyst investigates rule ID 5503 and consults online resources to understand what the rule represents.</p>
<p>Rule ID 5503 is identified as a Wazuh rule that monitors Unix/Linux logs and generates alerts for failed user login attempts.</p>

<p><img width="671" height="227" alt="image" src="https://github.com/user-attachments/assets/123150cf-5650-4e9b-839d-ec15ed4db546" />
</p>

<p>The Analyst then examines the detailed event information and identifies:</p>

    Source IP: 10.0.2.15

    Target IP: 10.0.2.6

    Network: 10.0.2.0/24

    Target service: SSH

    Target port: 22

<p>Because 10.0.2.15 is within the organization's internal network range, the Analyst considers the possibility that the activity could be associated with an insider threat or an external threat actor who had already obtained access to the internal network.</p>

<p><img width="974" height="241" alt="image" src="https://github.com/user-attachments/assets/b50454a4-57df-4d3d-8823-14169a40f7a3" />
</p>

<p><img width="821" height="534" alt="image" src="https://github.com/user-attachments/assets/b7144ec0-c021-4924-af0e-bd8fc71d0725" />
</p>

<p><b>Objective:</b> Determine the source, destination, service, and context of the suspicious authentication activity.</p>

<br>
<h3>Phase 2 — Alert Correlation</h3>
<p>The SOC Analyst continues the investigation by examining additional Wazuh rules.</p>
<h4>Rule ID 5551</h4>
<p>The Analyst identifies rule ID 5551 as another Wazuh rule associated with multiple failed PAM authentication attempts from the same source IP within a short period.</p>

<p><img width="681" height="276" alt="image" src="https://github.com/user-attachments/assets/9ee5e240-93fa-41d6-80b9-f095d57ceb85" />
</p>

<p><img width="975" height="140" alt="image" src="https://github.com/user-attachments/assets/2805bd83-b8bb-46f6-97ce-9cb9c337a745" />
</p>

<p><img width="975" height="384" alt="image" src="https://github.com/user-attachments/assets/bcb78378-c2c0-4e3a-b04c-6d6973442bdb" />
</p>

<p><img width="696" height="284" alt="image" src="https://github.com/user-attachments/assets/beb5292f-133c-4a43-bd1d-5f262098ec61" />
</p>

<br>
<h4>Rule ID 100101</h4>
<p>The Analyst also examines the custom rule 100101, which detects multiple authentication failures originating from the same source IP address.</p>
<p>The Analyst correlates the events generated by rules 5503, 5551, and 100101 and identifies several common characteristics:</p>

    MITRE ATT&CK ID: T1110

    MITRE ATT&CK Tactic: Credential Access

    MITRE ATT&CK Technique: Brute Force

    Rule Group: Authentication failures

<p><img width="975" height="198" alt="image" src="https://github.com/user-attachments/assets/e09a73b1-0927-4989-bd19-7c48a18f55fa" />
</p>

<p><img width="921" height="600" alt="image" src="https://github.com/user-attachments/assets/0a0d0c48-69eb-482e-bbbb-9d245990c3cd" />
</p>

<p>This correlation strengthens the Analyst's assessment that the activity is consistent with a brute-force attack.</p>
<p><b>Objective:</b> Correlate multiple alerts and determine whether they represent the same security incident</p>

<br>
<h3>Phase 3 — Automated Response and Containment</h3>
<p>Before the incident occurred, the SOC Analyst had configured Wazuh's Active Response functionality in the ossec.conf configuration file.</p>
<p>The Active Response configuration was correlated with rule ID 651 to respond to multiple failed login attempts.</p>

<p><img width="665" height="162" alt="image" src="https://github.com/user-attachments/assets/406262d9-dbc3-469a-a4a3-1305baad4ba7" />
</p>

<p><img width="921" height="121" alt="image" src="https://github.com/user-attachments/assets/cff422f5-c561-4e01-b1fd-9d075947c7e6" />
</p>

<p><img width="975" height="425" alt="image" src="https://github.com/user-attachments/assets/c3a1a93f-07db-4149-8ce0-52a1125dfd13" />
</p>

<p><img width="975" height="335" alt="image" src="https://github.com/user-attachments/assets/c38ff7b3-e186-4c7f-8403-4df46e619587" />
</p>

<p><img width="975" height="147" alt="image" src="https://github.com/user-attachments/assets/7b810e50-ad29-4c0c-b548-07ba3600baba" />
</p>

<p><img width="975" height="258" alt="image" src="https://github.com/user-attachments/assets/de2fc7ba-a970-4f22-acb6-c18338321ebb" />
</p>

<p>Once the defined threshold was reached, Wazuh triggered the Active Response mechanism and invoked the firewall-drop mitigation.</p>
<p>As a result:</p>

    The suspicious source IP address was identified.

    The Active Response mechanism was triggered.

    The firewall-drop action was executed.

    The attacker's source IP address was blocked.

    The connection was terminated.

    Further connection attempts from that IP were prevented.

<p><b>Objective:</b> Automatically contain the threat and prevent continued unauthorized authentication attempts.</p>

<br>
<h3>Phase 4 — Threat Hunting and Further Investigation</h3>
<p>After the automated response, the SOC Analyst continues investigating rather than immediately closing the incident.</p>
<p>The Analyst navigates to the:</p>

    Threat Hunting dashboard

    Events section

<p><img width="975" height="279" alt="image" src="https://github.com/user-attachments/assets/c2a5ca6a-0fb7-4bb4-8eef-761368c2cf57" />
</p>

<p>#<img width="975" height="389" alt="image" src="https://github.com/user-attachments/assets/f0042bee-ef1c-4b1f-a989-2489901bb9a4" />
</p>

<p><img width="975" height="392" alt="image" src="https://github.com/user-attachments/assets/25e28b54-ab42-44ac-8454-76c0065ed707" />
</p>

<p>These provide additional information that can be used to investigate the incident and determine whether there was any other suspicious or related activity.</p>

<p><b>Objective:</b> Identify additional indicators, events, or evidence associated with the incident.</p>

<br>
<h3>Phase 5 — Prevention and Continuous Improvement</h3>
<p>The final phase focuses on the proactive security measures implemented by the SOC Analyst.</p>
<p>The Analyst had already anticipated the possibility of attacks such as brute-force authentication attempts and configured Wazuh's Active Response mechanism before the incident occurred.</p>
<p>Because of this preparation, Wazuh was able to automatically respond to the suspicious activity and block the adversary's IP address.</p>
<p>This demonstrates the importance of:</p>

    Proactive SIEM configuration

    Custom detection rules

    Alert correlation

    Automated incident response

    Firewall-based blocking

    Threat hunting

    Continuous security monitoring

<p>These preventive and responsive measures can help minimize the impact of similar attacks in the future and reduce the risk of significant damage to the organization's systems and reputation.</p>
<p><b>Objective:</b> Strengthen the organization's security posture and improve its ability to detect and respond to future attacks.</p>

<br>
<h3>MITRE ATT&CK</h3>
<ul>
    <li><b>Tactic:</b> Credential Access</li>
    <li><b>Technique:</b> T1110 — Brute Force</li>
    <li><b>Sub-technique:</b> Password Guessing — applicable to the credential-guessing behavior</li>
    <li><b>Observed behavior:</b> Repeated SSH authentication attempts</li>
    <li><b>Detection:</b> Wazuh authentication-failure rules</li>
    <li><b>Response:</b> Automated source-IP blocking</li>
</ul>

<br>
<h3>Indicators of Compromise (IoC)</h3>
<ul>
    <li><b>Source IP: </b>10[.]0[.]2[.]15</li>
    <li><b>Target IP:</b>10[.]0[.]2[.]6</li>
    <li><b>Target Port:</b>TCP/22</li>
    <li><b>Service:</b> SSH</li>
    <li><b>Username:</b> ubuntu-server</li>
    <li><b>Compromised/identified password: </b>kali</li>
    <li><b>Detection Rules: </b>5503, 5551, 100101, 651</li>
    <li><b>Network:</b></li>
</ul>
<p><b>Security note: </b>The password is included here because this is a controlled lab case study. It should be redacted from a production incident report.</p>

<br>
<h3>Lesson Learned</h3>
<p>The incident demonstrates that an exposed SSH service combined with weak authentication controls can provide an effective attack path for credential attacks. However, the exercise also demonstrates the defensive value of centralized authentication logging, SIEM correlation, custom detection rules, and automated containment. The strongest takeaway is that effective SOC operations extend beyond detecting a single failed login: analysts must establish context, correlate events, validate the source and target, map behavior to an adversary framework, contain the threat, and perform post-containment hunting. The case also highlights the importance of distinguishing <b>credential discovery, attempted access, and confirmed successful compromise</b> when documenting incident evidence.</p>

<br>
<h3>Recommendations</h3>
<p>Implement strong password policies and eliminate weak or default credentials; enforce SSH key-based authentication and disable password authentication where operationally feasible; restrict SSH exposure through network segmentation, VPN, allowlisting, or privileged-access controls; implement MFA for administrative access where supported; tune Wazuh authentication rules to reduce false positives while detecting high-volume and distributed attacks; maintain tested Active Response controls; monitor for successful authentication following brute-force activity; investigate internal source addresses for possible compromised hosts; and continuously threat-hunt around authentication anomalies. For production environments, credentials observed during testing should never appear unredacted in reports, dashboards, screenshots, or repositories.</p>

<br>
<h3>References & Acknowledgement</h3>
<p>This case study is based on a controlled cybersecurity lab scenario using Wazuh for security monitoring and automated response, Linux authentication and SSH telemetry, Nmap for service discovery, and Hydra for authorized credential-attack simulation. MITRE ATT&CK was used as the adversary-behavior framework for mapping the observed credential-access activity. Wazuh documentation and rule references should be used to validate detection-rule behavior and Active Response configuration when reproducing the exercise. All attack activity should be conducted only against systems for which explicit authorization has been provided.</p>
