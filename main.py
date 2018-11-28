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
    delete_content('data.json')
    for summary in market_summaries['result']:
        if summary['BaseVolume'] >= 12:
            market = summary['MarketName']
            last = summary['Last']
            agent.change_market(market)
            # rsi = agent.calculate_rsi(agent.trim_data(14))
            senkouspana = agent.calculate_senkouspana()
            senkouspanb = agent.calculate_senkouspanb(agent.trim_data(52))
            senkouspanashadow = agent.calculate_senkouspanashadow()
            senkouspanbshadow = agent.calculate_senkouspanbshadow(agent.trim_shadowdata(52))
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
            if last > kijunsen:
                kijunsencross = 'bullish'
            else:
                kijunsencross = 'bearish'
            if last > senkouspanb and last > senkouspana:
                kumocloudbreakout = 'bullish'
            else:
                if last < senkouspanb and last < senkouspana:
                    kumocloudbreakout = 'bearish'
                else:
                    kumocloudbreakout = 'consolidation'
            if last > senkouspanbshadow and last > senkouspanashadow:
                kumoshadowbreakout = 'bullish'
            else:
                if last < senkouspanbshadow and last < senkouspanashadow:
                    kumoshadowbreakout = 'bearish'
                else:
                    kumoshadowbreakout = 'consolidation'
            tempdict['Market'] = market
            tempdict['Senkou Span Cross'] = senkouspancross
            tempdict['Tenkensen/kijunsen cross '] = tenkensenkijunsencross
            tempdict['Kijunsen Cross'] = kijunsencross
            tempdict['Kumo Cloud Breakout'] = kumocloudbreakout
            tempdict['Kumo Shadow Breakout'] = kumoshadowbreakout
            tempdict['Chikun Span Cross'] = agent.calculate_chikouspan()
            with open('data.json', 'a') as outfile:
                json.dump(tempdict, outfile)
    print('Routine done, lets sleep')


def delete_content(fname):
    with open(fname, "w"):
        pass


def simple_request(url):
    r = requests.get(url)
    return r.json()


def format_float(f):
    return "%.8f" % f


if __name__ == "__main__":
    main()

