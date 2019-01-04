# Ichimoku analysis tools

## class AnalysisTools:

######def trim_data(self, units):
returns a list with the last **units** candles.

######def trim_shadowdata(self, units):
returns a list with the  last **units** candles, starting 26 candles in the past.

######def getnth_candleback(self, nth):
returns a dictionary with a single candle. 

######def change_market(self, market)
changes bittrex market pair

######def change_interval(self, interval):
sets the candlestick interval [“oneMin”, “fiveMin”, “thirtyMin”, “hour”, “day”] 

######def simple_request(self, market, interval):
requests data from bittrex


## class Ichimoku(analysis.AnalysisTools):

######def calculate_tenkansen(self, somedata):
((9-period high + 9-period low)/2)

######def calculate_kijunsen(self, somedata):
 ((26-period high + 26-period low)/2)

######def calculate_senkouspana(self):}
((Conversion Line + Base Line)/2) ; Plotted 26 days in the future

######def calculate_senkouspanb(self, somedata):
((52-period high + 52-period low)/2) ; Plotted 26 days in the future

######def calculate_senkouspanashadow(self):
calculates senkouspana 26 units back 

######def calculate_senkouspanbshadow(self, somedata):
calculates senkouspanb 26 units back 

######def calculate_chikouspan(self):
 Close plotted 26 days in the past
 
######def tenkansen_cross(self, somedata):
checks if tenkansen is over kijunsen

######def close_over_kumo_shadow(self):
checks the last candle to compere the close to both senkou span shadow a and senkou span shadow b



TODO:

