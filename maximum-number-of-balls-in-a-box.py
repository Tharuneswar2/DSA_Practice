# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countBalls(lowLimit: int, highLimit: int) -> int:
    # Initialize a dictionary to store the sum of digits as keys and their frequencies as values
    freq_dict = {}
    
    # Initialize the maximum frequency
    max_freq = 0
    
    # Iterate over the range from lowLimit to highLimit (inclusive)
    for num in range(lowLimit, highLimit + 1):
        # Calculate the sum of digits of the current number
        digit_sum = sum(int(digit) for digit in str(num))
        
        # If the sum of digits is already in the dictionary, increment its frequency
        if digit_sum in freq_dict:
            freq_dict[digit_sum] += 1
        # Otherwise, add the sum of digits to the dictionary with a frequency of 1
        else:
            freq_dict[digit_sum] = 1
        
        # Update the maximum frequency
        max_freq = max(max_freq, freq_dict[digit_sum])
    
    # Return the maximum frequency
    return max_freq