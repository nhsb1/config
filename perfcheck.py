#!/usr/bin/env python
import ConfigParser
import os
from argparse import ArgumentParser 
from yahoo_finance import Share
import time

currentrelease = ".82-2"


def assess():
	purchaseprice = get_setting(path, ticker, 'Purchase') #3.ini, oled, Purhcase
	support = get_setting(path, ticker, 'support')
	resistance= get_setting(path, ticker, 'resistance')
	stop = get_setting(path, ticker, 'stop')
	target = get_setting(path, ticker, 'target')
	#if get_setting(path, ticker, 'last change'):
	#	lastchange = get_setting(path, ticker, 'last change')
	startdate = get_setting(path, ticker, 'init tracking')
	return purchaseprice, support, resistance, stop, target, startdate


def readConfig(path):
    #global path
    parser = ConfigParser.ConfigParser()
    parser.read(path)
    for section_name in parser.sections():
        #print 'Section: ', section_name
        #print 'Options:', parser.options(section_name)
        for name, value in parser.items(section_name):
            print ' %s = %s ' % (name, value)
        print

def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)
 
    config = ConfigParser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    """
    Print out a setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    #print "{section} {setting} is {value}".format(
    #    section=section, setting=setting, value=value)
    return value
 

def getArgs():
    parser = ArgumentParser(description = currentrelease)
    parser.add_argument("-i", "--init", required=True, dest="init", help="init file to use", metavar="init")
    parser.add_argument("-s", "--shares", required=False, dest="shares", help="Shares held", metavar="init")
    parser.add_argument("-t", "--ticker", required=True, dest="ticker", help="ticker to check", metavar="ticker")
    parser.add_argument("-a", "--assess", required=False, dest="assess", help="assess performance", action="store_true")
    parser.add_argument("-ma","--movingaverage", dest="ma", help="Gets moving average; specify either 50 or 200 (e.g. -ma 200, -ma 50)", default=[], action='append')
    parser.add_argument("-d", "--debug", required=False, dest="debug", help="prints contents of ini file", action="store_true")
    args = parser.parse_args()
    return args

def getStock(self):
    return Share(self)

def getPrice(self):
    return self.get_price()

def priceperf(currentprice, purchaseprice):
	if currentprice >= purchaseprice:
		#print currentprice, purchaseprice
		profitloss = float(currentprice) - float(purchaseprice)
	else:
		#print currentprice, purchaseprice
		loss = float(purchaseprice) - float(currentprice)
		loss = (loss)*-1
		profitloss = loss
	return profitloss	

def currentPriceReport(currentprice):
	print "Current Price: " + currentprice

def pnlReport(currentprice, purchaseprice):
	pnl = priceperf(currentprice, purchaseprice)
	print "Profit/Loss: " + str(pnl)

def supportReport(currentprice, support):
	print "Support Set: " + str(support)

def stopReport(currentprice, stop):
	print "Stop Set: " + str(stop)

def resistanceReport(currentprice, resistance):
	print "Resistance Set: " + str(resistance)

def targetReport(currentprice, target):
	print "Target: " + str(target)

def stopAction(currentprice, stop):
	if stop > currentprice:
		stoploss = float(stop) - float(currentprice)
		#print "STOP VIOLATION: SELL!, LOSS: " + str(stoploss)
	else:
		stoploss = 0
	return stoploss

def targetAction(currentprice, target, purchaseprice):
	if currentprice > target:
		profit = float(currentprice) - float(purchaseprice)
		#print str(currentprice) + "+" str(purchaseprice)
		#print "TARGET HIT: SELL!, PROFIT: " + str(profit)
	else:
		profit = 0
	return profit

def targetHit(target):
	return "Target hit at " + target + ", sell!"

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


#----------------------------------------------------------------------
if __name__ == "__main__":
	myargs = getArgs()
	ticker = myargs.ticker
	path = myargs.init
	#print path

	if myargs.init:
		config = get_config(path)
		#print config

	if myargs.ticker:
		purchaseprice, support, resistance, stop, target, startdate = assess()
		#print purchaseprice
		stock = getStock(ticker)
		currentprice = getPrice(stock)
		currentPriceReport(currentprice)
		
		pnlReport(currentprice, purchaseprice)
		stopReport(currentprice, stop)
		resistanceReport(currentprice, resistance)
		supportReport(currentprice, resistance)
		saloss = stopAction(currentprice, stop)
		if saloss is not 0:
			print "STOP VIOLATION: SELL!, LOSS: " + str(saloss)

		targetReport(currentprice, target)
		#print target + "!!!!!!!!"
		targetAction(currentprice, target, purchaseprice)
		if myargs.shares:
			shares = myargs.shares
			if stopAction(currentprice, stop) > 0:
				myloss = stopAction(currentprice, stop)
				currentloss =  float(myloss) * float(shares)
				print "Current Loss: " + str(currentloss)
			if targetAction(currentprice, target, purchaseprice) >0:
				myprofit = targetAction(currentprice, target, purchaseprice)
				currentprofit = float(myprofit) * float(shares)
				print "Current Profit: " + str(currentprofit)
				print targetHit(target)
			
	if myargs.ma:
		for item in myargs.ma:
			if item == '50':
				ma50work(stock)
			elif item == '200':
				ma200work(stock)
			else:
				print "Specified an invalid moving average (-ma 50 -ma 200 are valid)"		

	
	if myargs.debug:
		readConfig(path)


	if myargs.assess:
		myperf = assess()
		



