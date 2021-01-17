# I am attempting to make simon says 
# started on jan/17/2021
# currently not
# developed by maced2020

import random
import os
import math
import time

# globasl variables 
colors = ['red', 'blue', 'yellow', 'green']
user_list = []
computer_list = []
loop = False


# this function creates a list of colors at random
def computer_selcetion():
    while len(computer_list) < 4:
        
        num = random.random()*4
        num = math.floor(num)
        computer_list.append(colors[num])
    # dev print statement
    print(computer_list)


# this function is attempting to match computer list to user list
def user_selection():
    while user_list != computer_list:
        user = input('please match the computer list: ')
        user_list.append(user)
        if len(user_list) > len(computer_list):
            print('you failed to match')
            break


try:
    computer_selcetion()
    user_selection()

except:
    print('\nsome kind of Error happened ')
    
