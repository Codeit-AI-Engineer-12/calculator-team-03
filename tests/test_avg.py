import unittest

from ops.avg import avg


class AvgValidationTests(unittest.TestCase):
    def test_avg_returns_mean_for_natural_numbers(self):
        self.assertEqual(avg(2, 4), 3.0)

    def test_avg_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            avg(2, -1)

        with self.assertRaises(ValueError):
            avg(2, "three")

        with self.assertRaises(ValueError):
            avg()


if __name__ == "__main__":
    unittest.main()
