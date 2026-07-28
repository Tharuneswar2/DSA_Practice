# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def increasingTriplet(nums):
    # Initialize the first and second elements of the increasing subsequence to infinity
    # This is because we want to ensure that the first and second elements are updated correctly
    first = second = float('inf')
    
    # Iterate over the input list
    for num in nums:
        # If the current number is less than or equal to the first element, update the first element
        # This is because we want to find the smallest possible first element of the increasing subsequence
        if num <= first:
            first = num
        # If the current number is less than or equal to the second element but greater than the first element, update the second element
        # This is because we want to find the smallest possible second element of the increasing subsequence
        elif num <= second:
            second = num
        # If the current number is greater than the second element, return True
        # This is because we have found an increasing subsequence of length 3
        else:
            return True
    
    # If we have iterated over the entire list and haven't found an increasing subsequence of length 3, return False
    return False