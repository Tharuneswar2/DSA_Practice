def findGCD(nums):
    # Define a helper function to calculate the GCD of two numbers using Euclid's algorithm
    def gcd(a, b):
        # If b is zero, the GCD is a
        if b == 0:
            return a
        # Otherwise, recursively call gcd with b and the remainder of a divided by b
        else:
            return gcd(b, a % b)

    # Initialize the GCD with the first number in the array
    result = nums[0]
    # Iterate over the rest of the numbers in the array
    for num in nums[1:]:
        # Update the GCD by calculating the GCD of the current GCD and the current number
        result = gcd(result, num)
    # Return the final GCD
    return result

# Example usage:
print(findGCD([2, 4, 6, 8]))  # Output: 2
print(findGCD([7, 5, 6, 8, 3]))  # Output: 1