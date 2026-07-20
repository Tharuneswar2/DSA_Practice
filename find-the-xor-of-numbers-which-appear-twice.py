# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findSingle(nums):
    # Initialize result variable to store the XOR of numbers that appear twice
    result = 0
    
    # Iterate over each number in the input list
    for num in nums:
        # XOR the current number with the result
        # This works because XOR of a number with itself is 0, and XOR of a number with 0 is the number itself
        # So, numbers that appear twice will cancel each other out, leaving only the number that appears once
        result ^= num
    
    # Return the result, which is the XOR of numbers that appear twice
    return result