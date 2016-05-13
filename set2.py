import ConfigParser
import os
from argparse import ArgumentParser 
from yahoo_finance import Share
import time


gticker = ""
gprice = ""
gsupport = ""
 
#----------------------------------------------------------------------
def createConfig(path):
    """
    Create a config file
    """
    global gticker, gprice
    config = ConfigParser.ConfigParser()
    config.add_section(gticker)
    config.set(gticker, "Init Tracking", mydate)
    config.set(gticker, "Purchase", gprice)
    config.set(gticker, "Support", myargs.support)
    config.set(gticker, "Resistance", myargs.resistance)
    config.set(gticker, "Stop", myargs.stop)
    config.set(gticker, "Target", myargs.target)
    # config.set("Settings", "font_size", "10")
    # config.set("Settings", "font_style", "Normal")
    # config.set("Settings", "font_info",
    #            "You are using %(font)s at %(font_size)s pt")
 
    with open(path, "wb") as config_file:
        config.write(config_file)
 
#----------------------------------------------------------------------
def crudConfig(path):
    """
    Create, read, update, delete config
    """
    global gticker, gprice
    if not os.path.exists(path):
        createConfig(path)
 
    config = ConfigParser.ConfigParser()
    config.read(path)

    if config.has_section(gticker):
        #print "Has Section"
        config.set(gticker, "Purchase", gprice)
        config.set(gticker, "Support", myargs.support)
        config.set(gticker, "Resistance", myargs.resistance)
        config.set(gticker, "Stop", myargs.stop)
        config.set(gticker, "Target", myargs.target)
        config.set(gticker, "Last Change", mydate)
    else:
        config.add_section(gticker)
        config.set(gticker, "Purchase", gprice)
        config.set(gticker, "Support", myargs.support)
        config.set(gticker, "Resistance", myargs.resistance)
        config.set(gticker, "Init Tracking", mydate)
        config.set(gticker, "Stop", myargs.stop)
        config.set(gticker, "Target", myargs.target)

    #config.add_section(gticker)
    #config.set(gticker, "Purchase", gprice )
 
    # read some values from the config
    #font = config.get("Settings", "font")
    #font_size = config.get("Settings", "font_size")
 
    # change a value in the config
    #config.set("Settings", "font_size", "12")
 
    # delete a value from the config
    #config.remove_option("Settings", "font_style")
 
    # write changes back to the config file
    with open(path, "wb") as config_file:
        config.write(config_file)


#----------------------------------------------------------------------

def getTime():
    #today = time.strftime('%Y-%m-%d %H:%M:%S')
    today = time.strftime('%Y-%m-%d')
    return today


def getStock(self):
    return Share(self)

def getPrice(self):
    return self.get_price()

def getArgs():
    global gticker, gprice, gsupport
    parser = ArgumentParser(description = 'Watchlist Filtering for Yahoo-Finance')
    parser.add_argument("-t", "--ticker", required=True, dest="ticker", help="ticker name to search for", metavar="ticker")
    parser.add_argument("-p", "--price", required=False, dest="price", help="specify to override the current price", metavar="price")
    parser.add_argument("-s", "--support", required=False, dest="support", help="init support level", metavar="support")
    parser.add_argument("-r", "--resistance", required=False, dest="resistance", help="init resistance level", metavar="resistance")
    parser.add_argument("-so", "--stopout", required=False, dest="stop", help="init stop level", metavar="stop")
    parser.add_argument("-x", "--exittarget", required=False, dest="target", help="init target level", metavar="target")
    #parser.add_argument("-r")
    args = parser.parse_args()
    gticker = args.ticker
    gprice = args.price
    gsupport = args.support
    return args


if __name__ == "__main__":
    path = "2.ini"
    # blah = getArgs()
    # print "getargs stuff:" + str(blah)
    # print "getargs.price: " + str(blah.price)
    # print "getargs.ticker: " + str(blah.ticker)
    myargs = getArgs()
    mydate = getTime()
    print mydate  
    print gticker, gprice, gsupport
    if myargs.ticker is not "": #better than using a global variable; myargs init'd as getArgs returns stuf like myargs.ticker
        #ticker = args.ticker
        mystock = getStock(gticker)
        #print "Gprice is: " + str(gprice)
        if gprice is None:
            gprice = getPrice(mystock)
            print gprice
            crudConfig(path)
        else:
            crudConfig(path)



# def delete_setting(path, section, setting):
#     """
#     Delete a setting
#     """
#     config = get_config(path)
#     config.remove_option(section, setting)
#     with open(path, "wb") as config_file:
#         config.write(config_file)
 
 
 
 
# #----------------------------------------------------------------------
# if __name__ == "__main__":
#     path = "settings.ini"
#     font = get_setting(path, 'Settings', 'font')
#     font_size = get_setting(path, 'Settings', 'font_size')
 
#     update_setting(path, "Settings", "font_size", "12")
 
#     delete_setting(path, "Settings", "font_style")