import unittest
import analysis

class AnalysisTestCase(unittest.TestCase):

    def setUp(self):
        self.usdbtc = analysis.AnalysisTools('USD-BTC', 'hour')
        pass

    def test_trimdata10days(self):
        print(self.usdbtc.trim_data(10))
        self.assertEqual(len(self.usdbtc.trim_data(10)), 10)

    def test_trimshadowdata10days(self):
        print(self.usdbtc.trim_shadowdata(10))
        self.assertEqual(len(self.usdbtc.trim_shadowdata(10)), 10)

    def test_getnthcandle(self):
        print(self.usdbtc.getnth_candleback(26))
        self.assertEqual(len(self.usdbtc.getnth_candleback(26)), 7)

if __name__ == "__main__":
    unittest.main()
