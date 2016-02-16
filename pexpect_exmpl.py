import pexpect
import sys
import re
from getpass import getpass

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = getpass()

    ssh_conn = pexpect.spawn("ssh -l{} {} -p {}".format(username, ip_addr, port))
    # following can be used to write to file for debugging, etc.
    '''
    ssh_conn.logfile = sys.stdout
    '''
    ssh_conn.timeout = 3
    ssh_conn.expext('ssword:')
    ssh_conn.sendline(password)



    ssh_conn.sendline('show ip int br')

    # this below sets ist up so that you can read the output before prompt #
    ssh_conn.expect('#')
 
    ssh_conn.sendline('term len 0')
    ssh_conn.expect('#')

    ssh_conn.sendline('sh ver')
    ssh_conn.expect('#')


    print ssh_conn.before

    # Can also do after
    '''
    print ssh_conn.after
    '''
    # following can be used to handle timeout
    '''
    try:
        ssh_conn.sendline('sh ver')
        # we will never see zzzz
        ssh_conn.expect('zzzz')
    # Timeout value was set above 3 secs
    except pexpect.TIMEOUT:
        print "some message to indicate timeout"
    '''
    # The RE below searches for any string starting with Lic and endinin UDI to the end of the line in the show version output. And, MULTILINE means all lines
    pattern = re.compile(r"^Lic.*DI:.*$", re.MULTILINE)
    ssh_conn.sendline('sh ver')
    ssh_conn.expect(pattern)
    print ssh_conn.after




if __name__ == '__main__':
    main()

