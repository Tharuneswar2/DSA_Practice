def longestNiceSubstring(s: str) -> str:
    def is_nice(substring):
        # Check if a substring is nice
        for char in substring:
            if char.isupper():
                if char.lower() not in substring:
                    return False
            else:
                if char.upper() not in substring:
                    return False
        return True

    def backtrack(start, path):
        # Backtrack to find the longest nice substring
        if is_nice(path):
            nonlocal res
            if len(path) > len(res):
                res = path
        for end in range(start + 1, len(s) + 1):
            backtrack(end, path + s[end - 1])

    res = ""
    for i in range(len(s)):
        backtrack(i + 1, s[i])
    return res