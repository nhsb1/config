import mystuff
import futures
import realtime
from argparse import ArgumentParser
from yahoo_finance import Share
import yahoofinancecalc
import re
import newhighs


#.47 - 
# - added real-time percent change function (realtimePercentChangeWork)
#.46 - 
#- fixed futures output bug counter (counter to counter2)
#- added real-time change function (realtimeChangeWork)

#- added non-verbose mode; (e.g. "51.22", vs. "Realtimeprice: 51.22")

counter = 0 
counter2 = 0


def realtimeWork(ticker):
	selections.append('Realtime: ')
	subrealtimequote = realtime.scraper(myargs.ticker)
	output.append(subrealtimequote)
	return subrealtimequote

def priceWork(stock):
	selections.append('Delayed Price: ')
	subpricequote = stock.get_price()
	output.append(subpricequote)
	return subpricequote

def volumeWork(stock):
	volume = stock.get_volume()
	output.append(volume)
	selections.append('Volume: ')
	return volume

def changeWork(stock):
	change = stock.get_change()
	output.append(change)
	selections.append('Change: ')
	return change

def realtimeChangeWork(stock): #I didn't put this in the yahoofinancecalc module because of the realtime 
	rto = float(stock.get_open())
	rtp =  float(realtimeprice)
	realtimechange = yahoofinancecalc.getRealtimeChangeWork(rto, rtp)
	output.append(realtimechange)
	selections.append("RT Change: ")
	return realtimechange

def avgvolumeWork(stock):
	avgvolume = stock.get_avg_daily_volume()
	output.append(avgvolume)
	selections.append('Average Volume: ')
	return avgvolume

def shortWork(stock):
	short = stock.get_short_ratio()
	output.append(short)
	selections.append('Short ratio: ')
	return short

def peWork(stock):
	pe = stock.get_price_earnings_ratio()
	output.append(pe)
	selections.append('PE ratio: ')
	return pe

def exchangeWork(stock):
	exchange = stock.get_stock_exchange()
	output.append(exchange)
	selections.append('Exchange: ')
	return exchange
	
def ma50work(stock):
	ma50 = stock.get_50day_moving_avg()
	output.append(ma50)
	selections.append('50-day MA: ')
	return ma50

def ma200work(stock):
	ma200 = stock.get_200day_moving_avg()
	output.append(ma200)
	selections.append('200-day MA: ')
	return ma200

def marketcapWork(stock):
	marketcap = stock.get_market_cap()
	output.append(marketcap)
	selections.append('Marketcap: ')
	return marketcap

def openWork(stock):
	getopen = stock.get_open()
	output.append(getopen)
	selections.append('Open: ')
	return getopen

def bookWork(stock):
	getbook = stock.get_book_value()
	output.append(getbook)
	selections.append('Book value: ')
	return getbook

def dividendshareWork(stock):
	getdiv = stock.get_dividend_share()
	output.append(getdiv)
	selections.append('Dividend Share: ')
	return getdiv

def dividendyieldWork(stock):
	dividendyield = stock.get_dividend_yield()
	output.append(dividendyield)
	selections.append('Dividend yield: ')
	return dividendyield

def epsWork(stock):
	eps = stock.get_earnings_share()
	output.append(eps)
	selections.append('EPS: ')
	return eps

def dayhighWork(stock):
	dayhigh = stock.get_days_high()
	output.append(dayhigh)
	selections.append('Day high: ')
	return dayhigh

def daylowWork(stock):
	daylow = stock.get_days_low()
	output.append(daylow)
	selections.append('Day low: ')
	return daylow	

def yearhighWork(stock):
	yearhigh = stock.get_year_high()
	output.append(yearhigh)
	selections.append('52-week High: ')
	return yearhigh

def yearlowWork(stock):
	yearlow = stock.get_year_low()
	output.append(yearlow)
	selections.append('52-week low: ')
	return yearlow

def ebitdaWork(stock):
	ebitda = stock.get_ebitda()
	output.append(ebitda)
	selections.append('ebitda: ')
	return ebitda

def psWork(stock):
	ps = stock.get_price_sales()
	output.append(ps)
	selections.append('Price to Sales: ')
	return ps

def pegWork(stock):
	peg = stock.get_price_earnings_growth_ratio()
	output.append(peg)
	selections.append('PEG: ')
	return peg

def percentchangeWork(stock):
	change = stock.get_change()
	getopen = stock.get_open()
	percentchange = yahoofinancecalc.getPercentChange(stock, change, getopen)
	percentchange = str(percentchange) + "%"
	output.append(percentchange)
	selections.append('Percent Change: ')
	return percentchange

