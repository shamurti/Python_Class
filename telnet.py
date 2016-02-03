import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

# Define remote telnet connection with specified command
def send_command(remote_conn, cmd):
        '''
        strip trailing new-line. 'r' in rstrip means on the end
        lstrip is the beginning. strip does both at beginning and at the end
        '''
        cmd = cmd.rstrip()
        remote_conn.write(cmd + '\n')
        time.sleep(1)
        return remote_conn.read_very_eager()

# Define login function

def login(remote_conn, username, password):
        output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
        remote_conn.write(username + '\n')
        # += indicates to keep the ouput
        output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        remote_conn.write(password + '\n')
        return output

def telnet_connect(ip_addr):
        try:
                return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
                sys.exit("Connection timed-out")

def main():
        ip_addr = 'ip address'
        username = 'name'
        password = 'password'

        remote_conn = telnet_connect(ip_addr)
        output = login(remote_conn, username, password)
        print output

        time.sleep(1)
        output = remote_conn.read_very_eager()

        output = send_command(remote_conn, 'term len 0')
        output = send_command(remote_conn, 'sh run | sec snmp')
        output = send_command(remote_conn, 'sh ver')

        print output + '\n'

        remote_conn.close()

if __name__ == "__main__":
        main()

