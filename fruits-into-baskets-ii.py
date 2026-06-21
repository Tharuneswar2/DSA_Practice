def totalFruit(fruits):
    # Initialize variables to keep track of the maximum number of fruits and the current window
    max_fruits = 0
    window_start = 0
    fruit_frequency = {}

    # Iterate over the list of fruits
    for window_end in range(len(fruits)):
        # Add the current fruit to the frequency dictionary
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        # Shrink the window if there are more than two types of fruits
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1

        # Update the maximum number of fruits
        max_fruits = max(max_fruits, window_end - window_start + 1)

    return max_fruits