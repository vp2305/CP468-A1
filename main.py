"""
CP-468 Assignment 1

Group:
- Vaibhav Patel (190559020)

Need to solve puzzle using A* algorithm.

TODO
- Need to make a class for creating random puzzle state
- Need to make an algorithm for h1(S)
- Need to make an algorithm for h2(S)
- Need to make an algorithm for g(S)
- Need to use the A* algorithm based on the heuristics
- Need to create two list that is open list and closed list
    - Open list is a list of nodes that are not yet expanded
    - Closed list is a list of nodes that are already expanded
"""

from node import Node


def aStar(currNode):
    """
    A* algorithm for the puzzle
    """

    # TODO
    # - Need to make a class for the A* algorithm
    # - Need to create two list that is open list and closed list
    #     - Open list is a list of nodes that are not yet expanded
    #     - Closed list is a list of nodes that are already expanded

    # f = g + h
    # g = The movement cost from the starting point to a given square on the grid, following the path generated to get there.
    # h = the estimated movement cost to move from that given square on the grid to the final destination.

    openList = []
    closedList = []

    openList.append(currNode)
    while True:
        currPuzzle: Node = openList[0]

        print("\nSelected puzzle state")
        print(currPuzzle)

        # Found the goal state
        if currPuzzle.h_2 == 0:
            # return path
            print("\nReached goal state")
            print(currPuzzle)
            print("Current Length of open list: ", len(openList))
            print("Current Length of Close list: ", len(closedList))
            print("\n")
            print("Path to reach goal state:")
            moves = currPuzzle.resultPath()
            for x in range(len(moves) - 1, -1, -1):
                print(moves[x].S)
            break

        # Make possible moves for the selected state
        currPuzzle.moveDown()
        currPuzzle.moveUp()
        currPuzzle.moveLeft()
        currPuzzle.moveRight()

        # Append new states after the moves to the open state
        if currPuzzle.right != None:
            if any(currPuzzle.right.S == obj.S for obj in openList):
                pass
            else:
                openList.append(currPuzzle.right)

        if currPuzzle.left != None:
            if any(currPuzzle.left.S == obj.S for obj in openList):
                pass
            else:
                openList.append(currPuzzle.left)

        if currPuzzle.up != None:
            if any(currPuzzle.up.S == obj.S for obj in openList):
                pass
            else:
                openList.append(currPuzzle.up)

        if currPuzzle.down != None:
            if any(currPuzzle.down.S == obj.S for obj in openList):
                pass
            else:
                openList.append(currPuzzle.down)

        # Update the close list by adding and removing the current selected puzzle state
        closedList.append(currPuzzle)
        del openList[0]

        # Sort the open list by the f value (g + h)
        openList.sort(key=lambda x: x.fValue, reverse=False)


puzzleNode = Node(3, [], 0)
puzzleNode.depth = 0

# print(puzzleNode)
# print(puzzleNode.stateSolvable())
aStar(puzzleNode)
