# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def min_operations(nums):
    # Initialize variables to store the count of elements with remainder 1 and 2 when divided by 3
    remainder_1 = 0
    remainder_2 = 0
    
    # Iterate over each element in the input list
    for num in nums:
        # Calculate the remainder when the current element is divided by 3
        remainder = num % 3
        
        # If the remainder is 1, increment the count of elements with remainder 1
        if remainder == 1:
            remainder_1 += 1
        # If the remainder is 2, increment the count of elements with remainder 2
        elif remainder == 2:
            remainder_2 += 1
    
    # The minimum number of operations is the minimum of the count of elements with remainder 1 and 2
    # This is because we can always make an element with remainder 1 or 2 divisible by 3 by adding 2 or 1 respectively
    # However, we can also make an element with remainder 1 divisible by 3 by adding 1 to an element with remainder 2
    # So, we need to consider the minimum of the two counts
    return min(remainder_1, remainder_2)