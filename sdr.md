# Security Decision Record

**Certification Package:** https://trust.example.com/cpo.json  
**SDR version:** 0.1.0  
**Last updated:** 2026-10-02T01:32:05Z (source: sdr_compile.py)  
**Ruleset:** CR26 2026.09.13.02, track 20x, class C  
**Schema version:** 1.1.1  

> Generated automatically from `sdr.json`. Do not hand-edit this file --
> edit the authored records or evidence inputs and rebuild.

## Summary

- FedRAMP Requirements: 0/168 applicable rules have a record
- Key Security Indicators: 46/46 in-scope KSIs have a record
- Open findings: 🔴 BLOCKING × 444

## FedRAMP Requirements

### AFC — Addressing FedRAMP Communication

#### `AFC-CSO-ACK` Acknowledge Receipt  ⬜ No record

*SHOULD* — Providers SHOULD promptly and automatically acknowledge the receipt of messages received from FedRAMP in their FedRAMP Security Inbox.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `AFC-CSO-CRA` Complete Required Actions  ⬜ No record

*MUST* — Providers MUST complete the required actions in Emergency or Emergency Test designated messages sent by FedRAMP within the timeframe included in the message.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `AFC-CSO-EMR` Emergency Message Routing  ⬜ No record

*MUST* — Providers MUST route Emergency designated messages sent by FedRAMP to a senior security official for their awareness.

**Artifacts required:** Configuration settings for FSI mailbox; Automated validation to check FSI mailbox configuration

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `AFC-CSO-IMA` Important Message Actions  ⬜ No record

*SHOULD* — Providers SHOULD complete the required actions in Important designated messages sent by FedRAMP within the timeframe specified in the message.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `AFC-CSO-INB` Maintain a FedRAMP Security Inbox  ⬜ No record

*MUST* — Providers MUST establish and maintain an email address to receive messages from FedRAMP; this inbox is a FedRAMP Security Inbox (FSI).

**Artifacts required:** Email address to receive messages from FedRAMP

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `AFC-CSO-NOC` Notification of Changes  ⬜ No record

*MUST* — Providers MUST immediately notify FedRAMP of any changes to the email address for their FedRAMP Security Inbox.

**Artifacts required:** Process, manual or automated, to notify FedRAMP of changes in the FedRAMP Security Inbox

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `AFC-CSO-RCV` Receive Email Without Disruption  ⬜ No record

*MUST* — Providers MUST receive and react to email messages from FedRAMP without disruption and without requiring additional actions from FedRAMP.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `AFC-CSO-TFG` Trust @fedramp.gov and @gsa.gov  ⬜ No record

*MUST* — Providers MUST treat any email originating from an @fedramp.gov or @gsa.gov email address as if it was sent from FedRAMP by default; if such a message is confirmed to originate from someone other than FedRAMP then the FedRAMP Security Inbox rules no longer apply.

**Artifacts required:** Configuration settings for FSI mailbox; Automated validation to check FSI mailbox configuration

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### CCM — Collaborative Continuous Monitoring

#### `CCM-OCR-AFS` Anonymized Feedback Summary  ⬜ No record

*MUST* — Providers MUST supply an anonymized and desensitized summary of the feedback, questions, and answers about each Ongoing Certification Report as an addendum to the Ongoing Certification Report OR in the next Ongoing Certification Report.

**Artifacts required:** How the summary will be delivered

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-OCR-AVL` Report Availability  ⬜ No record

*MUST* — Providers MUST supply an Ongoing Certification Report to all necessary parties every 3 months, covering the entire period since the previous summary, in a consistent format that is human readable; this report MUST include high-level summaries of at least the following information (if applicable):

**Artifacts required:** Most recent Ongoing Certification Report. If the report is not available, the provider MUST provide a sample report that includes all required information.; How the report will be delivered

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-OCR-FBM` Feedback Mechanism  ⬜ No record

*MUST* — Providers MUST supply an asynchronous mechanism for all necessary parties to provide feedback or ask questions about each Ongoing Certification Report.

**Artifacts required:** How to access the feedback mechanism.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-OCR-LSI` Limit Sensitive Information  ⬜ No record

*MUST NOT* — Providers MUST NOT irresponsibly disclose sensitive information in an Ongoing Certification Report that would likely have an adverse effect on the cloud service offering.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-OCR-NRD` Next Report Date  ⬜ No record

*MUST* — Providers MUST supply the target date for their next Ongoing Certification Report with other public FedRAMP Certification Data.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-OCR-RPS` Responsible Public Certification Report Sharing  ⬜ No record

*MAY* — Providers MAY responsibly supply some or all of the information an Ongoing Certification Report to the public or other parties if the provider determines doing so will NOT likely have an adverse effect on the cloud service offering.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-OCR-SOR` Spread Out Reports  ⬜ No record

*SHOULD* — Providers SHOULD establish a regular 3 month cycle for Ongoing Certification Reports that is spread out from the beginning, middle, or end of each quarter.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-ACT` Additional Content  ⬜ No record

*SHOULD* — Providers SHOULD supply additional information in Quarterly Reviews that the provider determines is of interest, use, or otherwise relevant to agencies.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-MTG` Quarterly Review Meeting  ⬜ No record

*MUST* — Providers with Class C Certifications MUST host a synchronous Quarterly Review every 3 months, open to all necessary parties, to review aspects of the most recent Ongoing Certification Reports that the provider determines are of the most relevance to agencies.

**Artifacts required:** selected ordinal recurrence for the Ongoing Certification Report cycle.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-NID` No Irresponsible Disclosure  ⬜ No record

*MUST NOT* — Providers MUST NOT irresponsibly disclose sensitive information in a Quarterly Review that would likely have an adverse effect on the cloud service offering.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-NRD` Next Review Date  ⬜ No record

*MUST* — Providers MUST publicly supply the target date for their next Quarterly Review with other public FedRAMP Certification Data.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-REG` Meeting Registration Info  ⬜ No record

*MUST* — Providers MUST supply either a registration link or a downloadable calendar file with meeting information for Quarterly Reviews to all necessary parties.

**Artifacts required:** URL to the registration page or calendar file.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-RTP` Restrict Third Parties  ⬜ No record

*SHOULD NOT* — Providers SHOULD NOT invite third parties to attend Quarterly Reviews intended for agencies unless they have specific relevance.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-RTR` Record/Transcribe Reviews  ⬜ No record

*SHOULD* — Providers SHOULD record or transcribe Quarterly Reviews and supply them to all necessary parties.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-SAR` Schedule Around Reports  ⬜ No record

*SHOULD* — Providers SHOULD regularly schedule Quarterly Reviews to occur at least 3 business days after releasing an Ongoing Certification Report AND within 10 business days of such release.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-SCR` Share Content Responsibly  ⬜ No record

*MAY* — Providers MAY responsibly supply content prepared for a Quarterly Review to the public or other parties if the provider determines doing so will NOT likely have an adverse effect on the cloud service offering.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CCM-QTR-SRR` Share Recordings Responsibly  ⬜ No record

*MAY* — Providers MAY responsibly supply recordings or transcriptions of Quarterly Reviews to the public or other parties ONLY if the provider removes all agency information (comments, questions, names, etc.) AND determines doing so will NOT likely have an adverse effect on the cloud service offering.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### CDS — Certification Data Sharing

#### `CDS-CSO-AVR` Availability Reporting  ⬜ No record

*MUST* — Providers with Class C Certifications MUST maintain a web service, available to all necessary parties, that indicates current and historical availability of core services within the cloud service offering over at least the past 30 days, including availability incidents, in both human-readable and machine-readable formats; this service MUST be available even if the primary cloud service offering is unavailable.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-CBF` Consistency Between Formats  ⬜ No record

*MUST* — Providers MUST use automation to ensure information remains consistent between human-readable and machine-readable formats when FedRAMP Certification Data is provided in both formats.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-FID` Always Include FedRAMP ID  ⬜ No record

