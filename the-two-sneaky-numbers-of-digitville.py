# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def find_sneaky_numbers(arr):
    # Create a hashmap to store the frequency of each number in the array
    freq_map = {}
    
    # Iterate over the array to populate the frequency map
    for num in arr:
        # If the number is already in the map, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the map, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Initialize variables to store the two sneaky numbers
    sneaky_num1, sneaky_num2 = None, None
    
    # Iterate over the array again to find the two sneaky numbers
    for num in arr:
        # If the frequency of the current number is 1, it's a sneaky number
        if freq_map[num] == 1:
            # If we've already found one sneaky number, this is the second one
            if sneaky_num1 is not None:
                sneaky_num2 = num
                # We've found both sneaky numbers, so we can break out of the loop
                break
            # If we haven't found a sneaky number yet, this is the first one
            else:
                sneaky_num1 = num
    
    # Return the two sneaky numbers
    return sneaky_num1, sneaky_num2