import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../../config/config.ini'))

print config.sections()

try:
	USERNAME = config.get('LINE', 'USERNAME')
	PASSWORD = config.get('LINE', 'PASSWORD')
	GROUPNAME = config.get('LINE', 'GROUPNAME')
	print USERNAME
	print PASSWORD
	print GROUPNAME
except:
	print 'Data not found.'
  
