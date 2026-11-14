import unittest

from scoring import calculate_pc, calculate_od, calculate_qc, calculate_ce, calculate_priority


def ev(fact_id="x", points=10, level="official_direct"):
    return {"fact_id": fact_id, "points": points, "source_url": "https://example.org/source",
            "verified_on": "2026-11-14", "evidence_level": level}


class ScoringTests(unittest.TestCase):
    def test_priority_regression_cases(self):
        self.assertEqual(calculate_priority(10, 0, 40, 0.85)["score"], 13)
        self.assertEqual(calculate_priority(35, 0, 10, 0.30)["score"], 4)
        self.assertEqual(calculate_priority(10, 0, 30, 0.30)["score"], 3)

    def test_pc_requires_source_and_date_and_deduplicates(self):
        result = calculate_pc({"porte": [ev("same", 15), ev("same", 15),
                                          {"fact_id": "no-source", "points": 10}]})
        self.assertEqual(result["score"], 15)

    def test_b3_takes_precedence_over_b2_and_b1(self):
        result = calculate_pc({"estrutura": {
            "multiple_units": [dict(ev(), unit_id="u1"), dict(ev(), unit_id="u2")],
            "recent_third_party_activity": ev("b2"),
            "current_operation": ev("b1")}})
        self.assertEqual(result["estrutura_b"], 30)

    def test_s3_only_adds_absence_points(self):
        self.assertEqual(calculate_od({"site_status": "S2"})["score"], 0)
        self.assertEqual(calculate_od({"site_status": "S3"})["score"], 10)

    def test_s4_requires_two_searches_for_five_points(self):
        self.assertEqual(calculate_od({"site_status": "S4", "completed_searches": 1})["score"], 0)
        self.assertEqual(calculate_od({"site_status": "S4", "completed_searches": 2})["score"], 5)

    def test_qc_requires_traceable_evidence(self):
        self.assertEqual(calculate_qc({"channel_type": "official_direct"})["score"], 0)
        self.assertEqual(calculate_qc({"channel_type": "official_direct", "evidence": ev(),
                                       "whatsapp_identified_by_company": True,
                                       "whatsapp_evidence": ev("wa")})["score"], 60)

    def test_ce_marks_critical_missing_and_s2_as_insufficient(self):
        result = calculate_ce({"site_status": "S2", "protocol_complete": True, "facts": {}})
        self.assertTrue(result["data_insufficient"])
        self.assertEqual(result["factor"], 0.30)

    def test_no_approach_is_ever_authorized_by_scoring(self):
        from scoring import evaluate_lead
        result = evaluate_lead({})
        self.assertFalse(result["approach_allowed"])
        self.assertEqual(result["funnel_status"], "Pendente de verificação")


if __name__ == "__main__":
    unittest.main()
