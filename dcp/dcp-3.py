class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node is None: return '#'
    return '{' + node.val + ',' + serialize(node.left) + ',' + serialize(node.right) + '}'

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

node = Node('root', Node('left', Node('left.left')), Node('right'))
print( serialize(node) )
print( deserialize(serialize(node)).left.left.val )
assert deserialize(serialize(node)).left.left.val == 'left.left'
