# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def kthDistinct(arr, k):
    # Create a dictionary to store the frequency of each string in the array
    freq_dict = {}
    for string in arr:
        # If the string is already in the dictionary, increment its count
        if string in freq_dict:
            freq_dict[string] += 1
        # If the string is not in the dictionary, add it with a count of 1
        else:
            freq_dict[string] = 1
    
    # Initialize a counter to keep track of the number of distinct strings found
    distinct_count = 0
    # Iterate over the array again to find the kth distinct string
    for string in arr:
        # If the string's frequency is 1, it's a distinct string
        if freq_dict[string] == 1:
            # Increment the distinct string count
            distinct_count += 1
            # If this is the kth distinct string, return it
            if distinct_count == k:
                return string
    
    # If there are less than k distinct strings, return an empty string
    return ""