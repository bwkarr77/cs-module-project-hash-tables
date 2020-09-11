def no_dups(s):
    # Your code here
    cache = {}
    lower = s.lower()
    for word in lower.split():
        if word == "":
            continue
        if word not in cache:
            # cache[word] = 1
            cache[word] = word
        else:
            # cache[word] += 1
            continue

    # return cache
    return " ".join(list(cache.keys()))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))