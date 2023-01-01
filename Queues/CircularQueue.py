class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.length = 0

    def enqueue(self, val):
        if self.length == 0:
            self.queue[0] = val
            self.front = self.rear = 0
            self.length += 1
        elif self.length == self.size:
            print('Full Buffer')
        else:
            next_index = ((self.rear + 1) % self.size)
            self.queue[next_index] = val
            self.length += 1
            self.rear += 1

    def dequeue(self):
        if self.length == 0:
            print('Empty Buffer')
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = self.rear = 0
            self.length -= 1
        else:
            self.queue[self.front] = None
            self.length -= 1
            self.front += 1

    def front(self):
        if self.length == 0:
            print('Empty Buffer')
        else:
            return self.queue[self.front]

    def rear(self):
        pass

    def count(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.size

    def traverse(self):
        for i in self.queue:
            print(i)


q = CircularBuffer(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)