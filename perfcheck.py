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
    parser.add_argument("-t", "--ticker", required=True, dest="ticker", help="ticker to check", metavar="ticker")
    parser.add_argument("-a", "--assess", required=False, dest="assess", help="assess performance", action="store_true")
    parser.add_argument("-d", "--debug", required=False, dest="debug", help="prints contents of ini file", action="store_true")
    args = parser.parse_args()
    return args

def getStock(self):
    return Share(self)

def getPrice(self):
    return self.get_price()

def priceperf(currentprice, purchaseprice):
	if currentprice >= purchaseprice:
		print currentprice, purchaseprice
		profitloss = float(currentprice) - float(purchaseprice)
	else:
		print currentprice, purchaseprice
		loss = float(purchaseprice) - float(currentprice)
		loss = (loss)*-1
		profitloss = loss
	return profitloss	

 

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
		pnl = priceperf(currentprice, purchaseprice)
		print pnl





	if myargs.debug:
		readConfig(path)


	if myargs.assess:
		myperf = assess()
		print myperf



