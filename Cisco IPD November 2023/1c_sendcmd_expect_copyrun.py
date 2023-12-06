import netmiko

device = '192.168.1.1'

connection = netmiko.ConnectHandler(ip=device, 
                                    device_type='cisco_ios', 
                                    username='admin', 
                                    password='cisco'
                                    )

print('\n')
# print with f-string = print(device, 'copy running-config startup-config')
print(f'{device} copy running-config startup-config' )
print('-'*11)

print(connection.send_command_expect('copy running-config startup-config',
                                      expect_string='Destination filename'))

print('Success!\n')


connection.disconnect()
