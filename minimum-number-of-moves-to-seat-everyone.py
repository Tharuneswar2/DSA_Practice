# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minMovesToSeat(seats, students):
    # Sort the seats and students arrays in ascending order
    seats.sort()
    students.sort()
    
    # Initialize a variable to store the total number of moves
    total_moves = 0
    
    # Iterate over the sorted seats and students arrays
    for seat, student in zip(seats, students):
        # For each pair of seat and student, calculate the absolute difference
        # This difference represents the number of moves required to seat the student
        moves = abs(seat - student)
        
        # Add the moves to the total number of moves
        total_moves += moves
    
    # Return the total number of moves
    return total_moves