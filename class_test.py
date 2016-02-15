
# Creating a simple dictionary
'''
def netw_device(ip, username, password):
	net_dev = {}
	net_dev['ip'] = ip
	net_dev['username'] = username
	net_dev['password'] = password
	return net_dev
'''

# Now creating the same but using Classes

''' 
Creating the class object. "object" below refers to base object. If inherting from another, then the class name would go in the paranthesis
'''

class NetworkDevice(object):
	# The "def" below defines a 'method' within the class
	# "__init__" is the method automatically invoked when the object is created
	def __init__(self, ip, username, password):
	    self.ip = ip
		self.username = username
		self.password = password
	# write code to telnet as a part of the class
	# def connect_telnet(self):
	#	code to telnet using above information
	# write code to go to enable mode
	# def connect_enable(self):
	#   code here for enable mode
	# write code to execute a command
	# def show_version(self):
	# code to execute show version 

rtr1 = NetworkDevice('10.1.1.1', 'admin', 'boo')
rtr2 = NetworkDevice('10.1.1.2', 'admin', 'boo')

print('Router1: %s %s %s') % (rtr1.ip, rtr1.username, rtr1.password) 
print "Router2: {0} {1} {2}".format(rtr2.ip, rtr2.username, rtr2.password)




