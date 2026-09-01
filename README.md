# JAWS Accessibility — Agent Skill

[English](#english) | [Español](#español)

---

<a id="english"></a>

A comprehensive accessibility engineering skill featuring **JAWS/NVDA screen reader compatibility**, **Spanish & European legislation**, **priority WCAG 2.2 patterns linked to the complete official matrix**, and **ARIA best practices**.

Works with **Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Windsurf, Cline, Roo Code**, and any tool that supports the [Agent Skills](https://agentskills.io) open standard.

## What makes this skill unique

| Feature | This skill | Other a11y skills |
|---|---|---|
| **JAWS/NVDA current-release testing caveats** | Yes | No |
| **Spanish legislation** (Ley 11/2023, RD 1112/2018, RD 193/2023) | Yes | No |
| **European Accessibility Act (EAA)** + EN 301 549 | Yes | No |
| **JAWS audit methodology** with commands and QA flow | Yes | No |
| Priority WCAG 2.2 patterns with official complete-matrix routing | Yes | Partial |
| Cross-reader risk patterns and evidence guidance | Yes | No |

## Installation

### Option 1: Clone

```bash
# OpenAI Codex
cd ~/.codex/skills && git clone https://github.com/Ambitos-1995/jaws-accessibility-skill.git jaws-accessibility

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
├── scripts/
│   └── validate_skill_content.py          # Semantic and synchronization validation
├── tests/
│   └── test_scenarios.py                  # Regression scenarios for critical guidance
└── references/
    ├── spanish-eu-legislation.md          # Ley 11/2023, RD 1112/2018, RD 193/2023, EAA, EN 301 549
    ├── wcag-22-criteria.md               # Priority patterns plus the official complete matrix
    ├── jaws-nvda-compatibility.md         # Cross-reader risks, evidence notes, version caveats
    ├── jaws-audit-methodology.md          # Setup, commands, 8-phase testing, CI/CD integration
    └── future-standards.md                # WCAG 3.0 tracking (non-normative)
```

## What it covers

### Screen reader compatibility
- JAWS vs NVDA fundamental differences and testing strategies
- Interaction modes (Browse Mode / Focus Mode) and mode switching
- Cross-reader risk patterns for ARIA, live regions, tables, labels, and SPA navigation
- Current-release caveats, including JAWS 2026 AI Labeler and browser pairings
- Anti-patterns that cause silent failures

### Spanish & European legislation
- **European Accessibility Act (EAA)** — Directive (EU) 2019/882, enforcement from June 2025
- **Ley 11/2023** — Scope-limited Spanish implementation of the EAA, with sector and microenterprise checks
- **RD 1112/2018** — Spanish public sector requirements
- **RD 193/2023** — Accessibility requirements and phased deadlines for goods and services offered to the public
- **EN 301 549** — v3.2.1 remains harmonized for the Web Accessibility Directive; EAA harmonization and newer v4 artifacts are tracked separately
- Microenterprise exemptions and disproportionate burden documentation
- Practical compliance roadmap

### WCAG 2.2 patterns
- Priority Level A and AA implementation patterns organized by POUR principles
- Explicit routing to the official complete WCAG 2.2 matrix; this skill does not reproduce all 86 criteria
- New criteria in 2.2: Focus Not Obscured, Dragging Movements, Target Size, Accessible Authentication, Redundant Entry, Consistent Help
- Deprecated criterion: 4.1.1 Parsing

### Audit methodology
- Curated essential JAWS web-audit commands, with Desktop/Laptop distinctions
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
- Run `python scripts/validate_skill_content.py .` and `python -m unittest discover -s tests -p "test_*.py"` before installation.

## License

MIT

---

<a id="español"></a>

# JAWS Accessibility — Agent Skill (Español)

Una skill de ingeniería de accesibilidad completa con **compatibilidad de lectores de pantalla JAWS/NVDA**, **legislación española y europea**, **patrones prioritarios WCAG 2.2 enlazados a la matriz oficial completa** y **buenas prácticas ARIA**.

Funciona con **Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Windsurf, Cline, Roo Code** y cualquier herramienta que soporte el estándar abierto [Agent Skills](https://agentskills.io).

## Qué hace única a esta skill

| Característica | Esta skill | Otras skills de a11y |
|---|---|---|
| **Consideraciones de prueba de versiones actuales de JAWS/NVDA** | Sí | No |
| **Legislación española** (Ley 11/2023, RD 1112/2018, RD 193/2023) | Sí | No |
| **Directiva Europea de Accesibilidad (EAA)** + EN 301 549 | Sí | No |
| **Metodología de auditoría JAWS** con comandos y flujo QA | Sí | No |
| Patrones prioritarios WCAG 2.2 con acceso a la matriz oficial | Sí | Parcial |
| Patrones de riesgo entre lectores y guía de evidencias | Sí | No |

## Instalación

### Opción 1: Clonar

```bash
# OpenAI Codex
cd ~/.codex/skills && git clone https://github.com/Ambitos-1995/jaws-accessibility-skill.git jaws-accessibility

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
├── scripts/
│   └── validate_skill_content.py          # Validación semántica y de sincronización
├── tests/
│   └── test_scenarios.py                  # Escenarios de regresión de guía crítica
└── references/
    ├── spanish-eu-legislation.md          # Ley 11/2023, RD 1112/2018, RD 193/2023, EAA, EN 301 549
    ├── wcag-22-criteria.md               # Patrones prioritarios y matriz oficial completa
    ├── jaws-nvda-compatibility.md         # Riesgos entre lectores, evidencias y versiones
    ├── jaws-audit-methodology.md          # Setup, comandos, pruebas de 8 fases, integración CI/CD
    └── future-standards.md                # Seguimiento WCAG 3.0 (no normativo)
```

## Qué cubre

### Compatibilidad de lectores de pantalla
- Diferencias fundamentales JAWS vs NVDA y estrategias de pruebas
- Modos de interacción (Modo Exploración / Modo Foco) y cambio de modos
- Patrones de riesgo entre lectores para ARIA, regiones vivas, tablas, etiquetas y navegación SPA
- Consideraciones de versiones actuales, incluido JAWS 2026 AI Labeler y combinaciones de navegador
- Anti-patrones que causan fallos silenciosos

### Legislación española y europea
- **Directiva Europea de Accesibilidad (EAA)** — Directiva (UE) 2019/882, aplicación desde junio 2025
- **Ley 11/2023** — Aplicación española de la EAA con alcance sectorial y comprobación de microempresas
- **RD 1112/2018** — Requisitos del sector público español
- **RD 193/2023** — Requisitos de accesibilidad y plazos escalonados para bienes y servicios ofrecidos al público
- **EN 301 549** — v3.2.1 sigue armonizada para la Directiva de accesibilidad web; la armonización para EAA y los artefactos v4 se controlan por separado
- Exenciones para microempresas y documentación de carga desproporcionada
- Hoja de ruta práctica de cumplimiento

### Patrones WCAG 2.2
- Patrones prioritarios de Nivel A y AA organizados por principios POUR
- Enlace explícito a la matriz oficial completa; la skill no reproduce los 86 criterios
- Nuevos criterios en 2.2: Foco No Oscurecido, Movimientos de Arrastre, Tamaño de Objetivo, Autenticación Accesible, Entrada Redundante, Ayuda Consistente
- Criterio obsoleto: 4.1.1 Análisis sintáctico

### Metodología de auditoría
- Selección de comandos esenciales para auditoría web con JAWS, diferenciando Desktop y Laptop
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
- Ejecutar `python scripts/validate_skill_content.py .` y `python -m unittest discover -s tests -p "test_*.py"` antes de instalar.

## Licencia

MIT
