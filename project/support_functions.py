"""
Module dedicated to getting to know with Charles Dickens and his creativity.
Created by Victoria Maksymiuk
"""
import pandas as pd
import time
import os


def timeprint(line):
    """
    This function prints a text in live mode
    """
    for i in line:
        print(i, end="", flush=True)
        time.sleep(0.02)
    print()


def intro_text():
    """
    This function prints the text below in live mode at the beginning of the
    game
    """
    timeprint("MINI-PROJECT \nVictoria Maksymiuk\nBA 2020")


def read_data(path):
    """
    this function reads the information from the csv file and returns the
    it as DataFrame. if path is not str the function returns None
    >>> read_data([])

    """
    if isinstance(path, str):
        dtf = pd.read_csv(path, low_memory=False)
        return dtf
    else:
        return None


def read_data_tsv(path):
    """
    this function reads the information from the csv file and returns the
    it as DataFrame. if path is not str the function returns None
    >>> read_data_tsv(111)

    """
    if isinstance(path, str):
        dtf = pd.read_csv(path, sep='\t', low_memory=False)
        return dtf
    else:
        return None


def find_books(dtf, author):
    """
    This function finds the book written by Charles Dickens and were published
    in English language. If author type is not str the function returns
    None. Database that should be used is titles.csv with the function \
    read_data()
    >>> find_books(111, [])

    """
    if not isinstance(author, str):
        return None
    book_lst_charles = []
    dtf = dtf[dtf['Name'] == author]
    dtf = dtf[dtf['Role'] == 'author']
    dtf = dtf[dtf['Languages'] == 'English']
    books = dtf['Title']
    for book in books:
        if book not in book_lst_charles:
            book_lst_charles.append(book)
    return book_lst_charles


book_csv = read_data(
    '/Users/vmaksymiuk/Downloads/UCU/ucu_programming/mini-project/titles.csv')


def find_other_books(dtf, author):
    """
    This function finds the book that were not written by Charles Dickens\
    and were published in English language. If author type is not str the
    function returns None. Data base that should be used is titles.csv with\
    the function read_data()
    >>> find_books(2353, 1111)

    """
    if not isinstance(author, str):
        return None
    book_lst_others = []
    dtf = dtf.dropna(subset=['Name'])
    dtf = dtf[dtf['Name'] != author]
    dtf = dtf[dtf['Languages'] == 'English']
    books = dtf['Title']
    for book in books:
        if book not in book_lst_others:
            book_lst_others.append(book)
    return book_lst_others


def find_authors(dtf, date):
    """
    This function finds the authors that were writting at the same period
    of time as Charles Dickens did. If date type is not str the function
    returns None. Data base that should be used is titles.csv with the\
    function read_data()
    >>> find_authors(1234, [])

    """
    if not isinstance(date, str):
        return None

    authors_lst = []
    dtf = dtf.dropna(subset=['Dates associated with name'])

    new_date = date.replace('-', '')
    first_number = new_date[:4]
    second_number = new_date[4:]

    dates = [first_number, second_number]
    max_date = max(dates)
    min_date = min(dates)

    dtf = dtf[(dtf["Dates associated with name"] >= min_date) &
              (dtf["Dates associated with name"] <= max_date)]
    dtf = dtf[dtf['Name'] != 'Dickens, Charles']
    authors = dtf['Name']

    for pers in authors:
        if pers not in authors_lst:
            authors_lst.append(pers)

    return authors_lst


def find_other_authors(dtf, date):
    """
    This function finds the authors that were not writting at the same period
    of time as Charles Dickens did. If date type is not str the function
    returns None. Data base that should be used is titles.csv with the \
    function read_data()
    >>> find_other_authors('', [])

    """
    if not isinstance(date, str):
        return None

    other_authors_lst = []
    dtf = dtf.dropna(subset=['Dates associated with name'])
    new_date = date.replace('-', '')

    first_number = new_date[:4]
    second_number = new_date[4:]
    dates = [first_number, second_number]
    max_date = max(dates)
    min_date = min(dates)

    dtf = dtf[(dtf["Dates associated with name"] < min_date) |
              (dtf["Dates associated with name"] > max_date)]
    dtf = dtf[dtf['Name'] != 'Dickens, Charles']
    authors = dtf['Name']

    for pers in authors:
        if pers not in other_authors_lst:
            other_authors_lst.append(pers)

    return other_authors_lst


name_basic = read_data_tsv('/Users/vmaksymiuk/Downloads/UCU/ucu_programming/mini-project/name.basics.tsv')


def get_author_id(dtf, author):
    """
    This function finds the author's code in IMDB. If author type is not str
    the function returns None. Data base that should be used is name.basics.tsv\
    with the function read_data_tsv()
    >>> get_author_id('', [])

    """
    if not isinstance(author, str):
        return None
    dtf = dtf[dtf['primaryName'] == author]
    code = dtf['nconst'].iloc[0]
    return code

# author_id = get_author_id(name_basic, 'Charles Dickens')


author_id = 'nm0002042'
title_crew = read_data_tsv(
    '/Users/vmaksymiuk/Downloads/UCU/ucu_programming/mini-project/title.crew.tsv')


def get_films_codes(dtf, author_id):
    """
    This function finds the code of films in which the author is in writers
    crew in IMDB. If author_id type is not str the function returns None.
    Data base that should be used is title.crew.tsv with the function \
    read_data_tsv() and author_id
    >>> get_films_codes('', [])

    """
    if not isinstance(author_id, str):
        return None
    dtf = dtf[dtf['writers'] == author_id]
    films = dtf['tconst']
    film_codes = []
    for ind in films:
        film_codes.append(ind)
    return film_codes

# film_codes = get_films_codes(title_crew, author_id)

# new_inform = '\n'.join(inform)


code = [line.replace('\n', '') for line in open("short_base.txt")]
title_basic_tsv = read_data_tsv(
    '/Users/vmaksymiuk/Downloads/UCU/ucu_programming/mini-project/title.basics.tsv')


def get_films_name(dtf, code):
    """
    This function finds names of films in which the author is in writers
    crew in IMDB. If author_id type is not str the function returns None.
    Data base that should be used is title.basics.tsv with the function \
    read_data_tsv() and code
    >>> get_films_name('', [])
    """
    if not isinstance(code, list):
        return None
    dtf = dtf.loc[dtf['tconst'].isin(code)]
    dtf_films = dtf[['primaryTitle']]
    film_names = set(iter(dtf_films['primaryTitle']))
    return film_names


def write_file(information, path):
    """
    This function writes the information given into txt file. If information
    type is not str, the function returns None
    >>> write_file([], 1234)

    """
    with open(path, "w") as file:
        file.write(information)
