def makeEqual(s1, s2):
    # If the two strings are not of the same length, they cannot be made equal
    if len(s1) != len(s2):
        return False

    # Initialize two dictionaries to store the frequency of each character in both strings
    freq_s1 = {}
    freq_s2 = {}

    # Populate the frequency dictionaries
    for char in s1:
        if char in freq_s1:
            freq_s1[char] += 1
        else:
            freq_s1[char] = 1

    for char in s2:
        if char in freq_s2:
            freq_s2[char] += 1
        else:
            freq_s2[char] = 1

    # If the frequency dictionaries are not equal, the strings cannot be made equal
    if freq_s1 != freq_s2:
        return False

    # Initialize a variable to store the greatest common divisor (GCD) of the frequencies
    gcd = 0

    # Calculate the GCD of the frequencies
    for key in freq_s1:
        gcd = gcd_helper(gcd, freq_s1[key])

    # If the GCD is 1, the strings can be made equal
    return gcd == 1


def gcd_helper(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a
    # Recursive case: return the GCD of b and the remainder of a divided by b
    else:
        return gcd_helper(b, a % b)