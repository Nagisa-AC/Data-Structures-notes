class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val):
        self.stack.append(val)
        self.length += 1

    def pop(self):
        self.stack.pop()
        self.length -= 1

    def peek(self):
        if self.length == 0:
            print('Empty stack')
        else:
            return self.stack[-1]

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def traverse(self):
        if self.length == 0:
            print('Empty stack')
        else:
            index = self.length - 1
            while index >= 0:
                print(self.stack[index])
                index -= 1


# s = Stack()
# s.push(0)
# s.push(10)
# s.push(20)
# s.traverse()
# print('Top element', s.peek())
# print('\n')
# s.pop()
# s.traverse()
# print('Top element', s.peek())