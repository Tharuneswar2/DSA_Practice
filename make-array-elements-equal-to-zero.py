# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def make_array_zero(nums):
    # Initialize a set to store unique elements from the array
    unique_nums = set()
    
    # Iterate over the array to find unique elements
    for num in nums:
        # Add each element to the set
        unique_nums.add(num)
        
    # Initialize a variable to store the minimum number of operations
    min_operations = 0
    
    # Iterate over the unique elements
    for num in unique_nums:
        # If the number is not zero, increment the minimum number of operations
        if num != 0:
            min_operations += 1
            
    # Return the minimum number of operations
    return min_operations