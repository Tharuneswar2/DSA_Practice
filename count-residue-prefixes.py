# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def countPrefixes(arr, n):
    # Initialize a hashmap to store the frequency of each element
    freq_map = {}
    
    # Initialize the count of residue prefixes
    count = 0
    
    # Initialize the prefix sum
    prefix_sum = 0
    
    # Iterate over the array
    for i in range(n):
        # Update the prefix sum
        prefix_sum += arr[i]
        
        # If the prefix sum is 0, increment the count
        if prefix_sum == 0:
            count += 1
        
        # If the prefix sum is already in the hashmap, increment the count by the frequency of the prefix sum
        if prefix_sum in freq_map:
            count += freq_map[prefix_sum]
        
        # Update the frequency of the prefix sum in the hashmap
        freq_map[prefix_sum] = freq_map.get(prefix_sum, 0) + 1
    
    # Return the count of residue prefixes
    return count