import time
import random
import pandas as pd
import os
from support_functions import read_data, find_books, find_other_books, timeprint
from support_functions import find_authors, book_csv, find_other_authors

def third_level(tickets):
    """
    This function is the third level of the game. It help the user to discover\
    more about the authors that wrote at the same time as Charles Dickens did.\
    The user gets names of 4 authors, one of them is a 'wrong'(did not wrote \
    at the same time) author, and the other 3 are 'right'. The user has to \
    choose the 'wrong' author to complete the level. With evety mistake the \
    number of possible pointsthe user can get reduces. If the answer is wrong,\
    then the user does not the user_input dissappears and there are one less \
    author left to choose. If the user fails to win, then he goes to level 4 \
    without any points.
    """
    tickets = int(tickets)
    authors = find_authors(book_csv, '1812-1870')
    others = find_other_authors(book_csv, '1812-1870')

    four_persons = []
    wrong_author = random.choice(others)
    four_persons.append(wrong_author)

    first_author = random.choice(authors)
    if first_author not in four_persons:
        four_persons.append(first_author)

    second_author = random.choice(authors)
    if second_author not in four_persons:
        four_persons.append(second_author)

    third_author = random.choice(authors)
    if third_author not in four_persons:
        four_persons.append(third_author)

    if len(four_persons) < 4:
        new_pers = random.choice(authors)
        if new_pers not in four_persons:
            four_persons.append(new_pers)

    four_persons = '\n'.join(four_persons)
    print()
    timeprint("Here are authors you have to choose from:")
    while True:
        print("-----------------------------------------------")
        timeprint(four_persons)
        print("-----------------------------------------------")
        print()
        timeprint("Enter the author's name who did not write when \
Charles Dickens did:")
        user_input = input()
        if user_input == wrong_author:
            print()
            tickets = tickets + 3
            timeprint("YEEES, you are right. Let's move on to level 4")
            break

        if user_input == first_author or user_input == second_author or \
            user_input == third_author:
            print()
            timeprint("Ooops wrongs answer :(")
            four_persons = four_persons.replace(user_input, '')
            four_persons = four_persons.strip()
            timeprint("Here are authors left you have to choose from:")
            print("-----------------------------------------------")
            timeprint(four_persons)
            print("-----------------------------------------------")
            print()
            user_input = input()

            if user_input == wrong_author:
                print()
                tickets += 2
                timeprint("YEEES, you are right. Let's move on to level 4")
                break

            if user_input == first_author or user_input == second_author \
                or user_input == third_author:
                print()
                timeprint("Ooops wrongs answer :( You have only one chance\
 left to complete this level")
                four_persons = four_persons.replace(user_input, '')
                four_persons = four_persons.strip()
                timeprint("Here are authors left you have to choose from:")
                print("-----------------------------------------------")
                timeprint(four_persons)
                print("-----------------------------------------------")
                print()
                user_input = input()

                if user_input == first_author or user_input == second_author \
                    or user_input == third_author:
                    print()
                    timeprint('You failed to complete this level without \
mistakes :( Lets move to level 4')
                    break
                if user_input == wrong_author:
                    print()
                    tickets = tickets + 1
                    timeprint("YEEES, you are right. Let's move on to level 4")
                    break
                else:
                    print()
                    timeprint('Ooops wrong input. Try again')

            else:
                print()
                timeprint('Ooops wrong input. Try again')

        else:
            print()
            timeprint('Ooops wrong input. Try again')

    return tickets
