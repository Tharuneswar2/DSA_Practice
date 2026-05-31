def count_pairs(nums, k):
    # Initialize a hashmap to store the frequency of each number
    freq_map = {}
    
    # Initialize the count of equal and divisible pairs
    count = 0
    
    # Iterate over the array to populate the hashmap
    for num in nums:
        # If the number is already in the hashmap, increment its frequency
        if num in freq_map:
            freq_map[num] += 1
        # If the number is not in the hashmap, add it with a frequency of 1
        else:
            freq_map[num] = 1
    
    # Iterate over the hashmap to count the equal and divisible pairs
    for num, freq in freq_map.items():
        # For each number, iterate from 1 to k (inclusive)
        for i in range(1, k + 1):
            # If the number is divisible by i, check if the quotient is in the hashmap
            if num % i == 0 and num // i in freq_map:
                # If the quotient is in the hashmap, increment the count by the product of their frequencies
                count += freq * freq_map[num // i]
    
    # Since we counted each pair twice, divide the count by 2
    count //= 2
    
    # Return the count of equal and divisible pairs
    return count

# Example usage:
nums = [1, 2, 3, 4, 5, 6]
k = 2
print(count_pairs(nums, k))