*MUST* — Providers MUST always include the FedRAMP ID of the related cloud service offering in all FedRAMP Certification Data once assigned, including all reports, notifications, and other communication that results from FedRAMP rules.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-FRC` FedRAMP Certification Reports  ⬜ No record

*MUST* — Providers MUST include FedRAMP Certification Reports with their FedRAMP Certification Data without inappropriate modifications, and make such reports available within 2 weeks of receiving the materials from FedRAMP.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-HAD` Historical FedRAMP Certification Data  ⬜ No record

*MUST* — Providers MUST supply snapshots of FedRAMP Certification Data aligned to Ongoing Certification Reports to all necessary parties; these snapshots MUST be available for the duration of FedRAMP Certification.

**Artifacts required:** Explanation of how to access this information.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-IRP` Include Relevant Policies  ⬜ No record

*MUST* — Providers MUST supply all relevant policies and procedures in the FedRAMP Certification Data, including a human-readable and machine-readable reference that explains at least the following about each included policy and procedure:

**Artifacts required:** Explanation of how to access this information.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-PSM` Per-Service Certification Materials  ⬜ No record

*MAY* — Providers with Class C Certifications MAY supply per-service FedRAMP Certification materials.

**Artifacts required:** Explanation of the supplied materials, including how to access and use them.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-PUB` Public Information  ⬜ No record

*MUST* — Providers MUST publicly share up-to-date information about the cloud service offering in both human-readable and JSON formats, including at least the following information that is available and applicable:

**Artifacts required:** URL to the human-readable data.; URL to the machine-readable data.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-RIS` Responsible Information Sharing  ⬜ No record

*MUST* — Providers MUST provide sufficient information in FedRAMP Certification Data to support agency authorization decisions but SHOULD NOT include sensitive information that would likely enable a threat actor to gain unauthorized access, cause harm, disrupt operations, or otherwise have a negative adverse impact on the cloud service offering.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-RPS` Responsible Public Package Sharing  ⬜ No record

*MAY* — Providers MAY responsibly share some or all of the information in a FedRAMP Certification Package publicly or with other parties if the provider determines doing so will NOT likely have an adverse effect on the cloud service offering.

**Artifacts required:** Explanation of if and how this information is shared with other parties.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-SVC` Public Service List  ⬜ No record

*MUST* — Providers MUST publicly share a detailed list of specific services and their security categories that are included in the cloud service offering using clear feature or service names that align with standard public marketing materials; this list MUST be complete enough for a potential customer to determine which services are and are not included in the FedRAMP Minimum Assessment Scope without requesting access to underlying FedRAMP Certification Data.

**Artifacts required:** URL to the human-readable data.; URL to the machine-readable data (if applicable).

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-CSO-UTC` Use Trust Centers  ⬜ No record

*MUST* — Providers MUST use a FedRAMP-compatible trust center to store and share FedRAMP Certification Data with all necessary parties.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-TRC-AAI` Agency Access Inventory  ⬜ No record

*MUST* — Trust centers MUST maintain an inventory and history of federal agency users or systems with access to FedRAMP Certification Data and MUST make this information available to FedRAMP upon request.

**Artifacts required:** Explanation of how FedRAMP can obtain this information.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-TRC-ACL` Access Logging  ⬜ No record

*MUST* — Trust centers MUST log access to FedRAMP Certification Data and store summaries of access for at least six months; such information, as it pertains to specific parties, SHOULD be made available upon request by those parties.

**Artifacts required:** Explanation of how the appropriate parties can obtain this log information.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-TRC-HMR` Human and Machine-Readable Certification Data  ⬜ No record

*SHOULD* — Trust centers SHOULD make FedRAMP Certification Data available to view and download in both human-readable and machine-readable formats.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-TRC-PAC` Programmatic Access  ⬜ No record

*MUST* — Trust centers MUST provide documented programmatic access to all FedRAMP Certification Data, including programmatic access to human-readable materials.

**Artifacts required:** URL to the documentation for programmatic access.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-TRC-SSM` Self-Service Access Management  ⬜ No record

*SHOULD* — Trust centers SHOULD include features that encourage all necessary parties to provision and manage access to FedRAMP Certification Data for their users and services directly.

**Artifacts required:** URL or explanation how to access documentation of these features and capabilities.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-TRC-USH` Uninterrupted Sharing  ⬜ No record

*MUST* — Trust centers MUST share FedRAMP Certification Data with all necessary parties without interruption.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-UTC-AAD` Agency Access Denial  ⬜ No record

*MUST* — Providers MUST notify FedRAMP within 5 business days of denying an agency access request for FedRAMP Certification Data.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CDS-UTC-AGA` Agency Access  ⬜ No record

*SHOULD* — Providers SHOULD supply access to the FedRAMP Certification Package with agencies upon request.

**Artifacts required:** URL or explanation of how to request these materials.; Explanation of how the provider decides whether or not to share these materials or other related policies.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### CMU — Cryptographic Module Use

#### `CMU-CSO-CAT` Configuration of Agency Tenants  ⬜ No record

*SHOULD* — Providers SHOULD configure agency tenants by default to use cryptographic services that use cryptographic modules or update streams of cryptographic modules with active validations under the NIST Cryptographic Module Validation Program when such modules are available.

**Artifacts required:** List of cryptographic modules used by default including whether these modules are validated under the NIST Cryptographic Module Validation Program or are update streams of such modules.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CMU-CSO-CMD` Cryptographic Module Documentation  ⬜ No record

*MUST* — Providers MUST document the cryptographic modules used in each service (or groups of services that use the same modules) where cryptographic services are used to protect federal customer data, including whether these modules are validated under the NIST Cryptographic Module Validation Program or are update streams of such modules.

**Artifacts required:** List of cryptographic modules including whether these modules are validated under the NIST Cryptographic Module Validation Program or are update streams of such modules.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CMU-CSO-UVM` Using Validated Cryptographic Modules  ⬜ No record

*SHOULD* — Providers with Class C Certifications SHOULD use cryptographic modules or update streams of cryptographic modules with active validations under the NIST Cryptographic Module Validation Program when using cryptographic services to protect federal customer data.

**Artifacts required:** List of cryptographic modules including whether these modules are validated under the NIST Cryptographic Module Validation Program or are update streams of such modules.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### CPO — Certification Package Overview

#### `CPO-CSO-MTD` Certification Package Overview Metadata  ⬜ No record

*MUST* — Providers MUST also include the following basic metadata in their Certification Package Overview:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CPO-CSO-OSA` Overall Summary of Assessment in Certification Package  ⬜ No record

*MUST* — Providers seeking Class C Certification MUST also include the overall summary of their FedRAMP independent assessment, supplied by the assessor per IVV-IAS-OSA (Overall Summary of Assessment), in their Certification Package Overview.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CPO-CSO-OVR` Overview of the Cloud Service Offering  ⬜ No record

*MUST* — Providers MUST supply a Certification Package Overview within their FedRAMP Certification Package, in both human-readable and JSON formats, that includes at least all of the information required by the following rules:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `CPO-CSX-CPM` Certification Package Maintenance for 20x  ⬜ No record

*MUST* — Providers with 20x Class C Certifications MUST persistently maintain their FedRAMP Certification Package to ensure it is up to date and complete at least once every 2 weeks.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### FRC — FedRAMP Certification

#### `FRC-APP-AFC` Applying for FedRAMP Certification  ⬜ No record

*MUST* — Providers MUST complete the FedRAMP Certification Application Form in full to request an initial assessment by FedRAMP.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-APP-FCP` Fresh FedRAMP Certification Package  ⬜ No record

*MUST* — Providers MUST supply a fresh initial FedRAMP Certification Package that shows the current status of the cloud service offering as verified and validated by the provider within the previous 7 days.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-APP-FIA` Fresh Independent Assessment  ⬜ No record

*MUST* — Providers seeking Class C Certification MUST supply a fresh initial FedRAMP independent assessment that was completed by a FedRAMP Recognized independent assessment service within the previous 3 months.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-APP-MLF` Marketplace Listing First  ⬜ No record

