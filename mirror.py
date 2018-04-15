class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def reflect(root):
    if root:
        self.left = reflect(self.left)
        self.right = refect(self.right)
        self.right, self.left = self.right, self.left
