from collections import Counter


def isanagram(s, t):
    # if len(s) < len(t):
    #    return False
    #t = list(t)
    # print(t)
    # for i in s:
    #    if i in t:
    #        t.remove(i)
    #    else:
    #        return False
    # return True
    c1 = Counter(s)
    c2 = Counter(t)
    keys = set(c1.keys()).union(c2.keys())

    for key in keys:
        if key not in c1 or key not in c2 or c1[key] != c2[key]:
            return False

    return True


def main():
    print(isanagram("anagram", "nagaram"))
    print(isanagram("rat", "car"))


if __name__ == "__main__":
    main()
