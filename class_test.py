
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
creating the class object. "object" below refers to base object. If inherting from another, then the class name would go in the paranthesis
'''

class NetworkDevice(object):
	#The "def below defines a 'method' within the class
	def __init__(self, ip, username, password):
		self.ip = ip
		self.username = username
		self.password = password

rtr1 = NetworkDevice('10.1.1.1', 'admin', 'boo')
rtr2 = NetworkDevice('10.1.1.2', 'admin', 'boo')

print('Router1: %s %s %s') % (rtr1.ip, rtr1.username, rtr1.password) 
print "Router2: {0} {1} {2}".format(rtr2.ip, rtr2.username, rtr2.password)




