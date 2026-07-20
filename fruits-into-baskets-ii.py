# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def totalFruit(fruits):
    # Initialize variables to keep track of the maximum length and the current window's start position
    max_length = 0
    window_start = 0
    
    # Create a dictionary to store the frequency of each fruit type in the current window
    fruit_freq = {}
    
    # Iterate over the fruits list
    for window_end in range(len(fruits)):
        # Add the current fruit to the frequency dictionary
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1
        
        # Shrink the window from the left if there are more than 2 types of fruits
        while len(fruit_freq) > 2:
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -= 1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            window_start += 1
        
        # Update the maximum length
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length