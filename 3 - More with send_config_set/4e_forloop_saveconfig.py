'''
Saves all running to startup configs
- save_config() method

Uses network configured with 3-router scripts

ChatGPT
'''


import netmiko

# Assign devices to a dictionary of IP addresses used to SSH into each device
devices = ['192.168.1.1', '192.168.2.2', '192.168.3.2']

print('\n')

for device in devices: 
    try:
        connection = netmiko.ConnectHandler(ip=device, 
                                            device_type='cisco_ios', 
                                            username='admin', 
                                            password='cisco')


        print(device)
        print('-'*11)
        
        output = connection.save_config        
        print(output)

        print('\n')
        connection.disconnect()


    # These exceptions 'netmiko.exceptions.NetmikoTimeoutException', etc. are from Python output when this problem occurs.    
    except netmiko.exceptions.NetmikoTimeoutException:
        print('Timeout occurred to', device)
        print('''Common causes of this problem are:
        1. Incorrect hostname or IP address.
        2. Wrong TCP port.
        3. Intermediate firewall blocking access.''')
        print('\n')
        
    except netmiko.exceptions.NetMikoAuthenticationException:
        print('Authentication error', device)
        print('''Common causes of this problem are:
        1. Invalid username and password
        2. Incorrect SSH-key file
        3. Connecting to the wrong device''')
        print('\n')
        
    except netmiko.exceptions.ReadTimeout:
        print('Read timeout. pattern not detected', device)
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

