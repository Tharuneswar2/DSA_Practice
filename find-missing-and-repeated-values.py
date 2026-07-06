def find_missing_repeated(arr):
    # Create a frequency array to store the frequency of each element
    freq = [0] * len(arr)
    
    # Traverse the array and update the frequency array
    for num in arr:
        freq[abs(num) - 1] += 1
    
    # Initialize variables to store the missing and repeated numbers
    missing = None
    repeated = None
    
    # Traverse the frequency array to find the missing and repeated numbers
    for i in range(len(freq)):
        if freq[i] == 0:
            missing = i + 1
        elif freq[i] > 1:
            repeated = i + 1
    
    return missing, repeated

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
missing, repeated = find_missing_repeated(arr)
print("Missing number:", missing)
print("Repeated number:", repeated)