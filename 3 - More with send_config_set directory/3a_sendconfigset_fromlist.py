'''
Introduces how to make changes using the send_config_set() method and a list of configuration commands

ConnetHandler() method: add secret password
- enable() method: enter privileged mode
- send_config_set() method: Configuration changes

'''


import netmiko

device = '192.168.1.1'

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


connection = netmiko.ConnectHandler(ip=device, 
                                    device_type='cisco_ios', 
                                    username='admin', 
                                    password='cisco',
                                    secret = 'class'
                                    )

# enable() method: Must use for privileged mode access unless the method does this for you.
# The send_config_set() method that follows, requires the enable() method.
# In Netmiko, the enable() method is used to enter privileged exec mode (sometimes referred to as enable mode or enable password) on a network device. It is required when you need to execute commands that require elevated privileges, typically commands that modify the device's configuration.
# This method checks whether you’re already in configuration mode. If you aren’t, it goes into config mode, executes the commands, and by default, exits configuration mode. 
# the output (response) of the commands is not stored or printed. This means you won't be able to see the response or verify if the commands were successful directly in your script.
connection.enable()
connection.send_config_set(ipv6_interface_list)
        
print(device)
print('-'*11)
print(connection.send_command('show ipv6 interface brief'))

print('\n')

connection.disconnect()
    




