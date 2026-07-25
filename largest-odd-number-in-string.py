# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def largestOddNumber(num: str) -> str:
    # Start from the end of the string and find the first odd digit
    for i in range(len(num) - 1, -1, -1):
        # Check if the current digit is odd
        if int(num[i]) % 2 != 0:
            # If it's odd, return the substring from the start to the current index + 1
            return num[:i + 1]
    # If no odd digit is found, return an empty string
    return ""