#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html5lib
import time
from argparse import ArgumentParser 
from yahoo_finance import Share

#source for "significance" of daily performance: http://seekingalpha.com/article/167991-s-and-p-500-60-years-of-monthly-and-daily-percentage-price-changes?page=2

url = 'https://en.wikipedia.org/wiki/List_of_largest_daily_changes_in_the_S%26P_500_Index'

dailyupextremempercent = 1.01
dailydownextremepercent = -.98

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

def getBottom20ByPercent():
	bottom20=[]
	bottom20.append(str(mysoup[313].text))
	bottom20.append(str(mysoup[318].text))
	bottom20.append(str(mysoup[323].text))
	bottom20.append(str(mysoup[328].text))
	bottom20.append(str(mysoup[333].text))
	bottom20.append(str(mysoup[338].text))
	bottom20.append(str(mysoup[343].text))
	bottom20.append(str(mysoup[348].text))
	bottom20.append(str(mysoup[353].text))
	bottom20.append(str(mysoup[358].text))
	bottom20.append(str(mysoup[363].text))
	bottom20.append(str(mysoup[368].text))
	bottom20.append(str(mysoup[373].text))
	bottom20.append(str(mysoup[378].text))
	bottom20.append(str(mysoup[383].text))
	bottom20.append(str(mysoup[388].text))
	bottom20.append(str(mysoup[393].text))
	bottom20.append(str(mysoup[398].text))
	bottom20.append(str(mysoup[403].text))
	bottom20.append(str(mysoup[408].text))

	return bottom20

def assessUpPerformance():
	daysbeat = []
	count = 0
	test = 0.01
	print "S&P 500 Index Percent Change: " + str(daysp500percentchange) + "%"
	print "S&P 500 Index Percent Move Significance: " + str(dailyupextremempercent)

	for item in top20bypercent:
		item = item[1:]
		if float(daysp500percentchange) >= float(item):
			count = count + 1
			daysbeat.append(str(item))
	if count >= 1:
		print "Today was better than: " + str(count) + " days, in the top 20 returns for the S&P 500 ever!!"
	elif  float(daysp500percentchange) > float(dailyupextremempercent):
		print dailyupextremempercent, daysp500percentchange
		print str(daysp500percentchange) + " is significant in terms of daily price movement!"
	else:
		print "Assessment: Normal price action in the S&P 500 index. "

def assessDownPerformance():
	daysbeat = []
	count = 0
	print "S&P 500 Index Percent Change: " + str(daysp500percentchange) + "%"
	print "S&P 500 Index Percent Move Significance: " + str(dailydownextremepercent)
	for item in bottom20bypercent:
		item = item[1:]
		if float(daysp500percentchange) >= float(item):
			count = count + 1
			daysbeat.append(str(item))
	if count >= 1:
		print "Today was worse than: " + str(count) + " days, in the BOTTOM 20 returns for the S&P 500 ever!!"
	elif float(dailydownextremepercent) >= float(daysp500percentchange):
		print str(daysp500percentchange) + " is significant in terms of daily price movement!"  
	else:
		print "Assessment: Normal price action in the S&P 500 index. "


mypercent = 7.5
mysoup = getSoup()

daysp500percentchange = sp500info()
#print daysp500percentchange

if daysp500percentchange >= 0:
	#print "UP!"
	top20bypercent = getTop20ByPercent()
	assessUpPerformance()
else:
	#print "Down!"
	bottom20bypercent = getBottom20ByPercent()
	assessDownPerformance()

