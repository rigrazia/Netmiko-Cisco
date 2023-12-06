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



# The send_config_set() method that follows, requires the enable() method.
# This method checks whether you’re already in configuration mode. If you aren’t, it goes into config mode, executes the commands, and by default, exits configuration mode. 
# Returns the output of the configuration commands, and you are storing that output in the variable output. Subsequently, you are printing the output to the console.
# The output variable will contain the response from the network device for each command in the configuration set.
# connection.enable()        
output = connection.send_config_set(ipv6_interface_list)
print(output)
        
print(device)
print('-'*11)
print(connection.send_command('show ipv6 interface brief'))

print('\n')

connection.disconnect()
    
 







