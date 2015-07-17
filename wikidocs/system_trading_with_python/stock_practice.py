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
kodex = []
kodex_profilt = []
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
	if idx == 0:
		bond_profit.append(0)
	else:
		bond_profit.append(bond[idx] - bond[0])

data['bond_profit'] = bond_profit
frame3 = DataFrame(data, index)

print(frame3)
