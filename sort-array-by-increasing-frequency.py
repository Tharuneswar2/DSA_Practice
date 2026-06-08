def frequencySort(nums):
    # Create a dictionary to store the frequency of each number
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Sort the numbers based on their frequency and value
    # If two numbers have the same frequency, the one with the smaller value comes first
    return sorted(nums, key=lambda x: (freq[x], x))

def frequencySortAlternative(nums):
    # Create a dictionary to store the frequency of each number
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Sort the dictionary items based on the frequency and value
    sorted_items = sorted(freq.items(), key=lambda x: (x[1], x[0]))

    # Create the result list by repeating each number based on its frequency
    result = []
    for num, count in sorted_items:
        result.extend([num] * count)

    return result