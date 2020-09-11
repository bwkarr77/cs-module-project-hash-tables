# Your code here
import string
ascii_letters = set(map(ord, string.ascii_letters))
non_letters = ''.join(chr(i) for i in range(256) if i not in ascii_letters)

with open("robin.txt") as f:
    words = f.read()

def histo_gen(words_list):
    cache = {}
    lower = words_list.lower()
    longest = 0
    for symbol in non_letters:
        if symbol == "'":
            pass
        else:
            lower = lower.replace(symbol, "\n")

    for each in lower.split():
        if each == "":
            continue
        if each not in cache:
            cache[each] = "#"
            if len(each) > longest:
                longest = len(each)
        else:
            cache[each] = cache[each] + "#"

    sorted_list = sorted(cache.items(), key=lambda item: item[1], reverse=True)
    for word, pounds in sorted_list:
        word = word + " " * (longest - len(word))
        print(f'{word}  {pounds}')
    # return sorted_list

histo_gen(words)

