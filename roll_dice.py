# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:30:02 2016

@author: Administrator
"""

import random

    
def roll_dice(numbers=3,point=None):
    print ('<<<<<Roll the dice>>>>>')
    if point is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers-1
    return points
    
def roll_result(total):
    if 11<=total<=18:
        return 'Big'
    else:
        return 'Small'
        

def start_game():
    print('<<<<<Game Starts!>>>>>')
    choices = ['Big','Small']
    initial_value = 1000
    while initial_value >0:
        your_choice = input('Big or Small :')
        your_bet = input('how much you wanna bet?')
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            if your_choice == roll_result(total):
                    print('The points are',points,'You win!')
                    initial_value = initial_value + int(your_bet)
            else:
                print('The points are',points,'You lose!')
                initial_value = initial_value - int(your_bet)
            print('now your having ' + str(initial_value))
        else:
            print('Invalid Words')
            start_game()
    print('now your having ' + str(initial_value) + 'game over')
start_game()