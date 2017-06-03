from BaseAI_3 import BaseAI
from math import inf
from random import randint, randrange
import sys
import time

sys.setrecursionlimit(100000)


class PlayerAI(BaseAI):

    pre = 0.0

    def getMove(self, grid):
        self.pre = time.clock()
        move = self.decision(grid)
        print(time.clock() - self.pre)
        return move
        # moves = grid.getAvailableMoves()
        # return moves[randint(0, len(moves) - 1)] if moves else None

    def maximize(self, grid, alpha, beta):
        availableMoves = grid.getAvailableMoves()

        # print(availableMoves)
        # print(grid.map)
        if not availableMoves or time.clock() - self.pre > 0.04:
            # print("----> CHECK MAX!")
            return None, self.heuristic(grid)

        maxChild = None
        maxScore = -inf

        for direction in availableMoves:
            # Make a copy of the current grid
            tempGrid = grid.clone()
            tempGrid.move(direction)

            nextState = self.minimize(tempGrid, alpha, beta)
            # nextState is a tuple with the form (direction, maxTile), for example: (1, 64)
            if nextState[1] > maxScore:
                maxScore = nextState[1]
                maxChild = direction
            if maxScore >= beta:
                break
            if maxScore > alpha:
                alpha = maxScore

        return maxChild, maxScore

    def minimize(self, grid, alpha, beta):
        # Check to see if there is any available cell on the board
        emptyCells = grid.getAvailableCells()
        # print("MIN: ")
        # print(grid.map)

        if not emptyCells or time.clock() - self.pre > 0.04:
            # print("----> CHECK MIN")
            return None, self.heuristic(grid)

        minChild = None
        minScore = inf

        # TODO: Generate all the possible moves, each empty cells will have 2 states, with 2 and 4, respectively
        allStates = [(value, pos) for value in [2, 4] for pos in emptyCells]

        for state in allStates:
            tempGrid = grid.clone()
            tempGrid.insertTile(state[1], state[0])
            nextState = self.maximize(tempGrid, alpha, beta)
            # next State is a tuple with the form (direction, maxTile), for example: (1, 64)
            if nextState[1] < minScore:
                minScore = nextState[1]
                minChild = tempGrid
            if minScore <= alpha:
                break
            if minScore < beta:
                beta = minScore

        return minChild, minScore

    def heuristic(self, grid):
        numEmptyCells = len(grid.getAvailableCells())
        return numEmptyCells

    def decision(self, grid):
        child = self.maximize(grid, -inf, inf)
        return child[0]
