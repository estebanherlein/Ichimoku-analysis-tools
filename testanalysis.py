import unittest
import analysis


class AnalysisTestCase(unittest.TestCase):

    def setUp(self):
        self.btceth = analysis.Analysis('BTC-ETH', 'hour')
        pass

    def test_gettrimdata10days(self):
        self.assertEqual(len(self.btceth.trim_data(10)), 10)

    def test_getsma21days(self):
        print(self.btceth.sma_units(self.btceth.trim_data(21)))

    def test_getrsi14days(self):
        print(self.btceth.rsi(self.btceth.trim_data(14)))


if __name__ == "__main__":
    unittest.main()
