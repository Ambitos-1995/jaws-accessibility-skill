# Spanish & European Accessibility Legislation

Last reviewed: 2026-08-31

## TOC

1. Scope and disclaimer
2. European Accessibility Act (EAA)
3. EN 301 549 — Harmonized standard
4. Spain: Ley 11/2023 (private sector)
5. Spain: RD 1112/2018 (public sector)
6. Spain: RD 193/2023 (goods and services offered to the public)
7. Practical scope and compliance roadmap
8. Official sources

---

## 1. Scope and disclaimer

This file provides implementation-oriented compliance context for digital accessibility. It is not legal advice. Always validate final legal interpretations with qualified counsel.

---

## 2. European Accessibility Act (EAA) — Directive (EU) 2019/882

The EAA harmonizes accessibility requirements across all EU member states.

### Scope
- **Products**: Computers, smartphones, tablets, self-service terminals (ATMs, ticketing machines, check-in kiosks), e-readers, consumer equipment for electronic communications.
- **Services**: Electronic communications, audiovisual media services, e-commerce, banking, e-books, transport passenger services (websites, apps, ticketing).

### Key dates
| Date | Milestone |
|---|---|
| June 2019 | EAA adopted (Directive 2019/882) |
| June 2022 | Transposition deadline for member states |
| June 28, 2025 | **Enforcement begins** — products and services must comply |
| June 2030 | Transition period ends for service contracts signed before June 2025 |

### Exemptions
- **Microenterprises** (fewer than 10 persons AND annual turnover **or** annual balance-sheet total not exceeding EUR 2 million) providing **services** are exempt. Microenterprises providing **products** are NOT exempt.
- **Disproportionate burden**: Organizations may claim exemption if compliance would impose a disproportionate burden, but must document the assessment, notify the competent authority, and review every 5 years or upon request.

### Technical standards and presumption of conformity
The EAA provides a presumption of conformity only for the requirements covered by a harmonized standard or technical specification whose reference has been published for that legislation in the Official Journal of the European Union. As of this review, do **not** claim that EN 301 549 V3.2.1 creates an EAA presumption of conformity merely because it is harmonized for the separate Web Accessibility Directive.

Operational guidance:
- Validate if the product/service is in EAA scope first.
- Then verify national transposition details (Spain: Ley 11/2023).

---

## 3. EN 301 549 — Standard and harmonization status

EN 301 549 provides testable accessibility requirements for ICT products and services. Its legal effect depends on the legislation and the version referenced in the Official Journal; one harmonization decision does not automatically carry across to another directive.

### Legally relevant published reference
- **EN 301 549 V3.2.1 (2021-03)** remains the version cited by Commission Implementing Decision (EU) 2021/1339 for the Web Accessibility Directive as of this review.
- It references **WCAG 2.1 Level AA** for web content (Clause 9), non-web documents (Clause 10), and software (Clause 11), and adds ICT-specific requirements beyond WCAG.

### Revision in progress
- ETSI published Draft EN 301 549 V4.1.0 (2025-11) and an approval-stage V4.1.0 artifact in June 2026. The revision work is intended to support the EAA and incorporates WCAG 2.2 criteria.
- Do not describe V4.1.0, or V3.2.1 by analogy, as an EAA harmonized legal baseline until the applicable reference is published in the Official Journal of the European Union.

### Important distinction
- Normative compliance baseline is set by the applicable legal instrument and harmonized standards.
- New W3C or ETSI publications are not automatically legally binding without the applicable legal bridge and, where relevant, an EU harmonization decision.
- **Practical recommendation**: use WCAG 2.2 AA as the engineering target now, while reporting the exact legally applicable baseline separately.

---

## 4. Spain: Ley 11/2023 (private sector)

**Ley 11/2023, de 8 de mayo** transposes the EAA into Spanish law. It does **not** make every private website an EAA service. First verify whether the product or service is listed in Title I and whether an exemption applies.

### What it requires
- All products and services within the EAA scope sold or provided in Spain must meet accessibility requirements.
- Enforcement date: **June 28, 2025**.
- Applies to the economic operators connected to the products and services listed in Title I.

### Who is affected
| Sector | Examples |
|---|---|
| E-commerce | Online stores, marketplaces, payment gateways |
| Banking | Online banking, ATMs, financial apps |
| Transport | Airline/train/bus booking websites and apps |
| Telecommunications | ISP websites, telecom service portals |
| Audiovisual | Streaming platforms, video-on-demand |
| Publishing | E-book platforms, digital news services |

### Enforcement and sanctions
- Article 30 routes infringements to the applicable **sector-specific** sanctions regime; where that regime does not cover the case, Title III of Real Decreto Legislativo 1/2013 applies supplementarily.
- Do not reuse the EUR 30,000 / 150,000 / 600,000 ranges found in amendments to other legislation as a universal Ley 11/2023 accessibility fine table.
- Autonomous communities and Ceuta/Melilla determine surveillance authorities within their competences; a central technical unit supports coordination and acts where no authority has been designated.

### Operational guidance
- Start by determining if the case is a covered product/service under Title I.
- For websites, distinguish information-only content from an e-commerce service: the EAA definition requires a distance service provided electronically at a consumer's individual request with a view to concluding a consumer contract.
- Record scope assumptions in audit reports.
- If exemptions are claimed, require documented justification.

---

## 5. Spain: RD 1112/2018 (public sector)

**RD 1112/2018** governs digital accessibility for the **public sector** in Spain (transposing Directive (EU) 2016/2102).

