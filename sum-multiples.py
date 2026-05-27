def sum_of_multiples(limit, multiples):
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over all numbers from 1 to limit (exclusive)
    for num in range(1, limit):
        # Check if the current number is a multiple of any of the given multiples
        for multiple in multiples:
            # If it is, add it to the sum and break the loop to avoid duplicates
            if num % multiple == 0:
                total_sum += num
                break
                
    # Return the calculated sum
    return total_sum

# Example usage
print(sum_of_multiples(1000, [3, 5]))