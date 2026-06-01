import math

def distance(person1, person2):
    # Calculate the Euclidean distance between two people
    return math.sqrt((person1[0] - person2[0])**2 + (person1[1] - person2[1])**2)

def find_closest_person(person, people):
    # Initialize the minimum distance and the closest person
    min_distance = float('inf')
    closest_person = None

    # Iterate over all people
    for p in people:
        # Skip the person itself
        if p == person:
            continue

        # Calculate the distance between the person and the current person
        dist = distance(person, p)

        # Update the minimum distance and the closest person if necessary
        if dist < min_distance:
            min_distance = dist
            closest_person = p

    return closest_person

# Example usage:
people = [(1, 2), (3, 4), (5, 6), (7, 8)]
person = (1, 2)
closest = find_closest_person(person, people)
print(closest)