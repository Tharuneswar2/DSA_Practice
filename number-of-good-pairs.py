def numIdenticalPairs(nums):
    # Create a dictionary to store the frequency of each number
    freq = {}
    
    # Initialize the count of good pairs
    count = 0
    
    # Iterate over the list of numbers
    for num in nums:
        # If the number is already in the dictionary, it means we have found a pair
        if num in freq:
            # Add the frequency of the number to the count of good pairs
            # This is because each occurrence of the number can form a pair with all previous occurrences
            count += freq[num]
        
        # Increment the frequency of the number
        freq[num] = freq.get(num, 0) + 1
    
    # Return the count of good pairs
    return count