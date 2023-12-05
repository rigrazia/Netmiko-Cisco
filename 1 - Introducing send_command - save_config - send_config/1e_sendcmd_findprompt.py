


import netmiko

devices = ['192.168.1.1']



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
        #connection.enable()
        
        current_prompt = connection.find_prompt()
        print(current_prompt, 'show ip interface brief')

        output = connection.send_command('show ip interface brief')
        print(output)

        # OR
        print('\n')
        
        prompt_command = connection.find_prompt()
        prompt_command += ' show ip interface brief\n'
        prompt_command += connection.send_command('show ip interface brief')
        print(prompt_command)

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









