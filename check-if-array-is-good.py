def isGoodArray(nums):
    # Initialize the gcd with the first element of the array
    gcd = nums[0]
    
    # Iterate over the rest of the array
    for num in nums[1:]:
        # Update the gcd using the Euclidean algorithm
        gcd = gcd_helper(gcd, num)
        
        # If the gcd becomes 1, we can return True immediately
        if gcd == 1:
            return True
            
    # If we've iterated over the entire array and the gcd is not 1, return False
    return False


def gcd_helper(a, b):
    # Base case: if b is 0, the gcd is a
    if b == 0:
        return a
    else:
        # Recursive case: gcd(a, b) = gcd(b, a % b)
        return gcd_helper(b, a % b)


# Example usage:
print(isGoodArray([12, 10, 18, 15]))  # False
print(isGoodArray([4, 2, 4, 2]))  # True