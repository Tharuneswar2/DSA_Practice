def maximum_value(strs):
    # Initialize max_value as negative infinity
    max_value = float('-inf')
    
    # Iterate over each string in the input list
    for s in strs:
        # Check if the string is numeric
        if s.isnumeric():
            # Convert the numeric string to an integer and update max_value if necessary
            max_value = max(max_value, int(s))
        else:
            # If the string is not numeric, calculate its length and update max_value if necessary
            max_value = max(max_value, len(s))
    
    # Return the maximum value found
    return max_value

# Example usage:
print(maximum_value(["alic3", "bob", "4", "3", "leetcod3"]))  # Output: 5