# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def valid_elements(arr):
    # Initialize an empty dictionary to store the frequency of each element in the array
    freq_dict = {}
    
    # Iterate over the array to count the frequency of each element
    for num in arr:
        # If the number is already in the dictionary, increment its count
        if num in freq_dict:
            freq_dict[num] += 1
        # If the number is not in the dictionary, add it with a count of 1
        else:
            freq_dict[num] = 1
    
    # Initialize an empty list to store the valid elements
    valid_arr = []
    
    # Iterate over the array again to check the validity of each element
    for num in arr:
        # If the frequency of the current number is greater than 1, it's a valid element
        if freq_dict[num] > 1:
            # Add the valid element to the result list
            valid_arr.append(num)
            # Decrement the frequency of the current number to avoid duplicates
            freq_dict[num] -= 1
    
    # Return the list of valid elements
    return valid_arr