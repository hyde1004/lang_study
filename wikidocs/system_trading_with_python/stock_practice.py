import pandas.io.data as web
import datetime

start = datetime.datetime(2012, 1, 1)

# KODEX 200
kodex_200 = web.DataReader('069500.KS', 'yahoo', start)
# print(kodex_200)

# KOSEF 10년국고채 (148070)
kosef_bond_10years = web.DataReader('148070.KS', 'yahoo', start)
# print(kosef_bond_10years['Close'].ix['2015-01-02'])
# print(kosef_bond_10years)

index = []
bond = []
bond_profit = []
bond_profit_diff = []
kodex = []
kodex_profit = []
kodex_profit_diff = []

import calendar
for year in range(2012, 2015):
	for month in range(1, 13):
		last_day = calendar.monthrange(year, month)[1]
		date =  str("%04d%02d%02d" % (year, month, last_day))

		while True:
			# To Be Done
			# 날짜 범위 넘어가면 예외발생

			if date in kosef_bond_10years.index:
				# print("%s : %d" % (date, kosef_bond_10years['Close'].ix[date] ))
				index.append(date)
				bond.append(kosef_bond_10years['Close'].ix[date])
				kodex.append(kodex_200['Close'].ix[date])
				break
			else:
				last_day = last_day - 1
				date =  str("%04d%02d%02d" % (year, month, last_day))


from pandas import Series, DataFrame

data = { 'bond':bond, 'kodex 200':kodex}

for idx, val in enumerate(bond):
	bond_profit.append( round((bond[idx] - bond[0])/bond[0]*100, 2))
	if idx == 0:
		bond_profit_diff.append(0)
	else:
		bond_profit_diff.append(round((bond[idx] - bond[idx-1])/bond[idx-1]*100, 2))

for idx, val in enumerate(kodex):
	kodex_profit.append( round((kodex[idx] - kodex[0])/kodex[0]*100, 2))
	if idx == 0:
		kodex_profit_diff.append(0)
	else:
		kodex_profit_diff.append(round((kodex[idx] - kodex[idx-1])/kodex[idx-1]*100, 2))


data['bond_profit'] = bond_profit
data['bond_profit_diff'] = bond_profit_diff

data['kodex_200_profit'] = kodex_profit
data['kodex_200_profit_diff'] = kodex_profit_diff

frame3 = DataFrame(data, index)

print(frame3)

import csv
csv_file = open('result.csv', 'w')
cw = csv.writer(csv_file, delimiter =',')
cw.writerow(['Date', 'Bond', 'KODEX'])

for idx, val in enumerate(index):
	cw.writerow([index[idx], bond[idx], kodex[idx]])



