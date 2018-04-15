class BTNode(object):
    '''A binary tree node.'''
    def __init__(self, value: int, left: 'BTNode'=None, right: 'BTNode'=None):
        self.left = left
        self.right = right
        self.value = value

##def BST_insert(root_node: 'Node', new_node: 'Node'):
##    cur_node = root_node
##    while True:
##        if new_node.value < cur_node.value:
##            if cur_node.left:
##                cur_node = cur_node.left
##            else:
##                cur_node.left = new_node
##                return root_node
##
##        elif new_node.value > cur_node.value:
##            if cur_node.right:
##                cur_node = cur_node.right
##            else:
##                cur_node.right = new_node
##                return root_node
##        else:
##            return root_node


def BST_insert(root_node: 'Node', value: 'int'):
    cur_node = root_node
    while True:
        if value < cur_node.value:
            if cur_node.left:
                cur_node = cur_node.left
            else:
                cur_node.left = BTNode(value)
                return root_node

        elif value > cur_node.value:
            if cur_node.right:
                cur_node = cur_node.right
            else:
                cur_node.right = BTNode(value)
                return root_node
        else:
            return root_node            
