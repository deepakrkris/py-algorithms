# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(strNode, start = 1):
    index = start
    begin = start
    rootNode = None
    left = None
    right = None

    while index < len(strNode) and strNode[index] != ',':
        index += 1

    rootNode = Node(strNode[begin:index])
    index += 1

    if strNode[index] == '{':
        index, left = deserialize(strNode, index + 1)
        # print(left.val)
    elif strNode[index] == '#':
        index += 1

    index += 1

    if strNode[index] == '{':
        index, right = deserialize(strNode, index + 1)
        # print(right.val)
    elif strNode[index] == '#':
        index += 1

    index += 1

    rootNode.left = left
    rootNode.right = right

    if start == 1:
        return rootNode
    else:
        return index, rootNode


def isUnival(node, value):
    if node is None:
        return True

    if node.left is not None and node.left.val != value:
        return False

    if node.right is not None and node.right.val != value:
        return False

    return isUnival(node.left, value) and isUnival(node.right, value)

def countTrees(node):
    if node is None:
        return 0

    count = 0

    if node.left is not None:
        count += countTrees(node.left)

    if node.right is not None:
        count += countTrees(node.right)

    return 1 + count

def numOfUnival(node):
    if node is None:
        return 0

    if isUnival(node, node.val):
        return countTrees(node)
    return numOfUnival(node.left) + numOfUnival(node.right)

print(numOfUnival(deserialize('{0,{1,#,#},{0,{1,{1,#,#},{1,#,#}},{0,#,#}}}')))
