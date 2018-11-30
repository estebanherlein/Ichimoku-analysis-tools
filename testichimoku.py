import unittest
import Ichimoku

class IchimokuTestCase(unittest.TestCase):

    def setUp(self):
        self.usdbtc = Ichimoku.Ichimoku('USD-BTC', 'hour')
        pass

    def test_calculatechikunspan(self):
        print(self.usdbtc.calculate_chikouspan())

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
