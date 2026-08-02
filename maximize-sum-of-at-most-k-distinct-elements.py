# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maximizeSum(nums, k):
    # Create a dictionary to store the frequency of each element in the array
    freq = {}
    for num in nums:
        # If the number is already in the dictionary, increment its frequency
        if num in freq:
            freq[num] += 1
        # If the number is not in the dictionary, add it with a frequency of 1
        else:
            freq[num] = 1
    
    # Sort the dictionary items by their frequency in descending order
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize variables to store the maximum sum and the number of distinct elements
    max_sum = 0
    distinct_count = 0
    
    # Iterate over the sorted dictionary items
    for num, count in sorted_freq:
        # If adding the current number's frequency to the sum does not exceed k distinct elements
        if distinct_count + 1 <= k:
            # Add the current number's frequency to the sum
            max_sum += num * count
            # Increment the distinct count
            distinct_count += 1
        # If adding the current number's frequency to the sum exceeds k distinct elements
        else:
            # Add the remaining frequency to the sum
            max_sum += num * (k - distinct_count)
            # Break the loop as we have reached k distinct elements
            break
    
    # Return the maximum sum
    return max_sum