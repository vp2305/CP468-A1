from copy import deepcopy
import copy
from puzzle import Puzzle


class Node(Puzzle):
    def __init__(self, numRowColumns, state, depth, heuristicType) -> None:
        super().__init__(
            numRowColumns=numRowColumns, state=state, heuristicType=heuristicType
        )
        self.parent = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.depth = depth
        self.fValue = self.fScore()

    def findCoordinates(self, value):
        """
        Find the coordinates of the blank tile
        """
        for c in range(self.numColumns):
            for r in range(self.numRows):
                if self.S[r][c] == value:
                    return (r, c)

    def moveLeft(self):
        """
        Move the blank tile to the left
        """
        changedState = deepcopy(self.S)
        emptyBlankTile = self.findCoordinates(0)

        if (emptyBlankTile[1] - 1) < self.numColumns and emptyBlankTile[1] != 0:
            changedState[emptyBlankTile[0]][emptyBlankTile[1]] = changedState[
                emptyBlankTile[0]
            ][emptyBlankTile[1] - 1]
            changedState[emptyBlankTile[0]][emptyBlankTile[1] - 1] = 0

            changedNode = Node(
                self.numColumns, changedState, self.depth + 1, self.heuristicType
            )
            changedNode.parent = self
            self.left = changedNode
        else:
            self.left = None

    def moveRight(self):
        """
        Move the blank tile to the right
        """
        changedState = deepcopy(self.S)
        emptyBlankTile = self.findCoordinates(0)

        if emptyBlankTile[1] + 1 < self.numColumns:
            changedState[emptyBlankTile[0]][emptyBlankTile[1]] = changedState[
                emptyBlankTile[0]
            ][emptyBlankTile[1] + 1]
            changedState[emptyBlankTile[0]][emptyBlankTile[1] + 1] = 0

            changedNode = Node(
                self.numColumns, changedState, self.depth + 1, self.heuristicType
            )
            changedNode.parent = self
            self.right = changedNode
        else:
            self.right = None

    def moveUp(self):
        """
        Move the blank tile up
        """
        changedState = deepcopy(self.S)
        emptyBlankTile = self.findCoordinates(0)

        if emptyBlankTile[0] - 1 < self.numRows and emptyBlankTile[0] != 0:
            changedState[emptyBlankTile[0]][emptyBlankTile[1]] = changedState[
                emptyBlankTile[0] - 1
            ][emptyBlankTile[1]]
            changedState[emptyBlankTile[0] - 1][emptyBlankTile[1]] = 0

            changedNode = Node(
                self.numColumns, changedState, self.depth + 1, self.heuristicType
            )
            changedNode.parent = self
            self.up = changedNode
        else:
            self.up = None

    def moveDown(self):
        """
        Move the blank tile down
        """
        changedState = deepcopy(self.S)
        emptyBlankTile = self.findCoordinates(0)

        if emptyBlankTile[0] + 1 < self.numRows and emptyBlankTile[0] != self.numRows:
            changedState[emptyBlankTile[0]][emptyBlankTile[1]] = changedState[
                emptyBlankTile[0] + 1
            ][emptyBlankTile[1]]
            changedState[emptyBlankTile[0] + 1][emptyBlankTile[1]] = 0

            changedNode = Node(
                self.numColumns, changedState, self.depth + 1, self.heuristicType
            )
            changedNode.parent = self
            self.down = changedNode
        else:
            self.down = None

    def resultPath(self):
        """
        Trace back steps to reach the solution.
        """
        moves = []
        parentNode: Node = deepcopy(self)
        moves.insert(0, parentNode.S)
        while parentNode.parent != None:
            parentNode = parentNode.parent
            moves.insert(0, parentNode.S)
        return moves
