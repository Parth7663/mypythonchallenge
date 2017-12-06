def map(s):
    list = []

    for i in range(len(s)):
        if ord(s[i]) < 97:
            list.append(s[i])
        elif ord(s[i]) > 120:
            list.append(chr(ord(s[i]) - 24))
        else:
            list.append(chr(ord(s[i])+2))

    for i in list:
        print(i, end="")

if __name__ == "__main__":
    import sys
    map(str(sys.argv[1]))
