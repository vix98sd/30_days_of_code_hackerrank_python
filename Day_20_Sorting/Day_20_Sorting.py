import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def bubble_sort(a):
    numSwap = 0
    for i in range(len(a)):
        j = 0
        while j != len(a) - i - 1:
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                numSwap += 1
            j+=1
    
    print("Array is sorted in", numSwap, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])

bubble_sort(a)