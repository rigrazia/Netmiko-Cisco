from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "cisco"
}

connection = ConnectHandler(**device)

print(connection.send_command('show ip route'))
print(connection.send_command('show interface description'))

print('Closing Connection')
connection.disconnect()