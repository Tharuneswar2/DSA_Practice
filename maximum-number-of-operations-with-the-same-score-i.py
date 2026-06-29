def maxEqualScore(operations):
    # Initialize variables to store the maximum score and the number of operations
    max_score = 0
    num_operations = 0

    # Iterate over the possible scores from 1 to 1000
    for score in range(1, 1001):
        # Calculate the number of operations required to reach the current score
        ops = (score + 1) // 2 + (score + 2) // 3

        # If the number of operations is greater than the current maximum, update the maximum score and number of operations
        if ops > num_operations:
            max_score = score
            num_operations = ops

    # Return the maximum score
    return max_score