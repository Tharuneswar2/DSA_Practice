def divideArray(nums):
    # Create a dictionary to store the frequency of each number
    freq = {}
    
    # Iterate over the array to count the frequency of each number
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Check if all frequencies are even
    for count in freq.values():
        if count % 2 != 0:
            return False
    
    return True