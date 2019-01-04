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
    market = 'USD-BTC'
    ticktable = PrettyTable()
    ticktable.clear()
    ticktable.field_names = ['-----', "5 minutes", "30 minutes", "Hour"]
    try:
        agent5m = Ichimoku.Ichimoku('USD-BTC', 'fiveMin')
        agent30m = Ichimoku.Ichimoku('USD-BTC', 'thirtyMin')
        agent1h = Ichimoku.Ichimoku('USD-BTC', 'hour')
        tenkansencross5m = agent5m.tenkansen_cross(agent5m.trim_data(9), agent5m.trim_data(26))
        tenkansencross30m = agent30m.tenkansen_cross(agent30m.trim_data(9), agent30m.trim_data(26))
        tenkansencross1h = agent1h.tenkansen_cross(agent1h.trim_data(9), agent1h.trim_data(26))
        closeoverkumoshadow5m = agent5m.close_over_kumo_shadow(agent5m.trim_shadowdata(52))
        closeoverkumoshadow30m = agent30m.close_over_kumo_shadow(agent30m.trim_shadowdata(52))
        closeoverkumoshadow1h = agent1h.close_over_kumo_shadow(agent1h.trim_shadowdata(52))
        limarketsep = [market, '****', '****', '****']
        litenkansen = ['Tenkan-sen cross', tenkansencross5m, tenkansencross30m, tenkansencross1h]
        licloseoverkumo = ['Close over Kumo shadow', closeoverkumoshadow5m, closeoverkumoshadow30m, closeoverkumoshadow1h]
        ticktable.add_row(limarketsep)
        ticktable.add_row(litenkansen)
        ticktable.add_row(licloseoverkumo)
    except TypeError:
        print('TypeError while proccesing market ' + market)
        pass

    print(ticktable)
    print('End of routine, lets sleep')


def simple_request(url):
    r = requests.get(url)
    return r.json()


if __name__ == "__main__":
    main()

