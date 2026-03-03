# JAWS Accessibility — Agent Skill

[English](#english) | [Español](#español)

---

<a id="english"></a>

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
cd ~/.claude/skills && git clone https://github.com/Ambitos-1995/jaws-accessibility-skill.git jaws-accessibility

# Cross-platform location (recognized by most tools)
cd ~/.agents/skills && git clone https://github.com/Ambitos-1995/jaws-accessibility-skill.git jaws-accessibility

# Windsurf
cd ~/.codeium/windsurf/skills && git clone https://github.com/Ambitos-1995/jaws-accessibility-skill.git jaws-accessibility
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

---

<a id="español"></a>

# JAWS Accessibility — Agent Skill (Español)

Una skill de ingeniería de accesibilidad completa con **compatibilidad de lectores de pantalla JAWS/NVDA**, **legislación española y europea**, **criterios WCAG 2.2** y **buenas prácticas ARIA**.

Funciona con **Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Windsurf, Cline, Roo Code** y cualquier herramienta que soporte el estándar abierto [Agent Skills](https://agentskills.io).

## Qué hace única a esta skill

| Característica | Esta skill | Otras skills de a11y |
|---|---|---|
| **Bugs de JAWS/NVDA por versión** (2024, 2025, 2026 betas) | Sí | No |
| **Legislación española** (Ley 11/2023, RD 1112/2018) | Sí | No |
| **Directiva Europea de Accesibilidad (EAA)** + EN 301 549 | Sí | No |
| **Metodología de auditoría JAWS** con comandos y flujo QA | Sí | No |
| Criterios WCAG 2.2 con ejemplos de código | Sí | Parcial |
| Tablas de divergencia ARIA por lector de pantalla | Sí | No |

## Instalación

### Opción 1: Clonar

```bash
# Claude Code / Copilot / Cline / Roo Code (todos escanean ~/.claude/skills/)
cd ~/.claude/skills && git clone https://github.com/Ambitos-1995/jaws-accessibility-skill.git jaws-accessibility

# Ubicación multiplataforma (reconocida por la mayoría de herramientas)
cd ~/.agents/skills && git clone https://github.com/Ambitos-1995/jaws-accessibility-skill.git jaws-accessibility

# Windsurf
cd ~/.codeium/windsurf/skills && git clone https://github.com/Ambitos-1995/jaws-accessibility-skill.git jaws-accessibility
```

### Opción 2: Copia manual

Copia la carpeta `jaws-accessibility/` en cualquier directorio de skills que tu herramienta de IA escanee.

### Verificar

La skill aparece automáticamente al iniciar una nueva sesión. Busca `jaws-accessibility` en la lista de skills disponibles o invócala con `/jaws-accessibility`.

## Estructura de la skill

```
jaws-accessibility/
├── SKILL.md                              # Archivo principal (cargado por todas las plataformas Agent Skills)
├── AGENTS.md                             # Instrucciones multiplataforma (Codex, Copilot, Cursor, Roo)
├── README.md                             # Este archivo
├── LICENSE                               # MIT
├── agents/
│   └── openai.yaml                       # Metadatos UI de OpenAI Codex (extensión específica)
└── references/
    ├── spanish-eu-legislation.md          # Ley 11/2023, RD 1112/2018, EAA, EN 301 549
    ├── wcag-22-criteria.md               # Todos los criterios WCAG 2.2 A/AA con ejemplos de código
    ├── jaws-nvda-compatibility.md         # Modos de interacción, divergencias ARIA, bugs por versión
    ├── jaws-audit-methodology.md          # Setup, comandos, pruebas de 8 fases, integración CI/CD
    └── future-standards.md                # Seguimiento WCAG 3.0 (no normativo)
```

## Qué cubre

### Compatibilidad de lectores de pantalla
- Diferencias fundamentales JAWS vs NVDA y estrategias de pruebas
- Modos de interacción (Modo Exploración / Modo Foco) y cambio de modos
- Roles, estados y propiedades ARIA con tablas de comportamiento por lector
- Bugs y regresiones específicos por versión (JAWS 2024, 2025, 2026 betas)
- Anti-patrones que causan fallos silenciosos

### Legislación española y europea
- **Directiva Europea de Accesibilidad (EAA)** — Directiva (UE) 2019/882, aplicación desde junio 2025
- **Ley 11/2023** — Obligaciones del sector privado español, sanciones de hasta 1.000.000 EUR
- **RD 1112/2018** — Requisitos del sector público español
- **EN 301 549** — Estándar armonizado europeo (actual v3.2.1, próxima v4.1.1)
- Exenciones para microempresas y documentación de carga desproporcionada
- Hoja de ruta práctica de cumplimiento

### Criterios WCAG 2.2
- Todos los criterios de Nivel A y AA organizados por principios POUR
- Ejemplos de código correcto/incorrecto para cada criterio
- Nuevos criterios en 2.2: Foco No Oscurecido, Movimientos de Arrastre, Tamaño de Objetivo, Autenticación Accesible, Entrada Redundante, Ayuda Consistente
- Criterio obsoleto: 4.1.1 Análisis sintáctico

### Metodología de auditoría
- Referencia completa de comandos JAWS (30+ comandos)
- Flujo de escaneo automatizado pre-auditoría (axe-core, Lighthouse)
- Flujo de pruebas manuales de 8 fases con pasos de verificación detallados
- Validación cruzada con NVDA
- Plantilla de reporte de incidencias
- Patrones de integración CI/CD (GitHub Actions, eslint-plugin-jsx-a11y, Playwright)

## Compatibilidad multiplataforma

Esta skill sigue el [estándar abierto Agent Skills](https://agentskills.io/specification). El formato central `SKILL.md` es reconocido por más de 30 herramientas de IA:

| Plataforma | Lee SKILL.md | Lee AGENTS.md | Lee openai.yaml |
|---|---|---|---|
| Claude Code | Sí | No | No |
| OpenAI Codex | Sí | Sí | Sí |
| GitHub Copilot | Sí | Sí | No |
| Cursor | Sí | Sí | No |
| Windsurf | Sí | No | No |
| Cline | Sí | No | No |
| Roo Code | Sí | Sí | No |

## Decisiones de diseño

- SKILL.md es procedimental y compacto — le dice a la IA *cómo* comportarse, no solo qué saber.
- El contenido de dominio vive en `references/` para carga progresiva.
- La base legal y los estándares futuros están separados: normativo (legislación española/UE) vs no normativo (borrador WCAG 3.0).
- Las extensiones específicas de plataforma (`agents/openai.yaml`) están aisladas y no afectan la portabilidad.

## Nota legal

Esta skill proporciona orientación de ingeniería, no asesoramiento jurídico. Valida siempre las interpretaciones legales finales con profesionales cualificados.

## Contribuir

¡Las contribuciones son bienvenidas! En particular:
- **Reportes de bugs**: Si encuentras comportamiento de JAWS/NVDA que difiera de lo documentado
- **Actualizaciones legislativas**: Transposiciones de estados miembros de la UE, actualizaciones de versión de EN 301 549
- **Nuevos criterios WCAG**: A medida que la adopción de WCAG 2.2 se expande y los borradores de WCAG 3.0 evolucionan
- **Ejemplos de código**: Patrones específicos de frameworks (Vue, Svelte, Angular, etc.)
- **Pruebas de plataforma**: Confirmar que la skill funciona correctamente en herramientas de IA adicionales

## Mantenimiento

- Revisar periódicamente las referencias legales y de estándares.
- Actualizar la fecha `Last reviewed` en cada archivo de referencia tras ediciones.
- Rastrear el comportamiento específico por versión de JAWS/NVDA en las notas de compatibilidad.

## Licencia

MIT
