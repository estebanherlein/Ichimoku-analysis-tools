import time
import requests

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

    market_summaries = simple_request('https://bittrex.com/api/v1.1/public/getmarketsummaries')
    for summary in market_summaries['result']:
        market = summary['MarketName']
        day_close = summary['PrevDay']
        last = summary['Last']
        percent_chg = ((last / day_close) - 1) * 100

        if 40 < percent_chg < 60:
            print("Fomo strikes! Let's buy some " + market + ' for ' + str(format_float(last)))

        if percent_chg < -20:
            print('We should buy some ' + market + ' for ' + str(format_float(last))+ ', it is damn cheap right now')


def simple_request(url):
    r = requests.get(url)
    return r.json()


def format_float(f):
    return "%.8f" % f


if __name__ == "__main__":
    main()

