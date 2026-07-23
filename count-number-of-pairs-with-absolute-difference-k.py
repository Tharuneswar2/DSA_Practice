# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def count_pairs_with_diff_k(arr, n, k):
    # Create a hashmap to store the frequency of each element in the array
    freq_map = {}
    
    # Initialize count of pairs with absolute difference k to 0
    count = 0
    
    # Iterate through the array to populate the hashmap
    for num in arr:
        # If the number is already in the hashmap, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the hashmap, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Iterate through the array again to find pairs with absolute difference k
    for num in arr:
        # Calculate the other number in the pair
        other_num = num - k
        
        # If the other number is in the hashmap and it's not the same as the current number
        if other_num in freq_map and other_num != num:
            # Increment the count by the frequency of the other number
            count += freq_map[other_num]
        # If the other number is the same as the current number
        elif other_num == num:
            # Increment the count by the frequency of the other number minus 1 (to avoid counting the same pair twice)
            count += freq_map[other_num] - 1
    
    # Return the count of pairs with absolute difference k
    return count // 2