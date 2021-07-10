#! /usr/bin/python3
# A SIMPLE PROGRAM TO CHECK STATUS OF MULTIPLE VM'S OR MACHINES VIA SSH
# FINISHED ON 11/15/2020


# CHANGE GLOBAL VARIABLES AS NEEDED.

# this is the module that supports ssh
import paramiko

# global variables
USERNAME = 'ubuntu'
KEYFILE = 'oracle_private.pem'
FILEPATH = 'hosts.txt'

print('-----Starting-----')
with open(FILEPATH) as fp:
   line = fp.readline()

   for HOST in line:
       try:
           HOST = line.strip()
           line = fp.readline()
           ssh = paramiko.SSHClient()
           ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           ssh.load_system_host_keys()
           # if host is blank we stop the loop
           if HOST == str(''):
               break
           # users see connecting to the host
           print('-----Connecting-----')
           print(HOST)
           # ssh.connect is how python connects to the host.
           ssh.connect(hostname=HOST, username=USERNAME, key_filename=KEYFILE)
           # this is how to read the command output remote connection.
           ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('uptime')
           print(ssh_stdout.read())
           # this closes my SSH connection
           ssh.close()
           
       except Exception as TimeoutError:
           print(' Failed')
print('-----Finsihed-----')