import requests


class Analysis:
    def __init__(self, market, interval):
        self.id = self
        self.market = market
        self.interval = interval
        string = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + market + '&tickInterval=' + interval
        self.data = self.simple_request(string)

    def sma_units(self, somedata):
        length = len(somedata)
        total = 0
        for item in somedata:
            total = total + item['O']
        return total/length

    def rsi(self, somedata):
        length = len(somedata)
        i = 0
        totaldown = 0.0
        totalup = 0.0
        for item in somedata:
            if i == 0:
                lastclose = item['C']
                i = i + 1
            else:
                thisclose = item['C']
                if thisclose - lastclose >= 0:
                    totalup = totalup + (thisclose - lastclose)
                else:
                    totaldown = totaldown + abs(thisclose - lastclose)
                lastclose = item['C']
        rs = (totalup /length) / (totaldown / length)
        rsi = 100 - (100 / (1 + rs))
        return rsi

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
