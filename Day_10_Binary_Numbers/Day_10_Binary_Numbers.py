if __name__ == "__main__":
    n = int(input())
    n = bin(n)
    maxc = 0
    temp = 0
    for i in range(2, len(n)):
        if n[i] == '1':
            temp += 1
        else:
            temp = 0
        if temp > maxc:
            maxc = temp

    print(maxc)