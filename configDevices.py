#!/usr/bin/python 
# -*- coding: utf-8 -*-f
import ConfigParser

import cgi, cgitb
import Cookie, os, time 

cgitb.enable()
form=cgi.FieldStorage()

config= ConfigParser.RawConfigParser()

# Uncomment add if you create new section or uncomment read when you want to update
config.add_section('NumDevice')
config.add_section('Device1')

#config.read(r'setting/devices.ini')

config.set('NumDevice','amount','4')

config.set('Device1','name','Temp.')
config.set('Device1','api-key','ABCDEF')
config.set('Device1','alert_type','max')
config.set('Device1','decision_point','50')
config.set('Device1','status','on')

# use 'ab' mode for append , use 'wb' mode for renew
with open(r'setting/devices.ini', 'wb') as configfile:
    config.write(configfile)