def realtimePercentChangeWork(stock):
	getopen = float(stock.get_open())
	rtp = float(realtimeprice)
	change = rtp - getopen
	realtimechange = yahoofinancecalc.getPercentChange(stock, change, getopen)
	realtimechange = str(realtimechange) + "%"
	output.append(realtimechange)
	selections.append("RT Percent Change: ")
	return realtimechange

def pohWork(stock):
	realtimequote = realtime.scraper(myargs.ticker)
	poh = yahoofinancecalc.offHigh(stock, realtimequote)
	output.append(poh)
	selections.append('Percent off high: ')
	return poh

def polWork(stock):
	realtimequote = realtime.scraper(myargs.ticker)
	yearlow = stock.get_year_low()
	pol = yahoofinancecalc.offlow(stock, realtimequote, yearlow)
	output.append(pol)
	selections.append('Percent off low: ')
	return pol

def poaWork(stock):
	avgvolume = stock.get_avg_daily_volume()
	volume = stock.get_volume()
	poa = yahoofinancecalc.ofAverageVolume(stock, avgvolume, volume)
	poa = str(poa) + "%"
	output.append(poa)
	selections.append('Percent of Average: ')
	return poa 

def getArgs():
	parser = ArgumentParser(description = 'Quote CMD')
	parser.add_argument("-t", "--ticker", required=False, dest="ticker", help="ticker for lookup", metavar="ticker")
	parser.add_argument("-f","--futures", dest="futures", help="Get all futures", default=False, action="store_true")
	parser.add_argument("-v","--volume", dest="volume", help="Get volume", default=False, action="store_true")
	parser.add_argument("-c","--change", dest="change", help="Get day's change", default=False, action="store_true")
	parser.add_argument("-av","--avgvolume", dest="avgvol", help="Get avgerage volume", default=False, action="store_true")
	parser.add_argument("-r","--realtime", dest="realtime", help="Get realtime price", default=False, action="store_true")
	parser.add_argument("-p","--price", dest="price", help="Get delayed price", default=False, action="store_true")
	parser.add_argument("-sr","--short", dest="short", help="Get short ratio", default=False, action="store_true")
	parser.add_argument("-pe","--peratio", dest="peratio", help="Get PE ratio", default=False, action="store_true")
	parser.add_argument("-ex","--exchange", dest="exchange", help="Get listed exchange", default=False, action="store_true")
	parser.add_argument("-ma50","--movingaverage50", dest="ma50", help="Get 50-day moving average", default=False, action="store_true")
	parser.add_argument("-ma200","--movingaverage200", dest="ma200", help="Get 200-day moving average", default=False, action="store_true")
	parser.add_argument("-mc","--marketcap", dest="marketcap", help="Get marketcap", default=False, action="store_true")
	parser.add_argument("-go","--getopen", dest="getopen", help="Get opening price", default=False, action="store_true")
	parser.add_argument("-book","--getbook", dest="getbook", help="Get book value", default=False, action="store_true")
	parser.add_argument("-div","--dividendshare", dest="dividendshare", help="Get dividend per share", default=False, action="store_true")
	parser.add_argument("-divy","--dividendyield", dest="dividendyield", help="Get dividend dividend yield", default=False, action="store_true")
	parser.add_argument("-eps","--earnings", dest="eps", help="Get earnings per share", default=False, action="store_true")
	parser.add_argument("-dh","--dayhigh", dest="dayh", help="Get day high", default=False, action="store_true")
	parser.add_argument("-dl","--daylow", dest="dayl", help="Get day low", default=False, action="store_true")
	parser.add_argument("-yh","--yearhigh", dest="yearhigh", help="Get year high", default=False, action="store_true")
	parser.add_argument("-yl","--yearlow", dest="yearlow", help="Get year low", default=False, action="store_true")
	parser.add_argument("-ebitda","--ebitda", dest="ebitda", help="Get ebitda", default=False, action="store_true")	
	parser.add_argument("-ps","--ps", dest="ps", help="Get price to sales", default=False, action="store_true")
	parser.add_argument("-peg","--pegratio", dest="peg", help="PEG ratio", default=False, action="store_true")
	parser.add_argument("-pc","--percentchange", dest="percentchange", help="Percent change", default=False, action="store_true")
	parser.add_argument("-poh","--percentoffhigh", dest="percentoffhigh", help="Percent off high", default=False, action="store_true")
	parser.add_argument("-pol","--percentofflow", dest="percentofflow", help="Percent off low", default=False, action="store_true")
	parser.add_argument("-poa","--percentofaverage", dest="percentofaverage", help="Percent of average volume", default=False, action="store_true")
	parser.add_argument("-fsp","--spfutures", dest="spfutures", help="Get S&P futures", default=False, action="store_true")
	parser.add_argument("-fdow","--dowfutures", dest="dowfutures", help="Get DOW futures", default=False, action="store_true")
	parser.add_argument("-fnas","--nasdaqfutures", dest="nasdaqfutures", help="Get NASDAQ futures", default=False, action="store_true")
	parser.add_argument("-frow","--rowfutures", dest="rowfutures", help="Get rest of world futures", default=False, action="store_true")
	parser.add_argument("-nh","--newhighs", dest="newhighs", help="Prints a list of new highs.  If run with -t, only prints ticker if that ticker is in the new high list", default=False, action="store_true")
	parser.add_argument("-d","--debug", dest="debug", help="debug", default=False, action="store_true")
	args = parser.parse_args()
	return args


