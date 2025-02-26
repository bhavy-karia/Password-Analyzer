import re
import hashlib, requests

def load_weak_passwords(filename="10-million-password-list-top-1000000.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print("Warning: Weak password file not found. Skipping dictionary check.")
        return set()

def is_weak_password(password, weak_passwords):
    return password.lower() in weak_passwords

def check_password_leaks(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if suffix in response.text:
        return "⚠️ Your password has been leaked in data breach!"
    return "✅ Your password is safe"

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
        return "✅ Strong Password"
    elif score >= 3:
        return "⚠️ Medium Password"
    else:
        return "❌ Weak Password"

if __name__ == "__main__":
    password = input("Enter a password to analyze: ")

    weak_passwords = load_weak_passwords()
    if is_weak_password(password, weak_passwords):
        print("❌ Your password is too common and weak")
    else:
        print(check_password_strength(password))
    
    print(check_password_leaks(password))