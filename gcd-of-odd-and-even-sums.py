# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def gcdOddEvenSums(arr):
    # Initialize variables to store the sum of odd and even numbers
    odd_sum = 0
    even_sum = 0
    
    # Iterate through the array to calculate the sum of odd and even numbers
    for num in arr:
        # Check if the number is odd
        if num % 2 != 0:
            # Add the odd number to the odd sum
            odd_sum += num
        else:
            # Add the even number to the even sum
            even_sum += num
    
    # Define a helper function to calculate the GCD using the Euclidean algorithm
    def gcd(a, b):
        # Base case: if b is zero, return a
        if b == 0:
            return a
        # Recursive case: call the gcd function with b and the remainder of a divided by b
        else:
            return gcd(b, a % b)
    
    # Calculate the GCD of the odd and even sums
    result = gcd(odd_sum, even_sum)
    
    # Return the result
    return result