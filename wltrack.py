import ConfigParser
import os
from argparse import ArgumentParser 
from yahoo_finance import Share
import time
 

overridewarning = "You are attempting to override an already saved price.  Re-Run and specify -o to override purchase price"


def create_config(path):
    """
    Create a config file
    """
    config = ConfigParser.ConfigParser()
    config.add_section(myargs.ticker)
    config.set(myargs.ticker, "Init Tracking", mydate)
    config.set(myargs.ticker, "last change", mydate)
    config.set(myargs.ticker, "Purchase", gprice)
    config.set(myargs.ticker, "Support", myargs.support)
    config.set(myargs.ticker, "Resistance", myargs.resistance)
    config.set(myargs.ticker, "Stop", myargs.stop)
    config.set(myargs.ticker, "Target", myargs.target)
 
    with open(path, "wb") as config_file:
        config.write(config_file)
 
 
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
    print "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value)
    return value
 
 
def update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "wb") as config_file:
        config.write(config_file)
 
 
def delete_setting(path, section, setting):
    """
    Delete a setting
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "wb") as config_file:
        config.write(config_file)
 
def getArgs():
    global gticker, gprice, gsupport
    parser = ArgumentParser(description = 'Watchlist Filtering for Yahoo-Finance')
    parser.add_argument("-t", "--ticker", required=True, dest="ticker", help="ticker name to search for", metavar="ticker")
    parser.add_argument("-p", "--price", required=False, dest="price", help="specify to override the current price", metavar="price")
    parser.add_argument("-s", "--support", required=False, dest="support", help="init support level", metavar="support")
    parser.add_argument("-r", "--resistance", required=False, dest="resistance", help="init resistance level", metavar="resistance")
    parser.add_argument("-so", "--stopout", required=False, dest="stop", help="init stop level", metavar="stop")
    parser.add_argument("-x", "--exittarget", required=False, dest="target", help="init target level", metavar="target")
    parser.add_argument("-g", "--getconfig", required=False, action="store_true", dest="config", help="Specify to use config.ini file (overrides -s -r)")
    parser.add_argument("-o", "--override", required=False, action="store_true", dest="override", help="Specify to override original purchase price")
    #parser.add_argument("-r")
    args = parser.parse_args()
    gticker = args.ticker
    gprice = args.price
    gsupport = args.support
    return args
 
def getTime():
    #today = time.strftime('%Y-%m-%d %H:%M:%S')
    today = time.strftime('%Y-%m-%d')
    return today
 

def getStock(self):
    return Share(self)

def getPrice(self):
    return self.get_price()

def readConfig():
    global path
    parser = ConfigParser.ConfigParser()
    parser.read(path)
    for section_name in parser.sections():
        print 'Section: ', section_name
        print 'Options:', parser.options(section_name)
        for name, value in parser.items(section_name):
            print ' %s = %s ' % (name, value)
        print


#----------------------------------------------------------------------
if __name__ == "__main__":
    path = "3.ini"
    #font = get_setting(path, 'Settings', 'font')
    #font_size = get_setting(path, 'Settings', 'font_size')
 
    #update_setting(path, "Settings", "font_size", "12")
 
    #delete_setting(path, "Settings", "font_style")


#set args


    myargs = getArgs()
    mydate = getTime()
    
    mytime = getTime()
    mystock = getStock(myargs.ticker)
    myprice = getPrice(mystock)
    myargsprice = myargs.price
    #print myprice
    mysupport = myargs.support
    myresistance = myargs.resistance
    mytarget = myargs.target
    mystop = myargs.stop
    myexit = myargs.target


#readConfig()

myconfig = get_config(path) #This get's the config file; if none exists it creates one with create_config and populates it initally.
if myconfig is not None: 
    for section_name in myconfig.sections():
        # print 'Section: ', section_name #this prints out
        # print 'Options:', myconfig.options(section_name)
        # for name, value in myconfig.items(section_name):
        #     print ' %s = %s ' % (name, value)
        print
else:
    print "Empty"

if myargs.config is True: #if argument -g (get config) is specified, it reports back what that ticker has in the config file.

    #second block
    get_setting(path, myargs.ticker, 'Purchase') #3.ini, oled, Purhcase
    get_setting(path, myargs.ticker, 'support')
    get_setting(path, myargs.ticker, 'resistance')
    get_setting(path, myargs.ticker, 'stop')
    get_setting(path, myargs.ticker, 'target')
    get_setting(path, myargs.ticker, 'last change')
    get_setting(path, myargs.ticker, 'init tracking')

    #print "Got from config: " + myprice
else:
    if myargs.ticker is not "": # If the config file wasn't specified, and a a -t argument exists... so run...
        if myargs.price is None and myargs.override is True: #if myargs.price is none that means that we've done a price lookup and we're going to override whatever is in the config file
            update_setting(path, myargs.ticker, 'Purchase', myprice)
            update_setting(path, myargs.ticker, 'last change', mydate)
            if myargs.support is "":
                print "Empty!"
            else: 
                update_setting(path, myargs.ticker, 'support', mysupport)
            if myargs.resistance is not "":
                update_setting(path, myargs.ticker, 'resistance', myresistance)
            if myargs.stop is not None:
                update_setting(path, myargs.ticker, 'stop', mystop)
            if myargs.target is not none:
                update_setting(path, myargs.ticker, 'target', mytarget)
            print "Existing record updated: ", myargs.ticker, myprice
            #readConfig() #bugtesting 
        elif myargs.price > 0 and myargs.override is True: #if -p price has been specified and override is true...
                update_setting(path, myargs.ticker, 'Purchase', myargs.price)
                update_setting(path, myargs.ticker, 'last change', mydate)
                update_setting(path, myargs.ticker, 'support', mysupport)
                update_setting(path, myargs.ticker, 'resistance', myresistance)
                update_setting(path, myargs.ticker, 'stop', mystop)
                update_setting(path, myargs.ticker, 'target', mytarget)
                update_setting(path, myargs.ticker, 'last change', mytime)
        else:
            print overridewarning
            #readConfig()
        
