from cosc_config import * # Including cosc_config.py

# Get the security token by using the function created in cosc_config.py
token = get_token( )

# API base url
url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/"

try:
    r = requests.get(url,auth=('token',token),verify=False)
    response_json = r.json() # Get the json-encoded content from response
    print ("Response Status: ",r.status_code)    # This is the http request status
    print ("\n**** The following is 'config store' inventory ****\n")
    nodes=response_json["nodes"]["node"]
    for item in nodes:
        print ("Node ID: ",item["id"])   
except:
    print ("Something wrong with the request!")



