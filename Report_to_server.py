import requests
import urllib

def sent_data(value):
    # Login
    url = 'http://siczones.coe.psu.ac.th/cgi-bin/UploadThingSpeakWithSensor.py'
    values = {'key': 'abcd',
              'Field4': value}
    try:
        r = requests.post(url, data=values)
        #print r.content
        print 'Report to server success'
    except:
        print 'Report to server failed.'
########################################################################

#scan input
print '============ Powered by Siczones ============'
sent_data(4)
########################################################################
