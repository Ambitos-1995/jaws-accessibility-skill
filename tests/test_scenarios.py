from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_skill_content.py"
SPEC = importlib.util.spec_from_file_location("validate_skill_content", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class SkillScenarioTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.copy = Path(self.temp_dir.name) / "jaws-accessibility"
        shutil.copytree(
            ROOT,
            self.copy,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def replace(self, relative: str, old: str, new: str) -> None:
        path = self.copy / relative
        content = path.read_text(encoding="utf-8")
        self.assertIn(old, content, f"scenario precondition missing in {relative}")
        path.write_text(content.replace(old, new), encoding="utf-8")

    def messages(self) -> str:
        return "\n".join(VALIDATOR.validate_root(self.copy))

    def test_canonical_skill_passes_semantic_validation(self) -> None:
        self.assertEqual([], VALIDATOR.validate_root(self.copy))

    def test_detects_regression_that_maps_k_to_links(self) -> None:
        self.replace(
            "references/jaws-audit-methodology.md",
            "**K / Shift+K** | Next / previous PlaceMarker",
            "**K / Shift+K** | Next / previous link",
        )
        messages = self.messages()
        self.assertIn("K PlaceMarker mapping", messages)
        self.assertIn("K as link navigation", messages)

    def test_detects_regression_that_maps_d_to_regions(self) -> None:
        self.replace(
            "references/jaws-audit-methodology.md",
            "**D / Shift+D** | Next / previous element of a different type",
            "**D / Shift+D** | Next / previous landmark region",
        )
        messages = self.messages()
        self.assertIn("D different-element mapping", messages)
        self.assertIn("D as landmark navigation", messages)

    def test_detects_virtual_cursor_and_layered_command_swap(self) -> None:
        self.replace(
            "references/jaws-audit-methodology.md",
            "**Insert + Z** | Toggle the virtual cursor",
            "**Insert + Z** | Toggle Forms Mode",
        )
        self.replace(
            "references/jaws-audit-methodology.md",
            "**Insert + Space** | Start a layered command; it is not a virtual-cursor toggle",
            "**Insert + Space** | Toggle the virtual cursor",
        )
        messages = self.messages()
        self.assertIn("virtual-cursor toggle", messages)
        self.assertIn("Insert+Z as Forms Mode", messages)
        self.assertIn("layered-command prefix", messages)
        self.assertIn("Insert+Space as virtual cursor", messages)

    def test_detects_missing_laptop_table_command(self) -> None:
        self.replace(
            "references/jaws-audit-methodology.md",
            "**Alt+Shift+Comma** (current cell)",
            "**Alt+Shift+Slash** (current cell)",
        )
        self.assertIn("Laptop current-table-cell command", self.messages())

    def test_detects_obsolete_wcag_em_draft_guidance(self) -> None:
        self.replace(
            "references/future-standards.md",
            "WCAG-EM 2.0 is no longer a future draft.",
            "WCAG-EM 2.0 remains a draft.",
        )
        self.assertIn("WCAG-EM draft status", self.messages())

    def test_detects_incomplete_microenterprise_definition(self) -> None:
        self.replace(
            "references/spanish-eu-legislation.md",
            "annual turnover **or** annual balance-sheet total not exceeding EUR 2 million",
            "annual turnover below EUR 2 million",
        )
        self.assertIn("microenterprise financial definition", self.messages())

    def test_detects_eaa_harmonization_conflation(self) -> None:
        self.replace(
            "references/spanish-eu-legislation.md",
            "do **not** claim that EN 301 549 V3.2.1 creates an EAA presumption",
            "claim that EN 301 549 V3.2.1 creates an EAA presumption",
        )
        self.assertIn("EAA harmonization distinction", self.messages())

    def test_detects_overbroad_public_sector_scope(self) -> None:
        path = self.copy / "references/spanish-eu-legislation.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\nAll websites and mobile applications of publicly funded entities are directly in scope.\n",
            encoding="utf-8",
        )
        self.assertIn("overbroad RD 1112 scope", self.messages())

    def test_detects_legacy_411_failure_guidance(self) -> None:
        self.replace(
            "references/wcag-22-criteria.md",
            "always satisfied for content using HTML or XML",
            "failed whenever HTML validation reports an error",
        )
        self.assertIn("4.1.1 current interpretation", self.messages())

    def test_detects_44px_promoted_to_wcag_aa_minimum(self) -> None:
        self.replace(
            "references/wcag-22-criteria.md",
            "24x24 CSS pixels",
            "44x44 CSS pixels",
        )
        self.assertIn("WCAG 2.5.8 AA minimum", self.messages())

    def test_detects_apg_promoted_to_normative_wcag(self) -> None:
        path = self.copy / "references/wcag-22-criteria.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\nAPG patterns are an additional WCAG requirement.\n",
            encoding="utf-8",
        )
        self.assertIn("APG treated as normative", self.messages())

    def test_detects_missing_not_tested_state(self) -> None:
        self.replace(
            "references/jaws-audit-methodology.md",
            "| **NOT TESTED** |",
            "| **UNVERIFIED** |",
        )
        self.assertIn("audit result NOT TESTED", self.messages())

    def test_detects_incomplete_environment_record(self) -> None:
        self.replace(
            "references/jaws-audit-methodology.md",
            "version, OS build, architecture",
            "version and architecture",
        )
        self.assertIn("environment field OS build", self.messages())

    def test_detects_missing_pdf_handoff(self) -> None:
        self.replace(
            "references/jaws-audit-methodology.md",
            "hand it to the dedicated PDF-accessibility evaluation",
            "spot-check it in the browser",
        )
        self.assertIn("PDF audit handoff", self.messages())

    def test_detects_missing_official_jaws_source(self) -> None:
        self.replace(
            "references/jaws-audit-methodology.md",
            "https://support.freedomscientific.com/SurfsUp/9-Forms.htm",
            "https://example.invalid/forms",
        )
        messages = self.messages()
        self.assertIn("official JAWS Forms Mode reference", messages)
        self.assertIn("non-official reference host", messages)

    def test_detects_nvda_conformance_oracle_language(self) -> None:
        path = self.copy / "references/jaws-nvda-compatibility.md"
        path.write_text(
            path.read_text(encoding="utf-8") + "\nUse NVDA as the stricter standards-compliance reference.\n",
            encoding="utf-8",
        )
        self.assertIn("NVDA as stricter reference", self.messages())

    def test_normalized_compare_accepts_crlf_and_trailing_space(self) -> None:
        target = Path(self.temp_dir.name) / "installed"
        shutil.copytree(
            self.copy,
            target,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )
        skill = target / "SKILL.md"
        text = skill.read_text(encoding="utf-8")
        skill.write_text(text.replace("\n", " \r\n"), encoding="utf-8", newline="")
        self.assertEqual([], VALIDATOR.compare_roots(self.copy, target))

    def test_compare_reports_semantic_drift(self) -> None:
        target = Path(self.temp_dir.name) / "installed"
        shutil.copytree(
            self.copy,
            target,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )
        skill = target / "SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8") + "\nDrift.\n", encoding="utf-8")
        self.assertIn("normalized content differs for SKILL.md", "\n".join(VALIDATOR.compare_roots(self.copy, target)))


if __name__ == "__main__":
    unittest.main()
