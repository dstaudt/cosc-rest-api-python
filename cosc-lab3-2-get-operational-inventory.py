from cosc_config import * # Including cosc_config.py

# Get security token by using function created in cosc_config.py
token = get_token( )

# API base url
# url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/node/openflow:387523572651296/table/0/flow/1"
url = "https://"+cosc_ip+"/controller/restconf/operational/opendaylight-inventory:nodes"
try:
    r = requests.get(url,auth=('token',token),verify=False)      
    response_json = r.json() # Get the json-encoded content from response
    print ("Response Status: ",r.status_code)    # This is the http request status
    # print ("Response:\r",json.dumps(response_json,indent=4))    # This is the entire response from the query
    nodes=response_json["nodes"]["node"]
    print ("\n**** The following is 'operational store' inventory ****\n")
    for item in nodes:
        if 'id' in item:
            print ("Node ID:",item["id"])
        if 'netconf-node-inventory:manufacturer' in item:           
            print ("Vender: ",item["netconf-node-inventory:manufacturer"])
        if 'netconf-node-inventory:hardware' in item:
            print ("Platform ID: ",item["netconf-node-inventory:hardware"])
        if 'netconf-node-inventory:serial-number' in item:
            print ("Serial Number: ",item["netconf-node-inventory:serial-number"])
        print ("\n")
except:
    print ("Something wrong with the request!")


    
