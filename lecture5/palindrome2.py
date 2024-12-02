name = "anna"

def is_palindrome(name: str) -> bool: 
    return name == name[::-1]

if __name__ == "__main__":
    if is_palindrome("anna"):
        print(f"anna is a palindrome.")
