def countTime(time: str) -> int:
    # Initialize count of valid times
    count = 0
    
    # Check for HH:MM format
    if len(time) == 5:
        # Extract hours and minutes
        hours, minutes = time.split(':')
        
        # Check for ? in hours
        if '?' in hours:
            # If ? is in the first position, it can be any number from 0 to 2
            if hours[0] == '?':
                # If the second digit is not ?, it must be less than or equal to 3 if the first digit is 2, otherwise it can be any digit
                if hours[1] != '?':
                    if hours[1] <= '3':
                        count += 3 if hours[1] == '2' else 24
                else:
                    # If the second digit is ?, it can be any digit from 0 to 9 if the first digit is not 2, otherwise it can be 0, 1, 2, or 3
                    count += 24 * 4 if hours[0] != '2' else 24
            # If ? is in the second position, the first digit must be less than or equal to 2
            else:
                # If the first digit is 2, the second digit can be 0, 1, 2, or 3
                if hours[0] == '2':
                    count += 4
                # If the first digit is not 2, the second digit can be any digit from 0 to 9
                else:
                    count += 10
        # Check for ? in minutes
        if '?' in minutes:
            # If ? is in the first or second position, it can be any digit from 0 to 5 for the first digit and 0 to 9 for the second digit
            count *= 6 if minutes[0] == '?' else 10
        # If there are no ? in the time, it is a valid time
        else:
            count = 1
    # Return the count of valid times
    return count