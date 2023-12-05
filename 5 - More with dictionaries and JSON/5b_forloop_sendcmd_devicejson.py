'''
Use JSON File for list of devices
- less cluttered
- changed copy run start to show clock - faster

Uses network configured with 3-router scripts

Network Automate - 07. JSON and getpass 
https://www.youtube.com/watch?v=-xK6CwTbsF8&list=PLtw40n4ybvFoHoigW7IwITNilmZn2cfNv&index=7
'''


import netmiko
import json

path = '/Users/rigrazia/MyInformation/Cabrillo/Courses/Python/Networking/netmiko/4 - For loop with dictionary of devices - json of devices/'


        
filename = 'my_devices.json'
filename = path + filename

with open(filename) as device_file:
    devices = json.load(device_file)


# Change Python individual dictionaries to a list of dictionaries, instead of defining each one separately
# Put it in a JSON fle instead of hardcoded in program

'''
r1 = {
    'ip': '192.168.1.1',
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco'
}
r2 = {
    'ip': '192.168.2.2',
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco'
}
etc.

As device.json file (need double quotes)
[
     {
    "ip": "192.168.1.1",
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "cisco"
},
r2 = {
    "ip": "192.168.2.2",
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "cisco"
},
etc.

]
'''

# REMOVE List of devices, could include any cisco ios device routers and switches
# devices = [r1, r2, r3, s1 ,s3]

print('\n')

for device in devices: 
    try:
        #The ** is used for unpacking the device dictionary as keyword argument, 
        #The ** notation allows you to pass the key-value pairs from the device dictionary as separate keyword arguments to the function.
        connection = netmiko.ConnectHandler(**device)

        # Change device to device[ip'] to print out the ip address since device no longer means ip  
        # Otherwise displays all information in the dictionary for each device
        print('-'*79)
        print('Connecting to device', device['ip'])
        
        print(connection.send_command('show clock'))        

        connection.disconnect()


    # These exceptions 'netmiko.exceptions.NetmikoTimeoutException', etc. are from Python output when this problem occurs.    
    except netmiko.exceptions.NetmikoTimeoutException:
        print('Timeout occurred to', device['ip'])
        print('''Common causes of this problem are:
        1. Incorrect hostname or IP address.
        2. Wrong TCP port.
        3. Intermediate firewall blocking access.''')
        print('\n')
        
    except netmiko.exceptions.NetMikoAuthenticationException:
        print('Authentication error', device['ip'])
        print('''Common causes of this problem are:
        1. Invalid username and password
        2. Incorrect SSH-key file
        3. Connecting to the wrong device''')
        print('\n')
        
    except netmiko.exceptions.ReadTimeout:
        print('Read timeout. pattern not detected', device['ip'])
        print('''Common causes of this problem are:
        1. Missing or incorrect secret password in ConnectHandler()
        2. Adjust the regex pattern to better identify the terminating
           string. Note, in many situations the pattern is
           automatically based on the network device's prompt.
        3. Increase the read_timeout to a larger value.''')
        print('\n')


    # Catch-all exception handler for any other exception
    except Exception as e:
        print("An error occurred:", str(e))