### Scope
- Websites and mobile applications of the bodies listed in Article 2: the General State Administration, autonomous-community and local administrations, the institutional public sector, associations constituted by those public bodies, and the Administration of Justice. Do not treat every university or publicly funded entity as directly in scope without checking its legal status.
- Additional Provision 1 also requires public administrations to demand the same accessibility criteria for sites/apps whose design or maintenance receives public funding, for entities contractually managing public services (especially education, health, culture, sport, and social services), and for publicly funded private education/training/university centers.
- Public funding received by an organization does not by itself prove that every one of its websites is in scope. Verify what the funding or public-service contract covers.

### Requirements
- Must meet **EN 301 549** (currently WCAG 2.1 AA).
- Must publish an **accessibility statement** for each in-scope website or mobile application.
- Must provide a **feedback mechanism** for users to report accessibility barriers.
- Must conduct periodic accessibility reviews.

### Key dates (already in effect)
| Date | Requirement |
|---|---|
| September 2018 | RD published |
| September 2020 | All new public websites must comply |
| September 2021 | All existing public websites must comply |
| June 2021 | All public mobile apps must comply |

### Enforcement
- **Observatorio de Accesibilidad Web (OAW)** conducts monitoring.
- Non-compliant entities may face administrative sanctions and mandatory remediation orders.

### Operational guidance
- For public-sector audits in Spain, this is a primary legal entry point.
- Accessibility statement must follow the official template (Modelo de declaracion de accesibilidad).
- Must cooperate with the applicable monitoring and reporting arrangements through the responsible accessibility unit or competent administration; verify the exact OAW reporting route for the entity instead of assuming that every obligated organization reports directly into one system.
- The accessibility statement must be updated at least annually or whenever an Article 17 accessibility review occurs. Article 17 requires periodic reviews but does not itself prescribe one universal annual interval for every full review.
- Keep evidence for each finding (URL/screen, steps, expected behavior, observed behavior).

---

## 6. Spain: RD 193/2023 (goods and services offered to the public)

**Real Decreto 193/2023, de 21 de marzo** establishes accessibility and non-discrimination conditions for goods and services offered to the public. It is a separate scope path from the EAA sectors in Ley 11/2023.

### Web and app requirement

Article 14.2 requires privately owned websites and mobile apps, not financed with public funds, whose content concerns goods or services offered to the public to incorporate the accessibility criteria of RD 1112/2018 and, in particular, priority A and AA criteria of UNE 139803 when the corresponding deadline applies.

### Calendar

| Case | Deadline |
|---|---|
| New public goods/services | 2025-01-01 |
| New private goods/services contracted or supplied to public administrations | 2025-01-01 |
| Existing public or publicly contracted private goods/services: reasonable adjustments | 2026-01-01 |
| Other new private goods/services | 2029-01-01 |
| Other existing private goods/services: reasonable adjustments | 2030-01-01 |

Do not assume that the later private-sector deadlines override an earlier or more specific obligation under Ley 11/2023, RD 1112/2018, procurement terms, funding conditions, or sectoral law.

---

## 7. Practical scope and compliance roadmap

### Scope decision order

1. Identify the legal person, public/private status, service offered, audience, funding for site design/maintenance, and any public-service contract.
2. Check RD 1112/2018 direct scope and Additional Provision 1.
3. Check Ley 11/2023 Title I covered products/services, including whether a website flow is an e-commerce service.
4. Check RD 193/2023 goods/services offered to the public and its calendar.
5. Check procurement, grant, sector-specific, and contractual requirements.
6. Record uncertainty and seek qualified legal advice before making a formal compliance claim.

### For private sector (Ley 11/2023)

```
Phase 1 — Audit (immediate)
├── Automated scan with axe-core / Lighthouse
├── Manual testing with JAWS + Chrome, NVDA + Firefox
├── Identify high-impact barriers
└── Document findings per EN 301 549 clauses

Phase 2 — Remediate and verify (ongoing since 2025-06-28 for in-scope services)
├── Fix critical barriers: keyboard access, focus management, alt text
├── Fix ARIA: live regions, roles, states
├── Fix forms: labels, error messages, autocomplete
└── Fix contrast and target sizes

Phase 3 — Maintain (ongoing)
├── Accessibility statement on website
├── Feedback mechanism for users
├── CI/CD integration: axe-core in tests
├── Quarterly manual audit cycle
└── Screen reader regression testing per JAWS/NVDA version
```

### Engineering order
1. Apply the exact mandatory baseline identified by the scope analysis.
2. Use WCAG 2.2 AA as the practical engineering target unless a stricter requirement applies.
3. Test representative pages and complete processes with automated tools, keyboard, JAWS, and NVDA.
4. Track EN 301 549 revisions and EU harmonization decisions without treating drafts as law.

---

## 8. Official sources

- BOE Ley 11/2023: https://www.boe.es/buscar/act.php?id=BOE-A-2023-11022
- BOE RD 1112/2018: https://www.boe.es/buscar/act.php?id=BOE-A-2018-12699
- BOE RD 193/2023: https://www.boe.es/buscar/act.php?id=BOE-A-2023-7417
- BOE Real Decreto Legislativo 1/2013: https://www.boe.es/buscar/act.php?id=BOE-A-2013-12632
- EAA summary (EUR-Lex): https://eur-lex.europa.eu/EN/legal-content/summary/accessibility-of-products-and-services.html
- EN 301 549 harmonization decision: https://eur-lex.europa.eu/eli/dec_impl/2021/1339/oj/eng
- ETSI EN 301 549 publications: https://www.etsi.org/deliver/etsi_en/301500_301599/301549/
- EU Web Accessibility Directive harmonization page: https://digital-strategy.ec.europa.eu/en/policies/web-accessibility-directive-standards-and-harmonisation
- AccessibleEU status of EN 301 549 and its update for the EAA: https://accessible-eu-centre.ec.europa.eu/content-corner/digital-library/en-3015492021-accessibility-requirements-ict-products-and-services_en
