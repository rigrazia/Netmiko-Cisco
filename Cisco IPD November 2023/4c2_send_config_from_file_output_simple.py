import netmiko
import os


# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the file containing configuration commands
config_file = os.path.join(script_directory, 'r1-ipv6-config.txt')


device = '192.168.1.1'



# Establish SSH connection
connection = netmiko.ConnectHandler(ip=device, 
                                    device_type='cisco_ios', 
                                    username='admin', 
                                    password='cisco',
                                    secret = 'class'
                                    )

print("SSH Connection Successful\n")

print("\nBefore configuration")
print(connection.send_command('show ipv6 interface brief'))

# Use send_config_from_file() to send configuration commands from a file
output = connection.send_config_from_file(config_file)
print(f"Config Output:\n{output}\n")
    
print("After configuration")
print(connection.send_command('show ipv6 interface brief'))


connection.disconnect()
print("\nSSH Connection Closed")
