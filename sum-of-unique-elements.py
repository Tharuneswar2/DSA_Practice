def sum_of_unique_elements(nums):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    
    # Iterate through the list to count the frequency of each number
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Initialize a variable to store the sum of unique elements
    unique_sum = 0
    
    # Iterate through the dictionary to find the unique elements (frequency 1) and add them to the sum
    for num, freq in freq_dict.items():
        if freq == 1:
            unique_sum += num
    
    return unique_sum

# Alternatively, you can use a collections.Counter object to simplify the code
from collections import Counter

def sum_of_unique_elements(nums):
    # Create a Counter object to store the frequency of each number
    freq_counter = Counter(nums)
    
    # Initialize a variable to store the sum of unique elements
    unique_sum = 0
    
    # Iterate through the Counter object to find the unique elements (frequency 1) and add them to the sum
    for num, freq in freq_counter.items():
        if freq == 1:
            unique_sum += num
    
    return unique_sum