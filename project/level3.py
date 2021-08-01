"""third level of my game yes!!!"""
import random
from support_functions import timeprint, find_authors, book_csv, find_other_authors


def third_level(tickets):
    """
    This function is the third level of the game. It help the user to discover\
    more about the authors that wrote at the same time as Charles Dickens did.\
    The user gets names of 4 authors, one of them is a 'wrong'(did not wrote \
    at the same time) author, and the other 3 are 'right'. The user has to \
    choose the 'wrong' author to complete the level. With every mistake the \
    number of possible points the user can get reduces. If the answer is wrong,\
    then the user does not the user_input disappears and there are one less \
    author left to choose. If the user fails to win, then he goes to level 4 \
    without any points.
    """
    tickets = int(tickets)
    authors = find_authors(book_csv, '1812-1870')
    others = find_other_authors(book_csv, '1812-1870')

    four_authors = []
    wrong_author = random.choice(others)
    four_authors.append(wrong_author)

    three_authors = [[auth for auth in random.choice(authors) if auth not in four_authors] for _ in range(3)]
    three_authors = [''.join(x) for x in three_authors]
    four_authors += three_authors

    if len(four_authors) < 4:
        for _ in range(4-len(four_authors)):
            new_author = random.choice(authors)
            if new_author not in four_authors:
                four_authors.append(new_author)

    four_authors = '\n'.join(four_authors)
    print()
    timeprint("Here are authors you have to choose from:")
    while True:
        print("-----------------------------------------------")
        timeprint(four_authors)
        print("-----------------------------------------------")
        print()
        timeprint("Enter the author's name who did not write when \
Charles Dickens did:")
        user_input = input()
        if user_input == wrong_author:
            print()
            tickets = tickets + 3
            timeprint("Yes! you are right. Let's move on to level 4")
            break

        if user_input in three_authors:
            print()
            timeprint("Oops, wrongs answer :(")
            four_authors = four_authors.replace(user_input, '')
            four_authors = four_authors.strip()
            timeprint("Here are authors left you have to choose from:")
            print("-----------------------------------------------")
            timeprint(four_authors)
            print("-----------------------------------------------")
            print()
            user_input = input()

            if user_input == wrong_author:
                print()
                tickets += 2
                timeprint("Yes! you are right. Let's move on to level 4")
                break

            if user_input in three_authors:
                print()
                timeprint("Oops, wrongs answer :( You have only one chance\
 left to complete this level")
                four_authors = four_authors.replace(user_input, '')
                four_authors = four_authors.strip()
                timeprint("Here are authors left you have to choose from:")
                print("-----------------------------------------------")
                timeprint(four_authors)
                print("-----------------------------------------------")
                print()
                user_input = input()

                if user_input in three_authors:
                    print()
                    timeprint('You failed to complete this level without \
mistakes :( Lets move to level 4')
                    break
                if user_input == wrong_author:
                    print()
                    tickets = tickets + 1
                    timeprint("Yes! you are right. Let's move on to level 4")
                    break
                else:
                    print()
                    timeprint('Oops, wrong input. Try again')

            else:
                print()
                timeprint('Oops, wrong input. Try again')

        else:
            print()
            timeprint('Oops, wrong input. Try again')

    return tickets
