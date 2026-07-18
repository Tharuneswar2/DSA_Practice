# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minOperations(nums):
    # Create a set to store unique elements from the array
    unique_nums = set()
    
    # Initialize the count of operations
    operations = 0
    
    # Iterate over each element in the array
    for num in nums:
        # If the number is already in the set, it's not distinct
        if num in unique_nums:
            # Increment the operations count
            operations += 1
            
            # Make the number distinct by incrementing it
            while num in unique_nums:
                num += 1
                operations += 1
            
            # Add the distinct number to the set
            unique_nums.add(num)
        else:
            # If the number is distinct, add it to the set
            unique_nums.add(num)
    
    # Return the total operations count
    return operations