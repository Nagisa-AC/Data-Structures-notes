# Queue implementation with linked list

class Node:
	def __init__(self, val):
		self.val = val 
		self.next = None 


class Queue:
	def __init__(self):
		self.front = None 
		self.rear = None 
		self.count = 0 

	def enqueue(self, val):
		newNode = Node(val)
		if self.front == None:
			self.front = newNode
			self.rear = newNode
			self.count += 1
			return 
		self.rear.next = newNode
		self.rear = newNode

	def print(self):
		iterNode = self.front
		if iterNode == None:
			print('Linked list is empty')
			return 
		while iterNode != None:
			print(f'{iterNode.val}', end=" --> ")
			iterNode = iterNode.next
		print('None')


	def dequeue(self):
		if self.isEmpty():
			print('Cannot dequeue from empty queue')
			return 
		self.front = self.front.next

	def isEmpty(self):
		if self.front == None:
			return True 
		return False

	def peek(self):
		if self.isEmpty():
			print('Queue is empty')
			return 
		return self.front.val


a = Queue()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.print()
print(a.peek())
a.dequeue()
a.print()
print(a.peek())