import time
import requests
import analysis

TICK_INTERVAL = 60  # seconds


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
        market = summary['MarketName']
        last = summary['Last']
        agent.change_market(market)
        rsi = agent.calculate_rsi(agent.trim_data(14))
        sma_5 = agent.calculate_sma(agent.trim_data(5))
        sma_50 = agent.calculate_sma(agent.trim_data(50))
        sma_200 = agent.calculate_sma(agent.trim_data(200))

        if rsi < 20:
            print("This Market is oversold :" + market + ' . RSI = ' + format_float(rsi))

        if last >= sma_5 and last >= sma_50 and last >= sma_200:
            print('This market' + market + ' is over SMA 5, 50 AND 200 ')

        if last >= sma_5 and last >= sma_50 :
            print('This market' + market + ' is over SMA 5, 50 ')

        if last >= sma_5 :
            print('This market' + market + ' is over SMA 5')


def simple_request(url):
    r = requests.get(url)
    return r.json()


def format_float(f):
    return "%.8f" % f


if __name__ == "__main__":
    main()

