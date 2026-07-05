def pick_peaks(arr):
    # Initialize an empty dictionary to store the peaks
    peaks = {'pos': [], 'peaks': []}
    
    # Iterate over the array from the second element to the second last element
    for i in range(1, len(arr) - 1):
        # Check if the current element is greater than its neighbors
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            # If it's a peak, add its position and value to the dictionary
            peaks['pos'].append(i)
            peaks['peaks'].append(arr[i])
    
    # Return the dictionary of peaks
    return peaks

# Test the function
print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]))