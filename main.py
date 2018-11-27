import time
import requests
import analysis
import json

TICK_INTERVAL = 3600  # seconds


def main():
    print('Starting bot...')

    while True:
        start = time.time()
        tick()
        end = time.time()

        if end - start < TICK_INTERVAL:
            time.sleep(TICK_INTERVAL - (end - start))


def tick():
    print('Running routine')
    agent = analysis.Analysis('USD-BTC', 'hour')
    market_summaries = simple_request('https://bittrex.com/api/v1.1/public/getmarketsummaries')
    for summary in market_summaries['result']:
        if summary['BaseVolume'] >= 12:
            market = summary['MarketName']
            last = summary['Last']
            agent.change_market(market)
            # rsi = agent.calculate_rsi(agent.trim_data(14))
            senkouspana = agent.calculate_senkouspana()
            senkouspanb = agent.calculate_senkouspanb(agent.trim_data(52))
            tenkansen = agent.calculate_tenkansen(agent.trim_data(9))
            kijunsen = agent.calculate_kijunsen(agent.trim_data(26))
            tempdict = {}

            if senkouspana > senkouspanb:
                senkouspancross = 'bearish'
            else:
                senkouspancross = 'bullish'
            if tenkansen < kijunsen:
                tenkensenkijunsencross = 'bearish'
            else:
                tenkensenkijunsencross = 'bullish'
            if last >kijunsen :
                kijunsencross = 'bullish'
            else:
                kijunsencross = 'bearish'
            if last > senkouspanb and last > senkouspana:
                kumobreakout = 'bullish'
            else:
                if last < senkouspanb and last < senkouspana:
                    kumobreakout = 'bearish'
                else:
                    kumobreakout = 'inside the kumo'
            tempdict['Market'] = market
            tempdict['Senkou Span Cross'] = senkouspancross
            tempdict['Tenkensen/kijunsen cross '] = tenkensenkijunsencross
            tempdict['Kijunsen Cross'] = kijunsencross
            tempdict['Kumo Breakout'] = kumobreakout
        

def simple_request(url):
    r = requests.get(url)
    return r.json()


def format_float(f):
    return "%.8f" % f


if __name__ == "__main__":
    main()

