"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1:
Partner 2:
Date:
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        a = 0
        for k in range(0,len(self.queue)):
            if self.queue[k] is not None:
                a += 1
        return a == len(self.queue)

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        a = 0
        for k in range(0, len(self.queue)):
            if self.queue[k] is None:
                a += 1
        return a == len(self.queue)

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        # Unwrapping
        if self.front > self.rear:
            self.queue = self.queue[self.front:] + self.queue[:self.rear]
            self.rear = len(self.queue)
            # resize queue to be double the size
            new_length = 2 * len(self.queue)
            # initialize new array of double the size
            B = [None for x in range(0, new_length)]
            # fill new list with elements from original list
            for k in range(0, len(self.queue)):
                B[k] = self.queue[k]
                # reset the queue and the front
            self.queue = B
            self.front = 0
        elif self.front < self.rear:
            # resize queue to be double the size
            new_length = 2*len(self.queue)
            # initialize new array of double the size
            B = [None for x in range(0, new_length)]
            # fill new list with elements from original list
            for k in range(0, len(self.queue)):
                B[k] = self.queue[k]

            # reset the queue and the front
            self.queue = B
            self.front = 0
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        # As long as the rear is not at the end of queue
        # then push value to the rear of queue
        # and update rear and numElems
        if self.isFull() is True:
            self.resize()
            self.rear += 1
            self.queue[self.rear] = val
            self.numElems += 1

        elif self.isFull() is False:
            self.rear = self.rear % len(self.queue)
            self.queue[self.rear] = val
            self.rear += 1
            self.numElems += 1

        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        # check if front is at the end of list and resize if so
        if self.front == len(self.queue) - 1:
            self.resize()
        # remove value from front of the queue
        # update front and numElems
        self.queue[self.front] = None
        self.front += 1
        self.numElems -= 1

        return

# Check
q = Queue()
q.push(5)
q.push(4)
q.push(3)
q.pop()
q.pop()
q.push(2)
q.pop()
q.pop()
q.push(1)
print(q)
print(q.resize())
print(q.isFull())
print(q.isEmpty())
