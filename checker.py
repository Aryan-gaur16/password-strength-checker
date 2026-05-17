import re

def check_password_strength(password):
    # start with a score of 0
    score = 0
    feedback = []

    # checks the length of the password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Please make sure that the password is at least 8 characters long")

    # checks for uppercase letters in password
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Please add at least one uppercase letter")

    # checks for lowercase letters in password
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Please add at least one lowercase letter")

    # check for numbers in the password
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Please add at least one number to your password")

    # check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    # decide the strength based on score
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "password": password,
        "score": score,
        "strength": strength,
        "feedback": feedback
    }