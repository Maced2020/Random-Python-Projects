
#! /usr/bin/python3
# A SIMPLE PROGRAM TO FILL A 5 GIG DRIVE
# FINISHED ON 11/28/2020
# will fill a 5 gig drive to 95%
# used tqdm to create a progress bar


import os
from tqdm import tqdm


print('Adding Text into star.txt')
for i in tqdm(range(1000)):
    os.system('df -h >> star.txt')

print('Adding text into star2.txt')
for i in tqdm(range(13500)):
    os.system('cat star.txt >> star2.txt')
