'''
Introduces how to make changes using the send_config_set() method and a list of configuration commands

ConnetHandler() method: add secret password
- enable() method: enter privileged mode
- send_config_set() method: Configuration changes

Uses network configured with 3-router scripts

ChatGPT
'''


import netmiko

devices = ['192.168.1.1']

ipv6_interface_list = [
    'ipv6 unicast-routing',
    'interface g0/0',
    'ipv6 address 2001:db8:cafe:1::1/64',
    'ipv6 address fe80::1:1 link-local',
    'exit',
    
    'interface g0/1',
    'ipv6 address 2001:db8:cafe:2::1/64',
    'ipv6 address fe80::1:2 link-local'
]

for device in devices:
    try:
        connection = netmiko.ConnectHandler(ip=device, 
                                            device_type='cisco_ios', 
                                            username='admin', 
                                            password='cisco',
                                            secret = 'class'
                                            )



        # enable() method: Must use for privileged mode access unless the method does this for you.
        # The send_config_set() method that follows, requires the enable() method.
        # The send_config_set() method
        # In Netmiko, the enable() method is used to enter privileged exec mode (sometimes referred to as enable mode or enable password) on a network device. It is required when you need to execute commands that require elevated privileges, typically commands that modify the device's configuration.
        # This method checks whether you’re already in configuration mode. If you aren’t, it goes into config mode, executes the commands, and by default, exits configuration mode. 
        # Returns the output of the configuration commands, and you are storing that output in the variable output. Subsequently, you are printing the output to the console.
        # The output variable will contain the response from the network device for each command in the configuration set.
        connection.enable()        
        output = connection.send_config_set(ipv6_interface_list)
        print(output)
        
        print(device)
        print('-'*11)
        print(connection.send_command('show ipv6 interface brief'))

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








