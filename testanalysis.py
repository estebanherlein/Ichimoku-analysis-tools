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

    def test_calculate_tenkansen(self):
        print(self.usdbtc.calculate_tenkansen(self.usdbtc.trim_data(9)))

    def test_calculate_kijunsen(self):
        print(self.usdbtc.calculate_kijunsen(self.usdbtc.trim_data(26)))

    def test_calculate_senkouspana(self):
        print(self.usdbtc.calculate_senkouspana())

    def test_calculate_senkouspanb(self):
        print(self.usdbtc.calculate_senkouspanb(self.usdbtc.trim_data(52)))


if __name__ == "__main__":
    unittest.main()
