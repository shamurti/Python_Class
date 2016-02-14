import paramiko

from getpass import getpass

ip_addr = "50.76.53.27"
usr_nm = "pyclass"
passwd = getpass()
port = 8022

remote_conn_pre = paramiko.SSHClient()

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip_addr, username=usr_nm, password=passwd, look_for_keys=False, allow_agent=False, port=port)

remote_conn = remote_conn_pre.invoke_shell()

#this makes the script read upto 5000 bytes
outp = remote_conn.recv(5000)

print outp

