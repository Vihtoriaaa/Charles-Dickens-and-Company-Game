"""Welcome to Charles Dickens and Company game!"""
import webbrowser
from level1 import first_level
from level2 import second_level
from level3 import third_level
from level4 import four_level
import os
from support_functions import timeprint


def clear():
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def wikipedia(url: str):
    """This function cleans the terminal and opens the webpage.
    >>> wikipedia("https://en.wikipedia.org/wiki/Charles_Dickens")"""
    clear()
    print("\n    |    WIKIPEDIA PAGE    |")
    webbrowser.open(url, new=1)
    timeprint('Thanks for playing. Have a good day :)')


def start_game():
    """This function is used to start the game."""
    clear()
    print('------------------------')
    timeprint(
        '|     MINI-PROJECT     |\n|  Victoria Maksymiuk  |\n|    IT&BA UCU 2020\
    |')
    print('------------------------')
    start_tickets = 0
    level1_tickets = first_level(start_tickets)
    if level1_tickets == 0:
        timeprint("Game over, thanks for playing :)")
    else:
        timeprint("Lets move on to level 2")
        clear()
        timeprint("Welcome to level 2!\nYou have a new challenge. Your task is:\
    \nChoose the books which were not written by Charles Dickens.\nFor the right \
answer you get some bonus points. If the answer is wrong, then it \
disappears and there are 2 books left to choose from.\nGood luck:)")
        print()
        level2_tickets = second_level(level1_tickets)
        timeprint("Let's move on right to level 3")
        clear()
        timeprint('Welcome to level 3!\nYou have a new challenge. Your task is: \
\nChoose the author that did not wrote at the same period of time as Charles \
Dickens did. With every mistake the number of points you can get reduces. \
If the answer is wrong, then it disappears and there are one less authors \
left to choose from.\nGood luck:)')
        level3_tickets = third_level(level2_tickets)
        timeprint("Let's move on right to level 4")
        clear()
        level4_tickets = four_level(level3_tickets)
        print()
        timeprint('Congratulations for winning the game :)')
        print('Your score is -', level4_tickets)
        timeprint("Do you want to discover more about Charles Dickens?")
        user_input = input('Yes/No?: ')
        if user_input == 'Yes':
            wikipedia("https://en.wikipedia.org/wiki/Charles_Dickens")
        elif user_input == 'No':
            timeprint('Thanks for playing. Have a good day :)')
        else:
            timeprint('Thanks for playing. Have a good day :)')


start_game()
