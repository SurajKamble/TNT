__author__ = 'Suraj'


class Node():
    def __init__(self, node):
        self.grid = node
        self.children = []
        self.parent = None
        self.value = None
        self.visited = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.numberOfChildrenPossible = self.emptySpaces(node)
        self.computerTurn = True
        self.eitherWin = False

    def parent(self):
        return self.parent

    def add(self, node):
        node1 = Node(node)
        self.children.append(node1)
        node1.parent = self
        for i in range(9):
            if node1.grid[i] != ' ':
                self.visited[i] = node1.grid[i]
        if self.computerTurn:
            node1.computerTurn = False
        else:
            node1.computerTurn = True
        node1.eitherWin = self.checkCompWin(node1.grid) | self.checkUserWin(node1.grid)
        if node1.eitherWin:
            node1.numberOfChildrenPossible = 0
        return node1

    def emptySpaces(self, grid):
        emptySpaces = 0
        if grid is not None:
            for i in range(0, len(grid)):
                if grid[i] == ' ':
                    emptySpaces += 1
        return emptySpaces

    def checkUserWin(self, grid):
        b = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [3, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i in range(len(b)):
            if [grid[j] for j in b[i]] == ['X', 'X', 'X']:
                print('grid', (b[i]))
                return True
            else:
                return False

    def checkCompWin(self, grid):
        b = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [3, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i in range(len(b)):
            if [grid[j] for j in b[i]] == ['O', 'O', 'O']:
                return True
            else:
                return False