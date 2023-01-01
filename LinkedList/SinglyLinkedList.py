import math


class Node:
	'''
		Try and modify the source code to use a hashmap to improve
		the efficiencies of various operations
	'''
	def __init__(self, val):
		self.val = val
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	@staticmethod
	def empty_list():
		print('Empty list')
		return

	def traverse(self):
		if self.head is None:
			print('Empty list')
			return
		curr = self.head
		while curr is not None:
			print(f'{curr.val}', end=' --> ')
			curr = curr.next
		print('None')

	def add_head(self, val):
		new_head = Node(val)
		if self.head is not None:
			new_head.next = self.head
		self.head = new_head
		return

	def count_occur(self, val):
		if self.head is None:
			print('Empty list')
			return 0
		counter = 0
		curr = self.head
		while curr:
			if curr.val == val:
				counter += 1
			curr = curr.next
		return counter

	def add_before(self, val, k):
		if self.head is None:
			self.empty_list()
		# fix dup issue pls (hmap I think)
		curr = self.head
		if curr.val == k:
			self.add_head(val)
			return

		new_node = Node(val)
		while curr.next.val != k:
			curr = curr.next
		if curr is None:
			print(f'{k} not found')
			return
		new_node.next = curr.next
		curr.next = new_node

	def add_after(self, val, k):
		if self.head is None:
			self.empty_list()
		new_node = Node(val)
		curr = self.head
		while curr.val != k:
			curr = curr.next
		if curr is None:
			print(f'{k} not found')
			return
		new_node.next = curr.next
		curr.next = new_node

	def length(self):
		counter = 0
		if not self.head:
			return counter
		curr = self.head
		while curr:
			counter += 1
			curr = curr.next
		return counter

	def is_palindrome(self):
		if self.head is None:
			print('Empty')
			return False
		curr = self.head
		string = ""
		while curr:
			string += f'{curr.val}'
			curr = curr.next
		return string == string[::-1]

	def reverse(self):
		prev = None
		next_ = None
		curr = self.head

		while curr:
			next_ = curr.next
			curr.next = prev
			prev = curr
			curr = next_
		self.head = prev

	def del_by_index(self, index):
		if index < 0:
			raise IndexError('Index out of bounds')
		curr = self.head
		if index == 0:
			self.head = self.head.next
			del curr
			return
		counter = 0
		target_index = index - 1
		while counter != target_index:
			curr = curr.next
			counter += 1
		if not curr and curr.next:
			raise IndexError('Index out of bounds')
		curr.next = curr.next.next

	def del_by_val(self, val):
		if self.head is None:
			self.empty_list()
		curr = self.head
		if curr.val == val:
			self.head = curr.next
			del curr
			return

		while curr.next.val != val:
			curr = curr.next
		if not curr and curr.next:
			print(f'{val} not found')
			return
		curr.next = curr.next.next

	def remove_dup_by_val(self, val):
		if self.head is None:
			self.empty_list()
		curr = self.head
		while curr.next.val != val:
			curr = curr.next
		if not curr:
			print(f'{val} not in list')
			return
		while curr.next.next.val != val:
			curr = curr.next
		print(curr, curr.val)

	def swap_nodes(self, node_one, node_two):
		pass

	def add_tail(self, tail_value):
		new_tail = Node(tail_value)
		if self.head is None:
			self.head = new_tail
			self.tail = new_tail
			return
		curr_node = self.head
		while curr_node.next is not None:
			curr_node = curr_node.next
		curr_node.next = new_tail
		self.tail = new_tail

	def sorted_insert(self, val):
		new_node = Node(val)
		curr_node = self.head
		if curr_node is None:
			self.head = new_node
			return
		if val < curr_node.val:
			new_node.next = curr_node
			self.head = new_node
			return

		while curr_node.next and new_node.val >= curr_node.next.val:
			curr_node = curr_node.next
		next_node = curr_node.next
		curr_node.next = new_node
		new_node.next = next_node

	def kth_to_last_node(self, k):
		fast_node = self.head
		counter = 0
		while fast_node is not None:
			counter += 1
			counter_node = fast_node.next
		target_node = self.head
		while counter != k:
			counter -= 1
			target_node = target_node.next
		return target_node

	def middle_node(self):
		fast_node = self.head
		counter = 0
		while fast_node:
			counter += 1
			fast_node = fast_node.next
		if counter % 2 == 0:
			mid_point = int(counter / 2)
		else:
			mid_point = math.ceil(counter / 2)
		target_node = self.head
		target_index = 1

		while target_index != mid_point:
			target_node = target_node.next
			target_index += 1
		print(target_node.val)
		return target_node

