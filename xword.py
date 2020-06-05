#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "hpost2019"


def word_lookup(test_word, words):
    word_list = filter(lambda word: len(word) == len(test_word), words)
    for index in range(len(test_word)):
        if test_word[index] != " ":
            word_list = [word for word in word_list if
                         word[index] == test_word[index]]
    return word_list


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()
    test_word = input(
        'Please enter a word to solve.\nUse spaces to'
        'signify unknown letters: ').lower()

    fin_list = word_lookup(test_word, words)
    for word in fin_list:
        print(word)


if __name__ == '__main__':
    main()
