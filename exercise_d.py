class BTNode(object):
    '''A binary tree node.'''
    def __init__(self, value: int, left: 'BTNode'=None, right: 'BTNode'=None):
        self.left = left
        self.right = right
        self.value = value
        

### DRAFT -- docstrings not necessarily complete
def count_lists(outer_list: list) -> int:
    '''Return the total number of lists in outer_list (including outer_list
    itself). Each element of outer_list and any nested lists are either ints or
    other lists.
    
    Example:
    >>> count_lists([1, 2, 3])
    1
    >>> count_lists([[1], [2], [3]])
    4
    >>> count_lists([[[1, 2], [], 3]])
    4
    '''
    counter = 1
    for item in outer_list:
        if isinstance(item, list):
            counter += count_lists(item)
    return counter

    
def is_special_tree(root_node: 'BTNode') -> bool:
    '''Return True iff the following properties are true for every node in the
    tree rooted by root_node:
       * If the node has a left subtree, the value of that subtree's root is
         less than or equal to the node's value.
       * If the node has a right subtree, the value of that subtree's root is
         greater than or equal to the node's value.

    Precondition: All the values in the tree rooted at root_node are ints
    or floats. root_node is not None.
    
    Example:
    >>> is_special_tree(BTNode(3))
    True
    >>> is_special_tree(BTNode(3, None, BTNode(1)))
    False
    >>> is_special_tree(BTNode(3, BTNode(1, BTNode(-1))))
    True
    >>> is_special_tree(BTNode(3, BTNode(1, None, BTNode(-1))))
    False
    >>> is_special_tree(BTNode(3, BTNode(1, None, BTNode(2))))
    True'''
    
    if root_node is None:
        return True
    
    if root_node.right is None and root_node.left is None:
        return True
     
    if not root_node.left is None:
        if root_node.left.value > root_node.value:
            return False
        
    if not root_node.right is None:
        if root_node.right.value < root_node.value:
            return False

    if is_special_tree(root_node.left) is True:
        if is_special_tree(root_node.right) is True:
            return True
    else:
        return False

##    if root_node.right:
##        if root_node.right.value >= root_node.value:
##            # Check if the left value given right value is correct
##            if root_node.left:
##                if root_node.left.value <= root_node.value:
##                    return is_special_tree(root_node.right)
##    if root_node.left:
##        if root_node.left.value <= root_node.value:
##            # Check if the right value given left value is correct
##            if root_node.right:
##                if root_node.right.value >= root_node.value:
##                    return is_special_tree(root_node.left)
    

