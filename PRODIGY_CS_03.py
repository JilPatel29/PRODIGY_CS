import re                                                                                                                                                                                                                           

def assess_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length!")
    else:
        score += 1

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters for a stronger password.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters for a stronger password.")

    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers for a stronger password.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters for a stronger password.")

    # Check strength
    if score < 2:
        strength = "Very Weak"
    elif score < 3:
        strength = "Weak"
    elif score < 4:
        strength = "Moderate"
    elif score < 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback

def main():
    while True:
        password = input("Enter a password to check its strength (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break

        strength, feedback = assess_password_strength(password)

        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions for improvement:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("Excellent password!")
        print()

if __name__ == "__main__":
    main()

