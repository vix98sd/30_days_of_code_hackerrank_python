if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    output = ""
    for i in range(1, len(arr) + 1):
        output += str(arr[-i]) + " "
    print(output)