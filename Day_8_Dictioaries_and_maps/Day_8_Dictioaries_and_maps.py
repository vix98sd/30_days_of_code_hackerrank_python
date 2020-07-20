if __name__ == "__main__":
    n = int(input())
    phone_book = {}
    for i in range(n):
        s = input().rstrip().split()
        phone_book[s[0]] = s[1]

    s = "a"
    while s != "":
        try:
            s = input()
            if s not in phone_book.keys():
                print("Not found")
            else:
                print(s + "=" + phone_book[s])
        except EOFError:
            break