def find_subarrays(nums):
    # Initialize an empty dictionary to store the cumulative sum and its frequency
    cumulative_sum_freq = {0: 1}  # Base case: sum 0 has a frequency of 1
    cumulative_sum = 0
    subarrays = []

    # Iterate over the array
    for i in range(len(nums)):
        cumulative_sum += nums[i]
        # If the cumulative sum is already in the dictionary, it means we have found a subarray with equal sum
        if cumulative_sum in cumulative_sum_freq:
            # Append all subarrays ending at the current index with the same cumulative sum
            for j in range(i + 1):
                subarrays.append(nums[j:i + 1])
        # Update the frequency of the cumulative sum
        cumulative_sum_freq[cumulative_sum] = cumulative_sum_freq.get(cumulative_sum, 0) + 1

    return subarrays


def find_subarrays_with_equal_sum(nums):
    # Initialize an empty dictionary to store the cumulative sum and its frequency
    cumulative_sum_freq = {0: 1}  # Base case: sum 0 has a frequency of 1
    cumulative_sum = 0
    subarrays = []

    # Iterate over the array
    for i in range(len(nums)):
        cumulative_sum += nums[i]
        # If the cumulative sum is already in the dictionary, it means we have found a subarray with equal sum
        if cumulative_sum in cumulative_sum_freq and cumulative_sum_freq[cumulative_sum] > 1:
            # Append all subarrays ending at the current index with the same cumulative sum
            for j in range(i + 1):
                subarrays.append(nums[j:i + 1])
        # Update the frequency of the cumulative sum
        cumulative_sum_freq[cumulative_sum] = cumulative_sum_freq.get(cumulative_sum, 0) + 1

    return subarrays


# Test the function
nums = [1, 2, 3, 4, 5, 6]
print(find_subarrays(nums))
print(find_subarrays_with_equal_sum(nums))