import random
import string

ascii_letters = set(map(ord, string.ascii_letters))
non_letters = ''.join(chr(i) for i in range(256) if i not in ascii_letters)

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # print(words)


# TODO: analyze which words can follow other words
# Your code here

def create_library(word_file):
    cache = {}
    words_list = word_file.split()

    for i, word in enumerate(words_list):
        if word == "":
            continue
        if i < len(words_list) - 1:
            cache[word] = words_list[i + 1]
        else:
            cache[word] = word

    # print(cache)
    return cache


# TODO: construct 5 random sentences
# Your code here
def writer_func(cache):
    # random number is picked, search through the keys in cache, return the first/only value found, and capitalize
    # the first letter.
    # - random.choices():  searches through a list for any random number picked.
    # - list(cache.keys()): cache is turned into a list of keys
    # - [0]: returns the first/only value returned from random.choices()
    #
    is_start = False
    is_stop = False
    start = ''
    are_quotes = 0

    while is_start is False:
        word = random.choices(list(cache.keys()))[0]
        if word[0].isupper():
            start = word
            is_start = True
        elif word[0] == '"' and len(word) > 1:
            if word[1].isupper():
                start = word
                are_quotes += 1
                is_start = True

    sentence = start + " "
    stop_check = [".", "?", "!"]

    while is_stop is False:
        next_word = random.choices(list(cache.keys()))[0]
        # check for stop words
        last_char = next_word[len(next_word)-1]
        if next_word[0] == '"':
            are_quotes += 1
        if (are_quotes == 0) and (last_char in stop_check):
            is_stop = True
        elif (are_quotes > 0) and (last_char == '"'):
            are_quotes -= 1
            if are_quotes == 0:
                is_stop

        sentence = sentence + next_word + " "
    return sentence


loop_count = 5
for i in range(0, loop_count):
    print(writer_func(create_library(words)))
