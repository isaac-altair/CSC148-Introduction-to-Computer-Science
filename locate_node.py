from tree import BinaryTree
from tree import BinaryTreeNode


def _l_n(start: 'Node', target: 'int') -> None:

    if not start:
        return (None, -1)

    print(str(start.value))
    if start.value == target:
        return (start, 0)
    
    l, r = _l_n(start.left, target), _l_n(start.right, target)
    
    if l[1] == -1 and r[1] == -1:
        return (None, -1)

    if l[1] > r[1]:
        return (l[0], l[1] + 1)
    else:
        return (r[0], r[1] + 1)

    return max(l[1], r[1]) + 1


def locate_node(start: 'Node', target: 'int'):
    return _l_n(start, target)
    

def heap_remove(heap: 'list') -> int:
    root = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    if len(heap) == 1:
        not_heap = False
    else:
        not_heap = True
    i = 0
    while not_heap:
        if (2 * i + 1) <= len(heap) - 1:
            if (2 * i + 2) <= len(heap) - 1:
                if heap[2 * i + 1] < heap[2 * i + 2]:
                    min_i = 2 * i + 1
                else:
                    min_i = 2 * i + 2
                if heap[i] > heap[min_i]:
                    top = heap[i]
                    heap[i] = heap[min_i]
                    heap[min_i] = top
                    i = min_i
                else:
                    not_heap = False
            else:
                if heap[i] > heap[2 * i + 1]:
                    top = heap[i]
                    heap[i] = heap[2 * i + 1]
                    heap[2 * i + 1] = top
                    i = 2 * i + 1
                else:
                    not_heap = False
        else:
            not_heap = False
    return root

if __name__ == '__main__':
    a = BinaryTreeNode(1)
    b = BinaryTreeNode(2)
    c = BinaryTreeNode(3)
    d = BinaryTreeNode(4)
    e = BinaryTreeNode(5)
    f = BinaryTreeNode(6)
    g = BinaryTreeNode(7)
    h = BinaryTreeNode(8)
    i = BinaryTreeNode(9)
    d.left = b
    d.right = f
    d.left.left = a
    d.left.right = c
    d.right.left = e
    d.right.right = g
    d.right.right.right = h
    d.right.right.right.right = i

    i.left = h
    i.left.left = g
    i.left.left.left = f
    i.left.left.left.left = e
    i.left.left.left.left.left = d
    i.left.left.left.left.left.left = c
    i.left.left.left.left.left.left.left = b
    i.left.left.left.left.left.left.left.left = a

    print(locate_node(i, b.value))
    print("(" + str(g) + " ,", str(3) + ")")
