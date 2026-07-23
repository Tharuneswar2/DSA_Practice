# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    # If the original tree is empty, return None
    if not original:
        return None
    
    # If the current node in the original tree matches the target node, 
    # return the current node in the cloned tree
    if original == target:
        return cloned
    
    # Recursively search for the target node in the left subtree
    left_result = getTargetCopy(original.left, cloned.left, target)
    
    # If the target node is found in the left subtree, return the result
    if left_result:
        return left_result
    
    # Recursively search for the target node in the right subtree
    return getTargetCopy(original.right, cloned.right, target)