from cosc_config import * # Including cosc_config.py

# Get security token by using function created in cosc_config.py
token = get_token( )

xml_template =  '''
<module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">

    <type
        xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">prefix:sal-netconf-connector</type>
    <name>%s</name>
    <address
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">%s</address>
    <port
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">%s</port>
    <username
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">%s</username>
    <password
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">%s</password>
    <tcp-only
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">false</tcp-only>
    <event-executor
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:netty">prefix:netty-event-executor</type>
        <name>global-event-executor</name>
    </event-executor>
    <binding-registry
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:binding">prefix:binding-broker-osgi-registry</type>
        <name>binding-osgi-broker</name>
    </binding-registry>
    <dom-registry
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:dom">prefix:dom-broker-osgi-registry</type>
        <name>dom-broker</name>
    </dom-registry>
    <client-dispatcher
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:config:netconf">prefix:netconf-client-dispatcher</type>
        <name>global-netconf-dispatcher</name>
    </client-dispatcher>
    <processing-executor
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:threadpool">
            prefix:threadpool</type>
        <name>global-netconf-processing-executor</name>
    </processing-executor>
</module>
'''

# user input
name = ""
ip = ""
port = ""
username = ""
password = ""

# API base url
url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/node/controller-config/yang-ext:mount/config:modules"


# take user input
print ('!!! For simplicity, demo program will NOT verify the data format you entered, please enter carefully !!!\n')
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

# insert user input
xml_payload = xml_template % (name,ip,port,username,password)

# content type is XML
headers = {'Content-Type': 'application/xml'}
try:
    r = requests.post(url,auth=('token',token), headers=headers,data=xml_payload,verify=False)
    print ("Response Status: ",r.status_code)    # This is the http request status
except:
    print ("Something wrong with the request!")

    
    


