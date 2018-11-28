# Trade Signal Harvester
This routine calculates the different values associated to the Ichimoku Cloud analysis.
After that it saves the data into a file as a json object that will be the database from which we will pick trending markets

## Indicators
##### Tenkan-sen (Turning Line): 
 ((9-period high + 9-period low)/2)

##### Kijun-sen (Standard Line):
 ((26-period high + 26-period low)/2)

##### Senkou Span A (Leading Span A):
 ((Conversion Line + Base Line)/2) ; Plotted 26 days in the future

##### Senkou Span B (Leading Span B):
 ((52-period high + 52-period low)/2) ; Plotted 26 days in the future
 
##### Chikou Span (Lagging Span): 

 Close plotted 26 days in the past


## Signals

##### Senkou Span Cross

The Senkou Span Cross signal occurs when the Senkou Span A (1st leading line) crosses the Senkou Span B (2nd leading line).

##### Tenkan-sen/ kijun-sen Cross

The Tenkan Sen / Kijun Sen Cross signal occurs when the Tenkan Sen (Turning line) crosses the Kijun Sen (Standard line).


##### Kijunsen Cross

The Kijun Sen Cross signal occurs when the price crosses the Kijun Sen (Standard line).

##### Kumo Cloud Breakout

The Kumo Breakout signal occurs when the price leaves or crosses the Kumo cloud (26 days in the future)

##### Kumo Shadow Breakout

The Kumo Shadow Breakout signal occurs when the price leaves or crosses the Kumo shadow (present)


##### Chikou Span Cross

The Chikou Span Cross signal occurs when the Chikou Span (Lagging line) rises above or falls below the price.