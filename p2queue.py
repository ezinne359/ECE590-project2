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
        # returns True is numElems is equal to the length of the queue
        return self.numElems == len(self.queue)

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        # returns True is queue is empty so numElems is equal to zero
        return self.numElems == 0

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        # Unwrapping
        # resize queue to be double the size
        new_length = 2 * len(self.queue)
        # initialize new array of double the size
        B = [None for x in range(0, new_length)]
        k = 0
        # while the queue is not empty
        while not self.isEmpty():
            # pop  values to new list of double the size
            B[k] = self.pop()
            k += 1

        # reset the queue and the front values
        self.queue = B
        self.front = 0

        # reset the rear values and numElems
        self.rear = k
        self.numElems = k

        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        # As long as the rear is not at the end of queue
        # then push value to the rear of queue
        # and update rear and numElems
        # if the queue is full then first resize the list
        if self.isFull() is True:
            self.resize()
        # push value to the rear of the queue
        self.queue[self.rear] = val
        # increment rear value by one
        self.rear += 1
        # update rear value to be current rear mod length of the queue
        # if queue is  not full but rear is at the end of the  list
        # then this will induce wrap around behavior
        self.rear = self.rear % len(self.queue)
        # increment numElems
        self.numElems += 1

        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        # remove value from front of the queue
        # update front and numElems
        # store  value to be popped
        pop_val = self.queue[self.front]
        # replace popped value with None
        self.queue[self.front] = None
        # increment front
        self.front += 1
        # if queue is  not full but front is at the end of the list
        # then this will induce wrap around behavior
        self.front = self.front % len(self.queue)
        # decrease numElems
        self.numElems -= 1

        return pop_val
