"""
Password Generator Module
A simple tool to generate secure passwords of different complexity levels.
Perfect for beginners learning Python!
"""

import random
import string


def generate_simple_password(length=8):
    """
    Generate a simple password with letters and numbers only.
    
    Args:
        length (int): Length of the password. Default is 8.
    
    Returns:
        str: A simple password containing letters and numbers.
    
    Example:
        >>> password = generate_simple_password(10)
        >>> len(password)
        10
    """
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_medium_password(length=12):
    """
    Generate a medium difficulty password with letters, numbers, and special characters.
    
    Args:
        length (int): Length of the password. Default is 12.
    
    Returns:
        str: A medium difficulty password.
    
    Example:
        >>> password = generate_medium_password(12)
        >>> len(password)
        12
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_strong_password(length=16):
    """
    Generate a strong password ensuring it contains uppercase, lowercase, 
    numbers, and special characters.
    
    Args:
        length (int): Length of the password. Default is 16.
    
    Returns:
        str: A strong password with mixed character types.
    
    Example:
        >>> password = generate_strong_password(16)
        >>> len(password)
        16
    """
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure at least one character from each set
    password_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest with random characters from all sets
    all_characters = uppercase + lowercase + digits + special
    password_chars += [random.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password_chars)
    
    password = ''.join(password_chars)
    return password


def check_password_strength(password):
    """
    Check and analyze the strength of a given password.
    
    Args:
        password (str): The password to check.
    
    Returns:
        dict: A dictionary with strength analysis.
    
    Example:
        >>> result = check_password_strength("MyPass123!")
        >>> result['strength']
        'Strong'
    """
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    length = len(password)
    
    # Count criteria met
    criteria_met = sum([has_uppercase, has_lowercase, has_digits, has_special])
    
    # Determine strength
    if length < 8:
        strength = "Weak"
    elif criteria_met == 4 and length >= 12:
        strength = "Strong"
    elif criteria_met >= 3 and length >= 10:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {
        'password': password,
        'length': length,
        'has_uppercase': has_uppercase,
        'has_lowercase': has_lowercase,
        'has_digits': has_digits,
        'has_special_chars': has_special,
        'strength': strength
    }


def generate_multiple_passwords(count=5, difficulty='medium'):
    """
    Generate multiple passwords at once.
    
    Args:
        count (int): Number of passwords to generate. Default is 5.
        difficulty (str): Level of difficulty: 'simple', 'medium', or 'strong'.
    
    Returns:
        list: List of generated passwords.
    
    Example:
        >>> passwords = generate_multiple_passwords(3, 'strong')
        >>> len(passwords)
        3
    """
    passwords = []
    
    if difficulty == 'simple':
        passwords = [generate_simple_password() for _ in range(count)]
    elif difficulty == 'medium':
        passwords = [generate_medium_password() for _ in range(count)]
    elif difficulty == 'strong':
        passwords = [generate_strong_password() for _ in range(count)]
    else:
        raise ValueError("Difficulty must be 'simple', 'medium', or 'strong'")
    
    return passwords
