"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1:
Partner 2:
Date:
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

    def bdfs(maze, alg):
        # If the alg is not BFS or DFS, raise exception.
        if (alg != 'BFS') and (alg != 'DFS'):
            raise Exception('Incorrect alg! Need BFS or DFS!')

        # Depth First Search
        if alg == 'DFS':

            # Step 1: Initialize and Set Flags to False
            m = maze
            for vertex in m.adjList:
                vertex.visited = False
                vertex.prev = None

            # Step 2: Set Start Visited Flag to True, Push start to stack
            m.start.visited = True
            stack = Stack()
            stack.push(m.start)

            # Step 3:
            while stack.numElems > 0:
                current = stack.pop()
                for neighbor in current.neigh:
                    if neighbor.visited == False:
                        neighbor.visited = True
                        stack.push(neighbor)
                        neighbor.prev = current
                        if neighbor == m.exit:
                            break

            last = m.exit
            m.path.append(m.exit.rank)
            while last != m.start:
                m.path.append(last.prev.rank)
                last = last.prev
            m.path = m.path[::-1]

    return []
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)