def findNumbers(nums):
    # Initialize count of numbers with even number of digits
    count = 0
    
    # Iterate over each number in the list
    for num in nums:
        # Convert the number to a string to easily get the number of digits
        num_str = str(num)
        
        # Check if the number of digits is even
        if len(num_str) % 2 == 0:
            # If the number of digits is even, increment the count
            count += 1
    
    # Return the count of numbers with even number of digits
    return count