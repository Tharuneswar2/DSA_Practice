def max_product_of_two_digits(nums):
    # First, sort the list in descending order to get the largest numbers first
    nums.sort(reverse=True)
    
    # The maximum product will be the product of the first two numbers in the sorted list
    # This is because the product of two numbers is maximized when the numbers are as large as possible
    max_product = nums[0] * nums[1]
    
    return max_product

# Example usage:
numbers = [1, 20, 3, -10, 5]
print(max_product_of_two_digits(numbers))