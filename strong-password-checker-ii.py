def strongPasswordCheckerII(password: str) -> bool:
    # Check if password length is at least 8
    if len(password) < 8:
        return False

    # Initialize flags for different conditions
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    # Iterate over the password
    for i in range(len(password)):
        # Check for lowercase letter
        if password[i].islower():
            has_lower = True
        # Check for uppercase letter
        elif password[i].isupper():
            has_upper = True
        # Check for digit
        elif password[i].isdigit():
            has_digit = True
        # Check for special character
        elif not password[i].isalnum():
            has_special = True

        # Check for repeating characters
        if i > 0 and password[i] == password[i-1]:
            return False

    # Return True if all conditions are met
    return has_lower and has_upper and has_digit and has_special