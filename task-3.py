import re

def assess_password_strength(password):
    # Define strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[^A-Za-z0-9]', password))

    # Calculate strength
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, 
                          number_criteria, special_char_criteria])

    # Strength message
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Return results
    return {
        'length': length_criteria,
        'uppercase': uppercase_criteria,
        'lowercase': lowercase_criteria,
        'numbers': number_criteria,
        'special_characters': special_char_criteria,
        'strength': strength
    }

# Example usage:
password = input("Enter a password to assess: ")
result = assess_password_strength(password)

print("\nPassword Assessment:")
print(f"Length >= 8: {'Yes' if result['length'] else 'No'}")
print(f"Contains Uppercase: {'Yes' if result['uppercase'] else 'No'}")
print(f"Contains Lowercase: {'Yes' if result['lowercase'] else 'No'}")
print(f"Contains Numbers: {'Yes' if result['numbers'] else 'No'}")
print(f"Contains Special Characters: {'Yes' if result['special_characters'] else 'No'}")
print(f"Overall Strength: {result['strength']}")
