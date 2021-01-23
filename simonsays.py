# I am attempting to make simon says 
# started jan/17/2021
# Finished jan/22/2021 
# developed by maced2020

import random
import os
import math
import time


# global varibles
colors = ['red', 'blue', 'yellow', 'green']
computer_list = []
winning = True

# game loop  function (simon keeps saying colors assuming you match him)
def game_loop():
    user_list = []
    timer = 1
    while winning == True:
        # picking a randodm color
        num = random.random()*4
        num = math.floor(num)
        computer_list.append(colors[num])
        # printing out what simon said and then clearing the board to prevent cheating
        print('Simon says: ', computer_list)
        time.sleep(timer)
        timer += .5
        os.system('clear')
        # asks the player for colors and adds them to the user list until both lists are the same length
        while len(user_list) < len(computer_list):
            user_input = input('What did the Simon say?: ').lower()
            user_list.append(user_input)

        if user_list != computer_list:
            winning == False
            print('You have lost!')
            print(' Computer list: ', computer_list)
            print(' Player list: ', user_list, '\n', 'You got: ', len(user_list) - 1, 'Correct')
            break
        # clears out the user list so you can match with simon
        user_list = []

game_loop()
