'''
In Netmiko, the connection.enable() method is used to enter privileged exec mode (sometimes referred to as enable mode or enable password) on a network device. It is required when you need to execute commands that require elevated privileges, typically commands that modify the device's configuration. 

It is not required for the show the running-config command and it is not required to copy the running-config to the startup config. 

The show running-config and copy running-config startup-config commands do not require the secret password.
'''

# Import Netmiko library
import netmiko



connection = netmiko.ConnectHandler(ip='192.168.1.1', 
                                    device_type='cisco_ios', 
                                    username='admin', 
                                    password='cisco'
                                    )


print(connection.send_command('show running-config'))

'''The disconnect method in Netmiko is used to close the SSH connection to a network device, ensuring proper cleanup and freeing up system resources.'''
connection.disconnect()
