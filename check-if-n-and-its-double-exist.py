# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def checkIfExist(arr):
    # Create a set to store the elements we have seen so far
    seen = set()
    
    # Iterate over the array
    for num in arr:
        # If the double of the current number exists in the set, return True
        if num * 2 in seen:
            return True
        # If the current number is double of another number in the set, return True
        if num % 2 == 0 and num // 2 in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    
    # If we have iterated over the entire array and haven't found any pair, return False
    return False