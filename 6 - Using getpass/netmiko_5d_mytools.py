'''
Library for get_input() and get_credentials() functions so they can be used by other programs

Uses network configured with 3-router scripts

Network Automate - 07. JSON and getpass 
https://www.youtube.com/watch?v=-xK6CwTbsF8&list=PLtw40n4ybvFoHoigW7IwITNilmZn2cfNv&index=7
'''


# import netmiko
# import json
# Use from getpass so we don't have to use getpass.getpass(), just getpass()
from getpass import getpass


## Generic prompt with try and except. 
## Can be used with any prompt
def get_input(prompt=''):
    try:
        line = input(prompt)
    except NameError:
        line = input(prompt)
    return(line)

# Prompts and returns username and password (not shown)
def get_credentials():
    # Username entered shown in clear text
    username = get_input('Enter SSH username:')
    
    # Password entered not shown
    password = getpass('Enter SSH password: ')
    
    '''
    Option for having user enter password twice
    
    password = None
    while not password:
        password = getpass()
        password_verify = getpass('Retype your password:')
        if password != password_verify:
            print('Passwords do not match. Try again.')
            password = None    
    '''   

    return username, password


