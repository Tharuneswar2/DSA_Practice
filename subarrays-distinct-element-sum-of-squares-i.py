def sum_of_squares(arr):
    n = len(arr)
    # Initialize a hashmap to store the frequency of each element
    freq_map = {}
    # Initialize variables to store the sum of squares and the current window sum
    sum_squares = 0
    window_sum = 0
    # Initialize variables to store the start of the window and the number of distinct elements
    window_start = 0
    distinct_count = 0

    for window_end in range(n):
        # Add the current element to the frequency map
        if arr[window_end] not in freq_map:
            freq_map[arr[window_end]] = 0
            distinct_count += 1
        freq_map[arr[window_end]] += 1

        # Add the square of the current element to the window sum
        window_sum += arr[window_end] ** 2

        # Shrink the window from the left if the number of distinct elements exceeds 1
        while distinct_count > 1:
            freq_map[arr[window_start]] -= 1
            if freq_map[arr[window_start]] == 0:
                distinct_count -= 1
            window_sum -= arr[window_start] ** 2
            window_start += 1

        # If the window contains only one distinct element, add the window sum to the sum of squares
        if distinct_count == 1:
            sum_squares += window_sum

    return sum_squares