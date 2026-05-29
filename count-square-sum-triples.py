def count_square_sum_triples(n):
    # Initialize count variable to store the number of triples
    count = 0
    
    # Iterate over all possible values of a and b
    for a in range(1, n):
        for b in range(a, n):
            # Calculate c using the formula c = sqrt(a^2 + b^2)
            c = (a ** 2 + b ** 2) ** 0.5
            
            # Check if c is an integer and a^2 + b^2 = c^2
            if c == int(c) and a ** 2 + b ** 2 == int(c) ** 2:
                # If the condition is met, increment the count
                count += 1
                
    # Return the total count of triples
    return count

# Test the function
print(count_square_sum_triples(5))