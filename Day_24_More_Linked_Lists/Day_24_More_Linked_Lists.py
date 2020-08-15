class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Solution:
	def insert(self, head, data):
		if head is None:
			head = Node(data)
		else:
			head.next =  self.insert(head.next, data)
		return head

	def display(self, head):
		print(self.display2(head))

	def display2(self, head):
		if head is None:
			return ""
		return str(head.data) + " " + self.display2(head.next) 

	def removeDuplicates(self,head):
		if head is None:
			return None

		if head.next is None:
			return head

		if head.next.next is None and head.next.data == head.data:
			head.next = None
			return head
		outher = head
		try:
			while outher.next is not None:
				inner = outher.next
				while inner is not None:
					if outher.data == inner.data:
						outher.next = inner.next
					inner = inner.next
		
				outher = outher.next	
		except:
			return head
		
		return head		
myList = Solution()
T = int(input())
head = None
for i in range(T):
	data = int(input())
	head = myList.insert(head, data)
head = myList.removeDuplicates(head)
myList.display(head)
