#! /usr/bin/python3
# I am atempting to automaticly zip and unzip large files (with no user input)
# so far i have gotten to the point where i ask the users 

import os


# for linunx only
# This function asks the user if they would like to zip or unzip files
# This function also takes in files from the user and zips them for the user 
def zip_and_gunzip():
    choice = ''
    while choice is not 'ZIP' or choice is not 'UNZIP':
        if choice == 'DONE':
            break
        choice = input('would you like to Zip or Unzip a file? ').upper()
         
        if choice == 'ZIP':
            multiple_files = []
            file_name = input('Give me a File(s) to Zip:')
            multiple_files.append(str(file_name))
            print('Zipping ' + str(multiple_files))
            for file_name in multiple_files:
                os.system('sudo gzip ' + str(file_name))
                print('ZIP SUCCESSFUL')
                choice = 'DONE'


        elif choice == 'UNZIP':
            multiple_files = []
            file_name = input('Give me a File(s) to Unzip:')
            multiple_files.append(str(file_name))
            print('Unzipping ' + str(multiple_files))
            for file_name in multiple_files:
                os.system('sudo gunzip ' + str(file_name))
                print('UNZIP SUCCESSFUL')
                choice = 'DONE'

zip_and_gunzip()
