# JAWS Accessibility

This project contains the **jaws-accessibility** Agent Skill for accessible web development with JAWS/NVDA screen reader compatibility and Spain/EU regulatory compliance.

## How to use

The main skill definition is in `SKILL.md`. Reference materials are in `references/`.

When working on accessibility tasks, consult the reference routing table in SKILL.md to load the appropriate reference file for the current task.

## Scope

- Priority WCAG 2.2 Level A and AA implementation patterns with routing to the complete official matrix
- JAWS and NVDA screen reader compatibility, including current-release testing caveats
- Spanish legislation: Ley 11/2023, RD 1112/2018, and RD 193/2023 with explicit scope checks
- European Accessibility Act (EAA) and EN 301 549 harmonized standard
- ARIA patterns, anti-patterns, and component patterns (forms, modals, tables, SPAs)
- Audit methodology with JAWS commands, 8-phase testing flow, and CI/CD integration

## Validation

Before distributing or installing changes, run the structural validator, `python scripts/validate_skill_content.py .`, and `python -m unittest discover -s tests -p "test_*.py"`. Do not treat a frontmatter-only validation as proof that commands, standards, or legal guidance are current.
