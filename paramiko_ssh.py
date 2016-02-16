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

'''
This requires that have 'host_keys' file in a .ssh directory
remote_conn_pre.load_system_host_keys()
'''

'''
This can be used to point to the location of the known_hosts file
remote_conn_pre.load_system_host_keys("/home/user_name/.ssh/host_keys")
'''



remote_conn_pre.connect(ip_addr, username=usr_nm, password=passwd, look_for_keys=False, allow_agent=False, port=port)

# invoke_shell allows for multiple commands within the same ssh session
remote_conn = remote_conn_pre.invoke_shell()

#this makes the script read upto 5000 bytes
outp = remote_conn.recv(5000)

print outp

