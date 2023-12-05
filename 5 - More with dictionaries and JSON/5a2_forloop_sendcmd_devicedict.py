'''
Saves all running to startup configs using a dictionary 
- What if you had devices with different device_types, usernames, or passwords
- use dictionary to store individual device information

Uses network configured with 3-router scripts

Network Automate - 06. Passing Dictionaries to Netmiko 
https://www.youtube.com/watch?v=4L_L_ZlMT_8&list=PLtw40n4ybvFoHoigW7IwITNilmZn2cfNv&index=6
'''


import netmiko

# Make a list of dictionaries
devices = [

 {
    'ip': '192.168.1.1',
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco'
},

{
    'ip': '192.168.2.2',
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco'
},

{
    'ip': '192.168.3.2',
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco'
},

{
    'ip': '192.168.1.5',
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco'
},

{
    'ip': '192.168.4.5',
    'device_type': 'cisco_ios',
    'username': 'admin',
    'password': 'cisco'
}
]

# List of devices, could include any cisco ios device routers and switches
#devices = [r1, r2, r3, s1 ,s3]

print('\n')

for device in devices: 
    try:
        #The ** is used for unpacking the device dictionary as keyword argument, 
        #The ** notation allows you to pass the key-value pairs from the device dictionary as separate keyword arguments to the function.
        connection = netmiko.ConnectHandler(**device)

        # Change device to device[ip'] to print out the ip address since device no longer means ip  
        # Otherwise displays all information in the dictionary for each device
        print(device['ip'])
        print('-'*11)
        
        output = connection.send_command('show clock')     
        print(output)

        print('\n')
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