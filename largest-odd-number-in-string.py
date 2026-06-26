def largestOddNumber(num: str) -> str:
    # Start from the end of the string and check each character
    for i in range(len(num) - 1, -1, -1):
        # If the current character is an odd digit, return the substring from the start to this index + 1
        if int(num[i]) % 2 != 0:
            return num[:i + 1]
    # If no odd digit is found, return an empty string
    return ""