# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxSubsequence(nums, k):
    # Create a list of tuples where each tuple contains the value and its index
    indexed_nums = [(val, idx) for idx, val in enumerate(nums)]
    
    # Sort the list of tuples in descending order based on the values
    indexed_nums.sort(key=lambda x: x[0], reverse=True)
    
    # Select the k largest values and sort them based on their original indices
    max_k = sorted(indexed_nums[:k], key=lambda x: x[1])
    
    # Return the subsequence of length k with the largest sum
    return [val for val, idx in max_k]