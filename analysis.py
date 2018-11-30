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
        firstcandle = len(dataset) - units
        for item in dataset[firstcandle:]:
            li.append(item)
        return li

    def trim_shadowdata(self, units):
        data = self.simple_request(self.market, self.interval)
        dataset = data['result']
        li = []
        firstcandle = len(dataset) - (units + 26)
        a = 1
        for item in dataset[firstcandle:]:
            if a <= units:
                li.append(item)
                a = a + 1
        return li

    def getnth_candleback(self, units):
        data = self.simple_request(self.market, self.interval)
        dataset = data['result']
        li = {}
        nthcandle = len(dataset) - units
        for item in dataset[nthcandle:]:
            li = item
            break
        return li

    def change_market(self, market):
        self.market = market

    def change_interval(self, interval):
        self.interval = interval

    def simple_request(self, market, interval):
        url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + market + '&tickInterval=' + interval
        r = requests.get(url)
        return r.json()

