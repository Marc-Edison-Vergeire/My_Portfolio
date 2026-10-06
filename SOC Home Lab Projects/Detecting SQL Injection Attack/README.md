<h1>SQL Injection Detection, Investigation & Automated Response Using Wazuh SIEM</h1>

<p><b>Role:</b> SOC Analyst / Blue Team Security Analyst</p>
<p><b>Environment:</b> Ubuntu Server/Apache2, Wazuh Manager/Agent/Dashboard, Kali Linux, Apache access logs, and firewall-based Active Response.</p>
<p><b>Attack:</b> SQL Injection (SQLi) Emulation (A crafted HTTP GET request containing a SQL query was sent to a web application endpoint to simulate an SQL injection attempt.)</p>
<p><b>Target:</b> Ubuntu Web Server — 10.0.2.6</p>
<p><b>Attacker:</b> Kali Linux — 10.0.2.15</p>
<p><b>Target Service:</b> Apache2 HTTP Web Server — TCP/80</p>
<p><b>Detection:</b> Wazuh Threat Detection / Apache Access Log Monitoring</p>
<p><b>Response: </b>Automated IP blocking using Wazuh Active Response and firewall-drop</p>
<p><b>Investigation:</b> Reviewed Wazuh alerts for the source IP, HTTP request/payload, detection rule, timestamp, and automated firewall response.</p>
<p><b>Framework: </b>MITRE ATT&CK</p>

<br>
<h2>Executive Summary</h2>
<p>A controlled SQL injection attack simulation was conducted against an Apache2 web server hosted on Ubuntu to validate the effectiveness of Wazuh-based detection, investigation, and automated response capabilities. The simulated attacker, originating from <b>10.0.2.15</b>, submitted a crafted HTTP GET request containing a SQL query against the target server at <b>10.0.2.6</b>. Apache access logs were monitored by the Wazuh agent, resulting in a security alert that identified the activity as SQL injection-related.</p>
<p> The investigation confirmed the source IP, HTTP request, payload, and detection rule. An Active Response mechanism was subsequently configured to automatically invoke <b>firewall-drop</b> and block the offending IP for 10 minutes. A second test validated that the detection and containment workflow operated as intended. Because the requested application endpoint returned <b>404 Not Found</b>, there was no evidence of successful application or database exploitation; the exercise primarily <b>validated detection, triage, and automated containment</b>.</p>

<br>
<h2>Objective</h2>
<p>The objective of this exercise was to demonstrate an end-to-end SOC detection and response workflow for an SQL injection attempt, from web-server log collection and security-event detection through alert investigation and automated containment. The project specifically validated Wazuh's ability to monitor Apache access logs, identify suspicious SQL injection activity, provide actionable investigation data, and automatically block the suspected source IP through Active Response. The exercise also emphasized distinguishing an attack attempt from a confirmed compromise, a critical capability in professional security operations.</p>

<br>
<h2>Scenario</h2>
<p>A simulated external attacker using Kali Linux (<b>10.0.2.15</b>) targeted an Ubuntu Apache2 web server (<b>10.0.2.6</b>) with a crafted HTTP GET request containing <b>SELECT * FROM users;</b> as a URL parameter. The request represented a basic SQL injection attempt intended to test whether user-controlled input could be interpreted as a database query. Apache received the request and logged the activity, while the Wazuh agent collected the Apache access logs for centralized security monitoring. Wazuh subsequently generated an SQL injection-related alert. During investigation, the request, source IP, payload, timestamp, and detection rule were reviewed. The response workflow was then enhanced with an Active Response configuration using <b>firewall-drop</b> to automatically block the source IP for 600 seconds. A repeat request was used to validate the detection and containment workflow.</p>

<br>
<h2>Skills Learned</h2>
<ul>
    <li>SOC alert triage</li>
    <li>SQL injection detection</li>
    <li>Web-server log analysis</li>
    <li>Wazuh SIEM/EDR monitoring</li>
    <li>Detection-rule analysis</li>
    <li>MITRE ATT&CK mapping</li>
    <li>Incident investigation</li>
    <li>IOC identification</li>
    <li>Active Response configuration</li>
    <li>Firewall-based containment</li>
    <li>Attack validation</li>
    <li>Incident documentation</li>
    <li>Detection-to-response workflow design</li>
</ul>

