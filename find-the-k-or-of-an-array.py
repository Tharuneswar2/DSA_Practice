# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def kth_element_after_removal(nums, k):
    # Create a copy of the input list to avoid modifying the original list
    nums_copy = nums.copy()
    
    # Sort the copied list in ascending order
    nums_copy.sort()
    
    # Remove the smallest element from the sorted list k times
    for _ in range(k):
        # Remove the smallest element (first element in the sorted list)
        nums_copy.pop(0)
    
    # If the list is not empty after removals, return the first element (kth element after removals)
    if nums_copy:
        return nums_copy[0]
    else:
        # If the list is empty after removals, return None (or any other value to indicate the list is empty)
        return None

def findKthNumber(nums, k):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each number in the input list
    for num in nums:
        # Add the number to the result list
        result.append(num)
        
        # Find the kth element after removals
        kth_element = kth_element_after_removal(result, k)
        
        # If the kth element is not None, return it
        if kth_element is not None:
            return kth_element
    
    # If no kth element is found after iterating over the entire list, return None
    return None