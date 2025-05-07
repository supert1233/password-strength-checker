import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @#$%^&+=!]", password) is None

    if length_error or digit_error or uppercase_error or lowercase_error or symbol_error:
        print("Weak Password ❌")
    else:
        print("Strong Password ✅")

# Example usage
pwd = input("Enter a password to check: ")
check_password_strength(pwd)
