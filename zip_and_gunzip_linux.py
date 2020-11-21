#! /usr/bin/python3
# I am atempting to automaticly zip and unzip large files

import os

def zip_and_gunzip():
    choice = ''
    while choice is not 'ZIP' or choice is not 'UNZIP':
        if choice == 'DONE':
            break
        choice = input('would you like to Zip or Unzip a file? ').upper()
         
        
        if choice == 'ZIP':
            file_name = input('Give me a File to zip: ')
            print('zipping ' + file_name)
            os.system('sudo gzip ' + file_name) 
            print('Done')
            choice = 'DONE'


        elif choice == 'UNZIP':
            file_name = input(' Give me a File to unzip: ')
            print(' unzipping ' + file_name)
            os.system('sudo gunzip ' + file_name)
            print('Done')
            choice = 'DONE'

zip_and_gunzip()
