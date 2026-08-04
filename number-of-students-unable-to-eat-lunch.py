# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countStudents(students, sandwiches):
    # Initialize counters for students who prefer 0 and 1 type of sandwiches
    students_0 = students.count(0)
    students_1 = len(students) - students_0
    
    # Iterate over the sandwiches
    for sandwich in sandwiches:
        # If there are no students who prefer the current type of sandwich, break the loop
        if (sandwich == 0 and students_0 == 0) or (sandwich == 1 and students_1 == 0):
            break
        # Decrement the counter for the current type of sandwich
        if sandwich == 0:
            students_0 -= 1
        else:
            students_1 -= 1
    
    # Return the total number of students who are unable to eat lunch
    return students_0 + students_1