*MUST* — Providers MUST be listed in the FedRAMP Marketplace before applying for FedRAMP Certification, including:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-APP-NTP` No Third-Party Applicants  ⬜ No record

*MUST NOT* — Providers MUST NOT use a third party to apply for a FedRAMP Certification on their behalf; this includes independent assessment services.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-APP-USA` Updating Stale Assessments  ⬜ No record

*MAY* — Providers MAY freshen a stale initial independent verification and validation assessment by having a FedRAMP Recognized independent assessment service review any changes between the original assessment and the current status of the cloud service offering in place of a full re-assessment, UNLESS the stale assessment is more than 9 months old.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-APS-ATO` Agency Authorization to Operate  ⬜ No record

*MUST* — Providers seeking a FedRAMP Rev5 Agency Certification MUST have completed the Authorization to Operate (ATO) process with their agency sponsor for the cloud service offering, concluding with a formal signed ATO letter that the agency has sent over official government channels to FedRAMP.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CCL-DCC` Downgrading Certification Class  ⬜ No record

*MUST* — Providers MUST apply for a new FedRAMP Certification to downgrade their Certification Class.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CCL-DNP` Downgrade Notification Period  ⬜ No record

*SHOULD* — Providers SHOULD notify all necessary parties at least 120 days in advance of an intended downgrade or cancellation of FedRAMP Certification.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CCL-UCC` Upgrading Certification Class  ⬜ No record

*MUST* — Providers MUST apply for a new FedRAMP Certification to upgrade their Certification Class; all applicable requirements MUST be met in advance.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CLA-ASF` Approved Alternative Security Frameworks  ⬜ No record

*MUST* — Providers seeking a FedRAMP Class A Certification MUST have completed a certification or equivalent process, including an independent assessment if applicable, from one of the following alternative security frameworks within the past 12 months:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CLA-EAM` External Assessment Materials  ⬜ No record

*MUST* — Providers seeking a FedRAMP Class A Certification MUST supply the following materials from their alternative security framework assessment to all necessary parties:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CLA-IVV` Optional Independent Verification and Validation  ⬜ No record

*MAY* — Providers seeking a FedRAMP Class A Certification MAY have the FedRAMP Certification Package independently verified and validated by a FedRAMP Recognized assessor before submission to FedRAMP.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CLA-MFR` Mandatory FedRAMP Rules for Class A  ⬜ No record

*MUST* — Providers seeking a Class A FedRAMP Certification MUST address all rules in this FedRAMP Class A Certification subset (FRC-CLA) AND the following additional FedRAMP Class A rules; the appropriate artifacts or information mapping for all rules MUST be supplied in the FedRAMP Certification Package.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CLA-OFR` Address Optional FedRAMP Rules for Class A  ⬜ No record

*MAY* — Providers seeking a Class A FedRAMP Certification MAY address the following additional optional FedRAMP Class A rules (if applicable):

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CLA-RFR` Recommended FedRAMP Rules for Class A  ⬜ No record

*SHOULD* — Providers seeking a Class A FedRAMP Certification SHOULD address the following additional recommended FedRAMP Class A rules (if applicable):

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSO-FCP` FedRAMP Certification Profile  ⬜ No record

*MUST* — Providers MUST identify a target FedRAMP Certification Profile and apply all relevant FedRAMP Practices to the cloud service offering.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSO-JSN` FedRAMP JSON Schemas  ⬜ No record

*MUST* — Providers MUST supply machine-readable information in JSON documents that are valid against the corresponding JSON schema when a rule contains a FedRAMP JSON schema, UNLESS otherwise specified in the rule.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSO-MRA` Maintain Responsibility and Accountability  ⬜ No record

*MUST* — Providers MUST maintain responsibility and accountability for the accuracy and completeness of all information in the FedRAMP Certification Package, especially when they engage a third party (such as an independent assessor, advisory service, or external tools) to supply information on their behalf.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSO-PKG` FedRAMP Certification Package  ⬜ No record

*MUST* — Providers seeking a Certification MUST supply a complete FedRAMP Certification Package to FedRAMP for initial certification; the FedRAMP Certification Package MUST include at least the following information:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSO-POP` Pick One Program Certification Type  ⬜ No record

*MUST NOT* — Providers MUST NOT seek both FedRAMP Rev5 Program Certification and FedRAMP 20x Program Certification for the same cloud service offering; pick one type.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSX-MAS` Application within MAS  ⬜ No record

*SHOULD* — Providers SHOULD apply ALL Key Security Indicators to ALL aspects of their cloud service offering that are within the FedRAMP Minimum Assessment Scope.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSX-MOT` Metrics Over Time for Key Security Indicators  ⬜ No record

*MUST* — Providers seeking 20x Class C Certification MUST supply historical metrics including status from persistent validation over at least the past 6 months for all Key Security Indicators.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSX-VVK` Automated Verification and Validation of Key Security Indicators  ⬜ No record

*MUST* — Providers seeking 20x Class C Certification MUST implement automated methods to persistently verify and validate the accuracy and completeness of Key Security Indicators with at least 2 automated methods for each Key Security Indicator.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `FRC-CSX-VVR` Automated Verification and Validation of FedRAMP Rules  ⬜ No record

*SHOULD* — Providers seeking 20x Class C Certification SHOULD implement automated methods to persistently verify and validate the accuracy and completeness of the Security Decision Record for FedRAMP rules when applicable.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### IEC — Incident Evaluation and Communication

#### `IEC-CSO-AIR` Automated Incident Reporting  ⬜ No record

*SHOULD* — Providers SHOULD use automation to minimize human intervention in the process of reporting FedRAMP Reportable Incidents to all affected parties.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IEC-CSO-DPR` Default PAIN Rating  ⬜ No record

*MUST* — Providers MUST treat FedRAMP Reportable Incidents as if they have a Potential Agency Impact N-rating (PAIN) of 5 UNLESS they promptly estimate the PAIN rating following the rule in IEC-CSO-EFI (Estimate Federal Impact).

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IEC-CSO-EFI` Estimate Federal Impact  ⬜ No record

*SHOULD* — Providers SHOULD promptly estimate the likely adverse impact of an incident on agency customers to assign a Potential Agency Impact N-rating; this step is called Incident Rating.

**Artifacts required:** An incident log showing an example of one or more incidents being evaluated including the reason for the determination. The log can be from real incidents, simulated incidents, or a combination of sources.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IEC-CSO-EFR` Evaluate FedRAMP Reportability  ⬜ No record

*MUST* — Providers MUST promptly evaluate incidents to determine if they affect confidentiality or integrity of federal customer data or are likely to affect confidentiality or integrity of federal customer data; such incidents are FedRAMP Reportable Incidents and must be reported following the FedRAMP Incident Evaluation and Communication rules.

**Artifacts required:** An incident log showing an example of one or more incidents being evaluated including the reason for the determination. The log can be from real incidents, simulated incidents, or a combination of sources.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IEC-CSO-FIR` Final Incident Report  ⬜ No record

*MUST* — Providers with Class C Certifications MUST responsibly notify all affected parties by providing a Final Incident Report once the incident has been resolved and recovery is complete, including final updates to all previously reported information.

**Artifacts required:** An Final Incident Report for one or more incidents. The report can be from real incidents, simulated incidents, or a combination of sources.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IEC-CSO-IIR` Initial Incident Report  ⬜ No record

*MUST* — Providers with Class C Certifications MUST responsibly notify all affected parties after identifying FedRAMP Reportable Incidents by providing an Initial Incident Report with as much of the following information that is available at the time of reporting and/or the current relevant status for each item:

**Artifacts required:** An Initial Incident Report for one or more incidents. The report can be from real incidents, simulated incidents, or a combination of sources.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IEC-CSO-OIR` Ongoing Incident Reports  ⬜ No record

*MUST* — Providers with Class C Certifications MUST responsibly notify all affected parties of ongoing activity as new information becomes available during incident response for FedRAMP Reportable Incidents, including updates (or lack of updates) to all previously reported information and as much of the following additional information that is available and/or the current relevant status for each item:

