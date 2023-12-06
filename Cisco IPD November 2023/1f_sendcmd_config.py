import netmiko

connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='class') # Enable password

print("\nUsing send_command() create an access list 'access-list 1 permit any'\n")
    
# Secret password is required
connection.enable()                  # Privileged exec mode
connection.config_mode()             # Global config mode
connection.send_command('access-list 1 permit any')
connection.exit_config_mode()        # Exit global config mode

print("\nDone...Verify with 'show running-config | section access-list 1'")
print(connection.send_command('show running-config | section access-list 1'))
print("\n")

connection.disconnect()
