def k_or(arr, k):
    # Initialize an empty dictionary to store the frequency of each element
    freq_dict = {}
    
    # Iterate over the array to count the frequency of each element
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Initialize an empty list to store the k-or elements
    k_or_elements = []
    
    # Iterate over the frequency dictionary to find the k-or elements
    for num, freq in freq_dict.items():
        # If the frequency of the element is greater than or equal to k, add it to the k-or elements list
        if freq >= k:
            k_or_elements.append(num)
    
    # Return the k-or elements list
    return k_or_elements

# Example usage:
arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 3
print(k_or(arr, k))  # Output: [3, 4]