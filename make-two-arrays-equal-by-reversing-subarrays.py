def canBeEqual(target, arr):
    # If the two arrays are not of the same length, they cannot be equal
    if len(target) != len(arr):
        return False

    # Sort both arrays
    target.sort()
    arr.sort()

    # Compare the sorted arrays
    return target == arr

def canBeEqualAlternative(target, arr):
    # If the two arrays are not of the same length, they cannot be equal
    if len(target) != len(arr):
        return False

    # Create a dictionary to store the frequency of each element in the target array
    freq = {}
    for num in target:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate over the arr array and decrement the frequency of each element
    for num in arr:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1

    # If we have iterated over the entire arr array and the frequency of each element is 0, the arrays can be equal
    return True