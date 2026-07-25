# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def categorizeBox(length, width, height, mass):
    # Check if the box is heavy (mass > 10000)
    isHeavy = mass > 10000
    
    # Check if the box is bulky (length, width, height > 10000 or volume > 1000000000)
    isBulky = length > 10000 or width > 10000 or height > 10000 or length * width * height > 1000000000
    
    # Check if the box is both heavy and bulky
    if isHeavy and isBulky:
        return "Both"
    
    # Check if the box is heavy but not bulky
    elif isHeavy:
        return "Heavy"
    
    # Check if the box is bulky but not heavy
    elif isBulky:
        return "Bulky"
    
    # If the box is neither heavy nor bulky
    else:
        return "Neither"