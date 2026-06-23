def distributeElements(nums):
    # Sort the input array in ascending order
    nums.sort()
    
    # Initialize two empty arrays
    arr1, arr2 = [], []
    
    # Initialize two pointers, one at the start and one at the end of the sorted array
    left, right = 0, len(nums) - 1
    
    # Distribute elements into two arrays
    while left <= right:
        # Push the smaller element into arr1
        arr1.append(nums[left])
        left += 1
        
        # If the left pointer is still less than or equal to the right pointer
        if left <= right:
            # Push the larger element into arr2
            arr2.append(nums[right])
            right -= 1
    
    # Return the two arrays
    return arr1, arr2

# Test the function
nums = [1, 2, 3, 4, 5]
arr1, arr2 = distributeElements(nums)
print("Array 1:", arr1)
print("Array 2:", arr2)