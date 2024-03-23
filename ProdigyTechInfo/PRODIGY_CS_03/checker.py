def is_uppercase(char):
    return 'A' <= char <= 'Z'

def is_lowercase(char):
    return 'a' <= char <= 'z'

def is_digit(char):
    return '0' <= char <= '9'

def has_uppercase(password):
    for char in password:
        if is_uppercase(char):
            return True
    return False

def has_lowercase(password):
    for char in password:
        if is_lowercase(char):
            return True
    return False

def has_digit(password):
    for char in password:
        if is_digit(char):
            return True
    return False

def has_special_character(password):
    special_characters = "!@#$%^&*()_+{}:\"<>?|[];',./\\"
    for char in password:
        if char in special_characters:
            return True
    return False

def assess_password_strength(password):
    length = len(password)
    score = 0

    # Check length
    if length < 8:
        return "Very Weak"
    elif length < 12:
        score += 1
    elif length < 16:
        score += 2
    else:
        score += 3

    # Check for uppercase letters
    if has_uppercase(password):
        score += 1

    # Check for lowercase letters
    if has_lowercase(password):
        score += 1

    # Check for numbers
    if has_digit(password):
        score += 1

    # Check for special characters
    if has_special_character(password):
        score += 1

    # Evaluate score
    if score < 3:
        return "Weak"
    elif score < 5:
        return "Moderate"
    elif score < 7:
        return "Strong"
    else:
        return "Very Strong"

password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Your password strength is:", strength)