<br>
<h2>Tools Utilized</h2>
<ul>
    <li>Wazuh Dashboard/Manager</li>
    <li>Wazuh Agent</li>
    <li>Apache2 Server</li>
    <li>Ubuntu Server</li>
    <li>Kali Linux</li>
    <li>cURL command</li>
    <li>Linux CLI</li>
    <li>Firewall/firewall-drop</li>
    <li>MITRE ATT&CK</li>
</ul>

<br>
<h2>Artifacts</h2>
<ul>
    <li>Wazuh security alert</li>
    <li>Wazuh Rule ID <b>31103</b></li>
    <li>(Attacker) Source IP <b>10.0.2.15</b></li>
    <li>(Target) Destination IP <b>10.0.2.6</b></li>
    <li>SQL injection HTTP request</li>
    <li>Wazuh Active Response configuration</li>
    <li><b>firewall-drop</b> execution</li>
    <li>10-minute IP-blocking configuration</li>
    <li>Investigation timeline</li>
    <li>Detection/response evidence</li>
</ul>

<br>
<h2>Findings</h2>
<p>Before I started the simulation, I made sure that Apache2 was installed and configured the Wazuh agent to monitor the Apache logs. I also verified that the firewall was properly configured. I typed the following commands:</p>

    sudo apt update && sudo apt upgrade –y

<p><img width="670" height="90" alt="image" src="https://github.com/user-attachments/assets/03a6ac4b-e738-4f72-9d22-86a1f5a93314" />
</p>

    sudo apt install apache2

<p><img width="975" height="276" alt="image" src="https://github.com/user-attachments/assets/14d7b266-8f66-48f5-b78f-e12b230d89cd" />
</p>

<p>After that, I checked the status of Apache2 to verify that it was running and active by typing:</p> 

    sudo systemctl status apache2

<p><img width="975" height="347" alt="image" src="https://github.com/user-attachments/assets/f05b7fe7-44ec-4751-a407-3c249ad948e6" />
</p>

<p>To confirm that Apache2 was working properly, I opened a browser and entered the Ubuntu server's IP address:</p>

    http://10.0.2.6

<p><img width="975" height="302" alt="image" src="https://github.com/user-attachments/assets/32fb9a09-791a-492d-a46f-9f953cbd1120" />
</p>

<p>I then started configuring the Wazuh agent by navigating to <b>/var/ossec/etc/ossec.conf</b> and entering the following command:</p>

    sudo nano /var/ossec/etc/ossec.conf

<p><img width="675" height="94" alt="image" src="https://github.com/user-attachments/assets/fc9c357c-32d7-47cc-8ab9-1de206e06a97" />
</p>

<p>I inserted the following lines into the Wazuh agent configuration file. This configuration allows the Wazuh agent to monitor the Apache access logs:</p>

    <ossec_config>
      <localfile>
        <log_format>apache</log_format>
        <location>/var/log/apache2/access.log</location>
      </localfile>
    </ossec_config>

<p><img width="606" height="287" alt="image" src="https://github.com/user-attachments/assets/bd2853da-3b3f-400f-bc04-5a908302131f" />
</p>

<p>For the changes to take effect, I restarted the Wazuh agent by entering:</p>

    sudo systemctl restart wazuh-agent

<p><img width="602" height="87" alt="image" src="https://github.com/user-attachments/assets/55fef352-a6a3-4832-8d27-639311f2f0f2" />
</p>

<p>For the attack emulation using Kali Linux on <b>October 4, 2026</b>, at <b>1:00 AM</b>, I entered the following command:</p>

    curl –XGET http://(UBUNTU_IP)/users/?id=SELECT+*+FROM+users;

<p><img width="975" height="243" alt="image" src="https://github.com/user-attachments/assets/924145ad-ca6e-4b09-926a-0f2ad66e06c3" />
</p>

<p>The result showed <i>404 Not Found</i> because there was no active database on the Ubuntu server.</p>

<p><img width="946" height="295" alt="image" src="https://github.com/user-attachments/assets/61dd9699-f9d5-4767-bc94-48e0d8b5a953" />
</p>

<p>I then opened the Wazuh dashboard and selected the Wazuh agent.</p>

<p><img width="975" height="120" alt="image" src="https://github.com/user-attachments/assets/6f846372-7d2e-4ad5-a742-0e9290c8d17a" />
</p>
<p><img width="975" height="103" alt="image" src="https://github.com/user-attachments/assets/64f413e6-a4eb-4582-98a7-522a7275258d" />
</p>

