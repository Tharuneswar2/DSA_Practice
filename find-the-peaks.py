# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findPeaks(arr):
    # Initialize an empty list to store the indices of peaks
    peaks = []
    
    # Check if the array is not empty
    if len(arr) > 0:
        # Check if the first element is a peak
        if len(arr) == 1 or arr[0] > arr[1]:
            # If it's a peak, add its index to the list
            peaks.append(0)
        
        # Iterate over the array from the second element to the second last element
        for i in range(1, len(arr) - 1):
            # Check if the current element is a peak
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                # If it's a peak, add its index to the list
                peaks.append(i)
        
        # Check if the last element is a peak
        if len(arr) > 1 and arr[-1] > arr[-2]:
            # If it's a peak, add its index to the list
            peaks.append(len(arr) - 1)
    
    # Return the list of indices of peaks
    return peaks