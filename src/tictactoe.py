__author__ = 'Suraj'
# Updated

from tree import Tree
from node import Node

'''
grid = ['X', 'O', 'X',
        'X', 'O', 'X',
        'X', 'X', 'O']
node = Node(grid)

print(node.checkUserWin(grid))
'''

tree = Tree()
tree.userTurn()
tree.compTurn()

'''
grid = ['O', 'O', 'X',
        'O', 'O', 'X',
        'O', 'X', 'O']
print(tree.checkWin(grid))

def test():
    node = Node('root')
    child1 = node.add('child1')
    child11 = child1.add('child11')
    print(child1.parent.grid)
    print(child11.parent.grid)

test()
'''
