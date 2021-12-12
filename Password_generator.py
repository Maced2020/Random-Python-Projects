# this python script will generate a random password
# started 12/11/2021
# you left off trying to conver the dictionary into a string with no Commas or quotes
# maybe i shouldnt use a dictionary and just make it one long string.
import random
import json





# this function randomizes the order of the letters, numbers and symbles available for your random password
def create_random_list():
    # this is showing all the possible letters, numbers and simbles that could be used.
    string = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X",
    "Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"
    ,"z","1","2","3","4","5","6","7","8","9","0","~","!","@","#","$","%","^","&","*","(",")","_","-","=","+","|","]","}","{","[",";",":","?","/",".",">","<",]
    random_string = ""

    # this randomized the dicionary 
    random.shuffle(string)
    # this is asking the user for how long they would like the pasword to be.
    try:
        password_length = int(input("how long would you like your pasword to be?: "))
        # this while loop simply grabs the next index in the dictonary and adds to the randomized password
        while password_length > 0:
            random_string = string[password_length]
            password_length -= 1
            if password_length == 0:
                # randomizxing the pasword order again
                random.shuffle(random_string)
                
    # catches all errors and sxpits out a generic Error mesage
    except:
        print("You are clearly not following the rules; you must be a hacker")
    return random_string


# hopefully will print out a string that can be used as a password.
print(create_random_list())