def sortByBits(arr):
    # Create a custom sorting key that returns a tuple
    # The first element of the tuple is the number of 1 bits in the binary representation of the number
    # The second element is the number itself
    # This way, numbers with fewer 1 bits will come first, and numbers with the same number of 1 bits will be sorted by their value
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Test the function
print(sortByBits([0,1,2,3,4,5,6,7,8]))