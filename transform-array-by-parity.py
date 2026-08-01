# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sortArrayByParity(A):
    # Initialize two pointers, one at the start and one at the end of the array
    left, right = 0, len(A) - 1
    
    # Continue the loop until the two pointers meet
    while left < right:
        # If the left element is even, move to the next element
        if A[left] % 2 == 0:
            left += 1
        # If the right element is odd, move to the previous element
        elif A[right] % 2 != 0:
            right -= 1
        # If the left element is odd and the right element is even, swap them
        else:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
            
    # Return the modified array
    return A