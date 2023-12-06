import netmiko

# Assign devices to a list of IP addresses used to SSH into each device
devices = ['192.168.1.1', '192.168.2.2', '192.168.3.2']

print('\n')

# Loop through the IP addresses, device, in the list of devices. 
# device = Assign device to each item in the list, one by one
for device in devices: 
    
    # ip = current IP address in list of devices 
    connection = netmiko.ConnectHandler(ip=device, 
                                        device_type='cisco_ios', 
                                        username='admin', 
                                        password='cisco')

    # Print the current value of device, which is the IPv4 address from our list
    print(device)
    print('-'*11)    
    print(connection.send_command('show ip route static'))

    print('\n')

    connection.disconnect()
