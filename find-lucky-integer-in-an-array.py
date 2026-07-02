def findLucky(arr):
    # Create a dictionary to store the frequency of each number
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Initialize lucky integer as -1
    lucky = -1
    
    # Iterate through the dictionary to find the lucky integer
    for num, count in freq.items():
        # If the number is equal to its frequency, update the lucky integer
        if num == count:
            lucky = num
    
    # Return the lucky integer
    return lucky

# Test the function
print(findLucky([2,2,3,4]))  # Output: 2
print(findLucky([1,2,2,3,3,3]))  # Output: 3
print(findLucky([2,2,2,3,3]))  # Output: -1