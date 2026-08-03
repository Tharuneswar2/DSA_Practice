# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numBeautifulPairs(nums1, nums2):
    # Create a hashmap to store the frequency of each number in nums1
    freq_map1 = {}
    for num in nums1:
        # If the number is already in the hashmap, increment its frequency
        if num in freq_map1:
            freq_map1[num] += 1
        # If the number is not in the hashmap, add it with a frequency of 1
        else:
            freq_map1[num] = 1

    # Create a hashmap to store the frequency of each number in nums2
    freq_map2 = {}
    for num in nums2:
        # If the number is already in the hashmap, increment its frequency
        if num in freq_map2:
            freq_map2[num] += 1
        # If the number is not in the hashmap, add it with a frequency of 1
        else:
            freq_map2[num] = 1

    # Initialize a variable to store the total number of beautiful pairs
    total_pairs = 0
    # Iterate over the numbers in nums1
    for num in nums1:
        # For each number in nums1, find the number of beautiful pairs it can form with numbers in nums2
        for i in range(1, 7):
            # Calculate the corresponding number in nums2 that would form a beautiful pair with the current number in nums1
            corresponding_num = num + i
            # If the corresponding number is in the hashmap of nums2, increment the total number of beautiful pairs by the frequency of the corresponding number
            if corresponding_num in freq_map2:
                total_pairs += freq_map2[corresponding_num]

    # Return the total number of beautiful pairs
    return total_pairs