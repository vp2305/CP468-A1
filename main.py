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

from operator import itemgetter
from node import Node
import pandas as pd


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

    openList = {}
    closedList = {}

    openList[str(currNode.S)] = currNode

    while True:
        currPuzzle: Node = openList.popitem()[1]

        # print("\nSelected puzzle state")
        # print(currPuzzle)

        # Update the close list by adding and removing the current selected puzzle state
        closedList[str(currPuzzle.S)] = currPuzzle

        # Found the goal state
        if currPuzzle.h_2 == 0:
            # return path
            # print("\nReached goal state")
            # print(currPuzzle)
            # print("Current Length of open list: ", len(openList))
            # print("Current Length of Close list: ", len(closedList))
            # print("\n")
            # print("Path to reach goal state:")
            moves = currPuzzle.resultPath()
            return moves, currPuzzle.depth, len(openList), len(closedList)

        # Make possible moves for the selected state
        currPuzzle.moveDown()
        currPuzzle.moveUp()
        currPuzzle.moveLeft()
        currPuzzle.moveRight()

        # Append new states after the moves to the open state
        if currPuzzle.right != None:
            if (str(currPuzzle.right.S) in openList) == True:
                # Check the fValue and update the openList if it is lower.
                sameNode: Node = openList.get(str(currPuzzle.right.S))
                if currPuzzle.right.fValue < sameNode.fValue:
                    openList[str(currPuzzle.right.S)] = currPuzzle.right
            elif ((str(currPuzzle.right.S) in openList) == False) and (
                (str(currPuzzle.right.S) in closedList) == False
            ):
                openList[str(currPuzzle.right.S)] = currPuzzle.right

        if currPuzzle.left != None:
            if (str(currPuzzle.left.S) in openList) == True:
                # Check the fValue and update the openList if it is lower.
                sameNode: Node = openList.get(str(currPuzzle.left.S))
                if currPuzzle.left.fValue < sameNode.fValue:
                    openList[str(currPuzzle.left.S)] = currPuzzle.left
            elif ((str(currPuzzle.left.S) in openList) == False) and (
                (str(currPuzzle.left.S) in closedList) == False
            ):
                openList[str(currPuzzle.left.S)] = currPuzzle.left

        if currPuzzle.up != None:
            if (str(currPuzzle.up.S) in openList) == True:
                # Check the fValue and update the openList if it is lower.
                sameNode: Node = openList.get(str(currPuzzle.up.S))
                if currPuzzle.up.fValue < sameNode.fValue:
                    openList[str(currPuzzle.up.S)] = currPuzzle.up
            elif ((str(currPuzzle.up.S) in openList) == False) and (
                (str(currPuzzle.up.S) in closedList) == False
            ):
                openList[str(currPuzzle.up.S)] = currPuzzle.up

        if currPuzzle.down != None:
            if (str(currPuzzle.down.S) in openList) == True:
                # Check the fValue and update the openList if it is lower.
                sameNode: Node = openList.get(str(currPuzzle.down.S))
                if currPuzzle.down.fValue < sameNode.fValue:
                    openList[str(currPuzzle.down.S)] = currPuzzle.down
            elif ((str(currPuzzle.down.S) in openList) == False) and (
                (str(currPuzzle.down.S) in closedList) == False
            ):
                openList[str(currPuzzle.down.S)] = currPuzzle.down

        # Sort the open list by the f value (g + h)
        openList = dict(
            sorted(openList.items(), key=lambda x: x[1].fValue, reverse=True)
        )


table = []

for x in range(10):
    # Heuristic type. h1, h2, h3
    puzzleNode = Node(3, [], 0, "h1")
    h1_path, h1_num_moves, h1_unVisitedNode, h1_visitedNode = aStar(puzzleNode)

    puzzleNode2 = Node(3, puzzleNode.S, 0, "h2")
    h2_path, h2_num_moves, h2_unVisitedNode, h2_visitedNode = aStar(puzzleNode2)

    puzzleNode3 = Node(3, puzzleNode.S, 0, "h3")
    h3_path, h3_num_moves, h3_unVisitedNode, h3_visitedNode = aStar(puzzleNode3)

    table.append(
        {
            "H1 Path": h1_path,
            "H1 Moves": h1_num_moves,
            "H1 Visited nodes": h1_visitedNode,
            "H1 Unvisited nodes": h1_unVisitedNode,
            "H2 Path": h2_path,
            "H2 Moves": h2_num_moves,
            "H2 Visited nodes": h2_visitedNode,
            "H2 Unvisited nodes": h2_unVisitedNode,
            "H3 Path": h3_path,
            "H3 Moves": h3_num_moves,
            "H3 Visited nodes": h3_visitedNode,
            "H3 Unvisited nodes": h3_unVisitedNode,
        },
    )

df = pd.DataFrame(table)
df.to_csv("result.csv")
