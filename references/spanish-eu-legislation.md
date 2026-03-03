# Spanish & European Accessibility Legislation

Last reviewed: 2026-03-03

## TOC

1. Scope and disclaimer
2. European Accessibility Act (EAA)
3. EN 301 549 — Harmonized standard
4. Spain: Ley 11/2023 (private sector)
5. Spain: RD 1112/2018 (public sector)
6. Practical compliance roadmap
7. Official sources

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
- **Microenterprises** (< 10 employees AND < EUR 2M turnover) providing **services** are exempt. Microenterprises providing **products** are NOT exempt.
- **Disproportionate burden**: Organizations may claim exemption if compliance would impose a disproportionate burden, but must document the assessment, notify the competent authority, and review every 5 years or upon request.

### Technical standard
The EAA references **EN 301 549** as the harmonized European standard that provides a "presumption of conformity."

Operational guidance:
- Validate if the product/service is in EAA scope first.
- Then verify national transposition details (Spain: Ley 11/2023).

---

## 3. EN 301 549 — The European Harmonized Standard

EN 301 549 translates the EAA's requirements into testable criteria for ICT products and services.

### Current version: v3.2.1 (2021)
- References **WCAG 2.1 Level AA** for web content (Clause 9), non-web documents (Clause 10), and software (Clause 11).
- Adds ICT-specific requirements beyond WCAG: real-time communication, hardware, relay services.

### Upcoming version: v4.1.1 (expected February 2026)
- Will incorporate **WCAG 2.2 Level AA**.
- New requirements for cognitive accessibility aligned with W3C COGA guidance.
- Enhanced requirements for mobile applications.

### Important distinction
- Normative compliance baseline is set by the applicable legal instrument and harmonized standards.
- New W3C standards (like WCAG 2.2) are not automatically legally binding without the legal bridge (harmonization decision).
- **Practical recommendation**: Implement WCAG 2.2 AA now for forward compatibility. EN 301 549 v4.1.1 adoption is imminent.

---

## 4. Spain: Ley 11/2023 (private sector)

**Ley 11/2023, de 8 de mayo** transposes the EAA into Spanish law. Primary legislation governing digital accessibility for the **private sector** in Spain.

### What it requires
- All products and services within the EAA scope sold or provided in Spain must meet accessibility requirements.
- Enforcement date: **June 28, 2025**.
- Applies to all economic operators: manufacturers, importers, distributors, and service providers.

### Who is affected
| Sector | Examples |
|---|---|
| E-commerce | Online stores, marketplaces, payment gateways |
| Banking | Online banking, ATMs, financial apps |
| Transport | Airline/train/bus booking websites and apps |
| Telecommunications | ISP websites, telecom service portals |
| Audiovisual | Streaming platforms, video-on-demand |
| Publishing | E-book platforms, digital news services |

### Sanctions regime
Ley 11/2023 establishes a graduated sanctions system:

| Severity | Fine range | Examples |
|---|---|---|
| Minor (leve) | Up to EUR 30,000 | Incomplete accessibility statement, minor non-conformances |
| Serious (grave) | EUR 30,001 – EUR 150,000 | Systematic failure to meet requirements, obstructing inspections |
| Very serious (muy grave) | EUR 150,001 – EUR 600,000 | Repeated serious violations, refusal to remediate after formal notice |

In the most serious cases, fines can reach **EUR 1,000,000**. Additional consequences may include suspension of subsidies or disqualification from providing social services.

### Competent authority
- **Ministerio de Derechos Sociales, Consumo y Agenda 2030** (or successor ministry) oversees enforcement.
- Autonomous communities may also enforce within their jurisdiction.

### Operational guidance
- Start by determining if the case is a covered product/service under Title I.
- Record scope assumptions in audit reports.
- If exemptions are claimed, require documented justification.

---

## 5. Spain: RD 1112/2018 (public sector)

**RD 1112/2018** governs digital accessibility for the **public sector** in Spain (transposing Directive (EU) 2016/2102).

### Scope
- All websites and mobile applications of public sector bodies: central government, autonomous communities, local authorities, universities, publicly funded entities.

### Requirements
- Must meet **EN 301 549** (currently WCAG 2.1 AA).
- Must publish an **accessibility statement** (declaracion de accesibilidad) on every website.
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
- Must report to OAW monitoring system.
- Review cycle is annual minimum.
- Keep evidence for each finding (URL/screen, steps, expected behavior, observed behavior).

---

## 6. Practical compliance roadmap

### For private sector (Ley 11/2023)

```
Phase 1 — Audit (immediate)
├── Automated scan with axe-core / Lighthouse
├── Manual testing with JAWS + Chrome, NVDA + Firefox
├── Identify high-impact barriers
└── Document findings per EN 301 549 clauses

Phase 2 — Remediate (before June 2025)
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

### Decision order
1. Determine legal scope (private-sector EAA pathway vs public-sector pathway).
2. Apply mandatory baseline from law + harmonized standard.
3. Add WCAG 2.2 controls as engineering baseline for forward compatibility.
4. Track future changes (EN 301 549 updates and EU harmonization decisions).

---

## 7. Official sources

- BOE Ley 11/2023: https://www.boe.es/buscar/act.php?id=BOE-A-2023-11022
- BOE RD 1112/2018: https://www.boe.es/buscar/act.php?id=BOE-A-2018-12699
- EAA summary (EUR-Lex): https://eur-lex.europa.eu/EN/legal-content/summary/accessibility-of-products-and-services.html
- EN 301 549 harmonization decision: https://eur-lex.europa.eu/eli/dec_impl/2021/1339/oj/eng
- EU Web Accessibility Directive harmonization page: https://digital-strategy.ec.europa.eu/en/policies/web-accessibility-directive-standards-and-harmonisation
