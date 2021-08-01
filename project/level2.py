import time
import random
import pandas as pd
import os
from support_functions import read_data, find_books, find_other_books, timeprint, book_csv

def second_level(tickets):
    """
    This function is the second level of the game. It help the user to discover\
    more Charles Dickens' books. The user gets 3 books, one of them was\
    written by Charles Dickens, and the other 2 are from other authours. The\
    user has to choose the books which were not written by Charles to complete\
    this level. For the right answer the user gets some bonus points. If the \
    answer is wrong, then user_input dissappears and the user does not gets \
    points there are 2 books left to choose. If the user fails to win, then \
    he goes to level 3 without any points.
    """
    other_books = find_other_books(book_csv, 'Dickens, Charles')
    author_books = find_books(book_csv, 'Dickens, Charles')
    three_books = []
    one_book = random.choice(author_books)

    if one_book not in three_books:
        three_books.append(one_book)

    second_book = random.choice(other_books)
    if second_book not in three_books:
        three_books.append(second_book)

    third_book = random.choice(other_books)
    if third_book not in three_books:
        three_books.append(third_book)

    if len(three_books) < 3:
        new_book = random.choice(other_books)
        if new_book not in three_books:
            three_books.append(new_book)

    random.shuffle(three_books)
    three_books = '\n'.join(three_books)
    tickets = int(tickets)
    while True:
        timeprint("Here are 3 book you have to choose from:")
        print("-------------------------\n|      THREE BOOKS      |\n---------\
----------------")
        timeprint(three_books)
        print()
        timeprint("Choose not Charles Dickens' book and enter its name\
 (Copy Past): ")

        user_input = input()

        if user_input == one_book:
            print()
            timeprint("Ooops wrong answer:( You failed to pass this level.")
            break

        elif user_input == second_book or user_input == third_book:
            print()
            tickets += 1
            timeprint("YEES, you are rigth. Now there are 2 books left")
            three_books = three_books.replace(user_input, '')
            three_books = three_books.strip()

            timeprint("Here are 2 books you have to choose from:")
            print("--------------------------\n|        TWO BOOKS       |\n---\
-----------------------")
            timeprint(three_books)
            print()

            timeprint("Choose not Charles Dickens' book and enter its name\
 (Copy Past): ")

            user_input = input()
            if user_input == one_book:
                print()
                timeprint("Ooops wrong answer:( You failed to pass this level\
 without mistakes.")
                break

            elif user_input == second_book or user_input == third_book:
                print()
                tickets += 1
                timeprint("Congratulations for passing level 2:)")
                break

            else:
                print()
                timeprint("Ooops wrong input. Try again")

        else:
            print()
            timeprint("Ooops wrong input. Try again")

    return tickets
