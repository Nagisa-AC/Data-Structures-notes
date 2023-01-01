class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        if self.head is None:
            print('Doubly linked list is empty')
            return
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.val, end=' --> ')
            curr_node = curr_node.next
        print('None')

    def length(self):
        if self.head is None:
            return 0
        counter = 0
        curr_node = self.head
        while curr_node:
            counter += 1
            curr_node = curr_node.next
        return counter

    def add_head(self, head_val):
        new_head = Node(head_val)
        head_node = self.head
        if head_node is None:
            self.head = self.tail = new_head
            return
        new_head.next = head_node
        head_node.prev = new_head
        self.head = new_head

    def add_tail(self, tail_val):
        new_tail = Node(tail_val)
        curr_tail = self.tail
        if self.head is None:
            self.head = self.tail = new_tail
            return
        curr_tail.next = new_tail
        new_tail.prev = curr_tail
        self.tail = new_tail

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
        new_node.prev = curr_node
        self.tail = new_node

    def insert_before_k(self, val, k):
        if self.head is None:
            print('Linked list is empty')
            return
        new_node = Node(val)
        curr_node = self.head

        while curr_node.next.val != k:
            curr_node = curr_node.next
        if not curr_node:
            print(f'{k} not in list')
            return
        new_node.next = curr_node.next
        curr_node.next = new_node

    def insert_after_k(self, val, k):
        if self.head is None:
            print('empty list')
            return
        curr_node = self.head
        new_node = Node(val)

        while curr_node.val != k:
            curr_node = curr_node.next
        if not curr_node:
            print(f'{k} not in list')
            return
        new_node.next = curr_node.next
        curr_node.next = new_node

    def delete_node(self, index):
        if self.head is None:
            return
        if index < 0:
            print('invalid index')
            return
        if index == 0:
            head_node = self.head
            self.head = head_node.next
            del head_node
            return
        counter = 0
        curr_node = self.head
        while counter != (index - 1):
            curr_node = curr_node.next
            counter += 1
        node_to_delete = curr_node.next
        curr_node.next = node_to_delete.next
        del node_to_delete

    def delete_by_val(self, val):
        if self.head is None:
            print('empty list')
            return
        curr_node = self.head
        while curr_node.next.val != val:
            curr_node = curr_node.next
        if not curr_node:
            print(f'{val} not in list')
            return
        node_to_delete = curr_node.next
        curr_node.next = node_to_delete.next
        del node_to_delete

    def sorted_insert(self, val):
        pass

    def reverse(self):
        if self.head is None:
            print('empty list')
            return
        curr_node = self.head
        prev_node = None
        next_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