**Artifacts required:** An Ongoing Incident Report for one or more incidents. The report can be from real incidents, simulated incidents, or a combination of sources.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### IVV — Independent Verification and Validation

#### `IVV-CSO-DUS` Document Use of Representative Samples  ⬜ No record

*MUST* — Providers MUST document and explain the use of representative samples during verification and validation when using representative samples as allowed by IVV-CSO-USR (Use Representative Samples).

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IVV-CSO-FIA` FedRAMP Independent Assessments  ⬜ No record

*MUST* — Providers with Class C Certifications MUST persistently complete an independent verification and validation assessment of all applicable FedRAMP rules with a FedRAMP Recognized independent assessment service OR FedRAMP at least once per year; this is a FedRAMP independent assessment.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IVV-CSO-ICP` Inclusion in Certification Package  ⬜ No record

*MUST* — Providers MUST supply the results of FedRAMP independent assessments in their FedRAMP Certification Package without inappropriate modification.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IVV-CSO-RAA` Receiving Assessor Advice  ⬜ No record

*MAY* — Providers MAY ask for and accept advice from their assessor during assessment regarding techniques and procedures that will improve their security posture or the effectiveness, clarity, and accuracy of their verification, validation and reporting procedures, UNLESS doing so is likely to compromise the objectivity and integrity of the assessment.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IVV-CSO-SEE` Supply Evidence of Effectiveness  ⬜ No record

*MUST* — Providers MUST supply evidence to all necessary assessors of the effectiveness of the measures that have been implemented to meet FedRAMP Practices; this evidence is the result of validation.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IVV-CSO-SEI` Supply Evidence of Implementation  ⬜ No record

*MUST* — Providers MUST supply evidence to all necessary assessors of the implementation of the measures that have been documented to meet FedRAMP Practices; this evidence is the result of verification.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IVV-CSO-STE` Supply Technical Explanations  ⬜ No record

*SHOULD* — Providers SHOULD supply all necessary assessors with technical explanations, demonstrations, and other relevant supporting information about the technical capabilities they employ to address FedRAMP rules; this SHOULD be supplied as necessary to ensure the assessor can effectively complete verification and validation.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IVV-CSO-USR` Use Representative Samples  ⬜ No record

*MAY* — Providers MAY use representative samples as appropriate during verification and validation.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `IVV-CSX-AIA` Annual Independent Assessments for 20x  ⬜ No record

*MUST* — Providers with 20x Class C Certifications MUST include all Key Security Indicators in a FedRAMP independent assessment at least once per year.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### MAS — Minimum Assessment Scope

#### `MAS-CSO-FLO` Information Flows and Security Categories  ⬜ No record

*MUST* — Providers MUST clearly identify, document, and explain information flows and security categories for ALL information resources or sets of information resources in the cloud service offering.

**Artifacts required:** A machine readable output containing all required data of the permitted connections between components of the cloud service offering that are likely to handle federal customer data or likely to impact the confidentiality, integrity, or availability of federal customer data handled by the cloud service offering.; A human readable explanation of how the machine readable output is derived.; The code for the automated process used to generate the machine readable output.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `MAS-CSO-IIR` Identify Information Resources  ⬜ No record

*MUST* — Providers MUST identify a set of information resources to assess for FedRAMP Certification that includes all information resources that are likely to handle federal customer data or likely to impact the confidentiality, integrity, or availability of federal customer data handled by the cloud service offering; this set of information resources is the cloud service offering.

**Artifacts required:** A machine readable output containing all required data of the components of the cloud service offering that are likely to handle federal customer data or likely to impact the confidentiality, integrity, or availability of federal customer data handled by the cloud service offering.; A human readable explanation of how the machine readable output is derived.; The code for the automated process used to generate the machine readable output.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `MAS-CSO-MDI` Metadata Inclusion  ⬜ No record

*MUST* — Providers MUST include metadata (including metadata about federal customer data) in the Minimum Assessment Scope ONLY IF MAS-CSO-IIR (Identify Information Resources) APPLIES.

**Artifacts required:** A machine readable output containing all required data of the metadata collected or maintained by the cloud service offering that are likely to handle federal customer data or likely to impact the confidentiality, integrity, or availability of federal customer data handled by the cloud service offering.; A human readable explanation of how the machine readable output is derived.; The code for the automated process used to generate the machine readable output.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `MAS-CSO-SUP` Supplemental Information  ⬜ No record

*MAY* — Providers MAY include additional materials about other information resources that are not part of the cloud service offering in a FedRAMP Certification Package supplement; these resources will not be FedRAMP Certified and MUST be clearly marked and separated from the cloud service offering.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `MAS-CSO-TPR` Third-Party Information Resources  ⬜ No record

*MUST* — Providers MUST address the potential impact to federal customer data from third-party information resources used by the cloud service offering, ONLY IF MAS-CSO-IIR (Identify Information Resources) APPLIES, by documenting the following information about each applicable third-party information resource:

**Artifacts required:** A machine readable output containing all required data of the third-party information resources of the cloud service offering that are likely to handle federal customer data or likely to impact the confidentiality, integrity, or availability of federal customer data handled by the cloud service offering.; A human readable explanation of how the machine readable output is derived.; The code for the automated process used to generate the machine readable output.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### MKT — Marketplace Listing

#### `MKT-CSO-MLR` Marketplace Listing Requirements  ⬜ No record

*MUST* — Providers MUST address at least these FedRAMP rules to apply for a new FedRAMP Marketplace listing OR to request updates to an existing listing:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `MKT-CSO-PML` Provider Marketplace Listing Requests  ⬜ No record

*MUST* — Providers MUST notify FedRAMP using the FedRAMP Marketplace Providing Listing Request Form to request a listing in the FedRAMP Marketplace.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `MKT-IIP-AGU` Agency Use Cases  ⬜ No record

*MUST* — Providers MUST demonstrate that a cloud service offering is intended for one of the following use cases:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `MKT-IIP-DCP` Demonstrating Continuous Progress  ⬜ No record

*MUST* — Providers MUST demonstrate continuous progress towards a FedRAMP Certification, documented in their Trust Center or website and updated at least quarterly; progress is measured by the provider against documented goals and milestones.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `MKT-IIP-DLA` Deadline for Assessment  ⬜ No record

*MUST* — Providers MUST demonstrate that an assessment for a FedRAMP Certification Class B, C, or D has been scheduled within 2 years of initial listing in the Initial Implementation Phase.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### SCG — Secure Configuration Guide

#### `SCG-CSO-AUP` Use Instructions  ⬜ No record

*MUST* — Providers MUST include instructions in the FedRAMP Certification Package that explain how to obtain and use the Secure Configuration Guide.

**Artifacts required:** URL or explanation of how to request these materials.; Explanation of how the provider decides whether or not to share these materials or other related policies.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCG-CSO-PUB` Public Secure Configuration Guidance  ⬜ No record

*SHOULD* — Providers SHOULD make the Secure Configuration Guide available publicly.

**Artifacts required:** Explanation of how to access this information; or explanation why this functionality is not available

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCG-CSO-RSC` Recommended Secure Configuration  ⬜ No record

*MUST* — Providers MUST create, maintain, and make available recommendations for securely configuring their cloud services (the Secure Configuration Guide) that includes at least the following information:

**Artifacts required:** URL to the human-readable data.; URL to the machine-readable data.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCG-CSO-SDF` Secure Defaults  ⬜ No record

*SHOULD* — Providers SHOULD set all settings to their recommended secure defaults for top-level administrative accounts and privileged accounts when initially provisioned.

**Artifacts required:** Explanation of how to access this information; or explanation why this functionality is not available

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCG-ENH-API` API Capability  ⬜ No record

*SHOULD* — Providers SHOULD offer the capability to view and adjust security settings via an API or similar capability.

**Artifacts required:** Explanation of how to access this information; or explanation why this functionality is not available

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCG-ENH-CMP` Comparison Capability  ⬜ No record

*SHOULD* — Providers SHOULD offer the capability to compare all current settings for top-level administrative accounts and privileged accounts to the recommended secure defaults.

