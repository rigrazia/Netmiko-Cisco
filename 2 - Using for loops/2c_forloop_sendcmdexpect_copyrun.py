'''
Added: 
- doctring
- try: exception: Two exceptions are handled
   1. Authentication - Can't SSH (wrong username or password)
   2. Timeout - Can't connect (wrong IP or port)

Network Automate - 05. Handling Multiple Devices and Exceptions
See https://www.youtube.com/watch?v=L9_DVl3_0dQ&list=PLtw40n4ybvFoHoigW7IwITNilmZn2cfNv&index=5&t=476s

Uses network configured with 3-router scripts
'''

import netmiko



# Assign devices to a dictionary of IP addresses used to SSH into each device
devices = ['192.168.1.1',  '192.168.2.2', '192.168.3.2']

print('\n')

# ALTERNATIVE - SEE VIDEO
# The exceptions 'netmiko.exceptions.NetMikoAuthentcationException' and 'netmiko.exceptions.NetMikoTimeoutException' are displayed by Python output when this problem occurs. 
# These can be handled in the 'except:' which is commented out below.
# Create tuple with exceptions
#netmiko_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException, 
#                      netmiko.ssh_exception.NetMikoTimeoutException)


for device in devices:
    try:
        connection = netmiko.ConnectHandler(ip=device, 
                                            device_type='cisco_ios', 
                                            username='admin', 
                                            password='cisco')


        print(f'{device} copy runnning-config startup-config' )
        print('-'*11)
        print(connection.send_command_expect('copy running-config startup-config',
                                              expect_string='Destination filename'))

        print('Success!\n')

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

    # ALTERNATIVE - SEE VIDEO
    # Saves the netmiko exception that happened as the actual exception
    #except netmiko_exceptions as actual_exception:
        #print('Failed to device', router, actual_exception)