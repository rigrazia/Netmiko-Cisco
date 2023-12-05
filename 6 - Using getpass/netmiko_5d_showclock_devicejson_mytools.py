'''
Create library for get_input() and get_credentials() functions so they can be used by other programs


Uses network configured with 3-router scripts

Network Automate - 07. JSON and getpass 
https://www.youtube.com/watch?v=-xK6CwTbsF8&list=PLtw40n4ybvFoHoigW7IwITNilmZn2cfNv&index=7
'''


import netmiko
import json
# Use from getpass so we don't have to use getpass.getpass(), just getpass()
from getpass import getpass

import netmiko_5d_mytools

## DELETE FUNCITONS: def get_input() and def get_credentials()
# def get_input(prompt=''):
# def get_credentials():



username, password = netmiko_5d_mytools.get_credentials()


with open('netmiko-5c-devices-nocred.json') as dev_file:
    devices = json.load(dev_file)


for device in devices: 

    ## For each device in json file add username and password keys with values entered from user
    device['usermame'] = username
    device['password'] = password

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


    # Change device to device[ip'] to print out the ip address since device no longer means ip  
    # Otherwise displays all information in the dictionary for each device 
    except netmiko.exceptions.NetmikoTimeoutException:
        print('Timeout occured to', device['ip'])
        print('''Common causes of this problem are:
        1. Incorrect hostname or IP address.
        2. Wrong TCP port.
        3. Intermediate firewall blocking access.''')
        print('\n')

    # Change device to device[ip'] to print out the ip address since device no longer means ip       
    # Otherwise displays all information in the dictionary for each device  
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