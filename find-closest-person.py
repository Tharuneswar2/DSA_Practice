# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_closest_person(people, target_person):
    # Initialize the minimum distance and the closest person
    min_distance = float('inf')  # Initialize with infinity
    closest_person = None

    # Iterate over each person in the list of people
    for person in people:
        # Check if the person is not the target person
        if person != target_person:
            # Calculate the distance between the person and the target person
            distance = abs(person[0] - target_person[0]) + abs(person[1] - target_person[1])
            
            # Check if the distance is less than the current minimum distance
            if distance < min_distance:
                # Update the minimum distance and the closest person
                min_distance = distance
                closest_person = person

    # Return the closest person
    return closest_person

# Example usage:
people = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
target_person = (4, 5)
print(find_closest_person(people, target_person))