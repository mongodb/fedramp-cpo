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
    name: Jane Example
    title: Chief Information Security Officer
    email: jane.example@example.com
    phone: "+1-555-555-0100"

serviceIdentification:               # (required)
  fedRampPackageId: EXAMPLE-0000     # (required) FedRAMP ID, or provider name + acronym if none
  ueiNumber: ""                      # SAM.gov UEI; leave blank if none
  providerName: Example Corp
  serviceName: Example Cloud Platform
  serviceAcronym: ECP
  certificationType: 20x             # 20x | Rev5
  website: https://www.example.com/ecp
  logo: https://www.example.com/logo.svg   # must end in png/jpg/gif/svg/webp/ico/bmp/tiff

serviceProperties:                    # (required)
  serviceType: [SaaS]                # (required) SaaS | PaaS | IaaS
  deploymentModel: Public Cloud      # (required) Public Cloud | Government-Only Cloud | Hybrid Cloud | Community Cloud | Government Community Cloud
  businessCategory:                  # 1-10 values from the schema enum
    - Data Management
  trustCenter:
    repositoryType: [Trust Center]
    url: https://trust.example.com
    repositoryDescription: Public trust center with policies and compliance reports.
    authenticationRequired: false
  secureConfigurationGuidance:
    repositoryType: [Secure Configuration Guidance]
    url: https://docs.example.com/secure-config
    repositoryDescription: Secure configuration guide for agency customers.
    authenticationRequired: true
    accessRequestInstructions: Email fedramp@example.com to request access.
  nextOngoingCertificationReportDate: 2027-01-01

# Must include at least one Security and one Sales contact (CDS-CSO-PUB).
contactInformation:                  # (required)
  - contactType: Security
    contactName: Security Team
    contactEmail: security@example.com
    contactPhone: "+1-555-555-0101"
  - contactType: Sales
    contactName: Gov Sales
    contactEmail: gov-sales@example.com
    contactPhone: "+1-555-555-0102"

assessor:
  name: Example Assessor LLC
  assessorID: "123456"               # six digits

advisors:
  - name: Example Advisory Group

certifiedServices:
  - serviceName: Example Core
    serviceDescription: Core platform included in the certification boundary.
    dateAvailable: 2026-07-04

thirdPartyInformationResources:
  certified:
    - fedRampCertifiedThirdPartyInformationResource: Example IaaS Provider
      useCase: Hosts production workloads.
  nonCertified:
    - name: Example Email Service
      provider: Example Mail Inc.
      website: https://mail.example.com
      useCase: Sends transactional notifications; no federal data stored.
---

Example Cloud Platform is a SaaS offering that ... (EXAMPLE). Write the service
description here in plain Markdown. Everything below the frontmatter is published
as `serviceDescription`.
