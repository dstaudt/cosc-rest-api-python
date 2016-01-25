import requests   # We use Python external "requests" module to do HTTP GET query
import json       # External JSON encoder and decode module
import sys        # For system-specific functions

requests.packages.urllib3.disable_warnings() # Disable warning message


# Step 1
# Change COSC IP to the one you are using
cosc_ip = "oscsandbox.cisco.com"

# Step 2
# Enter user name and password to get a secerety token
# If you assign username and password here you don't need to pass parameter when calling
username = "admin"
password = "1vtG@lw@y"

def get_token(ip=cosc_ip,uname = username,pword = password):
    """ 
    This function returns a new secerety token.
    Passing ip, username and password when use as standalone function
    to overwrite the default configuration 
    """ 
    # To get secerety token, the following along with 'x-www-form-urlencoded' encoding(select this 
    payload = {'grant_type': 'password', 'username': uname,'password':pword,'scope':'sdn'}
 
    # url for the post token request 
    post_url = "https://"+ip+"/controller-auth"
    
    # POST token request and response
    try:
        r = requests.post(post_url, data=payload,verify=False)
        response_json = r.json()
        # remove '#' if need to print out response to see detail
        # print ("Response Status: ",r.status_code)
        # print ("Response:",json.dumps(response_json,indent=4))
        
        # The token we need is the value of access_token attribute
        return response_json["access_token"]
    except:
        # Something wrong, cannot get token
        print ("Something wrong, cannot get token")
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()