**Artifacts required:** Explanation of how to access this information; or explanation why this functionality is not available

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCG-ENH-EXP` Export Capability  ⬜ No record

*SHOULD* — Providers SHOULD offer the capability to export all security settings in a machine-readable format.

**Artifacts required:** Explanation of how to access this information; or explanation why this functionality is not available

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCG-ENH-MRG` Machine-Readable Guidance  ⬜ No record

*SHOULD* — Providers SHOULD also provide the Secure Configuration Guide in a machine-readable format that can be used by customers or third-party tools to compare against current settings.

**Artifacts required:** Explanation of how to access this information; or explanation why this functionality is not available

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCG-ENH-VRH` Versioning and Release History  ⬜ No record

*SHOULD* — Providers SHOULD provide versioning and a release history for recommended secure default settings for top-level administrative accounts and privileged accounts as they are adjusted over time.

**Artifacts required:** Explanation of how to access this information; or explanation why this functionality is not available

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### SCN — Significant Change Notification

#### `SCN-ADP-NTF` Notification Requirements  ⬜ No record

*MUST* — Providers MUST notify all necessary parties within 10 business days after finishing adaptive changes, also including the following information:

**Artifacts required:** At least the most recent SCN notification including the date it was sent and the date the change was applied. Additional examples may be provided. If no SCN notifications have been sent then this artifact is not required.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-CSO-ARI` Additional Relevant Information  ⬜ No record

*MAY* — Providers MAY include additional relevant information in Significant Change Notifications.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-CSO-EMG` Emergency Changes  ⬜ No record

*MAY* — Providers MAY execute significant changes (including transformative changes) during an emergency or incident without following the Significant Change Notification rules in advance. In such emergencies, providers MUST follow all relevant procedures, notify all necessary parties, retroactively provide all Significant Change Notification materials, and complete appropriate assessment after the incident.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-CSO-EVA` Evaluate Changes  ⬜ No record

*MUST* — Providers MUST evaluate all potential significant changes to determine the type of significant change and follow the appropriate Significant Change Notification rules.

**Artifacts required:** Evidence of significant change evaluation including a description fo the change, the determined type, and an explanation for the decision. At least one example must be provided for each type of change. Real examples are prefered but the provider may use fictitious examples as long as the example provides evidence of the decision making process.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-CSO-HIS` Historical Notifications  ⬜ No record

*MUST* — Providers MUST keep 12 months of historical Significant Change Notifications available with their FedRAMP Certification Data.

**Artifacts required:** Explanation of how FedRAMP can obtain this information.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-CSO-HRM` Human and Machine-Readable Notifications  ⬜ No record

*MUST* — Providers MUST make ALL Significant Change Notifications and related audit records available in human-readable and JSON formats.

**Artifacts required:** URL or explanation of how to request these materials.; Explanation of how the provider decides whether or not to share these materials or other related policies.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-CSO-INF` Required Information  ⬜ No record

*MUST* — Providers MUST include at least the following information in Significant Change Notifications:

**Artifacts required:** A recent Significant Change Notification or sample Significant Change Notification

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-CSO-MAR` Maintain Audit Records  ⬜ No record

*MUST* — Providers MUST maintain auditable records of the significant change evaluation activities required by SCN-CSO-EVA (Evaluate Changes) and make them available to FedRAMP as requested.

**Artifacts required:** Explanation of how FedRAMP can obtain this information.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-CSO-NOM` Notification Mechanisms  ⬜ No record

*MAY* — Providers MAY notify necessary parties in a variety of ways as long as the mechanism for notification is clearly documented in the FedRAMP Certification Package and easily accessible.

**Artifacts required:** Current list of available notification mechanisms

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-RTR-NNR` No Notification Requirements  ⬜ No record

*SHOULD NOT* — Providers SHOULD NOT make formal Significant Change Notifications for routine recurring changes; this type of change is exempted from notification requirements.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-TRF-NAF` Notification After Finishing  ⬜ No record

*MUST* — Providers MUST notify all necessary parties within 5 business days after finishing transformative changes, including updates to all previously sent information.

**Artifacts required:** At least the most recent post deployment SCN notification for a transformative change including the date it was sent and the date the change was applied. Additional examples may be provided. If no transformative SCN notifications have been sent then this artifact is not required.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-TRF-NAV` Notification After Verification  ⬜ No record

*MUST* — Providers MUST notify all necessary parties within 5 business days after completing the verification, assessment, and/or validation of transformative changes, also including the following information:

**Artifacts required:** At least the most recent after verification SCN notification for a transformative change including the date it was sent and the date the change was applied. Additional examples may be provided. If no transformative SCN notifications have been sent then this artifact is not required.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-TRF-NFP` Notification of Final Plans  ⬜ No record

*MUST* — Providers MUST notify all necessary parties of final plans for transformative changes at least 10 business days before starting transformative changes, including updates to all previously sent information.

**Artifacts required:** At least the most recent final SCN notification for a transformative change including the date it was sent and the date the change was applied. Additional examples may be provided. If no transformative SCN notifications have been sent then this artifact is not required.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-TRF-NIP` Notification of Initial Plans  ⬜ No record

*MUST* — Providers MUST notify all necessary parties of initial plans for transformative changes at least 30 business days before starting transformative changes, including a summary of any likely security impacts or changes in risk.

**Artifacts required:** At least the most recent initial SCN notification for a transformative change including the date it was sent and the date the change was applied. Additional examples may be provided. If no transformative SCN notifications have been sent then this artifact is not required.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-TRF-TPR` Third-Party Review  ⬜ No record

*SHOULD* — Providers SHOULD engage a third-party assessor to review the scope and impact of the planned change before starting transformative changes if human validation is necessary; such reviews SHOULD be limited to security decisions that require human validation.

**Artifacts required:** Third Party assesment report OR explanation why a third party assessor was not engaged

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SCN-TRF-UPD` Update Documentation  ⬜ No record

*MUST* — Providers MUST publish updated service documentation and other materials to reflect transformative changes within 30 business days after finishing transformative changes.

**Artifacts required:** Date of the most recent transformative change and the date of the corresponding documentation update. If no documentation updates were required as the result of this change, explain how this was determined.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### SDR — Security Decision Record

#### `SDR-CSO-FRR` FedRAMP Rules  ⬜ No record

*MUST* — Providers MUST supply a Security Decision Record, in both human-readable and JSON formats, that includes at least all of the following information for each applicable FedRAMP rule:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SDR-CSO-MTD` Security Decision Record Metadata  ⬜ No record

*MUST* — Providers MUST also include the following basic metadata in their Security Decision Record:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SDR-CSX-KMT` Key Security Indicator Metrics  ⬜ No record

*MUST* — Providers with 20x Class C Certifications MUST also include historical metrics in their Security Decision Record, supplying at least the following information for each applicable Key Security Indicator:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `SDR-CSX-KSI` Key Security Indicators  ⬜ No record

*MUST* — Providers MUST also include short and simple high-level summaries of at least the following for each applicable Key Security Indicator:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### VDR — Vulnerability Detection and Response

#### `VDR-CSO-ADT` Automate Detection  ⬜ No record

*SHOULD* — Providers SHOULD use automated services to improve and streamline vulnerability detection and response.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-CSO-AKE` Avoid KEVs  ⬜ No record

*SHOULD NOT* — Providers SHOULD NOT deploy or otherwise activate new machine-based information resources with Known Exploited Vulnerabilities.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-CSO-DAC` Detect After Changes  ⬜ No record

*SHOULD* — Providers SHOULD automatically perform vulnerability detection on representative samples of new or significantly changed information resources.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-CSO-DET` Vulnerability Detection  ⬜ No record

*MUST* — Providers MUST systematically, persistently, and promptly discover and identify vulnerabilities within their cloud service offering using appropriate techniques such as assessment, scanning, threat intelligence, vulnerability disclosure mechanisms, bug bounties, penetration testing, incident response, automated control testing, supply chain monitoring, and other relevant capabilities; this process is called vulnerability detection. Vulnerability detection includes persistently verifying and validating that information resources and processes are operating as intended and documented for FedRAMP Practices.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-CSO-DFR` Design For Resilience  ⬜ No record

