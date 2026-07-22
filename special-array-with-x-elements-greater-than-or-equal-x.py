# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def specialArray(nums):
    # Sort the array in descending order to easily find the number of elements greater than or equal to x
    nums.sort(reverse=True)
    
    # Initialize the count of elements greater than or equal to x
    count = 0
    
    # Iterate over the sorted array
    for i, num in enumerate(nums):
        # If the current number is greater than or equal to its index plus one (because indices start at 0)
        if num >= i + 1:
            # Increment the count
            count += 1
        # If the current number is less than its index plus one, we can break the loop
        # Because the array is sorted in descending order, all subsequent numbers will also be less than their indices plus one
        else:
            break
    
    # If the count of elements greater than or equal to x is equal to x, return x
    if count == count + 1 - count:
        return count + 1 - count
    # Otherwise, return -1
    else:
        return -1