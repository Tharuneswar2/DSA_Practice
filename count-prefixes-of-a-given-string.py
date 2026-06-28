def count_prefixes(arr, s):
    # Initialize count variable to store the count of prefixes
    count = 0
    
    # Iterate over each string in the array
    for string in arr:
        # Check if the string starts with the given string 's'
        if string.startswith(s):
            # If it does, increment the count
            count += 1
    
    # Return the count of prefixes
    return count

# Test the function
arr = ["hello", "world", "hell", "helloe", "helloworld"]
s = "hello"
print(count_prefixes(arr, s))  # Output: 3