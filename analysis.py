import requests


class Analysis:
    def __init__(self, market, interval):
        self.id = self
        self.market = market
        self.interval = interval

    def calculate_sma(self, somedata):
        total = 0
        for item in somedata:
            total = total + item['O']
        return total / len(somedata)

    def calculate_rsi(self, somedata):
        length = len(somedata)
        i = 0
        totaldown = 0
        totalup = 0
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
        rs = (totalup / length) / (totaldown / length)
        rsi = 100 - (100 / (1 + rs))
        return rsi

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

    def trim_data(self, units):
        data = self.simple_request(self.market, self.interval)
        dataset = data['result']
        li = []
        firstcandle = len(dataset) - units
        i = 0
        for item in dataset:
            if i >= firstcandle:
                li.append(item)
                i = i + 1
            else:
                i = i + 1
        return li

    def change_market(self, market):
        self.market = market

    def change_interval(self, interval):
        self.interval = interval

    def simple_request(self, market, interval):
        url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + market + '&tickInterval=' + interval
        r = requests.get(url)
        return r.json()

