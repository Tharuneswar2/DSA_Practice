def max_difference(nums):
    # Initialize variables to store the maximum and minimum frequencies
    max_freq = float('-inf')
    min_freq = float('inf')

    # Initialize variables to store the sum of even and odd frequencies
    even_sum = 0
    odd_sum = 0

    # Iterate over the list of numbers
    for num in nums:
        # Calculate the frequency of the current number
        freq = nums.count(num)

        # If the frequency is even, add it to the even sum
        if freq % 2 == 0:
            even_sum += freq
        # If the frequency is odd, add it to the odd sum
        else:
            odd_sum += freq

        # Update the maximum frequency
        max_freq = max(max_freq, freq)
        # Update the minimum frequency
        min_freq = min(min_freq, freq)

    # Return the maximum difference between the even and odd sums
    return max(abs(even_sum - odd_sum), max_freq - min_freq)