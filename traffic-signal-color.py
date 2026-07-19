# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def traffic_light_color(n):
    # Define the colors of the traffic light in the order they appear
    colors = ["red", "green", "yellow"]
    
    # Calculate the index of the color based on the input number
    # We use the modulus operator to ensure the index is within the bounds of the list
    index = (n - 1) % len(colors)
    
    # Return the color at the calculated index
    return colors[index]

# Test the function
print(traffic_light_color(1))  # red
print(traffic_light_color(2))  # green
print(traffic_light_color(3))  # yellow
print(traffic_light_color(4))  # red
print(traffic_light_color(5))  # green