#! /usr/bin/env python3

import os

FAV_SPORT = input('What is your favorite sport? ')
SIBLINGS = input('How many siblings do you have? ')
UVA_YEAR = input('What year are you at UVA? ')

os.environ['FAV_SPORT'] = FAV_SPORT
os.environ['SIBLINGS'] = SIBLINGS
os.environ['UVA_YEAR'] = UVA_YEAR

print(os.getenv('FAV_SPORT'))
print(os.getenv('SIBLINGS'))
print(os.getenv('UVA_YEAR'))