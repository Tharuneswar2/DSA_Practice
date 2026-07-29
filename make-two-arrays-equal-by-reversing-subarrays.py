# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def canBeEqual(target, arr):
    # First, we sort both the target and the array
    # This is because if the arrays are equal, they must have the same elements in the same quantity
    target.sort()
    arr.sort()
    
    # Then, we compare the sorted arrays
    # If they are equal, it means we can make the array equal to the target by reversing subarrays
    return target == arr