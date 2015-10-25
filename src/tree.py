import copy

__author__ = 'Suraj'

from node import Node


class Tree():  # Tree structure

    numberOfTurns = 0
    possiblePositions = 0
    leafNode = [1, 0, -1]
    entries = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    visitedNodes = []
    computerTurn = False
    userWin = False
    compWin = False

    def checkWin(self, grid):
        b = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [3, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i in range(len(b)):
            if [grid[j] for j in b[i]] == ['X', 'X', 'X']:
                print('grid', (b[i]))
                self.userWin = True
                return self.userWin
            elif [grid[j] for j in b[i]] == ['O', 'O', 'O']:
                self.compWin = True
                return self.compWin
        return False

    '''    if (bool(grid[:3] == ['X', 'X', 'X']) | bool(grid[3:6] == ['X', 'X', 'X']) | bool(grid[6:9] == ['X', 'X', 'X']) | bool(
                        grid[::2] == ['X', 'X', 'X']) | bool(grid[:2] == ['X', 'X', 'X']) | bool(
                        grid[:2] == ['X', 'X', 'X']) | bool(grid[:2] == ['X', 'X', 'X']) | bool(
                        grid[:2] == ['X', 'X', 'X'])):
            self.userWin = True
            return self.userWin
            '''




    def display(self, entries):  # Prints the present board position
        print('\n %s | %s | %s' % (entries[0], entries[1], entries[2]))
        print('---|---|---')
        print(' %s | %s | %s' % (entries[3], entries[4], entries[5]))
        print('---|---|---')
        print(' %s | %s | %s\n' % (entries[6], entries[7], entries[8]))

    def userTurn(self):
        self.display(self.entries)
        userInput = input('Your(X) turn to play:\t')
        self.entries[int(userInput[0]) - 1] = userInput[2]
        self.computerTurn = True
        return self.entries

    def emptySpaces(self, grid):
        emptySpaces = 0
        if grid is not None:
            for i in range(0, len(grid)):
                if grid[i] == ' ':
                    emptySpaces += 1
        return emptySpaces

    def compTurn(self):
        board = Node(self.entries)
        self.dfs(board)

    def dfs(self, board):  # Something's wrong with numberOfTurns. Fix it
        if bool(board is not None):
            if bool(board.numberOfChildrenPossible <= 0):
                return
            print('possible', board.numberOfChildrenPossible)
            self.visitedNodes.append(board.grid)
            print('Node')
            print(self.computerTurn)
            self.display(board.grid)
            print('board.visited', board.visited)
            board1 = copy.deepcopy(board)
            board2 = copy.deepcopy(board)
            next1 = self.generateNextBoard(board1)

            print('numberOfPossibleChildren before', board.numberOfChildrenPossible)
            nextBoard = board
            if board not in self.visitedNodes:
                nextBoard = board.add(next1)
            board.numberOfChildrenPossible -= 1
            if bool(self.checkWin(board.grid)):
                board.numberOfChildrenPossible = -1
            print('numberOfPossibleChildren After', board.numberOfChildrenPossible)
            '''
             if next1 not in self.visitedNodes:
                nextBoard = board.add(next1)
            print('children')
            self.display(board.children[0].grid)
            if board.parent is not None:
                print('parent')
                self.display(board.parent.grid)
                '''
            board = nextBoard
            self.dfs(board)
            print('next Iteration')
            emptySpaces = self.emptySpaces(board.grid)  # Add functionality for emptySpaces
            if bool(board is not None) & bool(emptySpaces != 0):
                print('In Parent')
                self.dfs(board.parent)

    def generateNextBoard(self, board):
        if board.numberOfChildrenPossible != 0:
            self.numberOfTurns += 1
            for i in range(0, len(board.visited)):
                if bool(board.grid[i] == ' ') & bool(board.visited[i] == ' '):
                    if board.computerTurn:
                        board.grid[i] = 'O'
                        break
                    else:
                        board.grid[i] = 'X'
                        break
        print('generatedNode', board.grid)
        return board.grid

    '''
    def traversal(self, node):  # Add tree with all the nodes first, then perform DFS.
        tree = Tree()
        tree.display(node)
        board = Node(node)
        if board.value in Tree.leafNode:
            return
        else:
            tree.display(board.board)
            nextBoard = tree.generateNextBoard(board)
            if nextBoard not in nextBoard.children:
                print(nextBoard.board)
                board.add(nextBoard)
                board = nextBoard
                Tree.numberOfTurns += 1

        while board.value not in Tree.leafNode:
            tree.display(board.board)
            nextBoard = tree.generateNextBoard(board)
            if nextBoard not in nextBoard.children:
                print(nextBoard.board)
                board.add(nextBoard)
                board = nextBoard
                Tree.numberOfTurns += 1
                '''

