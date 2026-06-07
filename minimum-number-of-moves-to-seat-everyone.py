def minMovesToSeat(seats, students):
    # Sort the seats and students arrays
    seats.sort()
    students.sort()
    
    # Initialize the total moves to 0
    total_moves = 0
    
    # Iterate over the seats and students
    for seat, student in zip(seats, students):
        # Calculate the absolute difference between the current seat and student
        # This represents the number of moves required to seat the current student
        moves = abs(seat - student)
        
        # Add the moves to the total moves
        total_moves += moves
    
    # Return the total moves
    return total_moves