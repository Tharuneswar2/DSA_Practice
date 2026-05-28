def countLargestGroup(n):
    # Initialize a hashmap to store the sum of digits as keys and their counts as values
    count_map = {}
    
    # Initialize the maximum count and the count of the maximum groups
    max_count = 0
    max_groups = 0
    
    # Iterate over the range from 1 to n
    for i in range(1, n + 1):
        # Calculate the sum of digits of the current number
        digit_sum = sum(int(digit) for digit in str(i))
        
        # Increment the count of the current sum in the hashmap
        count_map[digit_sum] = count_map.get(digit_sum, 0) + 1
        
        # Update the maximum count and the count of the maximum groups
        if count_map[digit_sum] > max_count:
            max_count = count_map[digit_sum]
            max_groups = 1
        elif count_map[digit_sum] == max_count:
            max_groups += 1
    
    # Return the count of the maximum groups
    return max_groups