#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html5lib
import time
from argparse import ArgumentParser 

url = 'http://www.barchart.com/stocks/high.php?_dtp1=0'

def getSoup():
	global url, target
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html5lib')
	target = soup.find("table", {"class": "datatable js"}) #good start
	target = soup.find_all('tr class')
	count = 0
	# for item in target:
	# 	print str(count) + "alpha", item
	# 	count = count + 1 
	#print target[76]


mysoup = getSoup()
print target

#print mysoup

