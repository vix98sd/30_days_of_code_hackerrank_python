def sum_of_hourglasses(arr):
    s = []
    for i in range(4):
        for j in range(4):
            s.append(sum_of_hourglass(i,j,arr))
    return max(s)
def sum_of_hourglass(x,y,arr):
    return arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(sum_of_hourglasses(arr))