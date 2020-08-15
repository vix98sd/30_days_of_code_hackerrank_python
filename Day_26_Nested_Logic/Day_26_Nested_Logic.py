if __name__ == "__main__":
	d1, m1, y1 = map(int,input().split())
	d2, m2, y2 = map(int, input().split())
	
	fee = 0
	if y1 > y2:
		fee = 10000
	elif m1 > m2 and y1 == y2:
		fee = 500 * (m1 - m2)
	elif d1 > d2 and m1 == m2:
		fee = 15 * (d1 - d2)
	print(fee)
