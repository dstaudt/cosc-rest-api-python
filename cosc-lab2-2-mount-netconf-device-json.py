from cosc_config import * # Including cosc_config.py

# Get security token by using function created in cosc_config.py
token = get_token( )

name = ""
ip = ""
port = ""
username = ""
password = ""
# API base url
url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/node/controller-config/yang-ext:mount/config:modules"

# take user input
print ('!!! For simplicity, the demo program will NOT verify the data format you entered, so please enter it carefully !!!\n')

name = input('=> Please use a unique name that easy for you to remember. We will use it for unmount API in later.\nEnter a device name: ')
name = name.replace(" ","") # ignore space
ip = input('=> Enter a device ip or DNS hostname: ')
ip = ip.replace(" ","") # ignore space
port = input('=> Enter a port number: ')
port = port.replace(" ","") # ignore space
username = input('=> Enter a device username: ')
username = username.replace(" ","") # ignore space
password = input('=> Enter a device password: ')
password = password.replace(" ","") # ignore space

json_payload = {
    "config:module": [
            {
                "name": name,
                "type": "odl-sal-netconf-connector-cfg:sal-netconf-connector",
                "odl-sal-netconf-connector-cfg:sleep-factor": 1.5,
                "odl-sal-netconf-connector-cfg:between-attempts-timeout-millis": 2000,
                "odl-sal-netconf-connector-cfg:address": ip,
                "odl-sal-netconf-connector-cfg:port": port,
                "odl-sal-netconf-connector-cfg:username": username,
                "odl-sal-netconf-connector-cfg:dom-registry": {
                    "type": "opendaylight-md-sal-dom:dom-broker-osgi-registry",
                    "name": "dom-broker"
                },
                "odl-sal-netconf-connector-cfg:client-dispatcher": {
                    "type": "odl-netconf-cfg:netconf-client-dispatcher",
                    "name": "global-netconf-dispatcher"
                },
                "odl-sal-netconf-connector-cfg:password": password,
                "odl-sal-netconf-connector-cfg:binding-registry": {
                    "type": "opendaylight-md-sal-binding:binding-broker-osgi-registry",
                    "name": "binding-osgi-broker"
                },
                "odl-sal-netconf-connector-cfg:tcp-only": False,
                "odl-sal-netconf-connector-cfg:event-executor": {
                    "type": "netty:netty-event-executor",
                    "name": "global-event-executor"
                },
                "odl-sal-netconf-connector-cfg:rpc-registry": {
                    "type": "opendaylight-md-sal-binding:binding-rpc-registry",
                    "name": "binding-rpc-broker"
                },
                "odl-sal-netconf-connector-cfg:processing-executor": {
                    "type": "threadpool:threadpool",
                    "name": "global-netconf-processing-executor"
                }
            }
        ]
}

# content type is JSON
headers = {'Content-Type': 'application/json'}
try:
    r = requests.post(url,auth=('token',token), headers=headers,data=json.dumps(json_payload),verify=False)
    print ("Response Status: ",r.status_code)    # This is the http request status
except:
    print ("Something wrong with the request!")





