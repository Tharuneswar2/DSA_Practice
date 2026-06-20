def is_prime(n):
    # Check if a number is prime
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_in_diagonal(matrix):
    # Check if there is a prime number in the diagonal of a matrix
    size = len(matrix)
    for i in range(size):
        if is_prime(matrix[i][i]):
            return True
    return False

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 11]]
print(prime_in_diagonal(matrix))  # Output: True