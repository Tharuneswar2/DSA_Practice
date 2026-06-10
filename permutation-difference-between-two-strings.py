def checkInclusion(s1: str, s2: str) -> bool:
    # If s1 is longer than s2, it's impossible for s1 to be a substring of s2
    if len(s1) > len(s2):
        return False

    # Create a hashmap to store the frequency of characters in s1
    s1_count = {}
    for char in s1:
        if char in s1_count:
            s1_count[char] += 1
        else:
            s1_count[char] = 1

    # Initialize a hashmap to store the frequency of characters in the current window of s2
    s2_count = {}
    for i in range(len(s2)):
        # Add the current character to the window
        if s2[i] in s2_count:
            s2_count[s2[i]] += 1
        else:
            s2_count[s2[i]] = 1

        # If the window size is larger than s1, remove the leftmost character
        if i >= len(s1):
            s2_count[s2[i - len(s1)]] -= 1
            if s2_count[s2[i - len(s1)]] == 0:
                del s2_count[s2[i - len(s1)]]

        # If the window size is equal to s1, check if the frequency of characters matches
        if i >= len(s1) - 1:
            if s1_count == s2_count:
                return True

    # If no match is found, return False
    return False