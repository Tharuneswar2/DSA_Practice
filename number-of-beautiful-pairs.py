def numBeautifulPairs(nums1, nums2):
    # Create a hashmap to store the frequency of each number in nums1
    freq_map = {}
    for num in nums1:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1

    # Initialize the count of beautiful pairs
    count = 0

    # Iterate over each number in nums2
    for num in nums2:
        # Check if the number plus one or minus one exists in the hashmap
        if num + 1 in freq_map and freq_map[num + 1] > 0:
            # If it exists, increment the count and decrement the frequency
            count += 1
            freq_map[num + 1] -= 1
        elif num - 1 in freq_map and freq_map[num - 1] > 0:
            # If it exists, increment the count and decrement the frequency
            count += 1
            freq_map[num - 1] -= 1

    return count