*SHOULD* — Providers SHOULD make design and architecture decisions for their cloud service offering that mitigate the risk of vulnerabilities by default AND decrease the risk and complexity of vulnerability detection and response.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-CSO-FAV` Failures Are Vulnerabilities  ⬜ No record

*MUST* — Providers MUST treat problems or failures with their vulnerability detection and response processes as vulnerabilities.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-CSO-MSP` Maintain Security  ⬜ No record

*SHOULD NOT* — Providers SHOULD NOT weaken the security of information resources to facilitate vulnerability scanning, detection, or assessment activities.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-CSO-RES` Vulnerability Response  ⬜ No record

*MUST* — Providers MUST systematically, persistently, and promptly track, evaluate, monitor, mitigate, remediate, assess exploitation of, report, and otherwise manage all detected vulnerabilities within their cloud service offering; this process is called vulnerability response.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-CSO-SIR` Sampling  ⬜ No record

*MAY* — Providers MAY sample effectively identical information resources, especially machine-based information resources, when performing vulnerability detection UNLESS doing so would decrease the efficiency or effectiveness of vulnerability detection.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-TFR-KEV` Remediate KEVs  ⬜ No record

*SHOULD* — Providers SHOULD remediate Known Exploited Vulnerabilities according to the due dates in the CISA Known Exploited Vulnerabilities Catalog (even if the vulnerability has been fully mitigated) as required by CISA Binding Operational Directive (BOD) 26-04 or any successor guidance from CISA.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-TFR-MVX` Persistent Machine Verification and Validation for 20x  ⬜ No record

*MUST* — Providers of FedRAMP 20x Class C offerings MUST verify and validate the status of machine-based information resources at least once every 3 days.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-TFR-NMV` Non-Machine Verification and Validation  ⬜ No record

*MUST* — Providers MUST verify and validate the status of non-machine-based information resources at least once every 3 months.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-TFR-PCD` Persistently Complete Detection  ⬜ No record

*SHOULD* — Providers with Class C Certifications SHOULD persistently perform vulnerability detection on all information resources that are NOT likely to drift, at least once every month.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-TFR-PDD` Persistent Drift Detection  ⬜ No record

*SHOULD* — Providers with Class C Certifications SHOULD persistently perform vulnerability detection on all information resources that are likely to drift, at least once every 14 days.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-TFR-PSD` Persistent Sample Detection  ⬜ No record

*SHOULD* — Providers with Class C Certifications SHOULD persistently perform vulnerability detection on representative samples of similar machine-based information resources, at least once every 3 days.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-TFR-PVR` Mitigation and Remediation Expectations  ⬜ No record

*SHOULD* — Providers with Class C Certifications SHOULD partially mitigate vulnerabilities, fully mitigate vulnerabilities, or remediate vulnerabilities to a lower Potential Agency Impact N-rating within the timeframes from evaluation shown below, factoring for the current Potential Agency Impact N-rating as defined in VER-EVA-EPA (Estimate Potential Agency Impact), internet reachability, and likely exploitability:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VDR-TFR-RMN` Remaining Vulnerabilities  ⬜ No record

*SHOULD* — Providers SHOULD mitigate or remediate remaining vulnerabilities during routine operations as determined necessary by the provider.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

### VER — Vulnerability Evaluation and Reporting

#### `VER-EVA-AIA` Assume It's Automatable  ⬜ No record

*MUST* — Providers MUST assume the exploitation of vulnerabilities can be automated UNLESS they have evidence proving otherwise.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-EVA-EFA` Evaluation Factors  ⬜ No record

*SHOULD* — Providers SHOULD consider at least the following factors when considering the context of the cloud service offering to evaluate detected vulnerabilities:

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-EVA-EFP` Evaluate False Positives  ⬜ No record

*SHOULD* — Providers SHOULD evaluate detected vulnerabilities, considering the context of the cloud service offering, to determine if they are false positive vulnerabilities.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-EVA-EIR` Evaluate Internet-Reachability  ⬜ No record

*MUST* — Providers MUST evaluate detected vulnerabilities, considering the context of the cloud service offering, to determine if they are internet-reachable vulnerabilities.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-EVA-ELX` Evaluate Exploitability  ⬜ No record

*MUST* — Providers MUST evaluate detected vulnerabilities, considering the context of the cloud service offering, to determine if they are likely exploitable vulnerabilities.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-EVA-EPA` Estimate Potential Agency Impact  ⬜ No record

*MUST* — Providers MUST evaluate detected vulnerabilities, considering the context of the cloud service offering, to estimate the potential agency impact of exploitation on government customers AND assign one of the following Potential Agency Impact N-ratings (PAIN):

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-EVA-GRV` Group Vulnerabilities  ⬜ No record

*SHOULD* — Providers SHOULD evaluate detected vulnerabilities, considering the context of the cloud service offering, to identify logical groupings of affected information resources that may improve the efficiency and effectiveness of vulnerability response by consolidating further activity; FedRAMP Vulnerability Detection and Response rules are then applied to these consolidated groupings of vulnerabilities instead of each individual detected instance.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-RPT-AVI` Accepted Vulnerability Info  ⬜ No record

*MUST* — Providers MUST include the following information on accepted vulnerabilities when reporting on vulnerability detection and response activity:

**Artifacts required:** A recent vulnerability report or a sample vulnerability report

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-RPT-HLO` High-Level Overviews  ⬜ No record

*SHOULD* — Providers SHOULD include high-level overviews of ALL vulnerability detection and response activities conducted during this period for the cloud service offering; this includes vulnerability disclosure programs, bug bounty programs, penetration testing, assessments, etc.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-RPT-NID` Responsible Disclosure  ⬜ No record

*MUST NOT* — Providers MUST NOT irresponsibly disclose specific sensitive information about vulnerabilities that would likely lead to exploitation, but MUST disclose sufficient information for informed risk-based decision-making to all necessary parties.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-RPT-PER` Persistent Reporting  ⬜ No record

*MUST* — Providers MUST report vulnerability detection and response activity (including persistent verification and validation) to all necessary parties persistently, summarizing ALL activity since the previous report; these reports are FedRAMP Certification Data and are subject to FedRAMP Certification Data Sharing rules.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-RPT-RPD` Responsible Public Disclosure  ⬜ No record

*MAY* — Providers MAY responsibly disclose vulnerabilities publicly or with other parties if the provider determines doing so will NOT likely lead to exploitation.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-RPT-VDT` Vulnerability Details  ⬜ No record

*MUST* — Providers MUST include the following information (if applicable) on detected vulnerabilities when reporting on vulnerability detection and response activity, UNLESS it is an accepted vulnerability:

**Artifacts required:** A recent vulnerability report or a sample vulnerability report

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-TFR-EVU` Evaluate Vulnerabilities Quickly  ⬜ No record

*SHOULD* — Providers with Class C Certifications SHOULD evaluate ALL vulnerabilities as required by VER-EVA (Evaluation) within 5 days of detection.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-TFR-IRI` Internet-Reachable Incidents  ⬜ No record

*SHOULD* — Providers with Class C Certifications SHOULD treat internet-reachable likely exploitable vulnerabilities where Potential Agency Impact N-rating > 3 as a FedRAMP Reportable Incident until they are partially mitigated vulnerabilities at N3 or below.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-TFR-MAV` Mark Accepted Vulnerabilities  ⬜ No record

*MUST* — Providers MUST categorize any vulnerability that is not or will not be fully mitigated or remediated within 192 days of evaluation as an accepted vulnerability.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-TFR-MHR` Monthly Activity Report  ⬜ No record

*MUST* — Providers MUST report vulnerability detection and response activity to all necessary parties in a consistent format that is human readable at least monthly.

