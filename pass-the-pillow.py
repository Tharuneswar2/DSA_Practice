# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def passThePillow(n, m):
    # Calculate the remainder of m divided by n to find the position of the pillow after m seconds
    # If the remainder is 0, the pillow will be at the first position
    remainder = m % n
    # If the remainder is 0, return n, otherwise return the remainder
    return n if remainder == 0 else remainder

def main():
    # Read the number of test cases
    t = int(input())
    # Iterate over each test case
    for _ in range(t):
        # Read the number of people and the number of seconds
        n, m = map(int, input().split())
        # Call the function to calculate the position of the pillow
        result = passThePillow(n, m)
        # Print the result
        print(result)

if __name__ == "__main__":
    main()