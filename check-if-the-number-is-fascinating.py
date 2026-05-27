def is_fascinating(n):
    # Convert the number to a string to easily access each digit
    str_n = str(n)
    
    # Check if the number has 3 digits
    if len(str_n) != 3:
        return False
    
    # Check if the number contains any zeros
    if '0' in str_n:
        return False
    
    # Check if the number contains any repeating digits
    if len(str_n) != len(set(str_n)):
        return False
    
    # Calculate the product of the number with 2 and 3
    product_2 = n * 2
    product_3 = n * 3
    
    # Convert the products to strings
    str_product_2 = str(product_2)
    str_product_3 = str(product_3)
    
    # Combine the number and its products into a single string
    combined = str_n + str_product_2 + str_product_3
    
    # Check if the combined string contains all digits from 1 to 9
    for i in range(1, 10):
        if str(i) not in combined:
            return False
    
    # If all checks pass, the number is fascinating
    return True

# Test the function
print(is_fascinating(192))  # True
print(is_fascinating(1))    # False