# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def isGoodArray(nums):
    # Check if the input is a list
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")

    # Check if the list is empty
    if len(nums) == 0:
        return True  # An empty list is considered a good array

    # Find the greatest common divisor (GCD) of the first two elements
    gcd = nums[0]
    for num in nums[1:]:
        # Use the Euclidean algorithm to calculate the GCD
        while num != 0:
            gcd, num = num, gcd % num

    # If the GCD is 1, the array is good
    return gcd == 1