# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def alternatingSum(nums):
    # Initialize two variables to store the sum of elements at even and odd indices
    even_sum = 0
    odd_sum = 0
    
    # Iterate over the list of numbers with their indices
    for i, num in enumerate(nums):
        # If the index is even, add the number to the even sum
        if i % 2 == 0:
            even_sum += num
        # If the index is odd, add the number to the odd sum
        else:
            odd_sum += num
    
    # Return the difference between the even sum and the odd sum
    return even_sum - odd_sum