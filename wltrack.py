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

def create_newrecord(path):
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
    parser.add_argument("-i", "--init", required=True, dest="init", help="init file to use", metavar="init")
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

def update_price():
    if myargs.price > 0:
        update_setting(path, myargs.ticker, 'Purchase', myargs.price)
    else:
        update_setting(path, myargs.ticker, 'Purchase', myprice)

def update_support():
    #if you specify a support level, update it.
    if myargs.support > 0:
        update_setting(path, myargs.ticker, 'support', myargs.support)

def update_resistance():
    if myargs.resistance > 0:
        update_setting(path, myargs.ticker, 'resistance', myargs.resistance)

def update_stop():
    if myargs.stop > 0:
        update_setting(path, myargs.ticker, 'stop', myargs.stop)

def update_exit():
    if myargs.target > 0:
        update_setting(path, myargs.ticker, 'target', myargs.target)

def update_stamp():
    if myargs.price > 0 or myargs.support > 0 or myargs.resistance > 0 or myargs.stop > 0 or myargs.target > 0:
        update_setting(path, myargs.ticker, 'last change', mytime)

def init_tracking():
    update_setting(path, myargs.ticker, 'init tracking', mytime)

#----------------------------------------------------------------------
if __name__ == "__main__":
    
    myargs = getArgs()
    path = myargs.init
    mydate = getTime()
    myconfig = get_config(path) #must have myargs and mydate already set
    mytime = getTime()
    mystock = getStock(myargs.ticker)
    myprice = getPrice(mystock)
    myargsprice = myargs.price
    mysupport = myargs.support
    myresistance = myargs.resistance
    mytarget = myargs.target
    mystop = myargs.stop
    myexit = myargs.target

    #If you're getting the config (-g), get the current config.
    if myargs.config is True: #if argument -g (get config) is specified, it reports back what that ticker has in the config file.
        print myargs.ticker
        #print get_setting()
        get_setting(path, myargs.ticker, 'Purchase') #3.ini, oled, Purhcase
        get_setting(path, myargs.ticker, 'support')
        get_setting(path, myargs.ticker, 'resistance')
        get_setting(path, myargs.ticker, 'stop')
        get_setting(path, myargs.ticker, 'target')
        get_setting(path, myargs.ticker, 'last change')
        get_setting(path, myargs.ticker, 'init tracking')
    else:

        parser = ConfigParser.ConfigParser()
        parser.read(path)

        print myargs.ticker
        if parser.has_section(myargs.ticker):
            update_price()
            update_support()
            update_resistance()
            update_stop()
            update_exit()
            update_stamp()            
        else:
            #print "nope!"
            parser.add_section(myargs.ticker)
            parser.set(myargs.ticker, "Init Tracking", mydate)
            parser.set(myargs.ticker, "last change", mydate)
            parser.set(myargs.ticker, "Purchase", gprice)
            parser.set(myargs.ticker, "Support", myargs.support)
            parser.set(myargs.ticker, "Resistance", myargs.resistance)
            parser.set(myargs.ticker, "Stop", myargs.stop)
            parser.set(myargs.ticker, "Target", myargs.target)
            with open(path, "wb") as config_file:
                parser.write(config_file)
