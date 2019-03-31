import time
import httplib, urllib
import json
import sys

sys.path.append('/home/pi/rpi/code/Package')

#---Device data on MCS Platform---
deviceId = "DKbFfFn9"
deviceKey = "MmcohoTcp8SYShus"


#---Use HTTP's POST Method to send data to MCS---
def post_to_mcs(payload):                                                   
    headers = {"Content-type": "application/json","deviceKey": deviceKey}
    not_connected = True
    while(not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = False
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers)
    response = conn.getresponse()
    #print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

#---Use HTTP's GET Method to get data from MCS---
def get_from_mcs(ID):
    headers = {"Content-type": "application/json","deviceKey": deviceKey}
    not_connected = True
    while(not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = False
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)
    
    
    conn.request("GET", "/mcs/v2/devices/" + deviceId + "/datachannels/"+ ID +"/datapoints","",headers)
    response = conn.getresponse()
    #print( response.status, response.reason, time.strftime("%c"))
    data = response.read()
    return data
    conn.close()



def local_to_cloud(data,ID):
    payload =  {"datapoints": [{"dataChnId":ID,"values":{"value":data}}]}
    post_to_mcs(payload)


def cloud_to_local(ID):
    raw = get_from_mcs(ID)
    data = json.loads(raw)
    data = data['dataChannels']
    data = data[0]
    data = data['dataPoints']
    data = data[0]
    data = data['values']
    data = data['value']

    #print data
    return data




