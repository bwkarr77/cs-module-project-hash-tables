# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import string
ascii_letters = set(map(ord, string.ascii_letters))
non_letters = ''.join(chr(i) for i in range(256) if i not in ascii_letters).join(['”', "€"])

with open('ciphertext.txt') as f:
    content = f.read()

frequency_order = [
    'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
    ]

def cipher(content):
    # Your code here
    cache = {}
    upper = content.upper()
    for symbol in non_letters:
        upper = upper.replace(symbol, "")

    for each in upper:
        if each == '':
            continue
        if each not in cache:
            cache[each] = 1
        else:
            cache[each] += 1

    sorted_cache = sorted(cache.items(), key=lambda item: item[1], reverse=True)

    cipher_cache = {}
    for index, each in enumerate(sorted_cache):
        cipher_cache[sorted_cache[index][0]] = frequency_order[index]

    return cipher_cache

ciphered_dict = cipher(content)
result = ''

for each in content:
    res = each
    if each in ciphered_dict.keys():
        res = ciphered_dict[each]
    result += res

print(result)


