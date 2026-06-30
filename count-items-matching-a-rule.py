def countMatches(items, ruleKey, ruleValue):
    # Define a dictionary to map rule keys to their corresponding indices
    rule_dict = {"type": 0, "color": 1, "name": 2}
    
    # Initialize a counter to store the count of items matching the rule
    count = 0
    
    # Iterate over each item in the list
    for item in items:
        # Check if the item at the index corresponding to the rule key matches the rule value
        if item[rule_dict[ruleKey]] == ruleValue:
            # If it matches, increment the counter
            count += 1
    
    # Return the count of items matching the rule
    return count