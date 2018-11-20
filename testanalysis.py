import unittest
import analysis


class AnalysisTestCase(unittest.TestCase):


    def setUp(self):
        self.btceth = analysis.Analysis('BTC-ETH', 'hour')
        pass

    def test_get10days(self):
        self.assertEqual(len(self.btceth.trim_data(10)), 10)

    def test_get21days(self):
        self.assertEqual(len(self.btceth.trim_data(21)), 21)

    def test_get30days(self):
        self.assertEqual(len(self.btceth.trim_data(30)), 30)


if __name__ == "__main__":
    unittest.main()
