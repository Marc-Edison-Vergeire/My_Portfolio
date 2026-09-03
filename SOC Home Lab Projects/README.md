# 🏗️ SOC Home Lab Projects

Welcome to the documentation of my security operations home lab. Here, I document the design, deployment, and configuration of my enterprise-grade home lab environments. This section showcases my system administration skills and my ability to build defensive infrastructure from scratch.

**Focus:** Simulating enterprise networks to analyze attack vectors, understand adversary behavior, and generate actionable security telemetry for defensive monitoring.

---

## 🛠️ Core Stack & Technologies Utilized

* **Operating Systems:** Windows Server 2016 (Target Endpoint), Ubuntu Server (Wazuh SIEM), Windows 10 (Target Endpoint), Kali Linux (Attacker Platform).
* **Telemetry & Logging:** Sysmon (System Monitor), Windows Event Logs.
* **SIEM Platforms:** Wazuh / Splunk / Elastic Stack (for centralized log ingestion, parsing, and alerting).

---

## 🚀 Lab Architecture & Implementation Goals

The primary objective of this lab is to mirror a realistic corporate environment to safely test attacks and refine detection engineering capabilities.

### 1. Infrastructure Deployment & Active Directory Setup
* Provisioned and configured a **Windows Server 2016** instance acting as the Primary Domain Controller, establishing a dedicated enterprise domain environment.
* Configured a **Windows 10** workstation as a domain-joined endpoint to simulate standard user activity and target behavior.

### 2. Advanced Telemetry Generation (Sysmon Integration)
* Deployed **SwiftOnSecurity’s Sysmon configuration** across endpoints to capture deep modular telemetry (e.g., process creation, network connections, file creation time changes).
* Fine-tuned Windows Event Forwarding (WEF) to ensure critical security event IDs are captured efficiently.

### 3. Centralized Log Ingestion (SIEM Architecture)
* Configured a **Splunk/Elastic** instance to act as the centralized security brain.
* Installed and configured universal forwarders on the Windows assets to stream Sysmon and Security logs into the SIEM in real time.

### 4. Attack Simulation & Detection Engineering
* Utilized **Kali Linux** to execute controlled adversary techniques (such as credential dumping, brute-forcing, and reverse shells).
* Correlated the generated log telemetry within the SIEM to build custom dashboards and write effective alert logic to detect the executed attacks.

---

## 📂 Project Documentation Index

*📁 Virtual Cybersecurity Lab (SOC Home Lab)* - A step-by-step setup of **VMs** (VirtualBox, Windows 10, Windows Server, Kali Linux, Splunk, ELK, Wazuh, Sysmon)

---

[⬅️ Back to Main Portfolio](../README.md)