<p>In the upper-left corner, I selected the <b>Threat Hunting</b> link.</p>

<p><img width="975" height="85" alt="image" src="https://github.com/user-attachments/assets/92b12250-5de2-4b38-bec7-45408119f286" />
</p>

<p>I selected the <b>Events</b> tab, where I observed the triggered alert from <b>October 4, 2026</b>, at <b>1:07 AM</b>, indicating that an SQL injection attempt had been detected.</p>

<p><img width="974" height="265" alt="image" src="https://github.com/user-attachments/assets/b3da5c6e-6f45-4f44-a28e-77b40f0b58fb" />
</p>

<p>I opened <b>Document Details</b> to view additional information about the attack, including the attacker's IP address (<b>10.0.2.15</b>), the curl command that was used, and the rule ID (<b>31103</b>).</p>

<p><img width="780" height="600" alt="image" src="https://github.com/user-attachments/assets/72df7f53-e8d9-4890-b5ae-8170cbeef32d" />
</p>

<p>I then configured Active Response for the SQL injection detection so that the adversary's IP address would be automatically banned and blocked. I opened the hamburger menu and selected <b>Rules</b> from the left pane.</p>

<p><img width="582" height="677" alt="image" src="https://github.com/user-attachments/assets/494c25b5-402d-40ac-82be-2f7978e0e53b" />
</p>

<p>I searched for <b>SQL injection</b> in the search bar and selected the first result.</p>

<p><img width="975" height="238" alt="image" src="https://github.com/user-attachments/assets/cdcaf92a-c6c4-47a2-bc2c-83a5aa4b912b" />
</p>

<p>I then created a separate Active Response configuration for the SQL injection rule and opened the Wazuh server configuration file by entering:</p>

    sudo nano /var/ossec/etc/ossec.conf

<p><img width="634" height="84" alt="image" src="https://github.com/user-attachments/assets/4020c9b1-2fc9-47f9-81e3-4cd72d6b5333" />
</p>

<p>I configured the system to ban the IP address for 10 minutes when an SQL injection attempt was detected. I inserted the following configuration:</p>

    <active-response>
      <disabled>no</disabled>
      <command>firewall-drop</command>
      <location>local</location>
      <rules_id>31103</rules_id>
      <timeout>600</timeout>
    </active-response>

<p><img width="565" height="427" alt="image" src="https://github.com/user-attachments/assets/ef88ac12-7d21-4dd9-87d4-57d5a7326fda" />
</p>

<p>I restarted the Wazuh manager for the changes to take effect by entering:</p>

    sudo systemctl restart wazuh-manager

<p><img width="617" height="71" alt="image" src="https://github.com/user-attachments/assets/b2ff519b-a16d-4bb8-935f-c495befa3b6a" />
</p>

<p>To test the configuration again, I returned to Kali Linux and sent another request using curl. The request does not cause any actual damage; it simply attempts to retrieve all entries from the <i>users</i> table. I entered the following command:</p>   

    curl –XGET http://10.0.2.6/users/?id=SELECT+*+FROM+users;

<p><img width="671" height="201" alt="image" src="https://github.com/user-attachments/assets/cc2fcc8e-7be4-4416-97bf-c06f48508452" />
</p>

<p>I received the same <i>404 Not Found</i> result, which means that the requested path does not exist on the server.</p>

<p><img width="921" height="301" alt="image" src="https://github.com/user-attachments/assets/5c174e97-02bb-419a-a339-443e47154a25" />
</p>

<p>After returning to the Wazuh dashboard, I confirmed that Wazuh successfully detected the attack and blocked the adversary's IP address, preventing it from continuing to perform SQL injection attempts.</p>

<p><img width="975" height="287" alt="image" src="https://github.com/user-attachments/assets/dbf85eeb-41c8-46d8-bb33-5f854140a86e" />
</p>

<p>I opened the <b>Inspect</b> view to examine additional details about the attack. The details showed the adversary's IP address, the parameter and command that were used, the rule ID, the <b>firewall-drop</b> action, and confirmation that the adversary's IP address had been blocked.</p>

<p><img width="975" height="701" alt="image" src="https://github.com/user-attachments/assets/1afe0891-6f73-4980-aca0-fc5db3de3dcc" />
</p>
<p><img width="975" height="702" alt="image" src="https://github.com/user-attachments/assets/8a75e798-a825-42f3-9964-3483111d1c73" />
</p>
<p><img width="975" height="205" alt="image" src="https://github.com/user-attachments/assets/df8d1b28-eb23-4dd4-bb8e-4b7ffd0ea1fd" />
</p>