**Artifacts required:** A recent vulnerability report or a sample vulnerability report

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-TFR-MRH` Historical Activity  ⬜ No record

*SHOULD* — Providers with Class C Certifications SHOULD make all recent historical vulnerability detection and response activity available in JSON format for automated retrieval by all necessary parties (e.g. using an API service or similar); this information SHOULD be updated persistently, at least once every 14 days.

**Artifacts required:** URL and access instructions for historical vulnerability detection and response activity in machine readable format; or an explanation of why machine readable content is not being provided

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

#### `VER-TFR-NRI` Non-Internet-Reachable Incidents  ⬜ No record

*MAY* — Providers with Class C Certifications MAY treat likely exploitable vulnerabilities that are NOT internet-reachable where Potential Agency Impact N-rating = 5 as a FedRAMP Reportable Incident until they are partially mitigated vulnerabilities at N4 or below.

_No authored record for this rule._


> **Open findings:**
> - 🔴 BLOCKING: frrImplementation is empty (schema-required)

---

## Key Security Indicators

### CED — Cybersecurity Education

#### `KSI-CED-RAT` Reviewing All Training  🔴 Not Implemented

The effectiveness of relevant cybersecurity education and training is persistently reviewed, including at least general training for all employees, role-specific training for employees in high risk roles, training for development and engineering staff on secure software delivery, and training for staff involved with incident response or disaster recovery.

**Controls:** CP-3, IR-2, PS-6, AT-2, AT-2.2, AT-2.3, AT-3.5, AT-4, IR-2.3, AT-3, SR-11.1

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### CMT — Change Management

#### `KSI-CMT-LMC` Logging Changes  🔴 Not Implemented

Modifications to the cloud service offering are logged and monitored.

**Controls:** AU-2, CM-3, CM-3.2, CM-4.2, CM-6, CM-8.3, MA-2

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CMT-RMV` Redeploying vs Modifying  🔴 Not Implemented

Changes to machine-based information resources are executed through the redeployment of version controlled resources rather than direct modification wherever reasonable.

**Controls:** CM-2, CM-3, CM-5, CM-6, CM-7, CM-8.1, SI-3

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CMT-RVP` Reviewing Change Procedures  🔴 Not Implemented

The effectiveness of documented change management procedures is persistently reviewed.

**Controls:** CM-3, CM-3.2, CM-3.4, CM-5, CM-7.1, CM-9

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CMT-VTD` Validating Throughout Deployment  🔴 Not Implemented

Persistent testing and validation of changes throughout deployment is automated.

**Controls:** CM-3, CM-3.2, CM-4.2, SI-2

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### CNA — Cloud Native Architecture

#### `KSI-CNA-DFP` Defining Functionality and Privileges  🔴 Not Implemented

The functionality and privileges for infrastructure and services are strictly defined.

**Controls:** CM-2, SI-3

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CNA-EIS` Enforcing Intended State  🔴 Not Implemented

Automated services are used to persistently assess the security of all machine-based information resources and automatically enforce their intended operational state.

**Controls:** CA-2.1, CA-7.1

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CNA-IBP` Implementing Best Practices  🔴 Not Implemented

The use and configuration of third-party machine-based information resources is persistently compared against the original provider's best practices and guidance.

**Controls:** AC-17.3, CM-2, PL-10

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CNA-MAT` Minimizing Attack Surface  🔴 Not Implemented

Machine-based information resources are persistently reviewed to ensure they have a minimal attack surface and that lateral movement is minimized if compromised.

**Controls:** AC-17.3, AC-18.1, AC-18.3, AC-20.1, CA-9, SC-7.3, SC-7.4, SC-7.5, SC-7.8, SC-8, SC-10, SI-10, SI-11, SI-16

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CNA-OFA` Optimizing for Availability  🔴 Not Implemented

Machine-based information resources are persistently reviewed to ensure they are appropriately optimized for high availability and rapid recovery.

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CNA-RNT` Restricting Network Traffic  🔴 Not Implemented

Machine-based information resources are persistently reviewed to ensure they are appropriately configured to limit inbound and outbound network traffic.

**Controls:** AC-17.3, CA-9, CM-7.1, SC-7.5, SI-8

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CNA-RVP` Reviewing Protections  🔴 Not Implemented

The effectiveness of protection against denial of service attacks and other unwanted activity for machine-based information resources is persistently reviewed.

**Controls:** SC-5, SI-8, SI-8.2

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-CNA-ULN` Using Logical Networking  🔴 Not Implemented

Logical networking and related capabilities are used and persistently reviewed to enforce traffic flow controls.

**Controls:** AC-12, AC-17.3, CA-9, SC-4, SC-7, SC-7.7, SC-8, SC-10

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### IAM — Identity and Access Management

#### `KSI-IAM-AAM` Automating Account Management  🔴 Not Implemented

The lifecycle and privileges of all accounts, roles, and groups are securely managed using automation.

**Controls:** AC-2.2, AC-2.3, AC-2.13, AC-6.7, IA-4.4, IA-12, IA-12.2, IA-12.3, IA-12.5

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-IAM-APM` Adopting Passwordless Methods  🔴 Not Implemented

Secure passwordless methods are used for user authentication and authorization when feasible, otherwise strong passwords with phishing-resistant MFA is used.

**Controls:** AC-3, IA-5.1, IA-5.2, IA-5.6, IA-6, AC-2, IA-2, IA-2.1, IA-2.2, IA-2.8, IA-5, IA-8, SC-23

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-IAM-ELP` Ensuring Least Privilege  🔴 Not Implemented

Identity and access management measures are used and persistently reviewed to ensure each user or device can only access the resources they need.

**Controls:** AC-2.5, AC-2.6, AC-3, AC-4, AC-6, AC-12, AC-14, AC-17, AC-17.1, AC-17.2, AC-17.3, AC-20, AC-20.1, CM-2.7, CM-9, IA-2, IA-3, IA-4, IA-4.4, IA-5.2, IA-5.6, IA-11, PS-2, PS-3, PS-4, PS-5, PS-6, SC-4, SC-20, SC-21, SC-22, SC-23, SC-39, SI-3

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-IAM-JIT` Authorizing Just-in-Time  🔴 Not Implemented

A least-privileged, role and attribute-based, and just-in-time security authorization model is used and persistently reviewed for all user and non-user accounts and services.

**Controls:** AC-2, AC-2.1, AC-2.2, AC-2.3, AC-2.4, AC-2.6, AC-3, AC-4, AC-5, AC-6, AC-6.1, AC-6.2, AC-6.5, AC-6.7, AC-6.9, AC-6.10, AC-7, AC-20.1, AC-17, AU-9.4, CM-5, CM-7, CM-7.2, CM-7.5, CM-9, IA-4, IA-4.4, IA-7, PS-2, PS-3, PS-4, PS-5, PS-6, PS-9, RA-5.5, SC-2, SC-23, SC-39

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-IAM-SNU` Securing Non-User Authentication  🔴 Not Implemented

Appropriately secure authentication methods are used and persistently reviewed for non-user accounts and services.

**Controls:** AC-2, AC-2.2, AC-4, AC-6.5, IA-3, IA-5.2, RA-5.5

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-IAM-SUS` Responding to Suspicious Activity  🔴 Not Implemented

Accounts with privileged access are disabled or otherwise secured in response to suspicious activity.

**Controls:** AC-2, AC-2.1, AC-2.3, AC-2.13, AC-7, PS-4, PS-8

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### INR — Incident Response

#### `KSI-INR-AAR` Generating After Action Reports  🔴 Not Implemented

Incident after action reports are generated and lessons learned are persistently incorporated.

**Controls:** IR-3, IR-4, IR-4.1, IR-8

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-INR-RIR` Reviewing Incident Response Procedures  🔴 Not Implemented

The effectiveness of documented incident response procedures is persistently reviewed.

**Controls:** IR-4, IR-4.1, IR-6, IR-6.1, IR-6.3, IR-7, IR-7.1, IR-8, IR-8.1, SI-4.5

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-INR-RPI` Reviewing Past Incidents  🔴 Not Implemented

Past incidents are persistently reviewed for patterns or vulnerabilities that were not previously apparent or identified.

