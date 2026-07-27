# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    # Define a dictionary to map ruleKey to its corresponding index in the items list
    ruleKeyMap = {"type": 0, "color": 1, "name": 2}
    
    # Initialize a counter variable to store the count of items matching the rule
    count = 0
    
    # Iterate over each item in the items list
    for item in items:
        # Check if the value at the index corresponding to ruleKey matches the ruleValue
        if item[ruleKeyMap[ruleKey]] == ruleValue:
            # If it matches, increment the counter
            count += 1
    
    # Return the count of items matching the rule
    return count