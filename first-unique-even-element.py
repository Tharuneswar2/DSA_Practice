def first_unique_even(nums):
    # Create a dictionary to store the frequency of each number
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate over the list again to find the first unique even number
    for num in nums:
        # Check if the number is even and its frequency is 1
        if num % 2 == 0 and freq[num] == 1:
            return num

    # If no unique even number is found, return None
    return None

# Test the function
print(first_unique_even([1, 2, 3, 4, 5, 6, 2, 4]))  # Output: 6
print(first_unique_even([1, 1, 2, 2, 3, 3, 4, 4]))  # Output: None