def most_frequent_key_following(arr, key):
    # Create a dictionary to store the frequency of each number following the key
    freq_dict = {}
    
    # Iterate over the array
    for i in range(len(arr) - 1):
        # Check if the current element is the key
        if arr[i] == key:
            # If the next element is already in the dictionary, increment its count
            if arr[i + 1] in freq_dict:
                freq_dict[arr[i + 1]] += 1
            # If the next element is not in the dictionary, add it with a count of 1
            else:
                freq_dict[arr[i + 1]] = 1
    
    # Check if the dictionary is empty (i.e., the key was not found in the array)
    if not freq_dict:
        return None
    
    # Find the number with the maximum frequency
    max_freq = max(freq_dict.values())
    
    # Find all numbers with the maximum frequency
    most_frequent_nums = [num for num, freq in freq_dict.items() if freq == max_freq]
    
    # Return the smallest of the most frequent numbers
    return min(most_frequent_nums)

# Example usage:
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
key = 2
print(most_frequent_key_following(arr, key))  # Output: 3