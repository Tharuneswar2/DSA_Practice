def checkIfExist(arr):
    # Create a set to store the elements we have seen so far
    seen = set()
    
    # Iterate over the array
    for num in arr:
        # Check if the double of the current number exists in the set
        if num * 2 in seen:
            return True
        # Check if the half of the current number exists in the set
        if num % 2 == 0 and num // 2 in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    
    # If we have iterated over the entire array and haven't found a pair, return False
    return False