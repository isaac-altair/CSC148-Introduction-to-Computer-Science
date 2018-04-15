from tree import BinaryTree
from tree import BinaryTreeNode


def _depth(start: 'Node', target: 'Node') -> int:

    if not start:
        return -1

    if start == target:
        return 0

    l, r = _depth(start.left, target), _depth(start.right, target)

    if l == -1 and r == -1:
        return -1
    
    return max(l, r) + 1


def depth(start: 'Node', target: 'Node'):
    x = _depth(start, target)
    if x == -1:
        return (None, -1)
    else:
        return (target.value, _depth(start, target))
    

def heap_remove(heap: 'list') -> int:
    root = heap[0]
    heap[0] = heap[-1]
    heap = heap[:-1]
    not_heap = True
    i = 0
    while not_heap:
        print("while loop")
        if (2 * i + 1) < len(heap) - 1:
            if (2 * i + 1) < len(heap) - 1:
                print("both exist")
                if heap[2 * i + 1] < heap[2 * i + 2]:
                    min_i = 2 * i + 1
                else:
                    min_i = 2 * i + 2
                if heap[i] > heap[min_i]:
                    print("changing")
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

    print(heap)        
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
    print(depth(d, d))
    a = [5, 9, 6, 12, 10, 13, 7, 18, 14]
    print(heap_remove(a))
