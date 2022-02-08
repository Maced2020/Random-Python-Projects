#this will be a password genterator
#started 1/22/2022
# This now generates passwords as of 1/23/2022
#
import random

def password_generator():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=`~;'?./"
    userchoice = input("How long would you like your password to be?: ")
    password = " "
    for i in range(userchoice):
        randomletter = random.choice(alphabet)
        password = randomletter + password      
    return password


print(password_generator())
