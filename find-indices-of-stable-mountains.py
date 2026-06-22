def find_stable_mountains(peaks):
    # Initialize an empty list to store the indices of stable mountains
    stable_mountains = []

    # Iterate over the peaks list with their indices
    for i in range(len(peaks)):
        # Check if the current peak is a mountain (i.e., it's greater than its neighbors)
        if (i == 0 or peaks[i] > peaks[i-1]) and (i == len(peaks)-1 or peaks[i] > peaks[i+1]):
            # If the current peak is a mountain, check if it's stable
            if (i == 0 or peaks[i] >= peaks[i-1]) and (i == len(peaks)-1 or peaks[i] >= peaks[i+1]):
                # If the current peak is stable, add its index to the stable_mountains list
                stable_mountains.append(i)

    # Return the list of indices of stable mountains
    return stable_mountains

# Example usage:
peaks = [1, 3, 5, 4, 3, 2, 1]
print(find_stable_mountains(peaks))