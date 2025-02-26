import re
import hashlib, requests

def check_password_leaks(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if suffix in response.text:
        return "Your password has been leaked in data breach!"
    return "Your password is safe"

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
    print(check_password_leaks(password))