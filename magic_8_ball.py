#! /usr/bin/python3
# this is going to be a magic 8 ball

import random
import math

num = random.random()*5
num = math.floor(num)

print()
print('I am the magic 8 ball')
print()
Question = input('Ask me a question: ')
print()

if num == 0:
    print('Yes!')
elif num == 1:
    print('My sources say Yes')
elif num == 2:
    print('Reply Hazy Try Again Later')
elif num == 3:
    print('Ask Again Later')
elif num == 4:
    print('Outlook Not So Good')
elif num == 5:
    print('No')

