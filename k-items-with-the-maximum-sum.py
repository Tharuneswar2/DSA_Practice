# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def kItemsWithMaximumSum(k, a, target):
    # Sort the array in descending order to prioritize larger numbers
    a.sort(reverse=True)
    
    # Initialize a variable to store the sum of the selected items
    total_sum = 0
    
    # Iterate over the sorted array
    for i in range(k):
        # If adding the current item exceeds the target, break the loop
        if total_sum + a[i] > target:
            break
        # Otherwise, add the current item to the total sum
        total_sum += a[i]
    
    # Return the total sum of the selected items
    return total_sum