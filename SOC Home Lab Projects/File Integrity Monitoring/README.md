<h1>Wazuh SIEM: File Integrity Monitoring (FIM) — Real-Time Detection and Investigation of Unauthorized Linux File Changes</h1>
<p>Simulated a potentially unauthorized filesystem change to validate whether Wazuh could detect and surface file-integrity events in near real time.</p>

<br>
<p><b>Role: </b>Security Operations Center (SOC) Analyst / Blue Team Analyst</p>
<p><b>Environment:</b> Ubuntu Linux | Wazuh Agent | Wazuh Manager/Dashboard | Syscheck/FIM</p>
<p><b>Attack:</b> Simulated unauthorized file creation within a monitored directory</p>
<p><b>Target: </b>Ubuntu Linux endpoint and monitored filesystem (/root) directory</p>
<p><b>Attacker: </b>Simulated privileged user / authorized lab operator</p>
<p><b>Target Service: </b>Wazuh File Integrity Monitoring (FIM / Syscheck)</p>
<p><b>Detection:</b> Wazuh FIM detected the new file and generated alert Rule ID 100211</p>
<p><b>Response: </b>Validated the alert, reviewed event telemetry, and classified the activity as authorized testing</p>
<p><b>Investigation: </b>Verified the endpoint, file path, event details, and filesystem change</p>
<p><b>Framework: </b>MITRE ATT&CK, NIST Cybersecurity Framework (CSF), Security Operations/Incident Response Lifecycle</p>

<br>
<h2>Executive Summary</h2>
<p>This case study demonstrates the implementation and validation of <b>Wazuh File Integrity Monitoring (FIM)</b> on an Ubuntu Linux server to detect unauthorized filesystem changes in real time. Wazuh was configured to monitor the /root directory with comprehensive integrity checks, change reporting, and real-time monitoring. Following configuration and agent restart, a controlled file-creation test generated a FIM alert that was investigated through <b>Wazuh Dashboard</b> → <b>Threat Hunting</b> → <b>Events</b>. The investigation confirmed that Wazuh successfully identified the filesystem change and generated <b>Rule ID 100211</b>, demonstrating effective endpoint-level detection and security-event visibility. Wazuh supports real-time monitoring, file-integrity checks, and change reporting through its Syscheck/FIM module.</p>

<br>
<h2>Objective</h2>
<p>The objective was to implement and validate real-time <b>File Integrity Monitoring (FIM)</b> on an Ubuntu endpoint using Wazuh, with emphasis on detecting unexpected changes to sensitive filesystem locations. The exercise was designed to demonstrate practical SOC capabilities across detection engineering, alert validation, event investigation, security triage, and evidence-based incident assessment. The configuration also provides a foundation for monitoring high-value Linux directories and identifying changes that could indicate persistence, defense evasion, unauthorized administrative activity, or system compromise.</p>

<br>
<h2>Scenario</h2>
<p>A controlled security test simulated unauthorized file activity on an Ubuntu server. The Wazuh agent configuration at <b>/var/ossec/etc/ossec.conf</b> was modified to monitor <b>/root</b>. The agent was restarted to apply the configuration, followed by controlled file activity within the monitored directory. Wazuh detected the new file and generated an alert that was reviewed through the Threat Hunting Events interface. Wazuh documentation confirms that <b>realtime="yes"</b> enables continuous monitoring of configured Linux directories.</p>

<br>
<h2>Skills Learned</h2>
<ul>
    <li>Wazuh FIM configuration</li>
    <li>SOC alert triage</li>
    <li>Linux Security Monitoring</li>
    <li>Detection engineering</li>
    <li>Security event investigation</li>
    <li>File Integrity Analysis</li>
    <li>Threat Hunting</li>
    <li>Incident documentation</li>
    <li>MITRE ATT&CK Mapping</li>
</ul>

<br>
<h2>Tools Utilized</h2>
<ul>
    <li>Wazuh Manager/Dashboard</li>
    <li>Wazuh Agent</li>
    <li>Ubuntu Linux</li>
    <li>ossec.conf</li>
    <li>Linux systemd</li>
    <li>FIM/Syscheck</li>
</ul>

<br>
<h2>Artifacts</h2>
<ul>
    <li>Wazuh FIM configuration</li>
    <li>FIM alert</li>
    <li>Rule ID 100211</li>
    <li><b>full_log</b> event data</li>
    <li>Monitored <b>/root</b> directory</li>
    <li>File-integrity metadata/telemetry</li>
    <li>Wazuh Dashboard Event record</li>
    <li>Investigation timeline</li>
</ul>

<br>
<h2>Findings</h2>
<h3>FIM Configuration</h3>
<p>The Wazuh agent configuration file was edited at:</p>

    /var/ossec/etc/ossec.conf

<p><img width="702" height="59" alt="image" src="https://github.com/user-attachments/assets/470d047d-5fba-46a9-a949-6ea4c2fd02bf" />
</p>

<p>The following Syscheck configuration was added:</p>

    <directories check_all="yes" report_changes="yes" realtime="yes">/root</directories>

<p><img width="876" height="331" alt="image" src="https://github.com/user-attachments/assets/81915493-8ba6-46d9-aa29-6732e964a113" />
</p>

<p>The Wazuh agent then restarted:</p>

    sudo systemctl restart wazuh-agent

<p><img width="684" height="75" alt="image" src="https://github.com/user-attachments/assets/9ea80336-a86b-489f-8e42-dfde65526afc" />
</p>

<p>This configuration enables comprehensive integrity checks, text-file change reporting, and real-time monitoring of the /root directory. Wazuh documents these attributes as separate FIM capabilities, with realtime providing continuous Linux directory monitoring.</p>

