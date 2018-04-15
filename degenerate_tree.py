class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None

def func(node):
    if node:
        node.left = func(node.left)
        node.right = func(node.right)

        cur_node = node
        while cur_node.right:
            cur_node = cur_node.right

        cur_node.right = node.left
        node.left = None

        return node
