class BinaryTree(object):
    '''A binary tree.'''
    def __init__(self: 'BinaryTree', root: 'BinaryTreeNode'=None):
        self.root = root

class BinaryTreeNode(object):
    '''A node in a binary tree.'''

    def __init__(self: 'BinaryTreeNode', value: int, parent: 'BinaryTreeNode'=None):
        '''Initialize a new BST node with the value provided and, optionally
        the parent.'''

        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
  
    def __str__(self: 'BinaryTreeNode'):
        '''Return a nice representation of this node.'''

        return "Node(%s)" % str(self.value)