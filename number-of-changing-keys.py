# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def numberOfChangingKeys(keyboard: str, targets: str) -> int:
    # Initialize a set to store the keys that have been pressed
    pressed_keys = set()
    
    # Initialize a variable to store the count of changing keys
    changing_keys = 0
    
    # Iterate over each character in the targets string
    for target in targets:
        # If the target character is not in the pressed_keys set
        if target not in pressed_keys:
            # Add the target character to the pressed_keys set
            pressed_keys.add(target)
            # If the target character is in the keyboard string
            if target in keyboard:
                # Increment the changing_keys count
                changing_keys += 1
                
    # Return the count of changing keys
    return changing_keys