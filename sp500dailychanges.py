#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import html5lib
import time
from argparse import ArgumentParser 

url = 'https://en.wikipedia.org/wiki/List_of_largest_daily_changes_in_the_S%26P_500_Index'
count = 0

def getSoup():
	global url, target
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	target = soup.find("div", {"id": "mw-collapsible mw-shown"}) #gets DJIA instead of S&P 500
	target = soup.find_all("td")
	return target

# def getSoup2():
# 	global url, target
# 	page = urllib2.urlopen(url)
# 	soup = BeautifulSoup(page, 'html.parser')
# 	target = soup.find("div", {"id": "mw-collapsible mw-shown"}) #gets DJIA instead of S&P 500
# 	target = soup.find_all("td")
# 	return target

mysoup = getSoup()
i=0
for item in mysoup:
	print i, item
	i+=1

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
