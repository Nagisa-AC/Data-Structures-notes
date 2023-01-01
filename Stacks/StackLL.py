# class Node:
# 	def __init__(self, val):
# 		self.val = val
# 		self.next = None
#
#
# class Stack:
# 	def __init__(self):
# 		self.head = None
# 		self.length = 0
#
# 	def size(self):
# 		return self.length
#
# 	def is_empty(self):
# 		if self.length == 0:
# 			return True
# 		else:
# 			return False
#
# 	def push(self, val):
# 		new_val = Node(val)
# 		if self.head is None:
# 			self.head = new_val
# 		else:
# 			new_val.next = self.head
# 			self.head = new_val
# 		self.length += 1
#
# 	def peek(self):
# 		if self.head is None:
# 			print('Linked list is empty')
# 		else:
# 			return self.head
#
# 	def pop(self):
# 		if self.length == 0:
# 			print('Empty stack')
# 			return
# 		curr_node = self.head
# 		if self.length > 1:
# 			new_head = curr_node.next
# 			self.head = new_head
# 			del curr_node
# 		elif self.length == 1:
# 			del curr_node
# 			self.head = None
# 		self.length -= 1
#
# 	def traverse(self):
# 		if self.head is None:
# 			print('Empty stack')
# 			return
# 		curr_node = self.head
# 		while curr_node is not None:
# 			print(curr_node.val)
# 			curr_node = curr_node.next
#
#
# s = Stack()
# s.push(0)
# s.push(10)
# s.push(20)
# s.push(30)
# s.traverse()
# s.pop()
# print('\n')
# s.traverse()



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print('Empty stack')
            return
        curr_head = self.head
        if self.length == 1:
            del curr_head
            self.head = None
        if self.length > 1:
            new_head = curr_head.next
            del curr_head
            self.head = new_head
        self.length += 1

    def peek(self):
        if self.head is None:
            print('Stack is empty')
        else:
            return self.head.val

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def traverse(self):
        if self.head is None:
            print('Stack empty')
        else:
            curr_node = self.head
            while curr_node is not None:
                print(curr_node.val)
                curr_node = curr_node.next





















