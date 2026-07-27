# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countLargestGroup(n: int) -> int:
    # Initialize a hashmap to store the frequency of each sum
    sum_freq = {}
    
    # Initialize the maximum frequency and the count of maximum frequency
    max_freq = 0
    max_freq_count = 0
    
    # Iterate over all numbers from 1 to n
    for i in range(1, n + 1):
        # Calculate the sum of digits of the current number
        digit_sum = sum(int(digit) for digit in str(i))
        
        # Increment the frequency of the current sum in the hashmap
        sum_freq[digit_sum] = sum_freq.get(digit_sum, 0) + 1
        
        # Update the maximum frequency and its count if the current frequency is higher
        if sum_freq[digit_sum] > max_freq:
            max_freq = sum_freq[digit_sum]
            max_freq_count = 1
        elif sum_freq[digit_sum] == max_freq:
            # If the current frequency is equal to the maximum frequency, increment its count
            max_freq_count += 1
    
    # Return the count of maximum frequency
    return max_freq_count