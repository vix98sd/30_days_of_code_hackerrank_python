def isWeird(n):
    if(n % 2 == 1):
        return True
    elif(n >= 2 and n <= 5):
        return False
    elif(n >= 6 and n <= 20):
        return True
    else:
        return False

if __name__ == "__main__":
    if(isWeird(int( input() ))):
        print("Weird")
    else:
        print("Not Weird")