class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        self.maximumDifference =  abs(min(self.__elements) - max(self.__elements))
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)