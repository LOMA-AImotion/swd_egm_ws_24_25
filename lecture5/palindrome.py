name = "anna"

def is_palindrome(name: str) -> bool: 
    if name == name[::-1]:
        print(f"{name} is a palindrome.")
        return True
    else:
        print(f"{name} is not a palindrome.")
        return False

if __name__ == "__main__":
    is_palindrome("anna")
    is_palindrome("Anna")
    is_palindrome("otto")
    is_palindrome("gnubelebung")