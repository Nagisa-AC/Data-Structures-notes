class Queue:
    """
    Dynamic-array based implementation of a queue with
    support of operations: push(), pop(), peek(), size(), empty()
    * Enqueue: O(1), amortized O(N)
    * Dequeue: O(N)
    * A dynamic array is not an efficient way to implement a queue
    """
    def __init__(self):
        self.queue = []
        self.length = 0

    def enqueue(self, val):
        self.queue.append(val)
        self.length += 1

    def dequeue(self):
        del self.queue[0]
        self.length -= 1

    def peek(self):
        if self.length == 0:
            print('Queue is empty')
        else:
            return self.queue[0]

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def traverse(self):
        for val in self.queue:
            print(val, end=' ')





















