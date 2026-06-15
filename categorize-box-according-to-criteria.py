def categorizeBox(length, width, height, mass) -> str:
    # Check if the box is bulky
    isBulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or length * width * height >= 10**9

    # Check if the box is heavy
    isHeavy = mass >= 100

    # Check if the box is large
    isLarge = length >= 20 or width >= 20 or height >= 20 or length + width + height >= 70

    # Categorize the box based on the criteria
    if isHeavy and isBulky:
        return "Both"
    elif isHeavy and isLarge:
        return "Heavy"
    elif isBulky and isLarge:
        return "Bulky"
    elif isHeavy or isBulky or isLarge:
        return "Neither"
    else:
        return "Neither"

# Test the function
print(categorizeBox(10000, 1, 1, 1))  # Bulky
print(categorizeBox(1, 1, 1, 100))  # Heavy
print(categorizeBox(20, 20, 20, 1))  # Large
print(categorizeBox(10000, 20, 20, 100))  # Both