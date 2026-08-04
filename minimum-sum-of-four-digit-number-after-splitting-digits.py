# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minimumSum(num):
    # Convert the number into a list of digits
    digits = [int(d) for d in str(num)]
    
    # Sort the digits in ascending order
    digits.sort()
    
    # Combine the smallest and second smallest digits to form the first number
    # Combine the third smallest and largest digits to form the second number
    # This way, we minimize the sum of the two numbers
    return digits[0]*10 + digits[1] + digits[2]*10 + digits[3]