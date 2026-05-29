def sum_of_elements_with_frequency_divisible_by_k(nums, k):
    # Create a dictionary to store the frequency of each number
    freq_dict = {}
    
    # Iterate over the list of numbers to populate the frequency dictionary
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Initialize a variable to store the sum of elements with frequency divisible by k
    total_sum = 0
    
    # Iterate over the frequency dictionary to calculate the sum
    for num, freq in freq_dict.items():
        # Check if the frequency is divisible by k
        if freq % k == 0:
            # If it is, add the number multiplied by its frequency to the total sum
            total_sum += num * freq
    
    # Return the total sum
    return total_sum