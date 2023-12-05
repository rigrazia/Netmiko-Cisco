import netmiko

# Define device parameters for Telnet


connection = netmiko.ConnectHandler(ip='192.168.1.1', 
                                    device_type='cisco_ios_telnet',  
                                    password='cisco'
                                    )
    
print("Telnet Connection Successful\n")

# Perform operations...
print(connection.send_command('show ip interface brief'))

