##class Node(object):
##    def __init__(self: 'Node', value) -> None:
##        self.value = value

def number_of_nodes_after_a_particular_node(front, value: 'int') -> int:
    c_node = front
    while c_node.value != value:
        c_node = c_node.next

    count = -1
    while c_node:
        c_node = c_node.next
        count += 1
    return count

class Node(object):
    '''A binary tree node.'''
    def __init__(self, value: int, left: 'BTNode' = None, right: 'BTNode' = None):
        self.left = left
        self.right = right
        self.value = value
        self.next = None

##def depth_count(root_node: 'BTNode', value: 'int', counter=0) -> int:
##    left_node = root_node.left
##    right_node = root_node.right
##
##    if root_node.value == value:
##        return counter
##    
##    if left_node:
##        counter += depth_count(left_node, value, counter + 1)
##
##    if right_node:
##        counter += depth_count(right_node, value, counter + 1)
##
##    return counter

def depth(s: 'Node', n: 'Node'):
    if s == n:
        return 0

    if not s:
        return -1

    l, r = depth(s.left, n), depth(s.right, n)

    if l == -1 and r == -1:
        return -1

    return max(l, r) + 1

temp_nodes = 0
temp_sum = 0
final_sum = 0
final_nodes = 0
n_lst = []

def average_value(root_node: 'Node') -> float:

    global temp_nodes, temp_sum, n_lst, final_sum, final_nodes
    temp_nodes = temp_nodes + 1
    temp_sum = temp_sum + root_node.value

    if root_node.left:
        n_lst.append(root_node.left)
    if root_node.right:
        n_lst.append(root_node.right)

    if n_lst != []:
        average_value(n_lst.pop())
    else:
        final_nodes = temp_nodes
        final_sum = temp_sum
        temp_nodes = 0
        temp_sum = 0
    return final_sum / final_nodes


def switch_tree(root_node: 'Node'):
    if root_node.right:
        root = root_node
        right_node = root.right
        root.right = None
        c_node = right_node
        while c_node.left:
            c_node = c_node.left
        c_node.left = root
    return right_node
    

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

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)
    i = Node(9)
    d.left = b
    d.right = f
    d.left.left = a
    d.left.right = c
    d.right.left = e
    d.right.right = g
    d.right.right.right = h
    d.right.right.right.right = i
    print((depth(d, h), e.value))
