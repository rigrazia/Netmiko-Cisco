'''
Use getpass so password is not shown, JSON File with no creditials
- Although AAA not configured, this would be similar to a AAA environment; admin user and password same on all devices

'''


import netmiko
import json
# Use from getpass so we don't have to use getpass.getpass(), just getpass()
from getpass import getpass


# Prompts and returns SSH username and password (not shown)
def get_ssh_credentials():
    # Username entered is shown in clear text
    username = input('Enter SSH username: ')
    
    # Password entered is not shown
    password = getpass('Enter SSH password: ')
    
    return username, password


# Prompts and returns privilged password (not shown)
def get_secret():    
    # Password entered not shown
    secret = getpass('Enter privileged exec password: ')
    
    return secret


# One option but passwords are shown in clear text:
# username = input('Enter username: ')
# password = input('Enter password: ')
# secret = input('Enter privileged password: ')


# SSH username and password
username, password = get_ssh_credentials()

# Privileged password
exec_mode = input('Do you need privileged exec mode? (y/n) ')
if exec_mode == 'y' or exec_mode == 'Y':
    secret = get_secret('Enter privileged exec password: ')
    

path = '/Users/rigrazia/MyInformation/Cabrillo/Courses/Python/Networking/netmiko/5 - Password with getpass/'

filename = 'my_devices_nocred.json'
filename = path + filename


with open(filename) as device_file:
    devices = json.load(device_file)


for device in devices: 

    ## For each device in json file add username and password keys with values entered from user
    device['username'] = username
    device['password'] = password
    if exec_mode == 'y' or exec_mode == 'Y':
        device['secret'] = secret


    try:
        #The ** is used for unpacking the device dictionary as keyword argument, 
        #The ** notation allows you to pass the key-value pairs from the device dictionary as separate keyword arguments to the function.
        connection = netmiko.ConnectHandler(**device)

        # Change device to device[ip'] to print out the ip address since device no longer means ip  
        # Otherwise displays all information in the dictionary for each device
        print('-'*79)
        print('Connecting to device', device['ip'])       
        
        if exec_mode == 'y' or exec_mode == 'Y':
            connection.enable()
        
        
        
        print(connection.send_command('show running-config'))        

        connection.disconnect()


    # Change device to device[ip'] to print out the ip address since device no longer means ip  
    # Otherwise displays all information in the dictionary for each device 
    except netmiko.exceptions.NetmikoTimeoutException:
        print('\nTimeout occurred to', device['ip'])
        print('''Common causes of this problem are:
        1. Incorrect hostname or IP address.
        2. Wrong TCP port.
        3. Intermediate firewall blocking access.''')
        print('\n')

    # Change device to device[ip'] to print out the ip address since device no longer means ip       
    # Otherwise displays all information in the dictionary for each device  
    except netmiko.exceptions.NetMikoAuthenticationException:
        print('\nAuthentication error', device['ip'])
        print('''Common causes of this problem are:
        1. Invalid username and password
        2. Incorrect SSH-key file
        3. Connecting to the wrong device''')
        print('\n')

    except netmiko.exceptions.ReadTimeout:
        print('\nRead timeout. pattern not detected', device['ip'])
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
        