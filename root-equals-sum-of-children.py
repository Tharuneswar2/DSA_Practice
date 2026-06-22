class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def checkTree(root):
    # Base case: If the tree is empty, return True
    if not root:
        return True
    
    # If the tree has no children, return True
    if not root.left and not root.right:
        return True
    
    # Calculate the sum of the children
    children_sum = 0
    if root.left:
        children_sum += root.left.val
    if root.right:
        children_sum += root.right.val
    
    # Check if the root's value equals the sum of its children
    if root.val != children_sum:
        return False
    
    # Recursively check the left and right subtrees
    return checkTree(root.left) and checkTree(root.right)