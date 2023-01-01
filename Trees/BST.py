# from collections import deque
# import queue
#
# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.left_child = None
# 		self.right_child = None
#
# class BinaryTree:
# 	def __init__(self, root):
# 		self.root = Node(root)
#
# 	def insert(self, value, root):
# 		if root == None:
# 			root = Node(value)
# 			return
#
# 		if value < root.value:
# 			if root.left_child:
# 				self.insert(value, root.left_child)
# 			else:
# 				root.left_child = Node(value)
# 		elif value > root.value:
# 			if root.right_child:
# 				self.insert(value, root.right_child)
# 			else:
# 				root.right_child = Node(value)
#
#
#
# 	def arr_to_bst(self):
# 		pass
#
# 	def delete(self):
# 		pass
#
#
# 	def print_tree(self, traversal):
# 		match traversal:
# 			case "preorder":
# 				print(self.preorder(tree.root, ""))
# 			case "inorder":
# 				print(self.inorder(tree.root, ""))
# 			case "postorder":
# 				print(self.postorder(tree.root, ""))
# 			case "levelorder":
# 				print(self.levelorder(tree.root, ""))
# 			case _:
# 				print(f'{traversal} traversal method not found')
#
#
# 	# <n, l, r>
# 	def preorder(self, root, traverse):
# 		if root:
# 			traverse += (str(root.value) + '-')
# 			traverse = self.preorder(root.left_child, traverse)
# 			traverse = self.preorder(root.right_child, traverse)
# 		return traverse
#
#
# 	# <l, n, r>
# 	def inorder(self, root, traverse):
# 		if root:
# 			traverse = self.inorder(root.left_child, traverse)
# 			traverse += (str(root.value) + '-')
# 			traverse = self.inorder(root.right_child, traverse)
# 		return traverse
#
#
# 	# <l, r, n>
# 	def postorder(self, root, traverse):
# 		if root:
# 			traverse = self.postorder(root.left_child, traverse)
# 			traverse += (str(root.value) + '-')
# 			traverse = self.postorder(root.left_child, traverse)
# 		return traverse
#
#
# 	# <L0, L1, L2, Ln>
# 	def levelorder(self, root, traverse) -> str:
# 		queue = deque()
# 		queue.append(root)
#
# 		while len(queue) > 0:
# 			node = queue.popleft()
# 			traverse += (str(node.value) + '-')
#
# 			if node.left_child:
# 				queue.append(node.left_child)
# 			if node.right_child:
# 				queue.append(node.right_child)
# 		return traverse
#
#
# 	def reverse_levelorder():
# 		pass
#
#
# 	def values_exists(self, root, value) -> bool:
# 		if root == None: return
# 		if root.value == value:
# 			return True
#
# 		result = False
# 		queue = deque()
# 		queue.append(root)
#
# 		while len(queue) > 0:
# 			node = queue.popleft()
# 			if node.value == value:
# 				return True
#
# 			if node.left_child:
# 				queue.append(node.left_child)
# 			if node.right_child:
# 				queue.append(node.right_child)
# 		return result
#
#
# 	def depth_values(self, root, values):
# 		if root:
# 			values.append(root.value)
# 			values = self.depth_values(root.left_child, values)
# 			values = self.depth_values(root.right_child, values)
# 		return values
#
#
# 	def breadth_values(self, root):
# 		queue, values = [], []
# 		queue.append(root)
#
# 		while len(queue) > 0:
# 			node = queue.pop(0)
# 			values.append(node.value)
#
# 			if node.left_child:
# 				queue.append(node.left_child)
# 			if node.right_child:
# 				queue.append(node.right_child)
# 		return values
#
#
# 	def tree_sum(self, root):
# 		sum = 0
# 		queue = []
# 		queue.append(root)
#
# 		while len(queue) > 0:
# 			node = queue.pop(0)
# 			sum += node.value
#
# 			if node.left_child:
# 				queue.append(node.left_child)
# 			if node.right_child:
# 				queue.append(node.right_child)
# 		return sum
#
#
# 	def tree_min_val(self, root):
# 		if root == None: return
#
# 		min_val = float('inf')
# 		queue = []
# 		queue.append(root)
#
# 		while len(queue) > 0:
# 			node = queue.pop(0)
# 			min_val = min(min_val, node.value)
#
# 			if node.left_child:
# 				queue.append(node.left_child)
# 			if node.right_child:
# 				queue.append(node.right_child)
# 		return min_val
#
#
# 	def tree_max_val(self, root):
# 		if root == None: return
#
# 		max_val = float('-inf')
# 		queue = []
# 		queue.append(root)
#
# 		while len(queue) > 0:
# 			node = queue.pop(0)
# 			max_val = max(max_val, node.value)
#
# 			if node.left_child:
# 				queue.append(node.left_child)
# 			if node.right_child:
# 				queue.append(node.right_child)
# 		return max_val
#
#
# 	def pre(self, root, res):
# 		if root:
# 			res.append(root.value)
# 			self.pre(root.left_child, res)
# 			self.pre(root.right_child, res)
# 		return res
#
#
# 	def sumall(self, root):
# 		sum = 0
# 		sum += root.value
#
# 		if (root.left_child != None):
# 			sum += self.sumall(root.left_child)
# 		if (root.right_child != None):
# 			sum += self.sumall(root.right_child)
# 		return sum
#
#
# 	def ino(self, root):
# 		pass
#
# 	def post(self, root):
# 		pass
#
# 	def level(sefl, root):
# 		pass
#
# tree = BinaryTree(50)
# tree.insert(10, tree.root)
# tree.insert(60, tree.root)
# tree.insert(30, tree.root)
# tree.insert(40, tree.root)
# tree.insert(70, tree.root)
# tree.insert(100, tree.root)
# print(tree.sumall(tree.root))
# # tree.root.left_child = Node(10)
# # tree.root.right_child = Node(60)
# # tree.root.left_child.left_child = Node(30)
# # tree.root.left_child.right_child = Node(40)
# # tree.root.right_child.right_child = Node(100)
# # tree.root.right_child.left_child = Node(70)
#
# # tree.print_tree("preorder") # 50, 10, 30, 40, 60, 70, 100
# # tree.print_tree("inorder") # 30, 10, 40, 50, 70, 60, 100
# # tree.print_tree("postorder") # 100, 60, 70, 50, 40, 10, 30
# # tree.print_tree("levelorder") # 50, 10, 60, 30, 40, 70, 100
#
#
# 		# '''
#
# 		# Traversal: Visiting each not in the tree
# 		# Traversals can be broken into 2 categories: BFS and DFS
#
# 		# Bredth-First-Search: Visiting all nodes in a
# 		# level before visiting any of its children. Ex.
#
# 		# 				   50
# 		# 				  /	 \
# 		# 			    10	 60
# 		# 		  	   / \   /  \
# 		# 		     30  40 70  100
#
# 		# 	The order the nodes would be visited would be:
# 		# 	50 --> 10 --> 60 --> 30 --> 40 --> 70 --> 100
#
# 		# 	This is known as Level-Order Traversal
# 		# 	Types of BFS traversals:
# 		# 		- Level-Order Traversal
# 		#			* 50 --> 10 --> 60 --> 30 --> 40 --> 70 --> 100
#
#
# 		# - Depth-First-Search: Starts at the root of the
# 		# tree (or some arbitrary node for a graph) and explored
# 		# as far as possible along each branch before backtracking.
#
#
#
# 		# Types of DFS traversals:
# 		# 	- Pre-Order Traversal ==> <root, left, right>
# 		# 	- In-Order Traversal ==>  <left, root, right>
# 		# 	- Post-Order Traversal ==> <right, root, left>
#
#
