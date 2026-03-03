# JAWS Accessibility — Agent Skill

A comprehensive accessibility engineering skill featuring **JAWS/NVDA screen reader compatibility**, **Spanish & European legislation**, **WCAG 2.2 criteria**, and **ARIA best practices**.

Works with **Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Windsurf, Cline, Roo Code**, and any tool that supports the [Agent Skills](https://agentskills.io) open standard.

## What makes this skill unique

| Feature | This skill | Other a11y skills |
|---|---|---|
| **JAWS/NVDA bugs by version** (2024, 2025, 2026 betas) | Yes | No |
| **Spanish legislation** (Ley 11/2023, RD 1112/2018) | Yes | No |
| **European Accessibility Act (EAA)** + EN 301 549 | Yes | No |
| **JAWS audit methodology** with commands and QA flow | Yes | No |
| WCAG 2.2 criteria with code examples | Yes | Partial |
| ARIA divergence tables per screen reader | Yes | No |

## Installation

### Option 1: Clone

```bash
# Claude Code / Copilot / Cline / Roo Code (all scan ~/.claude/skills/)
cd ~/.claude/skills && git clone https://github.com/YOUR_USERNAME/jaws-accessibility-skill.git jaws-accessibility

# Cross-platform location (recognized by most tools)
cd ~/.agents/skills && git clone https://github.com/YOUR_USERNAME/jaws-accessibility-skill.git jaws-accessibility

# Windsurf
cd ~/.codeium/windsurf/skills && git clone https://github.com/YOUR_USERNAME/jaws-accessibility-skill.git jaws-accessibility
```

### Option 2: Manual copy

Copy the `jaws-accessibility/` folder into any of the skill directories your AI tool scans.

### Verify

The skill appears automatically when you start a new session. Look for `jaws-accessibility` in the available skills list or invoke with `/jaws-accessibility`.

## Skill structure

```
jaws-accessibility/
├── SKILL.md                              # Main skill file (loaded by all Agent Skills platforms)
├── AGENTS.md                             # Cross-platform instructions (Codex, Copilot, Cursor, Roo)
├── README.md                             # This file
├── LICENSE                               # MIT
├── agents/
│   └── openai.yaml                       # OpenAI Codex UI metadata (platform-specific extension)
└── references/
    ├── spanish-eu-legislation.md          # Ley 11/2023, RD 1112/2018, EAA, EN 301 549
    ├── wcag-22-criteria.md               # All WCAG 2.2 A/AA criteria with code examples
    ├── jaws-nvda-compatibility.md         # Interaction modes, ARIA divergences, bugs by version
    ├── jaws-audit-methodology.md          # Setup, commands, 8-phase testing, CI/CD integration
    └── future-standards.md                # WCAG 3.0 tracking (non-normative)
```

## What it covers

### Screen reader compatibility
- JAWS vs NVDA fundamental differences and testing strategies
- Interaction modes (Browse Mode / Focus Mode) and mode switching
- ARIA roles, states, and properties with per-reader behavior tables
- Version-specific bugs and regressions (JAWS 2024, 2025, 2026 betas)
- Anti-patterns that cause silent failures

### Spanish & European legislation
- **European Accessibility Act (EAA)** — Directive (EU) 2019/882, enforcement from June 2025
- **Ley 11/2023** — Spanish private sector obligations, sanctions up to EUR 1,000,000
- **RD 1112/2018** — Spanish public sector requirements
- **EN 301 549** — Harmonized European standard (current v3.2.1, upcoming v4.1.1)
- Microenterprise exemptions and disproportionate burden documentation
- Practical compliance roadmap

### WCAG 2.2 criteria
- All Level A and AA success criteria organized by POUR principles
- Good/bad code examples for each criterion
- New criteria in 2.2: Focus Not Obscured, Dragging Movements, Target Size, Accessible Authentication, Redundant Entry, Consistent Help
- Deprecated criterion: 4.1.1 Parsing

### Audit methodology
- Complete JAWS command reference (30+ commands)
- Pre-audit automated scanning workflow (axe-core, Lighthouse)
- 8-phase manual testing flow with detailed verification steps
- Cross-validation with NVDA
- Issue reporting template
- CI/CD integration patterns (GitHub Actions, eslint-plugin-jsx-a11y, Playwright)

## Cross-platform compatibility

This skill follows the [Agent Skills open standard](https://agentskills.io/specification). The core `SKILL.md` format is recognized by 30+ AI tools including:

| Platform | Reads SKILL.md | Reads AGENTS.md | Reads openai.yaml |
|---|---|---|---|
| Claude Code | Yes | No | No |
| OpenAI Codex | Yes | Yes | Yes |
| GitHub Copilot | Yes | Yes | No |
| Cursor | Yes | Yes | No |
| Windsurf | Yes | No | No |
| Cline | Yes | No | No |
| Roo Code | Yes | Yes | No |

## Design decisions

- SKILL.md is procedural and compact — tells the AI *how* to behave, not just what to know.
- Domain content lives in `references/` for progressive loading.
- Legal baseline and future standards are separated: normative (Spanish/EU law) vs non-normative (WCAG 3.0 draft).
- Platform-specific extensions (`agents/openai.yaml`) are isolated and don't affect portability.

## Legal note

This skill provides engineering guidance, not legal advice. Always validate final legal interpretations with qualified counsel.

## Contributing

Contributions are welcome! Particularly:
- **Bug reports**: If you find JAWS/NVDA behavior that differs from what's documented
- **Legislation updates**: EU member state transpositions, EN 301 549 version updates
- **New WCAG criteria**: As WCAG 2.2 adoption expands and WCAG 3.0 drafts evolve
- **Code examples**: Framework-specific patterns (Vue, Svelte, Angular, etc.)
- **Platform testing**: Confirming the skill works correctly on additional AI tools

## Maintenance

- Review legal and standards references periodically.
- Update the `Last reviewed` date in each reference file after edits.
- Track JAWS/NVDA version-specific behavior in compatibility notes.

## License

MIT
