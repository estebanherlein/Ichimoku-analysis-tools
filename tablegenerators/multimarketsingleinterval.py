import time, requests
from classes import Ichimoku
from prettytable import PrettyTable

TICK_INTERVAL = 300  # seconds


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
    ticktable = PrettyTable()
    ticktable.clear()
    ticktable.field_names = ["Market name", "Tenkan sen Cross", "Close over kumo shadow"]
    agent = Ichimoku.Ichimoku('USD-BTC', 'fiveMin')
    market_summaries = simple_request('https://bittrex.com/api/v1.1/public/getmarketsummaries')
    string = 'BTC'
    for summary in market_summaries['result']:
        if string in summary['MarketName'] and summary['BaseVolume'] >= 80:
            market = summary['MarketName']
            agent.change_market(market)
            try:
                tenkansencross = agent.tenkansen_cross(agent.trim_data(9), agent.trim_data(26))
                closeoverkumoshadow = agent.close_over_kumo_shadow(agent.trim_shadowdata(52))
                li = [market, tenkansencross, closeoverkumoshadow]
                ticktable.add_row(li)
                print(market + ' is done')
            except TypeError:
                print('TypeError while proccesing market ' + market)
                pass
        else:
            pass
    print(ticktable)
    print('End of Routine, lets sleep')


def simple_request(url):
    r = requests.get(url)
    return r.json()


if __name__ == "__main__":
    main()

