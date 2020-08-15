class Node:
	def __init__(self, data):
		self.right=self.left=None
		self.data = data
class Solution:
	def insert(self,root,data):
		if root is None:
			return Node(data)
		else:
			if data <= root.data:
				cur = self.insert(root.left,data)
				root.left = cur
			else:
				cur = self.insert(root.right, data)
				root.right = cur
		return root

	def getHeight(self, root):
		# code
		if root is None:
			return -1
		return 1 + self.getHeight(root.left) if self.getHeight(root.left) > self.getHeight(root.right) else 1 + self.getHeight(root.right)

	def levelOrder(self, root):
		height = self.getHeight(root)
		lOrder = []
		for i in range(height+1):
			self.printLevel(0, i, root, lOrder)
		output = ""
		for i in lOrder:
			output += str(i) + " "
		print(output)
		
	def printLevel(self, current, level, root, lOrder):
		if root is None:
			return
		if current == level:
			lOrder.append(root.data)
			return		

		self.printLevel(current+1, level, root.left, lOrder)
		self.printLevel(current+1, level, root.right, lOrder)

def Main():
	T = int(input())
	myTree=Solution()
	root=None
	for i in range(T):
		data = int(input())
		root = myTree.insert(root,data)

	myTree.levelOrder(root)

if __name__ == "__main__":
	Main()





