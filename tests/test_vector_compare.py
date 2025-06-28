import unittest
from src.vector_compare import VectorCompare

class TestVectorCompare(unittest.TestCase):
    def setUp(self):
        self.vc = VectorCompare()

    def test_concordance_valid(self):
        doc = "hello world hello"
        expected = {"hello": 2, "world": 1}
        self.assertEqual(self.vc.concordance(doc), expected)

    def test_concordance_invalid_type(self):
        with self.assertRaises(ValueError):
            self.vc.concordance(123)

    def test_magnitude_valid(self):
        concordance = {"hello": 2, "world": 1}
        expected = (2**2 + 1**2)**0.5
        self.assertAlmostEqual(self.vc.magnitude(concordance), expected)

    def test_magnitude_invalid_type(self):
        with self.assertRaises(ValueError):
            self.vc.magnitude("not a dict")

    def test_relation_valid(self):
        c1 = {"hello": 1, "world": 1}
        c2 = {"hello": 1, "world": 1}
        self.assertAlmostEqual(self.vc.relation(c1, c2), 1.0)

    def test_relation_zero_magnitude(self):
        c1 = {"hello": 1}
        c2 = {}
        self.assertEqual(self.vc.relation(c1, c2), 0.0)

    def test_refine_query(self):
        query = "captcha security"
        refined = self.vc.refine_query(query)
        self.assertTrue(len(refined.split()) >= 2)  # Ensures some refinement

if __name__ == "__main__":
    unittest.main()