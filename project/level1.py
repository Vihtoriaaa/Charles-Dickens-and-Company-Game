""""first level of my game yes!"""
import random
import string
from support_functions import timeprint


def first_level(tickets):
    """
    This function is the first level of the game. It help the user to discover
    some facts about Charles Dickens. If the user gets the right answer, he
    passes to level 2. If the answer is wrong, then the user gets another fact
    about the writer. It continues until the moment the user makes 3 mistakes.
    Then the game is over
    """
    tickets = int(tickets)
    name_list = list('CHARLESDICKENS')
    random.shuffle(name_list)
    list_alphabet = list(string.ascii_uppercase)

    three_char = [[char for char in random.choice(list_alphabet)] for _ in range(3)]
    three_char = [''.join(x) for x in three_char]
    name_list += three_char

    all_letters = ' '.join(name_list)
    fact1 = "He published one of the most iconic Christmas stories of all \
times in 1843."
    fact2 = "He was an English writer and social critic \
during the 19th century"
    fact3 = "He is regarded as the greatest novelist of the Victorian era"
    fact4 = "He was born on February 7, 1812 in Portsmouth, United Kingdom"
    fact5 = "His last novel, The Mystery of Edwin Drood, remains a mystery."
    facts = [fact1, fact2, fact3, fact4, fact5]

    while True:
        timeprint("Welcome to Charles Dickens' and Company game:)\nNow you are \
at level 1.\nYour task - guess the author's name from the facts that \
will appear. \nGood luck, have fun and let's start.\n")

        print("--------------------------\n|        ROUND ONE       |\n---\
-----------------------")
        timeprint('Here is the first fact:')
        fact = random.choice(facts)
        timeprint(fact)
        print()
        facts.remove(fact)
        timeprint(all_letters)
        timeprint("\nUse the letters above and enter the writer's name \
with capital letters: ")

        user_input = input()
        if user_input == 'CHARLES DICKENS':
            print()
            timeprint("Congratulations for passing level 1:)")
            tickets += 3
            break

        else:
            print()
            timeprint("Oops, you've made a mistake.")
            timeprint("We can help you to get the right answer.")
            fact = random.choice(facts)
            print("--------------------------\n|        ROUND TWO       |\n---\
-----------------------")
            timeprint('Here is the first hint:')
            timeprint(fact)
            print()
            facts.remove(fact)
            timeprint(all_letters)

            timeprint("\nUse the letters above and enter the writer's name \
with capital letters: ")
            user_input = input()

            if user_input == 'CHARLES DICKENS':
                tickets += 2
                print()
                timeprint("Congratulations for passing level 1:)")
                break

            else:
                print()
                timeprint("Oops, you've made another mistake. You have only \
# one chance left to pass this level.")
                fact = random.choice(facts)
                print("-----------------------\
-----\n|        ROUND THREE       |\n----------------------------")
                timeprint("Here is another hint for you:")
                timeprint(fact)
                print()
                facts.remove(fact)
                timeprint(all_letters)

                timeprint("\nUse the letters above and enter the writer's name \
with capital letters: ")
                user_input = input()

                if user_input == 'CHARLES DICKENS':
                    print()
                    tickets += 1
                    timeprint("Congratulations for passing level 1:)")
                    break

                else:
                    print()
                    timeprint("Game Over. Thanks for playing a game!")
                    break
    return tickets
