def sortByBits(arr):
    # Use a custom sorting key that first considers the number of 1 bits in the binary representation of a number
    # and then the number itself in case of a tie
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Alternatively, you can use a more efficient approach by using the built-in bit_count function (Python 3.10+)
def sortByBits(arr):
    # Use a custom sorting key that first considers the number of 1 bits in the binary representation of a number
    # and then the number itself in case of a tie
    return sorted(arr, key=lambda x: (x.bit_count(), x))