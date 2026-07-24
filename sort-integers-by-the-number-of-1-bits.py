# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sortByBits(arr):
    # Use a custom sorting key that first sorts by the number of 1 bits in the binary representation of each number
    # and then by the number itself in case of a tie
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))