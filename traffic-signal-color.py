def traffic_light_color(color):
    # Define a dictionary to map traffic light colors to their corresponding durations
    traffic_light_durations = {
        'red': 5,
        'yellow': 2,
        'green': 10
    }

    # Check if the input color is valid
    if color not in traffic_light_durations:
        return "Invalid color"

    # Return the duration of the given traffic light color
    return traffic_light_durations[color]

# Test the function
print(traffic_light_color('red'))  # Output: 5
print(traffic_light_color('yellow'))  # Output: 2
print(traffic_light_color('green'))  # Output: 10
print(traffic_light_color('blue'))  # Output: Invalid color