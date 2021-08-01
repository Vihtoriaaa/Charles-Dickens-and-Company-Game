import time
import random
import pandas as pd
import os
from support_functions import read_data, timeprint
import random


def get_three_films():
    """
    This function outputs names of 3 films from txt file film_names
    e.g ['Los Nickleb', 'Story of the Christmas Caro', 'Walter Wildin']
    """
    films = []
    three_films = list()
    file = open('film_names.txt', 'r', encoding='utf-8')
    for line in file:
        line = line[:-2]
        films.append(line)
    for _ in range(3):
        result = random.choice(films)
        three_films.append(result)
    return three_films


def four_level(tickets):
    """
    This function is the fourth level of the game. It help the user to \
    discover more about the movies that based on Charles Dickens' books.\
    The user gets names of 6 films one by one. The user has to write 'True' if\
    he thinks that this film is based on our author's book, and 'False' if not\
    to complete the level. With every mistake the number of possible points\
    the user can get reduces.
    """
    tickets = int(tickets)
    author_films = get_three_films()
    other_films = ['The Clown Barber', 'The Derby 1895', 'Dancing Girls',
                   'Hotel room', 'Les forgerons', 'Chinese Opium Den']
    variants = [True, False]
    counter = 0
    timeprint("Welcome to level 4!")
    timeprint('Soon 6 names of films will appear one by one.')
    timeprint("Your task:\nprint 'True' if this film is based on Charles \
Dickens' book or 'False' if not.\nIf your answer is right, you get a point, \
if not - sorry not sorry.")
    timeprint('Good Luck have fun :)')
    author_films_str = '\n'.join(author_films)
    other_films_str = '\n'.join(other_films)
    while True:
        one_round = random.choice(variants)
        if one_round == True:
            right_film = random.choice(author_films)
            print()
            print('--------------------------')
            timeprint(right_film)
            print('--------------------------')
            user_input = input('Your thoughts? ')
            author_films_str = author_films_str.replace(right_film, '')
            if user_input != 'True':
                counter += 1
                timeprint("Ooops wrong answer ;(")
                if counter == 6:
                    break

            elif user_input == 'True':
                counter += 1
                timeprint("YEEES, you are right :)")
                tickets += 1
                if counter == 6:
                    break
        else:
            wrong_film = random.choice(other_films)
            print()
            print('--------------------------')
            timeprint(wrong_film)
            print('--------------------------')
            user_input = input('Your thoughts? ')
            other_films_str = other_films_str.replace(wrong_film, '')
            if user_input != 'False':
                counter += 1
                timeprint("Ooops wrong answer ;(")
                if counter == 6:
                    break

            elif user_input == 'False':
                counter += 1
                timeprint("YEEES, you are right :)")
                tickets += 1
                if counter == 6:
                    break
    return tickets
