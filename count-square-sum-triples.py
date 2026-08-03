# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def count_square_sum_triples(n):
    # Initialize count variable to store the number of triples
    count = 0
    
    # Iterate over all possible values of 'a' from 1 to n
    for a in range(1, n + 1):
        # Iterate over all possible values of 'b' from 'a' to n
        for b in range(a, n + 1):
            # Calculate 'c' using the formula c = sqrt(a^2 + b^2)
            c = (a ** 2 + b ** 2) ** 0.5
            
            # Check if 'c' is an integer and 'c' is less than or equal to n
            if c == int(c) and c <= n:
                # If 'c' is an integer and 'c' is less than or equal to n, increment the count
                count += 1
                
    # Return the total count of triples
    return count