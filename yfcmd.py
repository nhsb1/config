import mystuff
import futures
import realtime
from argparse import ArgumentParser
from yahoo_finance import Share
import yahoofinancecalc


def getArgs():
	parser = ArgumentParser(description = 'Get Realtime ticker from Yahoo-Finance')
	parser.add_argument("-t", "--ticker", required=False, dest="ticker", help="ticker for lookup", metavar="ticker")
	parser.add_argument("-f","--futures", dest="futures", help="Get futures", default=False, action="store_true")
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
	parser.add_argument("-d","--debug", dest="debug", help="debug", default=False, action="store_true")
	args = parser.parse_args()
	return args

myargs = getArgs()

if myargs.futures is True:
	mySoup = futures.getSoup()
	myFutures = futures.getFutures()
	futures.printReport()

if myargs.ticker is not None:

	stock = Share(myargs.ticker)
	
	if myargs.realtime is True:
		realtimequote = realtime.scraper(myargs.ticker)
		print realtimequote

	if myargs.price is True:
		price = stock.get_price()
		print price

	if myargs.volume is True:
		volume = stock.get_volume()
		print volume

	if myargs.change is True:
		change = stock.get_change()
		print change

	if myargs.avgvol is True:
		avgvolume = stock.get_avg_daily_volume()
		print avgvolume

	if myargs.short is True:
		short = stock.get_short_ratio()
		print short

	if myargs.peratio is True:
		pe = stock.get_price_earnings_ratio()
		print pe

	if myargs.exchange is True:
		exchange = stock.get_stock_exchange()

	if myargs.ma50 is True:
		ma50 = stock.get_50day_moving_avg()
		print ma50

	if myargs.ma200 is True:
		ma200 = stock.get_200day_moving_avg()
		print ma200

	if myargs.marketcap is True:
		marketcap = stock.get_market_cap()
		print marketcap

	if myargs.getopen is True:
		getopen = stock.get_open()
		print getopen

	if myargs.getbook is True:
		getbook = stock.get_book_value()
		print getbook

	if myargs.dividendshare is True:
		getdiv = stock.get_dividend_share()
		print getdiv

	if myargs.dividendyield is True:
		dividendyield = stock.get_dividend_yield()
		print dividendyield

	if myargs.eps is True:
		eps = stock.get_earnings_share()
		print eps

	if myargs.dayh is True:
		dayhigh = stock.get_days_high()
		print dayhigh

	if myargs.dayl is True:
		daylow = stock.get_days_low()
		print daylow

	if myargs.yearhigh is True:
		yearhigh = stock.get_year_high()
		print yearhigh

	if myargs.yearlow is True:
		yearlow = stock.get_year_low()
		print yearlow

	if myargs.ebitda is True:
		ebitda = stock.get_ebitda()
		print ebitda

	if myargs.ps is True:
		ps = stock.get_price_sales()
		print ps

	if myargs.peg is True:
		peg = stock.get_price_earnings_growth_ratio()
		print peg

	if myargs.percentchange is True:
		change = stock.get_change()
		getopen = stock.get_open()
		percentchange = yahoofinancecalc.getPercentChange(stock, change, getopen)
		print str(percentchange) + "%"

	if myargs.percentoffhigh is True:
		realtimequote = realtime.scraper(myargs.ticker)
		poh = yahoofinancecalc.offHigh(stock, realtimequote)
		print poh

	if myargs.percentofflow is True:
		realtimequote = realtime.scraper(myargs.ticker)
		yearlow = stock.get_year_low()
		pol = yahoofinancecalc.offlow(stock, realtimequote, yearlow)
		print pol

	if myargs.percentofaverage is True:
		avgvolume = stock.get_avg_daily_volume()
		volume = stock.get_volume()
		poa = yahoofinancecalc.ofAverageVolume(stock, avgvolume, volume)
		print str(poa) + "%" 

	if myargs.debug is True:
		debug = stock.get_price_sales()
		print debug





#print myargs.ticker, realtimequote, volume 