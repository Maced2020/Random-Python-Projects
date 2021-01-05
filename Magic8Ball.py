# this is a magic 8 ball 
# created  1/4/2021


#! /usr/bin/python3
import math
import random


# Question from the user 
def user_question():
    print() # adding a blank line
    question = ''
    while question == '':
        question = input('I am a Fortune Teller; Give me a Question: ')


# Random Answer
def answer():
    print() # adding a blank line
    num = random.random()*6
    num = math.floor(num)
    while num != 'null':
        if num == 0:
            fortune = 'yes!'
            break
        elif num == 1:
            fortune = 'my sources say Yes!'
            break
        elif num == 2:
            fortune = 'Reply hazy try again later!'
            break
        elif num == 3:
            fortune = 'ask again later!'
            break
        elif num == 4:
            fortune = 'outlook not so good!'
            break
        elif num == 5:
            fortune = 'No'
            break
    print('Answer: ' + fortune)


try:
    user_question()
    answer()

except:
    print('An Error occured check your code')
