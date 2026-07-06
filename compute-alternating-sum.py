def alternatingSum(nums):
    # Initialize two variables to store the sum of elements at even and odd indices
    even_sum = 0
    odd_sum = 0
    
    # Iterate over the list of numbers with their indices
    for i, num in enumerate(nums):
        # If the index is even, add the number to even_sum
        if i % 2 == 0:
            even_sum += num
        # If the index is odd, subtract the number from even_sum
        else:
            even_sum -= num
    
    # Return the final result
    return even_sum

# Alternatively, you can use list slicing to separate the numbers at even and odd indices
def alternatingSumAlternative(nums):
    # Separate the numbers at even and odd indices
    even_nums = nums[::2]
    odd_nums = nums[1::2]
    
    # Calculate the sum of numbers at even indices
    even_sum = sum(even_nums)
    
    # Calculate the sum of numbers at odd indices
    odd_sum = sum(odd_nums)
    
    # Return the difference between the sum of numbers at even indices and the sum of numbers at odd indices
    return even_sum - odd_sum