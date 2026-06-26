def countStudents(students, sandwiches):
    # Initialize counters for students with different sandwich preferences
    ones = students.count(1)
    zeros = students.count(0)

    # Iterate over the sandwiches
    for sandwich in sandwiches:
        # If there are no students with the current sandwich preference, break the loop
        if (sandwich == 1 and ones == 0) or (sandwich == 0 and zeros == 0):
            break
        # Decrement the counter for the current sandwich preference
        if sandwich == 1:
            ones -= 1
        else:
            zeros -= 1

    # Return the total number of students who cannot eat lunch
    return ones + zeros