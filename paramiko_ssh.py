import paramiko

from getpass import getpass

ip_addr = "50.76.53.27"
usr_nm = "pyclass"
passwd = getpass()
port = 8022

remote_conn_pre = paramiko.SSHClient()

# The AutoAddPolicy is not secure
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Use either one of these below instead of the one above:


# This requires to have a 'host_keys' file in a .ssh directory
'''
remote_conn_pre.load_system_host_keys()
'''


# This can be used to point to the location of the known_hosts file
'''
remote_conn_pre.load_system_host_keys("/home/user_name/.ssh/host_keys")
'''

remote_conn_pre.connect(ip_addr, username=usr_nm, password=passwd, look_for_keys=False, allow_agent=False, port=port)

# invoke_shell allows for multiple commands within the same ssh session
remote_conn = remote_conn_pre.invoke_shell()

# To send a command
outp = remote_conn.send("\n")

# To prevent command being hung set a timeout. In the example below it is 6.0 seconds
remote_conn.settimeout(6.0)

# To see if data is ready to be read
remote_conn.recv_ready()

# Use the above in a while or if loop to see if there is still data to ve read
'''
if remote_conn.recv_ready():
    output += remote_conn.recv(MAX_BUFFER)
'''

'''
Make sure to include delays when executing commands to allow the device to respond.
'''

#this makes the script read upto 5000 bytes
outp = remote_conn.recv(5000)

print outp


