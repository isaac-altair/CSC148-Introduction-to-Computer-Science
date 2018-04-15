class BTNode(object):
    def __init__(self, value, root=None, left=None, right=None):
        self.root = root
        self.value = value
        self.left = left
        self.right = right

def inorder(root):
    if not root:
        return
    else:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

if __name__ == "__main__":
    a = BTNode(5)
    b = BTNode(3)
    c = BTNode(2)
    d = BTNode(4)
    e = BTNode(6)
    root = a
    root.left = b
    root.right = e
    root.left.left = c
    root.left.right = d
    inorder(root)



