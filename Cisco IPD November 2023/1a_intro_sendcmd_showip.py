# Import Netmiko library
import netmiko

connection = netmiko.ConnectHandler(ip='192.168.1.1', 
                                    device_type='cisco_ios', 
                                    username='admin', 
                                    password='cisco')

print(connection.send_command('show ip interface brief'))

# OR send the output to a string variable and print the variable

output = connection.send_command('show ip interface brief')
print('\n')
print(output)

connection.disconnect()
