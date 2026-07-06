def shuffle(nums, n):
    # Initialize an empty list to store the shuffled array
    shuffled = []
    
    # Iterate over the first half of the array
    for i in range(n):
        # Append the elements from the first half and the second half in alternating order
        shuffled.append(nums[i])
        shuffled.append(nums[n + i])
    
    # Return the shuffled array
    return shuffled

# Example usage:
nums = [1, 2, 3, 4, 5, 6]
n = 3
print(shuffle(nums, n))  # Output: [1, 4, 2, 5, 3, 6]