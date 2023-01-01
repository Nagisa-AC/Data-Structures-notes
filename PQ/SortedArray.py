class PriorityQueue:
    def __init__(self):
        self.__PQ = []
        self.__size = 0

    def print_queue(self):
        print(self.__PQ)

    def enqueue(self, val):
        if self.__size == 0:
            self.__PQ.append(val)
        else:
            index = 0
            length = self.__size - 1

            while index <= length:
                curr_val = self.__PQ[index]
                if val > curr_val:
                    index = index + 1
                else:
                    self.__PQ.insert(index, val)
        self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            print('Empty PQ')
        else:
            self.__PQ.pop()
            self.__size -= 1

    def is_empty(self):
        return self.__size == 0

    def size(self):
        return self.__size

    def top(self):
        if self.__size == 0:
            print('Empty PQ')
        else:
            return self.__PQ[-1]


