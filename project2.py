"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1: George Lindner
Partner 2: Ezinne Nwankwo
Date: 10/22/20
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    maze.path = []

    # Step 1: Initialize and Set Flags to False
    for vertex in maze.adjList:
        vertex.dist = math.inf  # Infinite dist initially.
        vertex.visited = False  # Nothing visited at initialization.
        vertex.prev = None

    # Depth First Search
    if alg == 'DFS':
        # Step 2: Set Start Visited Flag to True, Push start to stack
        maze.start.visited = True
        stack = Stack()
        stack.push(maze.start)

        # Step 3: While the stack is not empty, loop
        while stack.numElems > 0:
            current = stack.pop() # Pop the top element off the stack and observe its neighbors
            if current == maze.exit:
                break

            for neighbor in current.neigh:
                if neighbor.visited == False:
                    # Set the visited flag to True for the neighbor
                    neighbor.visited = True
                    stack.push(neighbor)
                    neighbor.prev = current


        last = maze.exit
        maze.path.append(maze.exit.rank)
        while last != maze.start:
            maze.path.append(last.prev.rank)
            last = last.prev
        maze.path = maze.path[::-1]

    elif alg == 'BFS':

        queue = Queue()

        # Step 2: Mark start vertices as visited and push to queue
        maze.start.visited = True
        queue.push(maze.start)
        maze.start.dist = 0

        # Step 3: While queue is not empty
        while not queue.isEmpty():
            # pop the current element
            current = queue.pop()
            # for each current neighbor
            for neighbor in current.neigh:
                # check the the neighbor has not been visited
                if neighbor.dist == math.inf:
                    # mark as visited by incrementing distance attribute
                    neighbor.dist = current.dist + 1
                    # push to the queue
                    queue.push(neighbor)
                    # reset previous value
                    neighbor.prev = current
                    # once the neighbor we are checking is the exit then break
                    if neighbor == maze.exit:
                        break

        # Step 4: Return shortest path
        start = maze.start
        last = maze.exit
        # append rank of exit node to path
        maze.path.append(last.rank)
        while last != start:
            # go back through previous values and append to path
            maze.path.append(last.prev.rank)
            last = last.prev
        # return reversed path so that start is at the front of list
        maze.path = list(reversed(maze.path))

    return maze.path


"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
