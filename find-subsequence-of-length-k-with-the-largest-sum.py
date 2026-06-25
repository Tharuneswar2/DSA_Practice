def maxSubsequence(nums, k):
    # Create a list of tuples where each tuple contains a number from the input list and its index
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    
    # Sort the list of tuples in descending order based on the numbers
    indexed_nums.sort(key=lambda x: x[0], reverse=True)
    
    # Select the k largest numbers and sort them based on their original indices
    selected_nums = sorted(indexed_nums[:k], key=lambda x: x[1])
    
    # Return the selected numbers
    return [num for num, _ in selected_nums]

# Test the function
print(maxSubsequence([2,1,3,3], 2))  # Output: [3, 3]
print(maxSubsequence([-1,-2,3,4], 3))  # Output: [-1, 3, 4]