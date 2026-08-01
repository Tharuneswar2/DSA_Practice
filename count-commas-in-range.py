# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countCommasInRange(text, start, end):
    # Initialize a counter variable to store the count of commas
    comma_count = 0
    
    # Check if the start index is less than or equal to the end index
    if start <= end:
        # Iterate over the substring from the start index to the end index
        for char in text[start:end+1]:
            # Check if the character is a comma
            if char == ',':
                # If the character is a comma, increment the comma count
                comma_count += 1
                
    # Return the count of commas
    return comma_count