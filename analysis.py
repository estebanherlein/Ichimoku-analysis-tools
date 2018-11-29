import requests


class Analysis:
    def __init__(self, market, interval):
        self.id = self
        self.market = market
        self.interval = interval

    def calculate_tenkansen(self, somedata):
        ninedayhigh = 0
        ninedaylow = 1000000
        for item in somedata:
            if item['H'] > ninedayhigh:
                ninedayhigh = item['H']
            else:
                if item['H'] < ninedaylow:
                    ninedaylow = item['H']
        return (ninedayhigh + ninedaylow) / 2

    def calculate_kijunsen(self, somedata):
        twentysixhigh = 0
        twentysixlow = 1000000
        for item in somedata:
            if item['H'] > twentysixhigh:
                twentysixhigh = item['H']
            else:
                if item['H'] < twentysixlow:
                    twentysixlow = item['H']
        return (twentysixhigh + twentysixlow) / 2

    def calculate_senkouspana(self):
        return (self.calculate_tenkansen(self.trim_data(9)) + self.calculate_kijunsen(self.trim_data(26))) / 2

    def calculate_senkouspanb(self, somedata):
        fiftytwohigh = 0
        fiftytwolow = 1000000
        for item in somedata:
            if item['H'] >= fiftytwohigh:
                fiftytwohigh = item['H']
            else:
                if item['H'] < fiftytwolow:
                   fiftytwolow = item['H']
        return (fiftytwohigh + fiftytwolow) / 2

    def calculate_senkouspanashadow(self):
        return (self.calculate_tenkansen(self.trim_shadowdata(9)) + self.calculate_kijunsen(self.trim_shadowdata(26))) / 2

    def calculate_senkouspanbshadow(self, somedata):
        fiftytwohigh = 0
        fiftytwolow = 1000000
        for item in somedata:
            if item['H'] >= fiftytwohigh:
                fiftytwohigh = item['H']
            else:
                if item['H'] < fiftytwolow:
                    fiftytwolow = item['H']
        return (fiftytwohigh + fiftytwolow) / 2

    def calculate_chikouspan(self):
        pastcandle = self.getnth_candle(26)
        chikunspan = self.getnth_candle(1)

        if chikunspan['C'] > pastcandle['L'] and chikunspan['C'] > pastcandle['H']:
            result = 'bullish'
        else:
            if chikunspan['C'] < pastcandle['L'] and chikunspan['C'] < pastcandle['H']:
                result = 'bearish'
            else:
                result = 'consolidation'
        return result

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

    def getnth_candle(self, units):
        data = self.simple_request(self.market, self.interval)
        dataset = data['result']
        li = {}
        nthcandle = len(dataset) - units
        for item in dataset[nthcandle:]:
            li = item
        return li

    def change_market(self, market):
        self.market = market

    def change_interval(self, interval):
        self.interval = interval

    def simple_request(self, market, interval):
        url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + market + '&tickInterval=' + interval
        r = requests.get(url)
        return r.json()

