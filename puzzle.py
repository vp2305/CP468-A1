import random


class Puzzle:
    """
    Create a puzzle based on the numRows and numColumns
    """

    def __init__(self, numRowColumns: int, state: list, heuristicType: str) -> None:
        self.numRows = numRowColumns
        self.numColumns = numRowColumns
        self.heuristicType = heuristicType
        self.S = state
        self.goalState = []
        self.createGoalState()
        if len(self.S) <= 0:
            self.createPuzzle()
        self.h_1 = self.h1()
        self.h_2 = self.h2()

    def __str__(self) -> str:
        return f"{self.S}\nh1:{self.h_1}\nh2:{self.h_2}\nDepth:{self.depth}\nF Score: {self.fValue}"

    def createPuzzle(self):
        """
        Create a puzzle based on the numRows and numColumns
        """
        # self.S = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
        possibleValues = []
        for i in range(0, self.numRows * self.numColumns):
            possibleValues.append(i)

        for i in range(self.numRows):
            self.S.append([])
            for j in range(self.numColumns):
                self.S[i].append(
                    (possibleValues.pop(random.randint(0, len(possibleValues) - 1)))
                )

        puzzleStateCheck = self.stateSolvable()
        if puzzleStateCheck == False:
            self.S = []
            self.createPuzzle()

    def getInvCount(self):
        flatState = []
        for i in range(len(self.S)):
            flatState.extend(self.S[i])
        inv_count = 0
        for i in range(self.numColumns * self.numColumns - 1):
            for j in range(i + 1, self.numColumns * self.numColumns):
                if flatState[j] and flatState[i] and flatState[i] > flatState[j]:
                    inv_count += 1

        return inv_count

    def stateSolvable(self):
        """
        Check to see if the state is solvable.

        - if N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
        - If N is even, puzzle instance is solvable if
            - the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is odd.
            - the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is even.
        """
        invCount = self.getInvCount()

        if self.numColumns % 2 != 0:
            # If n is odd
            if invCount % 2 == 0:
                return True
        else:
            # If n is even
            blankTileCoordinates = self.findCoordinates(0)
            if (blankTileCoordinates[0] % 2 == 0) and (invCount % 2 != 0):
                # Blank tile is on even row and invCount is odd
                return True
            elif (blankTileCoordinates[0] % 2 != 0) and (invCount % 2 == 0):
                # Blank tile is on odd row and invCount is even
                return True
            else:
                return False
        return False

    def createGoalState(self):
        """
        Create a goal state for the given puzzle dimensions
        """
        for i in range(self.numRows):
            self.goalState.append([])
            for j in range(self.numColumns):
                self.goalState[i].append(i * self.numColumns + j)

    def h1(self):
        """
        h1(S) = number of misplaced tiles
        """
        misplacedTiles = 0
        for c in range(self.numColumns):
            for r in range(self.numRows):
                if self.S[r][c] != self.goalState[r][c]:
                    misplacedTiles += 1
        return misplacedTiles

    def h2(self):
        """
        h2(S) = sum of Manhattan distances
        Estimate the distance of each tile from its goal position
        """
        totalSumOfManhattanDistances = 0
        for c in range(self.numColumns):
            for r in range(self.numRows):
                if self.S[r][c] != 0 and self.S[r][c] != self.goalState[r][c]:
                    numRowMove = abs(self.S[r][c] // self.numColumns - r)
                    numColMove = abs(self.S[r][c] % self.numColumns - c)
                    totalSumOfManhattanDistances += numRowMove + numColMove

        return totalSumOfManhattanDistances

    def h3(self):
        """
        h3(S) = sum of Manhattan distances + 2 * linear conflict
        Linear conflict implementation
        """
        linearConflict = 0
        totalSumOfManhattanDistances = self.h2()

        # Check for linear conflicts
        for c in range(self.numColumns):
            for r in range(self.numRows):
                if self.S[r][c] != 0 and self.S[r][c] != self.goalState[r][c]:
                    # Check for row conflict
                    if self.S[r][c] % self.numColumns == c:
                        for i in range(r + 1, self.numRows):
                            if (
                                self.S[i][c] != 0
                                and self.S[i][c] != self.goalState[i][c]
                            ):
                                if self.S[i][c] % self.numColumns == c:
                                    if self.S[r][c] > self.S[i][c]:
                                        linearConflict += 1
                    # Check for column conflict
                    if self.S[r][c] // self.numColumns == r:
                        for j in range(c + 1, self.numColumns):
                            if (
                                self.S[r][j] != 0
                                and self.S[r][j] != self.goalState[r][j]
                            ):
                                if self.S[r][j] // self.numColumns == r:
                                    if self.S[r][c] > self.S[r][j]:
                                        linearConflict += 1

        return totalSumOfManhattanDistances + 2 * linearConflict

    def fScore(self):
        """
        f(S) = level + h2(S)
        """
        if self.heuristicType == "h1":
            return self.depth + self.h1()
        elif self.heuristicType == "h2":
            return self.depth + self.h2()
        else:
            return self.depth + self.h3()
