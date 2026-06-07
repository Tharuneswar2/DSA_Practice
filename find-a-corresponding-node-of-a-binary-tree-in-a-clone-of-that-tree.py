class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    # If the cloned tree is empty, return None
    if not cloned:
        return None
    
    # If the current node in the cloned tree matches the target node, return it
    if cloned.val == target.val:
        return cloned
    
    # Recursively search for the target node in the left subtree
    left_result = getTargetCopy(original, cloned.left, target)
    if left_result:
        return left_result
    
    # Recursively search for the target node in the right subtree
    return getTargetCopy(original, cloned.right, target)