# this python script will generate a random password
# started 12/11/2021
import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-=+|]}{[;:?/.><'
password_length = int(input("Password Length: "))

def random_password(num):
    password = ''
    password = password.join(random.choice(alphabet) for x in range(num))
    return password

print (random_password(password_length))
