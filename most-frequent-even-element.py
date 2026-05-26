def most_frequent_even(nums):
    # Create a dictionary to store the frequency of each even number
    even_freq = {}
    
    # Iterate through the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is already in the dictionary, increment its frequency
            if num in even_freq:
                even_freq[num] += 1
            # If the number is not in the dictionary, add it with a frequency of 1
            else:
                even_freq[num] = 1
    
    # If the dictionary is empty (i.e., no even numbers), return None
    if not even_freq:
        return None
    
    # Find the maximum frequency
    max_freq = max(even_freq.values())
    
    # Find all numbers with the maximum frequency
    most_frequent = [num for num, freq in even_freq.items() if freq == max_freq]
    
    # Return the smallest number with the maximum frequency
    return min(most_frequent)

# Example usage:
print(most_frequent_even([1, 2, 2, 3, 4, 4, 4, 5, 6, 6]))  # Output: 4