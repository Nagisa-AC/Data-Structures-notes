class Node:
	def __init__(self, val):
		self.val = val 
		self.next = None 


class CircularLinkedList:
	def __init__(self):
		self.head = None 


	def append(self, val):
		newNode = Node(val)
		if not self.head:
			self.head = newNode
			newNode.next = self.head
			return 
		iterNode = self.head
		while iterNode.next != self.head:
			iterNode = iterNode.next
		iterNode.next = newNode
		newNode.next = self.head


	def prepend(self, val):
		newNode = Node(val)
		if not self.head:
			self.head = newNode
			newNode.next = self.head
			return 
		iterNode = self.head
		while iterNode.next != self.head:
			iterNode = iterNode.next
		iterNode.next = newNode
		newNode.next = self.head
		self.head = newNode


	def traverse(self):
		if not self.head:
			print('Circular linked list is empty')
			return 
		iterNode = self.head  
		while iterNode != None:
			print(f'{iterNode.val}', end=" --> ")
			iterNode = iterNode.next
			if iterNode == self.head:
				break 
		print(f'{iterNode.val}')


	def remove(self, val):
		iterNode = self.head
		if self.head.val == val:
			while iterNode.next != self.head:
				iterNode = iterNode.next
			iterNode.next = iterNode.next.next
			self.head = self.head.next
			return 

		while iterNode.next.val != val:
			iterNode = iterNode.next
		if not iterNode:
			print('Not found')
			return 
		if iterNode.next.next == self.head:
			iterNode.next = self.head
		else:
			iterNode.next = iterNode.next.next


	def length(self):
		iterNode = self.head
		count = 0
		while iterNode != None:
			count += 1
			iterNode = iterNode.next
			if iterNode == self.head:
				break
		return count 


	def split_list(self):
		length = self.length()
		first_head, tail_node = self.head, self.head 
		counter, midpoint = 1, length // 2
		while counter !=  midpoint:
			tail_node = tail_node.next
			counter += 1
		second_head = tail_node.next
		tail_node.next = first_head
		sentinal_node = second_head
		while sentinal_node.next != self.head:
			sentinal_node = sentinal_node.next
		sentinal_node.next = second_head
		self.traverse()
		self.head = second_head
		self.traverse()





	#	1 --> 2 -- > 3 --> 4 --> 5 --> 6
		



	def josephus_circle(self, val):
		pass




cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.append(40)
cll.split_list()






