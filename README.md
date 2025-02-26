# 🔐 Password Analyzer  

## 📌 Overview  
**Password Analyzer** is a Python-based tool that evaluates password strength using **entropy calculation**, **dictionary-based weak password detection**, and **data breach checks** using the **Have I Been Pwned API**.  

### ✨ Features  
👉 **Entropy-Based Strength Evaluation** – Calculates password entropy and classifies security levels.  
👉 **Weak Password Detection** – Checks if the password is commonly used (from a dictionary file).  
👉 **Data Breach Check** – Uses the Have I Been Pwned API to detect if the password has been leaked and shows **breach count**.  

---

## 🛠️ How It Works  
1. **Checks if the password is weak** by comparing it against a dictionary of common passwords.  
2. **Calculates password entropy** based on its length and character variety.  
3. **Checks for data breaches** using the **Have I Been Pwned API** and reports the number of breaches (if any).  

---

## 🚀 Installation  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/your-username/password-analyzer.git
cd password-analyzer
```

### 2️⃣ **Install Dependencies**  
This project requires **Python 3.x** and the `requests` library. Install it using:  
```bash
pip install requests
```

### 3️⃣ **Download the Weak Password List**  
For **weak password detection**, download a common password list like:  
📚 [Top 10 million passwords dataset](https://github.com/danielmiessler/SecLists)  

Save it as:  
```plaintext
10-million-password-list-top-1000000.txt
```
Place the file in the **same directory** as the script.

---

## 🏋️ Usage  
Run the script using:  
```bash
python password_analyzer.py
```

**Example Input:**  
```plaintext
Enter a password to analyze: password123
```

**Example Output:**  
```plaintext
🔐 Password Entropy: 37.6 bits
⚠️ Weak Password (Guessable)
⚠️ Your password has been leaked 4,521,678 times in data breaches!
```

---

## 🔢 How Password Strength is Measured  

| **Entropy (bits)** | **Strength** |
|--------------------|-------------|
| < 28             | ❌ Very Weak (Easily Cracked) |
| 28 - 35          | ⚠️ Weak (Guessable) |
| 36 - 59          | ✅ Moderate (Decent Security) |
| ≥ 60            | 🔒 Strong (Difficult to Crack) |

👉 **Higher entropy means a stronger password!**  

---

## 🔍 How Breach Detection Works  
- Uses **SHA-1 hashing** to protect the password while checking for breaches.  
- Queries the **Have I Been Pwned API** with the **first 5 characters** of the SHA-1 hash.  
- If found, it displays how many times the password has been leaked.  

---

## 🛡️ Security Notes  
- This tool **does NOT store passwords** or send them over the internet.  
- Only the **SHA-1 hash prefix** is sent to the API for security.  

---

**⚠️ Disclaimer:** This project is intended for **educational purposes only**. The author is **not responsible** for any misuse of this tool. Always follow ethical security practices.  

