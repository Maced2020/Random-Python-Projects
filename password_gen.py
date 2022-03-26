#this will be a password genterator
#started 1/22/2022
# This now generates passwords as of 1/23/2022
#
import random

# this function 
def password_generator():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=`~;'?./"
    userchoice = input("How long would you like your password to be?: ")
    password = " "
    try:
        for i in range(int(userchoice)):
            randomletter = random.choice(alphabet)
            password = randomletter + password
        print(password)
    except:
        print("You are clearly not following the rules; you must be a hacker")


#this runs the functions and hands out a password
password_generator()
