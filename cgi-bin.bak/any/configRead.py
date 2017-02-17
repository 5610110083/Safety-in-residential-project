import ConfigParser

Config = ConfigParser.ConfigParser()
setting = Config.read("setting\config.ini")
settingSec = Config.sections()
print settingSec

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

try:
	'''
	USERNAME = Config.get('LINE', 'USERNAME')
	PASSWORD = Config.get('LINE', 'PASSWORD')
	GROUPNAME = Config.get('LINE', 'GROUPNAME')
	print USERNAME 
	print PASSWORD 
	print GROUPNAME
	'''
	LINE = ConfigSectionMap('LINE')
	#print LINE
	print LINE['username']
	print LINE['password']
	print LINE['groupname']
except:
	print 'Data not found.'



