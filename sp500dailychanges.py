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
baseurl = 'http://finance.yahoo.com/q?s='
endurl = '&ql=1'

def scraper(ticker): #gets the real-time price from Yahoo Finance of the ticker passed to it 
	url = baseurl + ticker + endurl
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "lxml")
	target = soup.find("span", {"class": "time_rtq_ticker"}).span.contents
	target = target[0]
	return target


def getSoup(): #gets the list of largest daily percent moves in the S&P 500 index
	global url, target
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	target = soup.find("div", {"id": "mw-collapsible mw-shown"}) #gets DJIA instead of S&P 500
	target = soup.find_all("td")
	return target

def sp500info(): #gets the S&P 500 price, ticker, changes, etc.
	sp500ticker = '^GSPC' 
	sp500desc = "S&P 500 Index: "
	sp500index = Share(sp500ticker)
	#sp500price = sp500index.get_price()
	sp500price = scraper(sp500ticker)
	#sp500change = sp500index.get_change()
	sp500open = sp500index.get_open()
	#print sp500index.get_50day_moving_avg()
	#print sp500index.get_200day_moving_avg()
	#print sp500ma50, sp500ma200
	sp500price = str(sp500price).strip('[]')
	sp500price = sp500price.replace(",", "")
	#print(repr(sp500price)) #scrub the ticker for hidden values; troubleshooting
	sp500change = float(sp500price) - float(sp500open)
	sp500dayhigh = sp500index.get_days_high()
	sp500percentchange = getPercentChange(sp500index, sp500change, sp500open)

	return sp500percentchange, sp500dayhigh, sp500open, sp500change, sp500price, sp500index, sp500desc

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
	top20.append(str(mysoup[212].text)) #highest percent return day over
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
	top20.append(str(mysoup[307].text)) #Number 20 in the top percent returns ever list

	#print t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20
	return top20

def getBottom20ByPercent():
	bottom20=[]
	bottom20.append(str(mysoup[313].text)) #Worst percent performance of all time
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
	bottom20.append(str(mysoup[408].text)) #20th worst performance of all time

	return bottom20

def assessUpPerformance():
	daysbeat = []
	count = 0
	test = 0.01
	print "S&P 500 Index Percent Change: " + str(daysp500percentchange) + "%"
	print "S&P 500 Index Percent Move Significance: " + str(dailyupextremempercent)

	for item in top20bypercent:
		item = item[1:] #snips off preceding character - in this case, the "+" from +11.58
		if float(daysp500percentchange) >= float(item):
			count = count + 1
			daysbeat.append(str(item))
	if count >= 1:
		print "Today was better than: " + str(count) + " days, in the top 20 returns for the S&P 500 ever!!"
	elif  float(daysp500percentchange) > float(dailyupextremempercent):
		#print dailyupextremempercent, daysp500percentchange
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

def spSummary(percentchange, dayhigh, dayopen, daychange, currentprice, index, indexdesc):
	ticker = '^GSPC'
	realtime = scraper(ticker)
	#print realtime
	print indexdesc
	print "Price: " + currentprice
	print "Change: " + str(daychange)
	print "Percent Change: " + str(percentchange)
	print "Day High: " + dayhigh
	print "Day Low: " + dayopen
	print "--------------------------------------------------------------"



mypercent = 7.5
mysoup = getSoup()

# sp500percentchange, sp500dayhigh, sp500open, sp500change, sp500price, sp500index, sp500desc
daysp500percentchange, dayhighsp500, dayopensp500, daychangesp500, currentpricesp500, indexsp500, indessp500desc = sp500info()


if daysp500percentchange >= 0:
	#print "UP!"
	top20bypercent = getTop20ByPercent()
	spSummary(daysp500percentchange, dayhighsp500, dayopensp500, daychangesp500, currentpricesp500, indexsp500, indessp500desc)
	assessUpPerformance()
else:
	#print "Down!"
	bottom20bypercent = getBottom20ByPercent()
	spSummary(daysp500percentchange, dayhighsp500, dayopensp500, daychangesp500, currentpricesp500, indexsp500, indessp500desc)
	assessDownPerformance()

