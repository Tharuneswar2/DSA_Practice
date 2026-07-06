def isCovered(ranges, left, right):
    # Create a set to store the covered numbers
    covered = set()
    
    # Iterate over each range
    for start, end in ranges:
        # Add all numbers in the range to the covered set
        covered.update(range(start, end + 1))
    
    # Check if all numbers in the given range are covered
    for num in range(left, right + 1):
        # If a number is not covered, return False
        if num not in covered:
            return False
    
    # If all numbers are covered, return True
    return True