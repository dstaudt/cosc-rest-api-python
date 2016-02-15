import requests   # We use Python "requests" module to do HTTP GET query
import json

requests.packages.urllib3.disable_warnings() # disable warning message
username = 'admin'
password = 'C!sc0123'

# To get secerety token, the following along with 'x-www-form-urlencoded' encoding(select this when using POSTMAN)
payload = {'grant_type': 'password', 'username': username,'password':password,'scope':'sdn'}
r = requests.post("https://oscsandbox.cisco.com/controller-auth", data=payload,verify=False)
# responase status
print ("Response Status: ",r.status_code)
response_json = r.json()

# response
print ("Response:",json.dumps(response_json,indent=4))

# The token we need is the value of access_token attribute
token = response_json["access_token"]
print ("token :",token)


