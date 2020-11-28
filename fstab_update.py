#! /usr/bin/python3
# A SIMPLE PROGRAM TO UPDATE FSTAB IN LINUX WITH NEW DRIVE MOUNT (ALSO CHANGES NEDW DRIVE PERMISSIONS TO 777)
# FINISHED ON 11/26/2020

import os

os.system('sudo chmod 0646 /etc/fstab')

def fstab_Add():
    UUID = input(' Please provide me the UUID: ')
    DIR = input('Please provide me the directory name: ')
    MOUNT_TYPE = input('Please provide me the drive type: ')
    os.system('sudo echo UUID=' + str(UUID) + ' ' + str(DIR) + ' '+ str(MOUNT_TYPE) + ' '+ 'defaults,noatime  1   1 >> /etc/fstab')
    os.system('sudo chmod 0644 /etc/fstab')
    os.sxystem('sudo mount -a')
    os.system('sudo chmod 777 ' + str(DIR))
    print('Done')
fstab_Add()