<p><img width="527" height="70" alt="image" src="https://github.com/user-attachments/assets/f60b08a8-d277-4418-b403-78dd06b8d204" />
</p>

<h3>Detection Result</h3>

<p>A controlled file-creation test was performed within the monitored /root directory. Wazuh detected the filesystem change and generated <b>Rule ID 100211</b>.</p>
<p>The alert was reviewed through:</p>

    Wazuh Dashboard → Threat Hunting → Events → Ubuntu Server Agent

<p><img width="975" height="213" alt="image" src="https://github.com/user-attachments/assets/63d1a401-151c-4dca-8c66-287a9fa876f6" />
</p>
<p><img width="975" height="107" alt="image" src="https://github.com/user-attachments/assets/25887677-8bab-4cab-854a-a9143b682392" />
</p>
<p><img width="975" height="67" alt="image" src="https://github.com/user-attachments/assets/51be93bb-5b52-4472-9718-df9cbd656c30" />
</p>
<p><img width="975" height="262" alt="image" src="https://github.com/user-attachments/assets/9add433e-bfd3-416f-840e-aabf5fe3de8c" />
</p>

<p>The event's <b>full_log</b> confirmed that a new file was detected under the monitored <b>/root</b> directory in real time.</p>

<p><img width="942" height="707" alt="image" src="https://github.com/user-attachments/assets/ffdbb63d-84e7-476f-99f3-165aa847b5dd" />
</p>

<h3>Technical Validation Note</h3>
<p>The original lab notes state that <b>/etc/profile</b> was renamed to <b>/etc/profile2</b> while the configured FIM path was <b>/root</b>. These are different filesystem locations. Therefore, for a technically rigorous portfolio demonstration, the test should create, modify, or rename a file inside <b>/root</b> when <b>/root</b> is the configured monitoring scope.</p>
<p>If <b>/etc/profile</b> is the intended security target, <b>/etc</b> should instead be explicitly configured as a monitored directory.</p>

<h3>Attribution Consideration</h3>
<p>The configuration shown above enables real-time monitoring and change reporting but does n<b>ot explicitly enable whodata="yes"</b>. If the objective is to identify the user and process responsible for the modification, Wazuh's who-data capability should be enabled and validated separately. Wazuh documents whodata as the mechanism for collecting user/process information associated with file changes.</p>

<br>
<h2>MITRE ATT&CK Mapping</h2>
<ul>
    <li><b>T1083 — File and Directory Discovery:</b> Relevant to filesystem enumeration; not directly demonstrated by this test.</li>
    <li><b>T1222.002 — File and Directory Permissions Modification: Linux and Mac:</b> Relevant to adversarial permission changes; not directly demonstrated by this test</li>
    <li><b>FIM Detection Context</b> Provides defensive visibility into filesystem changes that may support multiple ATT&CK techniques.</li>
</ul>

<br>
<h2>Indicators of Compromise (IoC)</h2>
<ul>
    <li>Newly created filename <b>/root</b> directory</li>
    <li>File creation timestamp</li>
    <li>File Integrity Monitoring (FIM) event</li>
    <li>Wazuh Rule ID 100211</li>
</ul>

<br>
<h2>Investigation Timeline</h2>
<ul>
    <li><b>October 4, 2026 — 00:21:</b> Wazuh Dashboard <b>Threat Hunting</b> → <b>Events</b> generated a FIM alert.</li>
    <li><b>00:21:</b> Ubuntu server agent reported a new file under <b>/root</b>.</li>
    <li><b>00:22:</b> Analyst reviewed the triggered Wazuh event and Rule ID <b>100211</b>.</li>
    <li><b>00:23: </b><b>full_log</b> was reviewed to validate the filesystem activity.</li>
    <li><b>00:25:</b> Activity was confirmed as an authorized security-validation test.</li>
    <li><b>00:30:</b> Detection results and recommendations were documented.</li>
</ul>

<br>
<h2>Lesson Learned</h2>
<p>This exercise demonstrated that effective <b>FIM</b> is not simply about generating an alert; it requires accurate monitoring scope, meaningful telemetry, validation, and contextual investigation. Wazuh successfully detected the controlled filesystem change, but determining whether a change is malicious requires correlation with identity, process, authentication, and endpoint telemetry. The exercise also reinforced the importance of precise documentation: the configured monitoring path, test activity, and evidence must align for a detection claim to be technically defensible.</p>

<br>
<h2>Recommendations</h2>
<p>Expand <b>FIM</b> coverage to security-sensitive Linux locations based on organizational risk, including <b>/etc</b>, privileged-user directories, application configurations, and other critical assets. Enable <b>who-data</b> monitoring when <b>user/proces</b>s attribution is required, correlate FIM events with authentication and process telemetry, and establish severity and triage criteria for unexpected changes. Use <b>report_changes</b> selectively because Wazuh stores copies of monitored files when collecting content differences.</p>

<br>
<h2>References & Acknowledgement</h2>
<p>This case study references official Wazuh documentation for Syscheck/FIM configuration, real-time monitoring, file-change reporting, and who-data monitoring, together with MITRE ATT&CK documentation for relevant Linux filesystem techniques. Wazuh's official documentation confirms that <b>/var/ossec/etc/ossec.conf</b> is the Linux agent configuration file and provides documented examples of configuring real-time FIM and reporting file changes.</p>

<p><b>References: </b>Wazuh File Integrity Monitoring Documentation | Wazuh Syscheck Configuration Reference | MITRE ATT&CK Enterprise Techniques</p>