**Controls:** IR-3, IR-4, IR-4.1, IR-5, IR-8

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### MLA — Monitoring, Logging, and Auditing

#### `KSI-MLA-ALA` Authorizing Log Access  🔴 Not Implemented

A least-privileged, role and attribute-based, and just-in-time access authorization model is used and persistently reviewed for access to log data based on organizationally defined data sensitivity.

**Controls:** SI-11

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-MLA-EVC` Evaluating Configurations  🔴 Not Implemented

The configuration of machine-based information resources, especially infrastructure as code, is persistently evaluated and tested.

**Controls:** CA-7, CM-2, CM-6, SI-7.7

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-MLA-LET` Logging Event Types  🔴 Not Implemented

A list of information resources and event types that will be logged, monitored, and audited is maintained and persistently reviewed to ensure these activities occur.

**Controls:** AC-2.4, AC-6.9, AC-17.1, AC-20.1, AU-2, AU-7.1, AU-12, SI-4.4, SI-4.5, SI-7.7

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-MLA-OSM` Operating SIEM Capability  🔴 Not Implemented

A Security Information and Event Management (SIEM) or similar system(s) is used and persistently reviewed for centralized, tamper-resistant logging of events, activities, and changes.

**Controls:** AC-17.1, AC-20.1, AU-2, AU-3, AU-3.1, AU-4, AU-5, AU-6.1, AU-6.3, AU-7, AU-7.1, AU-8, AU-9, AU-11, IR-4.1, SI-4.2, SI-4.4, SI-7.7

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-MLA-RVL` Reviewing Logs  🔴 Not Implemented

Logs are persistently reviewed and audited.

**Controls:** AC-2.4, AC-6.9, AU-2, AU-6, AU-6.1, SI-4, SI-4.4

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### PIY — Policy and Inventory

#### `KSI-PIY-GIV` Generating Inventories  🔴 Not Implemented

Authoritative sources are used to automatically generate real-time inventories of all information resources when needed.

**Controls:** CM-2.2, CM-7.5, CM-8, CM-8.1, CM-12, CM-12.1, CP-2.8

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-PIY-RES` Reviewing Executive Support  🔴 Not Implemented

Executive support for achieving the provider's security goals is persistently reviewed and demonstrated.

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-PIY-RIS` Reviewing Investments in Security  🔴 Not Implemented

The effectiveness of the provider's investments in achieving security goals is persistently reviewed.

**Controls:** AC-5, CA-2, CP-2.1, CP-4.1, IR-3.2, PM-3, SA-2, SA-3, SR-2.1

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-PIY-RSD` Reviewing Security in the SDLC  🔴 Not Implemented

The effectiveness of building security and privacy considerations into the Software Development Lifecycle and aligning with CISA Secure By Design principles is persistently reviewed.

**Controls:** AC-5, AU-3.3, CM-3.4, PL-8, PM-7, SA-3, SA-8, SC-4, SC-18, SI-10, SI-11, SI-16

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-PIY-RVD` Reviewing Vulnerability Disclosures  🔴 Not Implemented

The effectiveness of the provider's vulnerability disclosure program is persistently reviewed.

**Controls:** RA-5.11

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### RPL — Recovery Planning

#### `KSI-RPL-ABO` Aligning Backups with Objectives  🔴 Not Implemented

The alignment of machine-based information resource backups with defined recovery objectives is persistently reviewed.

**Controls:** CM-2.3, CP-6, CP-9, CP-10, CP-10.2, SI-12

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-RPL-ARP` Aligning Recovery Plan  🔴 Not Implemented

The alignment of recovery plans with defined recovery objectives is persistently reviewed.

**Controls:** CP-2, CP-2.1, CP-2.3, CP-4.1, CP-6, CP-6.1, CP-6.3, CP-7, CP-7.1, CP-7.2, CP-7.3, CP-8, CP-8.1, CP-8.2, CP-10, CP-10.2

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-RPL-RRO` Reviewing Recovery Objectives  🔴 Not Implemented

The desired Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) are defined and persistently reviewed for alignment with the provider's business needs and capabilities.

**Controls:** CP-2.3, CP-10

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-RPL-TRC` Testing Recovery Capabilities  🔴 Not Implemented

The capability to recover from incidents and contingencies aligned with defined recovery objectives is persistently tested.

**Controls:** CP-2.1, CP-2.3, CP-4, CP-4.1, CP-6, CP-6.1, CP-9.1, CP-10, IR-3, IR-3.2

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### SCR — Supply Chain Risk

#### `KSI-SCR-MIT` Mitigating Supply Chain Risk  🔴 Not Implemented

Persistently identify, review, and mitigate potential supply chain risks.

**Controls:** AC-20, RA-3.1, SA-9, SA-10, SA-11, SA-15.3, SA-22, SI-7.1, SR-5, SR-6, CA-7.4, SC-18

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-SCR-MON` Monitoring Supply Chain Risk  🔴 Not Implemented

Third party software information resources are automatically monitored for upstream vulnerabilities using mechanisms that may include contractual notification requirements or active monitoring services.

**Controls:** AC-20, CA-3, IR-6.3, PS-7, RA-5, SA-9, SI-5, SR-5, SR-6, SR-8

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

### SVC — Service Configuration

#### `KSI-SVC-ACM` Automating Configuration Management  🔴 Not Implemented

The configuration of machine-based information resources is managed using automation and persistently reviewed for drift.

**Controls:** AC-2.4, CM-2, CM-2.2, CM-2.3, CM-6, CM-7.1, PL-9, PL-10, SA-5, SI-5, SR-10

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-SVC-ASM` Automating Secret Management  🔴 Not Implemented

Management, protection, and regular rotation of digital keys, certificates, and other secrets is automated and persistently reviewed.

**Controls:** AC-17.2, IA-5.2, IA-5.6, SC-12, SC-17

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-SVC-EIS` Evaluating and Improving Security  🔴 Not Implemented

Information resources are persistently evaluated for opportunities to improve security and those improvements are persistently made.

**Controls:** CM-7.1, CM-12.1, MA-2, PL-8, SC-7, SC-39, SI-2.2, SI-4, SR-10

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-SVC-PRR` Preventing Residual Risk  🔴 Not Implemented

Plans, procedures, and the state of information resources are persistently reviewed after making changes to limit and remove unwanted residual elements that would likely negatively affect the confidentiality, integrity, or availability of federal customer data.

**Controls:** SC-4

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-SVC-RUD` Removing Unwanted Data  🔴 Not Implemented

Unwanted federal customer data is removed promptly when requested by an agency in alignment with customer agreements, including from backups if appropriate; this typically applies when a customer spills information or when a customer seeks to remove information from a service due to a change in usage.

**Controls:** SI-12.3, SI-18.4

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-SVC-SIN` Securing Information  🔴 Not Implemented

Information is encrypted or otherwise secured from unwanted access or modification.

**Controls:** AC-1, AC-17.2, CP-9.8, SC-8, SC-8.1, SC-13, SC-20, SC-21, SC-22, SC-23, SC-28, SC-28.1

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-SVC-VCM` Validating Communications  🔴 Not Implemented

The authenticity and integrity of communications between machine-based information resources is persistently validated using automation.

**Controls:** SC-23, SI-7.1

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---

#### `KSI-SVC-VRI` Validating Resource Integrity  🔴 Not Implemented

Use cryptographic methods to validate the integrity of machine-based information resources.

**Controls:** CM-2.2, CM-8.3, SC-13, SC-23, SI-7, SI-7.1, SR-10

**Implementation**
_none recorded_

**Internal validation**
_none recorded_

**Independent assessment**
_none recorded_

**Automated methods** (class requires 2):
_none recorded_

**Evidence**

_no evidence attached_


> **Open findings:**
> - 🔴 BLOCKING: ksiImplementation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiValidation is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiAssessment is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiTests is empty (schema-required for KSIs)
> - 🔴 BLOCKING: ksiEvidence is empty (schema-required for KSIs)
> - 🔴 BLOCKING: 0 automated method(s); class c requires 2 per FRC-CSX-VVK

---
