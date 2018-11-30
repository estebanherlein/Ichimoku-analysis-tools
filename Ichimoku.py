import analysis


class Ichimoku(analysis.AnalysisTools):

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
        pastcandle = self.getnth_candleback(26)
        chikunspan = self.getnth_candleback(1)

        if chikunspan['C'] > pastcandle['L'] and chikunspan['C'] > pastcandle['H']:
            result = 'bullish'
        else:
            if chikunspan['C'] < pastcandle['L'] and chikunspan['C'] < pastcandle['H']:
                result = 'bearish'
            else:
                result = 'consolidation'
        return result

