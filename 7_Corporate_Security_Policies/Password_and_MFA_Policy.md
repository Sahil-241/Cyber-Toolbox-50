Enterprise Password and Multi-Factor Authentication (MFA) Policy

Document Details:

Document ID: SEC-POL-001

Version: 1.1

Effective Date: June 24, 2026

Last Reviewed: June 24, 2026

Policy Owner: Chief Information Security Officer (CISO)

Classification: Internal Use Only

Document Control (Version History)

Version 1.0 (June 15, 2026)

Author: Sahil Kumar (GRC Analyst)

Approved By: CISO

Changes: Initial Draft of Password Policy.

Version 1.1 (June 24, 2026)

Author: Sahil Kumar (GRC Analyst)

Approved By: CISO

Changes: Added corporate Password Manager recommendations and MFA exceptions process.

1. Purpose & Objective

The purpose of this policy is to establish a strong credential management framework across the organization. This policy aims to minimize the risk of unauthorized access, brute-force attacks, and credential stuffing by enforcing secure Password Complexity and Multi-Factor Authentication (MFA) protocols.

2. Scope

This policy is strictly applicable to:

All permanent and temporary employees.

Third-party contractors, vendors, and partners.

All corporate assets, including servers, cloud environments (AWS, Azure), databases, emails, and SaaS applications.

3. Password Complexity Standards

All user-created passwords must meet or exceed the following criteria to ensure high security:

Minimum Length: Must be at least 12 characters.

Uppercase Letters: Minimum 1 uppercase letter (A-Z).

Lowercase Letters: Minimum 1 lowercase letter (a-z).

Numeric Digits: Minimum 1 numerical digit (0-9).

Special Characters: Minimum 1 special character (e.g., !, @, #, $, %).

Dictionary Check: Prohibited. Passwords must not contain common names, dictionary words, or sequential numbers.

4. Password Lifecycle & Account Lockout

To prevent active threat actors from maintaining long-term access, the following lifecycle rules are enforced:

Password Rotation (Expiry): User passwords must be rotated every 90 days.

Password History (Reuse): Users cannot reuse any of their last 5 previous passwords.

Account Lockout Threshold: After 5 consecutive failed login attempts, the account will be automatically locked for 30 minutes.

5. Multi-Factor Authentication (MFA) Mandate

Single-password authentication is no longer sufficient. Multi-Factor Authentication (MFA) is mandatory for accessing any corporate asset.

5.1 Approved MFA Factors:

Time-Based One-Time Password (TOTP) Apps: Microsoft Authenticator or Google Authenticator.

FIDO2 Hardware Keys: YubiKey (Mandatory for high-privilege administrators and developers).

5.2 Discouraged/Banned MFA Factors:

SMS & Voice OTP: Prohibited due to susceptibility to SIM Swapping and SS7 intercept attacks.

6. Password Management Best Practices

Password Managers: All employees are provided access to corporate-approved Password Managers (e.g., Bitwarden / 1Password) to store credentials securely. No passwords should be written in physical notebooks or plain text files.

Credential Sharing: Sharing of passwords or MFA tokens via email, Slack, or any communication channel is strictly prohibited.

7. Policy Exceptions Process

In exceptional cases where technical limitations prevent compliance with this policy:

The department manager must submit a formal Security Exception Request.

A formal Risk Assessment must be conducted by the GRC Team to identify compensating controls (e.g., IP whitelisting).

The exception must be approved in writing by the CISO.

All approved exceptions will expire after 1 year and must be re-reviewed annually.

8. Compliance & Monitoring

Automated Audits: The GRC team, along with Active Directory admins, will perform automated monthly credential checks using scripts (like password_strength_check.py and security_compliance_checker.py).

Disciplinary Actions: Any employee found violating this policy (e.g., bypassing MFA, sharing accounts) will be subject to disciplinary actions up to and including termination of employment.