if __name__ == "__main__":
    t = int(input())
    strings = []
    for i in range(t):
        strings.append(input())

    for s in strings:
        print(s[::2], s[1::2])