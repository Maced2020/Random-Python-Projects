# This is a password generator

# completed 10/7/2023


import random
import sys





# this function generates a random password: 

def password_generator():

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=`~;'?./"
    userchoice = input("How long would you like your password to be?: ")
    password = " "
    try:
        for i in range(int(userchoice)):
            randomletter = random.choice(alphabet)
            
            password = randomletter + password
        print(password)
        print()

    except:
        print("You are clearly not following the rules; you must be a hacker")
        sys.exit()

    print()







# this function allows the password generator to run as many times as the user would like

def multiple_passwords():
    while True:
        again = input("would you like A password?: ")
        print()
        if again.upper() == "YES" or again.upper() == "Y":
            password_generator()
        else:
            print()
            print("No more passwords will be generated")
            sys.exit()



multiple_passwords()
