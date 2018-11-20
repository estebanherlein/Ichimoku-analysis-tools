import requests

class Analysis:
    def __init__(self, market, interval):
        self.id = self
        self.market = market
        self.interval = interval
        string = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + market + '&tickInterval=' + interval
        self.data = self.simple_request(string)

    def trim_data(self, units):
        li = []
        dataset = self.data['result']
        length = len(dataset)
        firstcandle = length - units
        i = 0
        for item in dataset:
            if i >= firstcandle:
                li.append(item)
                i = i + 1
            else:
                i = i + 1
        return li

    def simple_request(self, url):
        r = requests.get(url)
        return r.json()

    def sma(self):
        return
