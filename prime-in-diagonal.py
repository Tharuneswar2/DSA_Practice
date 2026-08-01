# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

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
    # Check if there is a prime number in the diagonal of the matrix
    size = len(matrix)
    for i in range(size):
        # Check the primary diagonal
        if is_prime(matrix[i][i]):
            return True
        # Check the secondary diagonal
        if is_prime(matrix[i][size - i - 1]):
            return True
    return False

def main():
    # Read the size of the matrix
    size = int(input())
    # Read the matrix
    matrix = []
    for _ in range(size):
        row = list(map(int, input().split()))
        matrix.append(row)
    # Check if there is a prime number in the diagonal
    if prime_in_diagonal(matrix):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()