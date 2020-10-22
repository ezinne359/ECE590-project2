"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1: George Lindler
Partner 2: Ezinne Nwankwo
Date: October 22, 2020
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
    if alg == 'DFS':
        return []
    elif alg == 'BFS':
        # Step 1: Initialize all values and initialize empty queue
        m = maze
        queue = Queue()
        for vertex in m.adjList:
            vertex.dist = math.inf  # Infinite dist initially.
            vertex.visited = False  # Nothing visited at initialization.
            vertex.prev = None  # No

        # Step 2: Mark start vertices as visited and push to queue
        m.start.visited = True
        queue.push(m.start)
        m.start.dist = 0

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
                    if neighbor == m.exit:
                        break


        # Step 4: Return shortest path
        start = m.start
        last = m.exit
        # append rank of exit node to path
        m.path.append(last.rank)
        while last != start:
            # go back through previous values and append to path
            m.path.append(last.prev.rank)
            last = last.prev
        # return reversed path so that start is at the front of list
        m.path = list(reversed(m.path))

    return m.path






"""
Main function.
"""
if __name__ == "__main__":
      testMazes(False)