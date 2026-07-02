def gcd_odd_even_sums(arr):
    # Calculate the sum of odd numbers
    odd_sum = sum(num for num in arr if num % 2 != 0)
    
    # Calculate the sum of even numbers
    even_sum = sum(num for num in arr if num % 2 == 0)
    
    # Function to calculate GCD using Euclidean algorithm
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    # Calculate the GCD of odd and even sums
    result = gcd(odd_sum, even_sum)
    
    return result

# Test the function
arr = [1, 2, 3, 4, 5, 6]
print(gcd_odd_even_sums(arr))