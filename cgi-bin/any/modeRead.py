import ConfigParser

Config = ConfigParser.ConfigParser()
setting = Config.read('setting/config.ini')
settingSec = Config.sections()
#print settingSec

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def readMode():
	try:
		MODE = ConfigSectionMap('MODE')
		#print MODE
		print MODE['mode']

	except:
		print 'Data not found.'

readMode()



