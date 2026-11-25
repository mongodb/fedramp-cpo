---
# Certification Package Overview (CPO) source of truth. Started from cpo/template.md.
# Frontmatter keys mirror the official FedRAMP CPO JSON schema
# (schema/fedramp-certification-package-overview-schema-2026-06-24.json).
# The Markdown body below the frontmatter becomes serviceIdentification.serviceDescription.
#
# Fields marked (required) must be present for the build to pass; everything
# else is optional and may be deleted or left blank.
# Replace every EXAMPLE value before publishing.

# --- CPO-CSO-MTD: package metadata -------------------------------------------
# "Date and time of last update" and "source of update" are generated at build
# time from git (commit date and SHA); you only maintain the fields below.
metadata:                          # (required) CPO-CSO-MTD
  version: "0.1.0"
  responsibleOfficial:
    name: Valentina Poghosyan
    title: Chief Compliance Officer
    email: valentina.poghosyan@mongodb.com
    phone: "+1-555-555-0100"

serviceIdentification:               # (required)
  fedRampPackageId: FR2122150307     # (required) FedRAMP ID, or provider name + acronym if none
  ueiNumber: ""                      # SAM.gov UEI; leave blank if none
  providerName: MongoDB, Inc.
  serviceName: Atlas for Government
  serviceAcronym: A4G
  certificationType: Rev5             # 20x | Rev5
  website: https://www.mongodb.com/products/platform/atlas-for-government
  logo: https://raw.githubusercontent.com/mongodb/fedramp-cpo/refs/heads/main/MDB-A4G-Logo.png   # must end in png/jpg/gif/svg/webp/ico/bmp/tiff

serviceProperties:                    # (required)
  serviceType: [PaaS]                # (required) SaaS | PaaS | IaaS
  deploymentModel: Government Community Cloud      # (required) Public Cloud | Government-Only Cloud | Hybrid Cloud | Community Cloud | Government Community Cloud
  businessCategory:                  # 1-10 values from the schema enum
    - Data Management
    - Analytics
    - Storage
  trustCenter:
    repositoryType: [Trust Center]
    url: https://trust.mongodb.com/
    repositoryDescription: Public trust center with policies and compliance reports.
    authenticationRequired: true
    accessRequestInstructions: You must have a MongoDB Atlas for Government (A4G) account to request access or have been invited to our trust portal to access FedRAMP package details. Please contact fedramp@mongodb.com if you need access.
  secureConfigurationGuidance:
    repositoryType: [Secure Configuration Guidance]
    url: https://www.mongodb.com/docs/atlas/government/security/
    repositoryDescription: Secure configuration guide for agency customers.
    authenticationRequired: false
    accessRequestInstructions: Email fedramp@mongodb.com to request access.
  nextOngoingCertificationReportDate: 2027-01-01

# Must include at least one Security and one Sales contact (CDS-CSO-PUB).
contactInformation:                  # (required)
  - contactType: Security
    contactName: Security Team
    contactEmail: security@mongodb.com
    contactPhone: "+1-866-237-8815"
  - contactType: Sales
    contactName: Gov Sales
    contactEmail: fedramp@mongodb.com
    contactPhone: "+1-866-237-8815"

assessor:
  name: Schellman Compliance, LLC
  assessorID: "136571"               # six digits

certifiedServices:
  - serviceName: MongoDB Atlas
    serviceDescription: Core platform included in the certification boundary.
    dateAvailable: 2026-07-04

thirdPartyInformationResources:
  certified:
    - fedRampCertifiedThirdPartyInformationResource: AWS GovCloud
      useCase: Hosts production MongoDB database clusters (Class D/High impact level)
    - fedRampCertifiedThirdPartyInformationResource: AWS US East/West
      useCase: Hosts production MongoDB database clusters (Class C/Moderate impact level)
    - fedRampCertifiedThirdPartyInformationResource: Azure Government (includes Dynamics 365)
      useCase: Hosts production MongoDB database clusters (Class D/High impact level)
    - fedRampCertifiedThirdPartyInformationResource: Google Services (Google Cloud Platform Products and underlying Infrastructure)
      useCase: Hosts production MongoDB database clusters (Class D/High impact level)
    - fedRampCertifiedThirdPartyInformationResource: Okta IDaaS Regulated Cloud
      useCase: Customer authentication and sign-in
    - fedRampCertifiedThirdPartyInformationResource: Salesforce Government Cloud Plus
      useCase: Customer support ticketing
    - fedRampCertifiedThirdPartyInformationResource: Slack
      useCase: Customer support and internal operations
    - fedRampCertifiedThirdPartyInformationResource: Google Workspace
      useCase: Internal operations
    - fedRampCertifiedThirdPartyInformationResource: GitHub Enterprise Cloud
      useCase: Software source code
    - fedRampCertifiedThirdPartyInformationResource: PagerDuty Operations Cloud
      useCase: On-call alerting
  nonCertified:
    - name: Let's Encrypt
      provider: Internet Security Research Group
      website: https://letsencrypt.org/
      useCase: Trusted TLS certificates
    - name: Sentry
      provider: Functional Software, Inc.
      website: https://sentry.io/
      useCase: Stack trace and error debugging
    - name: SAP SuccessFactors
      provider: SAP SE
      website: https://www.sap.com/products/hcm.html
      useCase: Internal human resources operations
---

MongoDB Atlas for Government is a fully managed Platform as a Service (PaaS) trusted by U.S. federal, state, and local governments, including Criminal Justice Information Solutions (CJIS) applications, and the Independent Software Vendors (ISVs) that support them. Atlas for Government provisions, operates, monitors, backs up, and scales MongoDB database clusters on the customer’s behalf in a secure, scalable environment.

Atlas for Government integrates a suite of data and application services under a unified customer experience to provision and manage clusters through a simplified user interface. The services within the FedRAMP authorization boundary include Managed MongoDB database clusters, Atlas Search, time series collections, backup and restore, monitoring and alerting, and the Atlas UI, Administration API, and CLI. Altogether these services support transactional workloads, time series data, search, and petabyte-scale data storage.

Data is encrypted in transit using TLS and at rest using FIPS 140-validated encryption, with support for customer-managed keys. MongoDB supports Client-Side Field Level Encryption and Queryable Encryption, which encrypt sensitive fields in customer applications before reaching Atlas for Government. Customer database clusters are deployed in AWS GovCloud (US) regions, AWS U.S. East/West regions, GCP Assured Workloads U.S. regions, and now Microsoft Azure Government for a truly multi-cloud management platform.