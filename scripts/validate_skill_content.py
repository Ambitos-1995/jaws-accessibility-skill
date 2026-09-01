#!/usr/bin/env python3
"""Semantic and synchronization checks for the jaws-accessibility skill."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


REFERENCE_FILES = (
    "references/future-standards.md",
    "references/jaws-audit-methodology.md",
    "references/jaws-nvda-compatibility.md",
    "references/spanish-eu-legislation.md",
    "references/wcag-22-criteria.md",
)

RUNTIME_FILES = (
    "AGENTS.md",
    "README.md",
    "SKILL.md",
    "LICENSE",
    "agents/openai.yaml",
    *REFERENCE_FILES,
    "scripts/validate_skill_content.py",
    "tests/test_scenarios.py",
)

OFFICIAL_REFERENCE_HOSTS = {
    "accessible-eu-centre.ec.europa.eu",
    "digital-strategy.ec.europa.eu",
    "download.nvaccess.org",
    "eur-lex.europa.eu",
    "support.freedomscientific.com",
    "www.boe.es",
    "www.etsi.org",
    "www.w3.org",
}

MIN_REVIEW_DATE = date(2026, 7, 23)


def normalize_text(value: str) -> str:
    """Normalize content for cross-platform synchronization comparisons."""
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in value.split("\n")).rstrip() + "\n"


def normalized_bytes(path: Path) -> bytes:
    if path.suffix.lower() in {".md", ".yaml", ".yml", ".py", ".txt"} or path.name == "LICENSE":
        return normalize_text(path.read_text(encoding="utf-8-sig")).encode("utf-8")
    return path.read_bytes()


def normalized_hash(path: Path) -> str:
    return hashlib.sha256(normalized_bytes(path)).hexdigest()


def _require(text: str, needle: str, label: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"missing {label}: {needle!r}")


def _forbid(text: str, pattern: str, label: str, errors: list[str]) -> None:
    if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
        errors.append(f"obsolete or unsafe {label}: /{pattern}/")


def validate_root(root: Path) -> list[str]:
    errors: list[str] = []
    root = root.resolve()

    for relative in RUNTIME_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    if errors:
        return errors

    skill = (root / "SKILL.md").read_text(encoding="utf-8-sig")
    readme = (root / "README.md").read_text(encoding="utf-8-sig")
    method = (root / "references/jaws-audit-methodology.md").read_text(encoding="utf-8-sig")
    future = (root / "references/future-standards.md").read_text(encoding="utf-8-sig")
    legal = (root / "references/spanish-eu-legislation.md").read_text(encoding="utf-8-sig")
    wcag = (root / "references/wcag-22-criteria.md").read_text(encoding="utf-8-sig")
    compatibility = (root / "references/jaws-nvda-compatibility.md").read_text(encoding="utf-8-sig")
    all_guidance = "\n".join((skill, method, future, legal, wcag, compatibility))

    command_invariants = (
        ("**Tab / Shift+Tab** | Next / previous focusable control or link", "link navigation"),
        ("**K / Shift+K** | Next / previous PlaceMarker", "K PlaceMarker mapping"),
        ("**D / Shift+D** | Next / previous element of a different type", "D different-element mapping"),
        ("**R / Shift+R** | Next / previous region", "R region mapping"),
        ("**Q / Shift+Q** | Next / previous main region", "Q main-region mapping"),
        (
            "**NumPad +** | Exit Forms Mode / activate the PC cursor in Desktop layout",
            "Desktop Forms Mode exit / PC cursor",
        ),
        ("**Caps Lock + Semicolon**", "Laptop Forms Mode exit / PC cursor"),
        ("**Insert + Z** | Toggle the virtual cursor", "virtual-cursor toggle"),
        ("**Insert + Space** | Start a layered command", "layered-command prefix"),
        ("**Insert + Space, T**", "Desktop Table Layer entry"),
        ("**Caps Lock + Space, T**", "Laptop Table Layer entry"),
        ("**Alt+Shift+M** (previous cell)", "Laptop previous-table-cell command"),
        ("**Alt+Shift+Period** (next cell)", "Laptop next-table-cell command"),
        ("**Alt+Shift+Y** (cell above)", "Laptop table-cell-above command"),
        ("**Alt+Shift+N** (cell below)", "Laptop table-cell-below command"),
        ("**Alt+Shift+Comma** (current cell)", "Laptop current-table-cell command"),
        ("JAWS Laptop layout", "Laptop-layout distinction"),
    )
    for needle, label in command_invariants:
        _require(method, needle, label, errors)

    bad_command_patterns = (
        (r"K\s*/\s*Shift\+K[^\n|]*\|[^\n]*(?:link|enlace)", "K as link navigation"),
        (r"D\s*/\s*Shift\+D[^\n|]*\|[^\n]*(?:landmark|region)", "D as landmark navigation"),
        (r"Insert\s*\+\s*Z[^\n|]*\|[^\n]*Forms Mode", "Insert+Z as Forms Mode"),
        (r"Insert\s*\+\s*Space[^\n|]*\|[^\n]*virtual cursor", "Insert+Space as virtual cursor"),
        (r"Insert\s*\+\s*Shift\s*\+\s*T[^\n|]*\|[^\n]*(?:header|cabecera)", "undocumented table-header command"),
    )
    for pattern, label in bad_command_patterns:
        _forbid(method, pattern, label, errors)

    for url, label in (
        (
            "https://support.freedomscientific.com/content/html/jawshq/JAWS-Keystrokes.html",
            "official JAWS keystroke reference",
        ),
        ("https://support.freedomscientific.com/SurfsUp/9-Forms.htm", "official JAWS Forms Mode reference"),
        ("https://support.freedomscientific.com/SurfsUp/15-PlaceMarkers.htm", "official JAWS PlaceMarker reference"),
    ):
        _require(method, url, label, errors)

    _require(method, "WCAG-EM 2.0 W3C Group Note published 2026-07-23", "final WCAG-EM 2.0 status", errors)
    _require(future, "final Group Note on **2026-07-23**", "WCAG-EM final publication date", errors)
    _require(future, "https://www.w3.org/TR/wcag-em-2/", "official WCAG-EM 2.0 link", errors)
    _forbid(
        all_guidance,
        r"WCAG-EM 2\.0[^\n]*(?:remains (?:a )?(?:future )?draft|is (?!no longer)(?:a )?(?:future )?draft|published only as[^\n]*draft|sigue siendo (?:un )?borrador)",
        "WCAG-EM draft status",
        errors,
    )
    _forbid(all_guidance, r"use (?:stable )?WCAG-EM 1\.0", "WCAG-EM 1.0 fallback", errors)

    _require(
        legal,
        "annual turnover **or** annual balance-sheet total not exceeding EUR 2 million",
        "microenterprise financial definition",
        errors,
    )
    _require(legal, "fewer than 10 persons", "microenterprise personnel threshold", errors)
    _require(legal, "do **not** claim that EN 301 549 V3.2.1 creates an EAA presumption", "EAA harmonization distinction", errors)
    _require(legal, "bodies listed in Article 2", "RD 1112/2018 direct-scope boundary", errors)
    _require(legal, "instead of assuming that every obligated organization reports directly", "OAW reporting nuance", errors)
    _forbid(legal, r"<\s*10 employees AND <\s*EUR 2M turnover", "exclusive-turnover microenterprise definition", errors)
    _forbid(legal, r"All websites and mobile applications[^\n]*publicly funded entities", "overbroad RD 1112 scope", errors)
    for url, label in (
        ("https://www.boe.es/buscar/act.php?id=BOE-A-2023-11022", "official Ley 11/2023 source"),
        ("https://www.boe.es/buscar/act.php?id=BOE-A-2018-12699", "official RD 1112/2018 source"),
        (
            "https://digital-strategy.ec.europa.eu/en/policies/web-accessibility-directive-standards-and-harmonisation",
            "official EN 301 549 harmonization source",
        ),
    ):
        _require(legal, url, label, errors)

    _require(wcag, "Priority WCAG 2.2 Patterns (Not a Complete Criteria Matrix)", "priority-pattern title", errors)
    _require(wcag, "not all 86 success criteria and not a conformance checklist", "coverage boundary", errors)
    _require(wcag, "https://www.w3.org/WAI/WCAG22/quickref/", "complete official WCAG matrix", errors)
    _require(wcag, "always satisfied for content using HTML or XML", "4.1.1 current interpretation", errors)
    _require(wcag, "1.3.1 (Info and Relationships)", "4.1.1 impact remapping to 1.3.1", errors)
    _require(wcag, "4.1.2 (Name, Role, Value)", "4.1.1 impact remapping to 4.1.2", errors)
    _require(wcag, "24x24 CSS pixels", "WCAG 2.5.8 AA minimum", errors)
    _require(wcag, "44x44 CSS pixels as a strong usability recommendation", "44px recommendation distinction", errors)
    _require(wcag, "APG dialog pattern is informative guidance", "WCAG/APG modal distinction", errors)
    _require(method, "APG patterns are informative guidance, not additional WCAG success criteria", "methodology WCAG/APG distinction", errors)
    _require(
        wcag,
        "https://www.w3.org/WAI/ARIA/apg/about/introduction/",
        "official APG normative-status source",
        errors,
    )
    _require(
        wcag,
        "https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html",
        "official target-size source",
        errors,
    )
    _forbid(wcag, r"APG[^\n]*(?:normative requirement|additional WCAG requirement)", "APG treated as normative", errors)

    for result in ("PASS", "FAIL", "NOT TESTED", "NOT APPLICABLE"):
        _require(method, f"| **{result}** |", f"audit result {result}", errors)
        _require(skill, result, f"router result {result}", errors)

    environment_terms = (
        "Operating system",
        "OS build",
        "display scaling",
        "Keyboard",
        "physical keyboard",
        "Speech",
        "Voice/synthesizer",
        "Braille",
        "translation table",
        "verbosity",
        "AI Labeler",
        "custom labels",
        "UIA",
    )
    for term in environment_terms:
        _require(method, term, f"environment field {term}", errors)

    _require(skill, "PDF accessibility is outside this skill's testing scope", "PDF scope boundary", errors)
    _require(skill, "dedicated PDF-accessibility methodology", "PDF specialist routing", errors)
    _require(method, "hand it to the dedicated PDF-accessibility evaluation", "PDF audit handoff", errors)

    _forbid(all_guidance, r"NVDA (?:as|is) (?:the )?stricter", "NVDA as stricter reference", errors)
    _forbid(all_guidance, r"NVDA follows the spec strictly", "NVDA as conformance oracle", errors)
    _forbid(readme, r"Complete JAWS command reference", "claim of complete JAWS command coverage", errors)
    _forbid(readme, r"ARIA divergence tables per screen reader", "claim of non-existent ARIA divergence tables", errors)

    for relative in REFERENCE_FILES:
        content = (root / relative).read_text(encoding="utf-8-sig")
        match = re.search(r"^Last reviewed:\s*(\d{4}-\d{2}-\d{2})\s*$", content, flags=re.MULTILINE)
        if not match:
            errors.append(f"{relative}: missing Last reviewed date")
            continue
        try:
            reviewed = date.fromisoformat(match.group(1))
        except ValueError:
            errors.append(f"{relative}: invalid Last reviewed date {match.group(1)!r}")
            continue
        if reviewed < MIN_REVIEW_DATE:
            errors.append(f"{relative}: review date predates final WCAG-EM 2.0 publication")
        if reviewed > date.today():
            errors.append(f"{relative}: review date is in the future")

        for raw_url in re.findall(r"https://[^\s)>`]+", content):
            url = raw_url.rstrip(".,;:")
            host = (urlparse(url).hostname or "").lower()
            if host not in OFFICIAL_REFERENCE_HOSTS:
                errors.append(f"{relative}: non-official reference host {host!r} in {url}")

    return errors


def compare_roots(source: Path, target: Path) -> list[str]:
    errors: list[str] = []
    for relative in RUNTIME_FILES:
        source_file = source / relative
        target_file = target / relative
        if not target_file.is_file():
            errors.append(f"{target}: missing synchronized file {relative}")
            continue
        if normalized_hash(source_file) != normalized_hash(target_file):
            errors.append(f"{target}: normalized content differs for {relative}")
    return errors


def hash_report(root: Path) -> list[str]:
    return [f"{normalized_hash(root / relative)}  {relative}" for relative in RUNTIME_FILES]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="canonical skill directory")
    parser.add_argument("--compare", action="append", default=[], type=Path, help="installed copy to compare")
    parser.add_argument("--print-hashes", action="store_true", help="print normalized SHA-256 hashes")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors = validate_root(root)
    for target in args.compare:
        errors.extend(compare_roots(root, target.resolve()))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Semantic validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Semantic validation passed.")
    if args.print_hashes:
        print("Normalized SHA-256:")
        for line in hash_report(root):
            print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
