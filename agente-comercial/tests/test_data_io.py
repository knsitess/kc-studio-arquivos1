import json
import tempfile
import unittest
from pathlib import Path

from data_io import build_report, load_payload, save_report, validate_payload


class DataIoTests(unittest.TestCase):
    def payload(self):
        return {
            "business": {"name": "Empresa a verificar", "city": "Cidade/UF", "segment": "serviços"},
            "pc": {}, "od": {"site_status": "S4", "completed_searches": 0},
            "qc": {}, "ce": {"site_status": "S4", "facts": {}, "protocol_complete": False},
        }

    def test_rejects_missing_business_identity(self):
        with self.assertRaisesRegex(ValueError, "business.name"):
            validate_payload({"business": {"city": "x", "segment": "x"}})

    def test_build_report_preserves_business_and_blocks_approach(self):
        report = build_report(self.payload())
        self.assertEqual(report["business"]["name"], "Empresa a verificar")
        self.assertFalse(report["evaluation"]["approach_allowed"])
        self.assertTrue(report["operational_control"]["human_review_required"])

    def test_json_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "input.json"
            output = Path(folder) / "report.json"
            source.write_text(json.dumps(self.payload()), encoding="utf-8")
            loaded = load_payload(source)
            save_report(build_report(loaded), output)
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(result["business"]["city"], "Cidade/UF")
            self.assertFalse(result["operational_control"]["approach_allowed"])


if __name__ == "__main__":
    unittest.main()