<br>
<h2>MITRE ATT&CK Mapping</h2>
<ul>
    <li><b>T1190 — Exploit Public-Facing Application:</b> Relevant to attempted exploitation of a web-facing service.</li>
    <li><b>T1059 — Command and Scripting Interpreter:</b> Relevant to the command-line-based attack simulation using cURL.</li>
    <li><b>T1046 — Network Service Scanning</b> Not directly demonstrated; should not be claimed as an observed technique.</li>
    <li><b>T1210 — Exploitation of Remote Services</b> Not directly applicable; the activity targeted an HTTP application rather than demonstrating exploitation of a remote service.</li>
</ul>

<br>
<h2>Indicators of Compromise (IoC)</h2>
<ul>
    <li><b>Source IP:</b> 10.0.2.15</li>
    <li><b>Target IP:</b> 10.0.2.6</li>
    <li><b>Target service:</b> Apache HTTP</li>
    <li><b>HTTP method:</b> GET</li>
    <li><b>Target URI:</b> /users/</li>
    <li><b>Suspicious parameter:</b> id</li>
    <li><b>SQL payload: </b>SELECT * FROM users</li>
    <li><b>HTTP response:</b> 404 Not Found</li>
    <li><b>Wazuh Rule ID:</b> 31103</li>
    <li><b>Response mechanism:</b> firewall-drop</li>
    <li><b>Block duration:</b> 600 seconds</li>
</ul>

<br>
<h2>Investigation Timeline</h2>
<ul>
    <li><b>01:00 — Attack simulation:</b> Kali host initiated the crafted SQL injection request.</li>
    <li><b>01:00 — Web request received:</b> Apache processed the HTTP request.</li>
    <li><b>01:00 — Log generated:</b> Apache recorded the request in <b>access.log</b>.</li>
    <li><b>01:07 — Detection:</b> Wazuh generated the SQL injection-related alert.</li>
    <li><b>01:07 — Triage:</b> Analyst reviewed the Wazuh event.</li>
    <li><b>01:07 — Investigation:</b> Source IP, request, payload, and rule information were examined.</li>
    <li><b>Post-detection — Response engineering:</b> Wazuh Active Response was configured.</li>
    <li><b>Post-configuration — Containment:</b> <b>firewall-drop</b> was configured for a 600-second block.</li>
    <li><b>Validation — Attack replay:</b> The SQL injection request was sent again.</li>
    <li><b>Validation — Response confirmed:</b> Wazuh detected the activity and initiated IP blocking.</li>
</ul>

<br>
<h2>Lesson Learned</h2>
<p>The exercise demonstrated that effective SOC operations require more than simply generating an alert. The complete value comes from connecting <b>telemetry, detection, investigation, decision-making, and response</b> into a repeatable workflow. A particularly important lesson was the need to distinguish an attempted attack from a confirmed compromise: although the SQL injection payload was detected, the HTTP 404 response indicated that the targeted endpoint was unavailable, and there was no evidence of successful database interaction. </p>
<p>The project also demonstrated the value of automated containment for reducing attacker dwell time while highlighting the importance of carefully tuning Active Response rules to minimize the risk of blocking legitimate traffic.</p>

<br>
<h2>Recommendations</h2>
<p>For a production implementation, the detection should be strengthened with additional web-application telemetry, including HTTP status codes, request normalization, reverse-proxy/WAF logs, application logs, and database audit logs. SQL injection detection should be correlated with repeated requests, authentication context, unusual source behavior, and successful server responses rather than relying solely on a single payload pattern.</p>
<p>A WAF should be considered as an additional preventive control, while Active Response should be carefully tuned and tested against false positives before production deployment. The environment should also maintain centralized logging, appropriate log retention, alert severity classification, documented incident-response procedures, and continuous validation through controlled attack simulations.</p>

<br>
<h2>References & Acknowledgement</h2>
<p>This case study was developed as a controlled cybersecurity lab exercise using Wazuh, Apache2, Ubuntu, Kali Linux, Linux firewall capabilities, and the MITRE ATT&CK Enterprise framework. The attack traffic was intentionally generated in an isolated environment for defensive security testing and detection engineering. The project acknowledges the documentation and security research communities that support the development and understanding of SIEM-based detection, web-application security, incident response, and adversary emulation techniques.</p>
