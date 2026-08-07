# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def distanceBetweenBusStops(distance, start, destination):
    # Calculate the total distance of the circular route
    total_distance = sum(distance)
    
    # Calculate the distance from start to destination in the clockwise direction
    clockwise_distance = sum(distance[min(start, destination):max(start, destination)])
    
    # Calculate the distance from start to destination in the counter-clockwise direction
    counter_clockwise_distance = total_distance - clockwise_distance
    
    # Return the minimum distance between the two directions
    return min(clockwise_distance, counter_clockwise_distance)