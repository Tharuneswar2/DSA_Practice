def solution(A):
    # Create a set from the list for efficient lookups
    A_set = set(A)
    
    # Initialize the smallest missing integer to 1
    smallest_missing = 1
    
    # Iterate through the range from 1 to the maximum value in the list plus one
    while smallest_missing in A_set:
        # If the current integer is in the set, increment it
        smallest_missing += 1
    
    # Return the smallest missing integer
    return smallest_missing