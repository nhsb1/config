#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html5lib
import time
from argparse import ArgumentParser 
from yahoo_finance import Share

url = 'https://en.wikipedia.org/wiki/List_of_largest_daily_changes_in_the_S%26P_500_Index'
count = 0

def getSoup():
	global url, target
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	target = soup.find("div", {"id": "mw-collapsible mw-shown"}) #gets DJIA instead of S&P 500
	target = soup.find_all("td")
	return target

def sp500info():
	sp500ticker = '^GSPC'
	sp500desc = "S&P 500 Index: "
	sp500index = Share(sp500ticker)
	sp500price = sp500index.get_price()
	sp500change = sp500index.get_change()
	sp500open = sp500index.get_open()
	sp500percentchange = getPercentChange(sp500index, sp500change, sp500open)
	
	# if sp500percentchange >=bigmove:
	# 	print 'big change '+ str(sp500percentchange)
	# else:
	# 	print 'normal day ' + str(sp500percentchange)

	#return "ticker: " + sp500ticker, "price: " + sp500price, "change: " + sp500change, "open: " + sp500open, "percent change: " + str(sp500percentchange)
	return sp500percentchange

def getPercentChange(stock, change, getopen):
	if (change is not None) and (getopen is not None):
		tickerPercentChange = (float(change)/float(getopen))*100
		tickerPercentChange = round(tickerPercentChange, 2)
		return tickerPercentChange
	else:
		return 0


def getTop20ByPercent():
	#output.append(str(target[75].text))
	top20=[]
	top20.append(str(mysoup[212].text))
	top20.append(str(mysoup[217].text))
	top20.append(str(mysoup[222].text))
	top20.append(str(mysoup[227].text))
	top20.append(str(mysoup[232].text))
	top20.append(str(mysoup[237].text))
	top20.append(str(mysoup[242].text))
	top20.append(str(mysoup[247].text))
	top20.append(str(mysoup[252].text))
	top20.append(str(mysoup[257].text))
	top20.append(str(mysoup[262].text))
	top20.append(str(mysoup[267].text))
	top20.append(str(mysoup[272].text))
	top20.append(str(mysoup[277].text))
	top20.append(str(mysoup[282].text))
	top20.append(str(mysoup[287].text))
	top20.append(str(mysoup[292].text))
	top20.append(str(mysoup[297].text))
	top20.append(str(mysoup[302].text))
	top20.append(str(mysoup[307].text))

	#print t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20
	return top20

mypercent = 7.5
mysoup = getSoup()
top20bypercent = getTop20ByPercent()
daysp500percentchange = sp500info()
daysbeat = []
print "S&P 500 Index Percent Change: " + str(daysp500percentchange) + "%"
for item in top20bypercent:
	item = item[1:]
	if float(daysp500percentchange) >= float(item):
		count = count + 1
		daysbeat.append(str(item))
if count >= 1:
	print "Today was better than: " + str(count) + " days, in the top 20 returns for the S&P 500 ever!!"
else:
	print "Pretty normal day"



# i=0
# for item in mysoup:
# 	print i, item
# 	i+=1

#1, 212 - highest gain (11.58)
#2, 217, 10.79
#3, 222, 9.10 
#4, 227, 7.08
#5, 232, 6.92
#6, 237, 6.47
#7, 242, 6.37
#8, 247, 6.32,
#9, 252, 5.73
#10, 257, 5.42
#11, 262, 5.41
#12, 267, 5.33
#13, 272, 5.14
#14, 277, 5.12
#15, 282, 5.09
#16, 287, 5.02
#17, 292, 5.01
#18, 297, 4.93
#19, 302, 4.77
#20, 317, 4.76
#
#1, 313, -20.47
#2, 318, -9.03
#3, 323, -8.93
#4, 328, -8.81
#5, 333, -8.28
#6, 338, 7.62
#7, 343, -6.87
#8, 348, 6.80
#9, 353, 6.77
#10, 358, 6.71
#11, 363, 6.68
#12, 368, 6.66
#13, 373, 6.62
#14, 378, 6.12,
#15, 383, 6.12,
#16, 388, 6.10
#17, 393, 5.83
#18, 398, 5.74, 
#19, 403, 5.38
#20, 408, 5.28
#
