"""
WARNING : THIS IS THE FIRST VERSION | V0.0.1
The Heiken Ashi formula used to derive these average values is as follows:

* Open = (open of previous bar + close of previous bar)/2.
* High = the maximum value from the high, open, or close of the current period.
* Low = the minimum value from the low, open, or close of the current period
* Close = (open + high + low + close)/4. 

The main goal of this indicator is to detect the trend or the direction of the prices.

"""


# Initilize variables
candlesticks_data = []
open_list = []
high_list = []
low_list = []
close_list = []

# Save a CSV data to a Python object
with open("FILE_NAME_HERE.csv") as f:
	for line in f:
		candlesticks_data.append(line.split(","))

# Create Heiken Ashi (High_Low_Close) data
for each_candle in candlesticks_data:
	open_list.append( (float(each_candle[1]) + float(each_candle[4][:-1]))/2 )
	close_list.append( (float(each_candle[1]) + float(each_candle[2]) + float(each_candle[3]) + float(each_candle[4][:-1]) )/4 )
	high_list.append( max(float(each_candle[1]), float(each_candle[2]), float(each_candle[3]), float(each_candle[4])))
	low_list.append( min(float(each_candle[1]), float(each_candle[2]), float(each_candle[3]), float(each_candle[4])))

# Create the first HeikenAshi candle
first_candle_list = [float(open_list[0]), float(high_list[0]), float(low_list[0]), float(close_list[0])]
first_candle = str(candlesticks_data[0][0])+","+str(open_list[0])+","+str(high_list[0])+","+str(low_list[0])+","+str(close_list[0])
with open("NEW_FILE_NAME_HERE.csv", "w") as file:
	file.write(first_candle+"\n")

# Create and save all HeieknAshi candles
for i in range(1, len(candlesticks_data)):
	with open("NEW_FILE_NAME_HERE.csv", "a") as file:
		ha_candle_open 		= (first_candle_list[0] + first_candle_list[-1]) / 2
		ha_candle_high 		= float(high_list[i])
		ha_cnadle_low 		= float(low_list[i])
		ha_cnadle_close 	= float(close_list[i])
		first_candle_list = [ha_candle_open, ha_candle_high, ha_cnadle_low, ha_cnadle_close]
		first_candle = str(candlesticks_data[i][0])+","+str(ha_candle_open)+","+str(ha_candle_high)+","+str(ha_cnadle_low)+","+str(ha_cnadle_close)
		file.write(first_candle+"\n")