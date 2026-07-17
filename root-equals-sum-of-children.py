# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def checkTree(root):
    # Base case: if the tree is empty, return True
    if not root:
        return True
    
    # If the tree is a leaf node, return True
    if not root.left and not root.right:
        return True
    
    # Calculate the sum of the left and right child nodes
    left_sum = root.left.val if root.left else 0
    right_sum = root.right.val if root.right else 0
    
    # Check if the root's value equals the sum of its children
    if root.val != left_sum + right_sum:
        return False
    
    # Recursively check the left and right subtrees
    return checkTree(root.left) and checkTree(root.right)