import unittest
import analysis


class AnalysisTestCase(unittest.TestCase):

    def setUp(self):
        self.usdbtc = analysis.Analysis('USD-BTC', 'hour')
        pass

    def test_trimdata10days(self):
        self.assertEqual(len(self.usdbtc.trim_data(10)), 10)

    def test_calculate_sma(self):
        print(self.usdbtc.calculate_sma(self.usdbtc.trim_data(21)))

    def test_calculate_rsi(self):
        print(self.usdbtc.calculate_rsi(self.usdbtc.trim_data(14)))


if __name__ == "__main__":
    unittest.main()
