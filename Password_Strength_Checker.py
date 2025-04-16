import re
import time
import sys

def splash_screen():
    print("======================================")
    print("   Welcome to Password Strength App   ")
    print("        Developed by Khalid           ")
    print("======================================")
    print("> Loading", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print("\n")

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Length (8+ chars)": not length_error,
        "Lowercase letter": not lowercase_error,
        "Uppercase letter": not uppercase_error,
        "Number": not digit_error,
        "Special character": not special_char_error
    }

    score = sum(errors.values())

    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, errors

def main():
    splash_screen()
    print("> Password Complexity Checker")
    password = input(">> Enter your password: ")

    strength, criteria = check_password_strength(password)

    print(f"\n>> Password Strength: {strength}")
    print(">> Criteria Check:")
    for criterion, passed in criteria.items():
        status = "✔️" if passed else "❌"
        print(f"   {status} {criterion}")

    print("\n> Developed by Khalid")

if __name__ == "__main__":
    main()