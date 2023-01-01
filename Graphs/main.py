from collections import deque


class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinaryTree:
    def __init__(self, root) -> None:
        self.root = Node(root)
    
    def insert(self, root, value):
        if root == None:
            root = Node(value)
            return 
        
        if not root.left:
            root.left = Node(value)
        elif not root.right:
            root.right = Node(value)
        else:
            self.insert(root.left, value)
            self.insert(root.right, value)



    def reorder(self, root):
        '''
            - empty root
            - (l and r present) & (l <= root & r <= root )
            - after above condition, l or r is > root 
                - swap the greater of the two with root 
        '''

        if root == None:
            return 
        
        left, right = root.left, root.right
        if ((left and left.value <= root.value) and (right and right.value < root.value)):
            return 
        
        if left.value >= right.value:
            temp_node = left 
            left = root
            root = temp_node
        else:
            temp_node = right 
            right = root 
            root = temp_node

        self.reorder(root.left)
        self.reorder(root.right)


    def levelorder(self, root):
        queue = deque()
        queue.append(root)

        res, queue = [], deque()
        queue.append(root)
        
        while len(queue) > 0:
            level_len = len(queue)
            level_nodes = []

            for _ in range(level_len):
                curr_node = queue.popleft()
                level_nodes.append(curr_node.value)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            res.append(level_nodes)
        return res 


tree = BinaryTree(50)
tree.insert(tree.root, 100)
tree.insert(tree.root, 30)
print(tree.levelorder(tree.root))
tree.reorder(tree.root)
print(tree.levelorder(tree.root))
