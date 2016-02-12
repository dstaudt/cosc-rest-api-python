from cosc_config import * # Including cosc_config.py

# Get security token by using function created in cosc_config.py
token = get_token( )

# get config inventory url
config_url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/"
op_url = "https://"+cosc_ip+"/controller/restconf/operational/opendaylight-inventory:nodes/"

non_op_list = []
op_list = []

# get operational store id list
try:
    r = requests.get(op_url,auth=('token',token),verify=False)
    # print ("Response Status: ",r.status_code)
    response_json = r.json() # Get the json-encoded content from response
    nodes=response_json["nodes"]["node"]
    for item in nodes:
        if item["id"] != "controller-config": # exclude default node
            op_list.append(item["id"])
except:
    print ("Something wrong with the operational store request!")
    
# get config store id list
try:
    r = requests.get(config_url,auth=('token',token),verify=False)
    # print ("Response Status: ",r.status_code)
    response_json = r.json() # Get the json-encoded content from response
    nodes=response_json["nodes"]["node"]
    for item in nodes:
        if item["id"] not in op_list: 
            if item["id"] != "controller-config": # exclude default node
                non_op_list.append(item["id"])
except:
    print ("Something wrong with the config store request!")

select = True
while select:
    user_input = input('=> Please enter \n1: To delete a operational device\n2: To delete a non-operational device\nexit: To exit\nEnter your selection: ' )
    user_input= user_input.replace(" ","")
    if user_input.lower() == 'exit': 
        sys.exit()     
    if user_input == '1' or user_input == '2':
        select = False
    else:
        print ("Sorry, wrong selection, please try again to select 1 or 2 or enter 'exit'!")
    # End of while loop
    
# for deleting non-operational device    
if user_input == '2':
    print ('************************* Non-operational device list *************************')
    print (', '.join(non_op_list))
    if non_op_list ==[]:
        print ("No user mounted non-operational device!")
        sys.exit()       
    select = True
    while select:
        device = input('=> Enter a device from above list to delete: ')
        device = device.replace(" ","") # ignore space
        if device.lower() == 'exit': 
             sys.exit()
        if device in non_op_list: # if user_input is matched
           select = False
           break
        else:
            print ("Sorry, wrong selection, please try again or enter 'exit'!")
    del_config_url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/node/"+device 
    try:
        r = requests.delete(del_config_url,auth=('token',token),verify=False)
        print ("Delete device response status: ",r.status_code)    # This is the http request status
    except:
        print ("Something wrong with deleting operational store device!")
# for deleting operational device    
elif user_input == '1':
    print ('************************* Operational device list *************************')
    print (', '.join(op_list))
    if op_list ==[]:
        print ("No user mounted operational device!")
        sys.exit()    
    select = True
    while select:
        device = input('=> Enter a device from above list to delete: ')
        device = device.replace(" ","") # ignore space
        if device.lower() == 'exit': 
             sys.exit()
        if device in op_list: # if user_input is matched
           select = False
           break
    unmount_url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/node/controller-config/yang-ext:mount/config:modules/module/odl-sal-netconf-connector-cfg:sal-netconf-connector/"+device
    del_config_url = "https://"+cosc_ip+"/controller/restconf/config/opendaylight-inventory:nodes/node/"+device 
    try:
        r = requests.delete(unmount_url,auth=('token',token),verify=False)
        print ("Dismount device response status: ",r.status_code)    # This is the http request status
    except:
        print ("Something wrong with dismounting device!")

    # check if device is still in config data store
    config_list = []
    r = requests.get(config_url,auth=('token',token),verify=False)      
    response_json = r.json() # Get the json-encoded content from response
    nodes=response_json["nodes"]["node"]
    for item in nodes:
        config_list.append(item["id"])
    if device in config_list:
        try:       
            r = requests.delete(del_config_url,auth=('token',token),verify=False)
            print ("Delete config store device response status: ",r.status_code)    # This is the http request status
        except:
            print ("Something wrong with deleting config store device!")

