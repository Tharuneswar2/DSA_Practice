def have_conflict(event1, event2):
    # Unpack the start and end times of the two events
    start1, end1 = event1
    start2, end2 = event2

    # If the start time of the second event is less than the end time of the first event
    # and the start time of the first event is less than the end time of the second event,
    # then the two events have a conflict
    return start1 < end2 and start2 < end1

# Example usage:
event1 = (1, 3)  # Event 1 starts at 1 and ends at 3
event2 = (2, 4)  # Event 2 starts at 2 and ends at 4
print(have_conflict(event1, event2))  # Output: True

event1 = (1, 3)  # Event 1 starts at 1 and ends at 3
event2 = (4, 6)  # Event 2 starts at 4 and ends at 6
print(have_conflict(event1, event2))  # Output: False