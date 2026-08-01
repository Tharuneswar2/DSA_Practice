# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def intersection(nums):
    # Initialize the intersection set with the first list in nums
    intersection_set = set(nums[0])
    
    # Iterate over the rest of the lists in nums
    for num in nums[1:]:
        # Update the intersection set to include only the elements common to the current list and the intersection set
        intersection_set &= set(num)
        
    # Convert the intersection set back to a list and return it
    return list(intersection_set)

# Alternatively, we can use the built-in set intersection operation
def intersection_alternative(nums):
    # Initialize the intersection set with the first list in nums
    intersection_set = set(nums[0])
    
    # Use the built-in set intersection operation to find the intersection of all lists
    for num in nums[1:]:
        intersection_set = intersection_set.intersection(set(num))
        
    # Convert the intersection set back to a list and return it
    return list(intersection_set)

# We can also use the set intersection operation in a more concise way
def intersection_concise(nums):
    # Use the built-in set intersection operation to find the intersection of all lists
    return list(set.intersection(*map(set, nums)))