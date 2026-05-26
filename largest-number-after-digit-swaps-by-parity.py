def largestNumber(nums):
    # Separate the numbers into two lists based on the parity of their digits
    even = []
    odd = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    # Sort the even numbers in descending order
    even.sort(reverse=True)

    # Sort the odd numbers in descending order
    odd.sort(reverse=True)

    # Combine the sorted even and odd numbers
    result = []
    while even and odd:
        if even[0] > odd[0]:
            result.append(even.pop(0))
        else:
            result.append(odd.pop(0))

    # Append any remaining numbers
    result.extend(even)
    result.extend(odd)

    # If the list is empty or the first digit is 0, return 0
    if not result or result[0] == 0:
        return 0

    # Join the numbers into a single string and return
    return int(''.join(map(str, result)))