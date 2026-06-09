def mostVisited(n, rounds):
    # Initialize variables to store the start and end of the range
    start, end = rounds[0], rounds[-1]
    
    # If the end is less than the start, it means we have to consider the circular nature of the track
    if end < start:
        # In this case, we need to consider two ranges: from the start to the end of the track, and from the beginning of the track to the end
        return list(range(start, n + 1)) + list(range(1, end + 1))
    else:
        # If the end is not less than the start, we can simply return the range from the start to the end
        return list(range(start, end + 1))

# Test the function
print(mostVisited(3, [1, 2]))  # Output: [1, 2]
print(mostVisited(4, [1, 3]))  # Output: [1, 2, 3, 4]
print(mostVisited(7, [1, 5]))  # Output: [1, 2, 3, 4, 5]