# Corporate Incident Response Policy

**Document Details:**
* **Document ID:** SEC-POL-002  
* **Version:** 1.0  
* **Effective Date:** June 24, 2026  
* **Last Reviewed:** June 24, 2026  
* **Policy Owner:** Head of Cyber Security / Incident Commander  
* **Classification:** Internal Use Only  

---

## Document Control (Version History)

* **Version 1.0 (June 24, 2026)**
  * **Author:** Sahil Kumar (GRC Analyst)
  * **Approved By:** Chief Information Security Officer (CISO)
  * **Changes:** Initial Draft of Enterprise Incident Response Framework.

---

## 1. Purpose & Objective
The purpose of this policy is to establish a structured plan for detecting, responding to, and recovering from cyber security incidents (such as malware infections, data breaches, or ransomware attacks). The objective is to minimize downtime, protect corporate data, and ensure swift recovery.

## 2. Scope
This policy applies to all cyber security events impacting the organization's networks, cloud environments, endpoints, and physical IT infrastructure.

---

## 3. Incident Response Team (SIRT) Roles
When a cyber attack happens, the Security Incident Response Team (SIRT) will immediately take control:

* **Incident Commander (Sahil Kumar):** Coordinates the overall response, assigns tasks, and makes final decisions.
* **Lead Technical Investigator:** Analyzes logs, isolates infected machines, and tracks the hacker's activity.
* **Communications Lead:** Handles internal alerts and public notifications (if required by law).

---

## 4. The 6 Phases of Incident Response
The organization follows the standard NIST incident response framework split into six simple phases:

### Phase 1: Preparation (Taiyari)
* Ensuring all logging tools, firewalls, and monitoring scripts are active *before* an attack happens.
* Regular backup of critical data stored securely offline.

### Phase 2: Identification (Pehchan)
* Detecting unusual activity (e.g., thousands of failed login attempts or unauthorized file access).
* Employees reporting suspicious phishing emails or system misbehavior.

### Phase 3: Containment (Roktham)
* **Short-Term:** Disconnecting the infected computer or server from the network immediately to prevent the virus from spreading.
* **Long-Term:** Changing passwords for compromised accounts and blocking the attacker's IP address.

### Phase 4: Eradication (Khatma)
* Removing the malware, deleting web shells, and wiping out any backdoor left by the hacker.
* Running full antivirus scans across the network.

### Phase 5: Recovery (Wapsi)
* Restoring clean systems from verified secure backups.
* Monitoring the network closely to ensure the hacker does not return.

### Phase 6: Lessons Learned (Seekh)
* Holding a meeting within 72 hours of the incident to review what happened, how it was handled, and how to improve the scripts and defenses for next time.

---

## 5. Compliance & Reporting
* **Mandatory Reporting:** Any employee who notices suspicious activity must report it to the IT helpdesk within 15 minutes.
* **Failure to Comply:** Deliberately hiding a security breach or ignoring containment protocols will lead to strict disciplinary action.