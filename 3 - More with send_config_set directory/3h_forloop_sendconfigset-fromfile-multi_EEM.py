'''
EEM:
- Do not need SSH access once it runs. 
- Can use the event timer to delay it, and sync with  EEMs on other devices.

Option 1: EEM - Change static routes with an AD of 150, so static routes stay until ospf routes with AD of 110 are installed in routing table. Then enable OSPF. Little or no packet loss.

Option 2: include 'no ip route' statements in the EEM files but this causes delay. Some packet loss.

Option 3: Create separate EEM file with delay (or python sleep()) that has 'no ip route' to give time for ospf to converge. Some packet loss.
'''


import netmiko


# List of devices; 'ip' for SSH and 'name' for filename
devices = [ 
           {'ip': '192.168.1.1', 'name':'r1'}, 
           {'ip': '192.168.2.2', 'name':'r2'},
           {'ip': '192.168.3.2', 'name':'r3'}
           ]
    

for device in devices:
    try:
        

        
        connection = netmiko.ConnectHandler(ip=device['ip'], 
                                            device_type='cisco_ios', 
                                            username='admin', 
                                            password='cisco',
                                            secret = 'class'
                                            )



        ################################################################
        # EEM Commands (OSPF)
        ################################################################
                                            
        path = '/Users/rigrazia/MyInformation/Cabrillo/Courses/Python/Networking/netmiko/3 - Config send_config_set - Same with file/'

        filename = 'ospf_eem_'
        eem_filename = path + filename + device['name'] + '.txt'
        print(filename)

        # Read commands from a file
        with open(eem_filename, 'r') as file:
            eem_commands = file.read().splitlines()
        
        connection.enable()

        connection.send_config_set(eem_commands)
        
        ''' 'EEM policy configure-ospf-once not registered with event none Event Detector' - the EEM applet is not properly registered or associated with the specified event detector. To resolve this issue, you need to ensure that the EEM applet is correctly registered with the event detector before running it using the "event manager run" command.'''
        #output = connection.save_config        
        #print(output)
        
        connection.send_command('show event manager policy registered ')
        connection.send_command('event manager run configure-ospf-once')
        
        
        
        print(device['ip'])
        print('-'*11)
        print(connection.send_command('show running-config | section router ospf'))

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