def is_substring(s, t):
    # Concatenate the string with itself to handle edge cases
    temp = s + s
    
    # Check if the substring t exists in the concatenated string
    if t in temp:
        return True
    else:
        return False

def is_substring_reverse(s, t):
    # Reverse the substring t
    t_rev = t[::-1]
    
    # Check if the reversed substring exists in the original string
    if t_rev in s:
        return True
    else:
        return False

def check_substring(s, t):
    # Check if the substring t exists in the string s
    if t in s:
        return True
    else:
        return False

def main():
    s = input("Enter the main string: ")
    t = input("Enter the substring: ")
    
    if check_substring(s, t):
        print("Substring exists in the string.")
    else:
        print("Substring does not exist in the string.")
        
    if is_substring(s, t):
        print("Substring exists in the string or its rotation.")
    else:
        print("Substring does not exist in the string or its rotation.")
        
    if is_substring_reverse(s, t):
        print("Reversed substring exists in the string.")
    else:
        print("Reversed substring does not exist in the string.")

if __name__ == "__main__":
    main()