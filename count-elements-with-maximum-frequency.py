def countElementsWithMaximumFrequency(arr):
    # Create a dictionary to store the frequency of each element
    freq_dict = {}
    
    # Iterate over the array to count the frequency of each element
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Find the maximum frequency
    max_freq = max(freq_dict.values())
    
    # Count the elements with maximum frequency
    count = sum(1 for freq in freq_dict.values() if freq == max_freq)
    
    return count

# Test the function
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(countElementsWithMaximumFrequency(arr))