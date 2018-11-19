from netmiko import ConnectHandler
from getpass import getpass

# This will ask you to enter password
password = getpass()

# these dictionaries define the parameters for the devices

rtr-1 = {
	'device_type': 'cisco_ios',
	'ip': '10.1.1.1',
	'username': 'netwadmin',
	'password': password,
}

rtr-2 = {
	'device_type': 'cisco_ios',
	'ip': '10.1.1.2',
	'username': 'netwadmin',
	'password': password,
	'port': 8022,
}

rtr-3 = {
	'device_type': 'juniper',
	'ip': '10.1.1.3',
	'username': 'netwadmin',
	'password': pasword,
	# next line allows for an enable secret to be sent
	'secret': '',
	'port': 9822,
}

# now we try to connect to devices
#argument in the parenthesis below passes values from dictionary to the function

router_rtr-1 = ConnectHandler(**rtr-1)
router_rtr-2 = ConnectHandler(**rtr-2)
router_rtr-3 = ConnectHandler(**rtr-3)

# to see methods available
dir(router_rtr-1)

# to see the prompt on the device
router_rtr-1.find_prompt()

# to go into config mode
router_rtr-1.config_mode()

# to confirm being in config mode the command below should return True
router_rtr-1.check_config_mode()

# and, if you issue fine_prompt we should see (config) in the prompt
router_rtr-1.find_prompt()

# to exit config mode
outp = router_rtr-1.exit_config_mode()

# to send a command
outp = router_rtr-1.send_command("show ip int br")
print outp

'''
netmiko also diables paging and provides line feed and timing to make sure all commands execute correcty
'''

# to send multiple commands

config_commands = ['logging buffered 19999']
output = router_rtr-1.send_config_set(config_commands)

# to send command from a file. Uses SSH channel

net_connect.send_config_from_file(config_file='config_file.txt')

