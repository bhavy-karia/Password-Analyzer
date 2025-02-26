import re
import hashlib, requests
import math

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

def evaluate_password_using_entropy_strength(password):
    L = len(password)
    N = 0

    if any(c.islower() for c in password):
        N += 26
    if any(c.isupper() for c in password):
        N += 26
    if any(c.isdigit() for c in password):
        N += 10
    if any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
        N +=32
    if N == 0:
        return 0, "❌ Invalid Password (No characters detected)"
    
    entropy = round(L * math.log2(N), 2)

    if entropy < 28:
        strength = "❌ Very Weak Password (Easily Cracked)"
    elif entropy < 36:
        strength = "⚠️ Weak Password (Guessable)"
    elif entropy < 60:
        strength = "✅ Moderate Password (Decent Security)"
    else:
        strength = "🔒 Strong Password (Difficult to Crack)"
    
    return entropy, strength

if __name__ == "__main__":
    password = input("Enter a password to analyze: ")

    weak_passwords = load_weak_passwords()
    if is_weak_password(password, weak_passwords):
        print("❌ Your password is too common and weak")
    else:
        entropy, strength = evaluate_password_using_entropy_strength(password)
        print(f"🔐 Password Entropy {entropy} bits")
        print(strength)
    
    print(check_password_leaks(password))