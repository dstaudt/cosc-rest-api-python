from cosc_config import * # Including cosc_config.py

# Get security token by using function created in cosc_config.py
token = get_token( )

# API base url
url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/"

try:
    r = requests.get(url,auth=('token',token),verify=False)      
    print ("Response Status: ",r.status_code)    # This is the http request status
    response_json = r.json() # Get the json-encoded content from response
    print ("Response:\r",json.dumps(response_json,indent=4))    # This is the entire response from the query
except:
    print ("Something wrong with the request!")


    
