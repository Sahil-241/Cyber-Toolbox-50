# Corporate Access Control Policy

**Document Details:**
* **Document ID:** SEC-POL-003  
* **Version:** 1.0  
* **Effective Date:** June 24, 2026  
* **Last Reviewed:** June 24, 2026  
* **Policy Owner:** Head of Identity & Access Management (IAM)  
* **Classification:** Internal Use Only  

---

## Document Control (Version History)

* **Version 1.0 (June 24, 2026)**
  * **Author:** Sahil Kumar (GRC Analyst)
  * **Approved By:** Chief Information Security Officer (CISO)
  * **Changes:** Initial Framework for Identity and Access Management.

---

## 1. Purpose & Objective
The purpose of this policy is to safeguard corporate data by ensuring that only authorized users have access to specific IT assets. This policy enforces strict identity verification and access management to prevent internal data leaks and unauthorized external entry.

## 2. Core Principles of Access Control

To keep things secure, our organization strictly follows two golden rules:
* **Principle of Least Privilege (PoLP):** Kisi bhi employee ko sirf utna hi access milega jitna uske kaam ke liye zaroori hai. Ek HR manager ko production server ka access nahi milega, aur ek developer ko finance data ka access nahi milega.
* **Need-to-Know Basis:** Data ka access tabhi khola jayega jab uski sach me zaroori requirement hogi.

---

## 3. User Access Lifecycle Management

### 3.1 Onboarding (Naye Employee ka Access)
* HR onboarding process complete hone ke baad hi IT team formal email request par user ID create karegi.
* Default roop se naye account ka access 'Zero' hoga (No permissions by default).

### 3.2 Access Review (Regular Checking)
* GRC Team har 3 mahine (Quarterly) mein saare employees ke access levels ko review karegi.
* Agar koi employee team badal leta hai, toh uske purane saare access 24 ghante ke andar remove kar diye jayenge.

### 3.3 Offboarding (Company Chhodte Waqt)
* Jab koi employee company chhodta hai, toh uski termination block ke **1 ghante ke andar** uske saare corporate accounts (Email, Slack, GitHub, AWS) block aur delete kar diye jayenge taaki koi revenge attack ya data theft na ho.

---

## 4. Network & Remote Access Control
* **VPN Requirement:** Company ke internal tools ya cloud servers ko bina corporate VPN ke access karna sakht mana hai.
* **Device Restriction:** Sirf company ke diye gaye secure laptops se se hi network login allowed hoga. Personal devices completely banned hain.

---

## 5. Compliance & Monitoring
* **Unused Accounts:** Jo accounts 90 din tak login nahi honge, unhe active directory scripts automatic disable kar dengi.
* **Violations:** Kisi dusre employee ka password use karke login karna Security Violation mana jayega aur sidhe HR termination tak ki carwayi ho sakti hai.