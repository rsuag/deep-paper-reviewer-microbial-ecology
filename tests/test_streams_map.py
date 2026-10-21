import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).parents[1] / "deep-paper-reviewer" / "scripts"
sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location("streams_map", SCRIPTS / "streams_map.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class EvidenceMapTests(unittest.TestCase):
    def test_locates_candidates_without_claiming_compliance(self):
        report = MODULE.evidence_map([
            "Methods",
            "Samples were sequenced on an Illumina instrument.",
            "Raw reads are available under SRA accession PRJNA123.",
        ])
        items = {item["id"]: item for item in report["items"]}
        self.assertEqual(items["6.3"]["candidates"][0]["paragraph"], 2)
        self.assertEqual(items["8.2"]["candidates"][0]["paragraph"], 3)
        self.assertEqual(items["8.4"]["candidates"], [])
        self.assertNotIn("compliant", MODULE.markdown(report).lower())

    def test_reference_list_does_not_supply_evidence(self):
        report = MODULE.evidence_map([
            "## References",
            "A paper about Illumina sequencing and GitHub code availability.",
        ])
        self.assertTrue(all(not item["candidates"] for item in report["items"]))


if __name__ == "__main__":
    unittest.main()
