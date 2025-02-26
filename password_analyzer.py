import re

def check_password_strength(password):
    score = 0
    criteria = {
        "length" : len(password) >= 8,
        "upercase" : bool(re.search(r"[A-Z]", password)),
        "lowercase" : bool(re.search(r"[a-z]", password)),
        "digit" : bool(re.search(r"\d", password)),
        "special_char" : bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    score = sum(criteria.values())
    if score == 5:
        return "Strong Password"
    elif score >= 3:
        return "Medium Password"
    else:
        return "Weak Password"

if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    print(check_password_strength(password))