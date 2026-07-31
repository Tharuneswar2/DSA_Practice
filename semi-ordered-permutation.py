# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def semiOrderedPermutation(arr):
    # Separate the array into two lists: one for positive numbers and one for negative numbers
    positives = [x for x in arr if x > 0]
    negatives = [x for x in arr if x < 0]

    # Sort the positive numbers in ascending order
    positives.sort()

    # Sort the negative numbers in descending order
    negatives.sort(reverse=True)

    # Combine the sorted negative numbers and positive numbers
    result = negatives + positives

    return result