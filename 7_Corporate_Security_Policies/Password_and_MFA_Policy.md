# Enterprise Password and Multi-Factor Authentication (MFA) Policy

**Document Details:**
* **Document ID:** SEC-POL-001  
* **Version:** 1.1  
* **Effective Date:** June 24, 2026  
* **Last Reviewed:** June 24, 2026  
* **Policy Owner:** Chief Information Security Officer (CISO)  
* **Classification:** Internal Use Only  

---

## Document Control (Version History)

* **Version 1.0 (June 15, 2026)**
  * **Author:** Sahil Kumar (GRC Analyst)
  * **Approved By:** CISO
  * **Changes:** Initial Draft of Password Policy.

* **Version 1.1 (June 24, 2026)**
  * **Author:** Sahil Kumar (GRC Analyst)
  * **Approved By:** CISO
  * **Changes:** Added Password Manager and MFA details.

---

## 1. Purpose & Objective
The purpose of this policy is to establish a strong credential management framework across the organization. This policy aims to minimize the risk of unauthorized access, brute-force attacks, and credential stuffing by enforcing secure Password Complexity and Multi-Factor Authentication (MFA) protocols.

## 2. Scope
This policy is strictly applicable to: All permanent and temporary employees, third-party contractors, vendors, and partners. All corporate assets, including servers, cloud environments (AWS, Azure), databases, emails, and SaaS applications.

---

## 3. Password Complexity Standards
All user-created passwords must meet or exceed the following criteria to ensure high security:

* **Minimum Length:** Must be at least 12 characters.
* **Uppercase Letters:** Minimum 1 uppercase letter (A-Z).
* **Lowercase Letters:** Minimum 1 lowercase letter (a-z).
* **Numeric Digits:** Minimum 1 numerical digit (0-9).
* **Special Characters:** Minimum 1 special character (e.g., `!`, `@`, `#`, `$`, `%`).
* **Dictionary Check:** Prohibited. Passwords must not contain common names, dictionary words, or sequential numbers.

---

## 4. Password Lifecycle & Account Lockout
To prevent active threat actors from maintaining long-term access, the following lifecycle rules are enforced:

* **Password Rotation (Expiry):** User passwords must be rotated every 90 days.
* **Password History (Reuse):** Users cannot reuse any of their last 5 previous passwords.
* **Account Lockout Threshold:** After 5 consecutive failed login attempts, the account will be automatically locked for 30 minutes.

---

## 5. Multi-Factor Authentication (MFA)
MFA provides a critical layer of defense beyond passwords and is **mandatory** for all corporate access:

* **Enforcement:** MFA must be enabled on all external-facing portals, corporate emails, VPNs, and production environments.
* **Approved Methods:** * Authenticator Apps (Google Authenticator, Microsoft Authenticator) - *Preferred*
  * Hardware Tokens (YubiKey)
* **Banned Methods:** SMS-based OTPs are strictly discouraged due to SIM-swapping vulnerabilities.

---

## 6. Compliance & Enforcement
* **Audit:** Automated scripts will periodically scan systems to find weak or non-compliant credentials.
* **Non-Compliance:** Accounts found violating this policy will be disabled immediately, and incident tickets will be routed to the SIRT team.