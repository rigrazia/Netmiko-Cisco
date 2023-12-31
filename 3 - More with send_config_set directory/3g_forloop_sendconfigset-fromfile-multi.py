import netmiko



# List of devices; 'ip' for SSH and 'name' for filename
devices = [ 
           {'ip': '192.168.1.1', 'name':'r1'}, 
           {'ip': '192.168.2.2', 'name':'r2'},
           {'ip': '192.168.3.1', 'name':'r3'}
           ]
    

for device in devices:
    try:
        

        
        connection = netmiko.ConnectHandler(ip=device['ip'], 
                                            device_type='cisco_ios', 
                                            username='admin', 
                                            password='cisco',
                                            secret = 'class'
                                            )
                                            
        path = '/Users/rigrazia/MyInformation/Cabrillo/Courses/Python/Networking/netmiko/3 - Config send_config_set - Same with file/'

        filename = 'ipv6commands_'
        
        
        filename = path + filename + device['name'] + '.txt'

        print(filename)

        # Read commands from a file
        with open(filename, 'r') as file:
            commands = file.read().splitlines()
        
        ## send_config_set() method in Netmiko is designed to send a series of configuration commands to a network device, and it automatically handles the transition to privileged mode (if required) for executing those commands.
        connection.enable()

        connection.send_config_set(commands)
        
        
        print(device['ip'])
        print('-'*11)
        print(connection.send_command('show ipv6 interface brief'))

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