myargs = getArgs()
output = []
selections = []

if myargs.newhighs is True:
	nhsoup = newhighs.getSoup()
	newhighlist = newhighs.getTickers(nhsoup)
	if myargs.ticker is not None:
		for item in newhighlist:
			if item.lower() == myargs.ticker.lower():
				print item
	else:
		for item in newhighlist:
			print item




	


#mysoup = getSoup()
# mytickers = []
# mytickers = getTickers(mysoup)

# for item in mytickers:
# 	print item

if myargs.futures is True:
	mySoup = futures.getSoup()

	myFutures = futures.getSPFutures(), futures.getDOWFutures(), futures.getNASDAQFutures(), futures.getROWFutures()
	futures.printfuturesReport()

#if any of the futures flag (-fsp) have been specified getSoup the webpage that provides futures
if myargs.spfutures is True or myargs.dowfutures is True or myargs.nasdaqfutures is True or myargs.rowfutures is True:
	mySoup = futures.getSoup()

if myargs.spfutures is True:
	#mySoup = futures.getSoup()
	futures.getSPFutures()

	
if myargs.dowfutures is True:
	#mySoup = futures.getSoup()
	myFutures = futures.getDOWFutures()

if myargs.nasdaqfutures is True:
	myFutures = futures.getNASDAQFutures()

if myargs.rowfutures is True:
	myFutures = futures.getROWFutures()

if myargs.ticker is not None:

	stock = Share(myargs.ticker)
	
	if myargs.realtime is True:
		realtimeprice = realtimeWork(myargs.ticker)

	if myargs.price is True:
		priceWork(stock)

	if myargs.volume is True:
		volumeWork(stock)
		
	if myargs.change is True and myargs.price is True:
		changeWork(stock)
	elif myargs.change is True and myargs.realtime is True: #If you've specified the realtime flag WITH change, get the change in realtime terms.
		realtimeChangeWork(stock)
		
	if myargs.avgvol is True:
		avgvolumeWork(stock)

	if myargs.short is True:
		shortWork(stock)

	if myargs.peratio is True:
		peWork(stock)

	if myargs.exchange is True:
		exchangeWork(stock)
		
	if myargs.ma50 is True:
		ma50work(stock)

	if myargs.ma200 is True:
		ma200work(stock)
		
	if myargs.marketcap is True:
		marketcapWork(stock)
		
	if myargs.getopen is True:
		openWork(stock)

	if myargs.getbook is True:
		bookWork(stock)

	if myargs.dividendshare is True:
		dividendshareWork(stock)

	if myargs.dividendyield is True:
		dividendyieldWork(stock)

	if myargs.eps is True:
		epsWork(stock)

	if myargs.dayh is True:
		dayhighWork(stock)

	if myargs.dayl is True:
		daylowWork(stock)

	if myargs.yearhigh is True:
		yearhighWork(stock)
		
	if myargs.yearlow is True:
		yearlowWork(stock)

	if myargs.ebitda is True:
		ebitdaWork(stock)
		
	if myargs.ps is True:
		psWork(stock)

	if myargs.peg is True:
		pegWork(stock)
		
	if myargs.percentchange is True and myargs.price is True:
		percentchangeWork(stock)
	elif myargs.percentchange is True and myargs.realtime is True:
		#print "Hi!"
		realtimePercentChangeWork(stock)

	if myargs.percentoffhigh is True:
		pohWork(stock)

	if myargs.percentofflow is True:
		polWork(stock)
		
	if myargs.percentofaverage is True:
		poaWork(stock)

	if myargs.debug is True:
		debug = stock.get_price_sales()
		print debug


for item in selections:
	print item, output[counter]
	counter = counter + 1

for item in futures.selections:
	print item, futures.output[counter2]
	counter2 = counter2 + 1
