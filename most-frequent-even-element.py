# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def most_frequent_even(nums):
    # Create a dictionary to store the frequency of each even number
    even_freq = {}
    
    # Iterate over the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is already in the dictionary, increment its frequency
            if num in even_freq:
                even_freq[num] += 1
            # If the number is not in the dictionary, add it with a frequency of 1
            else:
                even_freq[num] = 1
                
    # If the dictionary is empty (i.e., there are no even numbers), return -1
    if not even_freq:
        return -1
    
    # Find the maximum frequency
    max_freq = max(even_freq.values())
    
    # Find all numbers with the maximum frequency
    max_freq_nums = [num for num, freq in even_freq.items() if freq == max_freq]
    
    # Return the smallest number with the maximum frequency
    return min(max_freq_nums)