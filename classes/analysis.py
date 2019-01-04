import requests


class AnalysisTools:
    def __init__(self, market, interval):
        self.id = self
        self.market = market
        self.interval = interval

    def trim_data(self, units):
        data = self.simple_request(self.market, self.interval)
        dataset = data['result']
        li = []
        i = 1
        for item in reversed(dataset):
            if i <= units:
                li.append(item)
                i = i + 1
            else:
                break
        return li

    def trim_shadowdata(self, units):
        data = self.simple_request(self.market, self.interval)
        dataset = data['result']
        li = []
        i = 1
        a = 1
        for item in reversed(dataset):
            if a >= 26 and i <= units:
                li.append(item)
                i = i + 1
            else:
                if a < 26:
                    a = a + 1
                else:
                    break
        return li

    def getnth_candleback(self, nth):
        data = self.simple_request(self.market, self.interval)
        dataset = data['result']
        li = {}
        i = 1
        for item in reversed(dataset):
            if i == nth:
                li = item
                break
            else:
                i = i + 1
        return li

    def change_market(self, market):
        self.market = market

    def change_interval(self, interval):
        self.interval = interval

    @staticmethod
    def simple_request(market, interval):
        url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + market + '&tickInterval=' + interval
        r = requests.get(url)
        return r.json()
