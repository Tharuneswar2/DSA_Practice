# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def first_unique_even(nums):
    # Create a dictionary to store the frequency of each number in the list
    freq_dict = {}
    
    # Iterate over the list to count the frequency of each number
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Iterate over the list again to find the first unique even number
    for num in nums:
        # Check if the number is even and its frequency is 1
        if num % 2 == 0 and freq_dict[num] == 1:
            # Return the first unique even number
            return num
    
    # If no unique even number is found, return -1
    return -1