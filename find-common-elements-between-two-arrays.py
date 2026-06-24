def find_common_elements(arr1, arr2):
    # Convert the input lists to sets for efficient lookup
    set1 = set(arr1)
    set2 = set(arr2)

    # Use set intersection to find common elements
    common_elements = set1.intersection(set2)

    # Convert the set of common elements back to a list and return it
    return list(common_elements)

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print(find_common_elements(arr1, arr2))  # Output: [4, 5]

def find_common_elements_without_set(arr1, arr2):
    # Initialize an empty list to store common elements
    common_elements = []

    # Iterate over the first array
    for element in arr1:
        # Check if the current element exists in the second array
        if element in arr2: