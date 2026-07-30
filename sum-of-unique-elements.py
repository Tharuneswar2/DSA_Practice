# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def sumOfUnique(nums):
    # Create a dictionary to store the frequency of each number in the list
    freq_dict = {}
    
    # Iterate over the list to count the frequency of each number
    for num in nums:
        # If the number is already in the dictionary, increment its count
        if num in freq_dict:
            freq_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            freq_dict[num] = 1
    
    # Initialize a variable to store the sum of unique elements
    unique_sum = 0
    
    # Iterate over the dictionary to find the numbers with a frequency of 1
    for num, freq in freq_dict.items():
        # If the frequency of the number is 1, add it to the sum
        if freq == 1:
            unique_sum += num
    
    # Return the sum of unique elements
    return unique_sum