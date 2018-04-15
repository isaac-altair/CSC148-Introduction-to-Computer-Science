class Node(object):
    def __init__(self: 'Node', value) -> None:
        self.value = value
        self.next = None

def number_of_nodes_after_a_particular_node(front, value: 'int') -> int:
    c_node = front
    while c_node.value != value:
        c_node = c_node.next

    count = -1
    while c_node:
        c_node = c_node.next
        count += 1
    return count

class BTNode(object):
    '''A binary tree node.'''
    def __init__(self, value: int, left: 'BTNode' = None, right: 'BTNode' = None):
        self.left = left
        self.right = right
        self.value = value

def depth_count(root_node: 'BTNode', value: 'int', counter=0) -> int:
    left_node = root_node.left
    right_node = root_node.right

    if root_node.value == value:
        return counter

    if left_node:
        counter += depth_count(left_node, value, counter + 1)

    if right_node:
        counter += depth_count(right_node, value, counter + 1)

    return counter

def average_value(root_node: 'Node') -> int:
    lst = []
    
    while not root_node is None:
        lst.append(root_node.value)
        
    if root_node.right is None and root_node.left is None:
        return root_node.value
     
    if not root_node.left is None:
       #lst.append(root_node.left.value)
        root_node = root_node.left
        average_value(root_node)
        
    if not root_node.right is None:
        #lst.append(root_node.right.value)
        root_node = root_node.right
        average_value(root_node)

    return sum(lst) / len(lst)
        

def ascension_order(value:'node'):
    counter = 0
    c_node = value
    lst = []
    while not c_node.next is None:
        if c_node.next is not None and c_node.value > c_node.next.value:
            c_node.value, c_node.next.value = c_node.next.value, c_node.value
            counter = counter + 1
        lst.append(c_node.value)
        c_node = c_node.next
    lst.append(c_node.value)
    if counter > 0:
        ascension_order(c_node)
    return lst
