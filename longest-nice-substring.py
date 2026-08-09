# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def longestNiceSubstring(s):
    def is_nice(substring):
        # Check if the substring is nice by verifying that for each character, 
        # its lowercase and uppercase versions are both present in the substring
        return all(lower in substring and upper in substring 
                   for lower, upper in zip('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    def dfs(start, path):
        # Perform a depth-first search to find the longest nice substring
        if is_nice(path):
            # If the current path is nice, return it
            return path
        for i in range(start, len(s)):
            # Recursively explore all possible substrings
            result = dfs(i + 1, path + s[i])
            if result:
                # If a nice substring is found, return it
                return result
        return ''

    return dfs(0, '')