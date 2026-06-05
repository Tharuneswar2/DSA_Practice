def decode(self, encoded: List[int], first: int) -> List[int]:
    # Initialize the result array with the first element
    result = [first]
    
    # Iterate over the encoded array
    for i in range(len(encoded)):
        # XOR the current element in the result array with the current element in the encoded array
        # This is based on the property of XOR that a ^ a = 0 and a ^ 0 = a
        # So, if we XOR the current element with the previous element, we get the original element
        result.append(result[-1] ^ encoded[i])
    
    # Return the result array
    return result