# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def distributeElements(nums):
    # Sort the input list in ascending order
    nums.sort()
    
    # Initialize two empty lists to store the distributed elements
    list1, list2 = [], []
    
    # Initialize two pointers, one at the start and one at the end of the sorted list
    left, right = 0, len(nums) - 1
    
    # Initialize a variable to keep track of the current sum of elements in list1
    sum1 = 0
    
    # Iterate over the sorted list
    while left <= right:
        # If the current sum of elements in list1 is less than or equal to the sum of elements in list2
        if sum1 <= sum(list2):
            # Add the smaller element to list1
            list1.append(nums[left])
            # Update the current sum of elements in list1
            sum1 += nums[left]
            # Move the left pointer to the right
            left += 1
        else:
            # Add the larger element to list2
            list2.append(nums[right])
            # Move the right pointer to the left
            right -= 1
    
    # Return the two lists
    return list1, list2