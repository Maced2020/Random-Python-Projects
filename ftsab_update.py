#! /usr/bin/python3
# using python to add to the fstab file

import os

os.system('sudo chmod 0646 /etc/fstab')

def fstab_Add():
    UUID = input(' Please provide me the UUID: ')
    DIR = input('Please provide me the directory name: ')
    MOUNT_TYPE = input('Please provide me the drive type: ')
    os.system('sudo echo UUID=' + str(UUID) + ' ' + str(DIR) + ' '+ str(MOUNT_TYPE) + ' '+ 'defaults,noatime  1   1 >> /etc/fstab')
    os.system('sudo chmod 0644 /etc/fstab')
    print('Done')
fstab_Add()
