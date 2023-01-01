class Node:
	def __init__(self, val):
		self.val = val 
		self.next = None 
		self.prev = None 


class DoublyLinkedList:
	def __init__(self):
		self.head = None 

	def append(self, val):
		newNode = Node(val)
		if not self.head:
			self.head = newNode
			return 
		iterNode = self.head 
		while iterNode.next != None:
			iterNode = iterNode.next
		newNode.prev = iterNode
		iterNode.next = newNode
		newNode.next = None 


	def traverse(self):
		iterNode = self.head
		while iterNode != None:
			print(f'{iterNode.val}')
			iterNode = iterNode.next

	def node_before(self, val):
		pass


	def prepend(self, val):
		pass 


	def add_before(self, val):
		pass 


	def add_after(self, val):
		pass 


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.traverse()