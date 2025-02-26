import re
import hashlib, requests
import math

def load_weak_passwords(filename="10-million-password-list-top-1000000.txt"):
    """
    Loads a dictionary of weak passwords from a file.
    If the file is missing, a warning is shown, and an empty set is returned.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return set(line.strip() for line in file)  # Store passwords in a set for fast lookup
    except FileNotFoundError:
        print("Warning: Weak password file not found. Skipping dictionary check.")
        return set()

def is_weak_password(password, weak_passwords):
    """
    Checks if the entered password is in the weak password list.
    Comparison is case insensitive.
    """
    return password.lower() in weak_passwords

def check_password_leaks(password):
    """
    Checks if the password has been leaked in a data breach.
    Uses the Have I Been Pwned API to fetch breach data based on SHA-1 hash.
    Returns breach count if found, otherwise confirms password safety.
    """
    # Hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()

    # Split the hash: First 5 characters (prefix) and remaining part (suffix)
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    # Query the Have I Been Pwned API with the hash prefix
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    response_lines = response.text.splitlines()

    # Check if the suffix is in the response data
    for line in response_lines:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return f"⚠️ Your password has been leaked **{int(count):,} times** in data breaches!"
    
    return "✅ Your password is safe"

def evaluate_password_using_entropy_strength(password):
    """
    Evaluates password strength using entropy.
    Entropy is calculated using: Entropy = L * log2(N),
    where L = password length and N = size of the character set used.
    Returns entropy score and password strength classification.
    """
    L = len(password)  # Password length
    N = 0  # Character set size

    # Determine the number of possible characters used in the password
    if any(c.islower() for c in password):  # If the password contains lowercase letters
        N += 26
    if any(c.isupper() for c in password):  # If the password contains uppercase letters
        N += 26
    if any(c.isdigit() for c in password):  # If the password contains digits
        N += 10
    if any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):  # If the password contains special characters
        N += 32

    # If no valid characters are found, return an invalid password warning
    if N == 0:
        return 0, "❌ Invalid Password (No characters detected)"
    
    # Calculate entropy (higher entropy = stronger password)
    entropy = round(L * math.log2(N), 2)

    # Classify password strength based on entropy value
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
    # Get password input from the user
    password = input("Enter a password to analyze: ")

    # Load weak passwords from file
    weak_passwords = load_weak_passwords()

    # Check if the password is weak (common in dictionary attacks)
    if is_weak_password(password, weak_passwords):
        print("❌ Your password is too common and weak")
    else:
        # Evaluate password entropy strength
        entropy, strength = evaluate_password_using_entropy_strength(password)
        print(f"🔐 Password Entropy: {entropy} bits")
        print(strength)
    
    # Check if the password has been leaked in past data breaches
    print(check_password_leaks(password))
