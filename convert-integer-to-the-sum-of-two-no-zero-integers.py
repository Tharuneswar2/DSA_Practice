# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def getNoZeroIntegers(n: int):
    # Loop through all possible values of 'a' from 1 to n-1
    for a in range(1, n):
        # Calculate 'b' as n - 'a'
        b = n - a
        # Convert 'a' and 'b' to strings to check if they contain any zeros
        str_a, str_b = str(a), str(b)
        # Check if 'a' and 'b' do not contain any zeros
        if '0' not in str_a and '0' not in str_b:
            # If 'a' and 'b' do not contain any zeros, return them as the result
            return [a, b]