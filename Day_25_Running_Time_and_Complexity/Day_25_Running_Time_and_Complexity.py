import math

if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		number = int(input())
		isPrime = True
		for j in range(2,math.ceil(math.sqrt(number)+1)):
			if number % j == 0:
				isPrime = False
				break
		if (isPrime and number != 1) or number == 2 :
			print("Prime")
		else:
			print("Not prime")
		
