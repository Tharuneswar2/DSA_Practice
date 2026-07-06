# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def evaluateTree(root):
    # Base case: if the tree is empty, return True
    if not root:
        return True
    
    # If the node is a leaf node (i.e., it has no children), return its value
    if not root.left and not root.right:
        return root.val == 1
    
    # Recursively evaluate the left and right subtrees
    left = evaluateTree(root.left)
    right = evaluateTree(root.right)
    
    # If the current node is an OR node, return True if either subtree is True
    if root.val == 2:
        return left or right
    
    # If the current node is an AND node, return True if both subtrees are True
    if root.val == 3:
        return left and right