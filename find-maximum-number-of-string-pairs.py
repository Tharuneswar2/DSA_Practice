def maxNumberOfFamilies(n, reservedSeats):
    # Create a dictionary to store the reserved seats for each row
    reserved = {}
    for i, j in reservedSeats:
        if i not in reserved:
            reserved[i] = set()
        reserved[i].add(j)

    # Initialize the count of maximum families
    max_families = 0

    # Iterate over each row
    for row in range(1, n + 1):
        # If the row is not reserved, we can fit 2 families
        if row not in reserved:
            max_families += 2
        else:
            # Check if we can fit a family in the left half
            left_half = {2, 3, 4, 5}.issubset(reserved.get(row, set()))
            # Check if we can fit a family in the right half
            right_half = {6, 7, 8, 9}.issubset(reserved.get(row, set()))
            # If we can fit a family in both halves, increment the count by 2
            if left_half and right_half:
                max_families += 2
            # If we can fit a family in either half, increment the count by 1
            elif left_half or right_half:
                max_families += 1

    return max_families