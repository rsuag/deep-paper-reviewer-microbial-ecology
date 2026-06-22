import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "deep-paper-reviewer" / "scripts" / "audit_manuscript.py"
SPEC = importlib.util.spec_from_file_location("audit_manuscript", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AuditTests(unittest.TestCase):
    def test_flags_results_citation_and_causality(self):
        report = MODULE.audit([
            "3. Results",
            "Latitude drove community structure (Smith et al., 2024).",
            "4. Discussion",
            "MAGs demonstrated activity.",
        ])
        rules = [item["rule"] for item in report["findings"]]
        self.assertIn("causal-language", rules)
        self.assertIn("results-literature-citation", rules)
        self.assertIn("mag-activity-inference", rules)

    def test_tracks_cross_references(self):
        report = MODULE.audit(["3. Results", "Patterns are shown in Fig. 2a, Fig. S4, and Dataset S6."])
        self.assertIn("Fig. 2a", report["cross_references"]["figures"])
        self.assertIn("Dataset S6", report["cross_references"]["datasets"])

    def test_cautious_phrases_are_not_flagged(self):
        report = MODULE.audit([
            "3. Results",
            "Statistical significance was determined by permutation tests.",
            "MAG abundance was expressed as TPM-like units.",
            "Substrate use was not demonstrated.",
        ])
        rules = [item["rule"] for item in report["findings"]]
        self.assertNotIn("causal-language", rules)
        self.assertNotIn("mag-activity-inference", rules)


if __name__ == "__main__":
    unittest.main()
