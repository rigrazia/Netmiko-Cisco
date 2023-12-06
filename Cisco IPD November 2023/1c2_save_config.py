import netmiko

connection = netmiko.ConnectHandler(ip='192.168.4.1', 
                                    device_type='cisco_ios', 
                                    username='admin', 
                                    password='cisco')

# Erase startup-config and verify no startup-config
# expect_string searching in "Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]"
print(connection.send_command_expect('erase startup-config',
                                      expect_string='Continue?'))
print("show startup-config...")
print(connection.send_command('show startup-config'))

# Save startup-config and verify startup-config
print("\n")
print("Save running-config to startup-config...")
connection.save_config()

print("Success!")

print("\n")
print("show startup-config...")
print(connection.send_command('show startup-config'))

connection.disconnect()
