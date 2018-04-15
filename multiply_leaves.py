class Node(object):
    def __init__(self, root, left=None, right=None):
        self.value = root
        self.left = left
        self.right = right

def product(node):
    if None:
        return 1
    else:
        if (node.left is None and node.right is None):
            return node.value
        else:
            return product(node.left) * product(node.right)

def remove_smallest(node):
    if node.left:
        return remove_smallest(node.left)
    else:
        return node.value
