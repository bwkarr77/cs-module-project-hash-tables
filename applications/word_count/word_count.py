import string
ascii_letters = set(map(ord, string.ascii_letters))
non_letters = ''.join(chr(i) for i in range(256) if i not in ascii_letters)

# cache = {}

def word_count(s):
    # Your code here
    cache = {}
    lower = s.lower()
    for symbol in non_letters:
        if symbol == "'":
            pass
        else:
            lower = lower.replace(symbol, "\n")

    for each in lower.split():
        # print('each: ', each)
        if each == "":
            continue
        if each not in cache:
            cache[each] = 1
        else:
            cache[each] += 1

    return cache

# def sort_by_val(s):
#     counts_dict = letter_counts(s)  # taken from lecture
#     ## sort by value
#     counts_list = list(counts_dict.items())
#     # sort by value, AND in descending order
#     counts_list.sort(reverse = True, key = lambda x: x(1))
#
#     for pair in counts_list:
#         print(f'count: {pair{1}} letter: {pair{0}')



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))