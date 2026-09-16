"""
Main script demonstrating how to use the Password Generator tool.
Run this file to see password generation in action!
"""

from password_generator import (
    generate_simple_password,
    generate_medium_password,
    generate_strong_password,
    check_password_strength,
    generate_multiple_passwords
)


def print_section(title):
    """Helper function to print formatted section titles."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def main():
    """Main function demonstrating all password generator features."""
    
    print_section("🔐 Password Generator - Beginner Project")
    
    # Example 1: Generate a simple password
    print_section("1. Simple Password (letters + numbers)")
    simple = generate_simple_password(10)
    print(f"Generated: {simple}")
    print(f"Length: {len(simple)}")
    
    # Example 2: Generate a medium password
    print_section("2. Medium Password (letters + numbers + special chars)")
    medium = generate_medium_password(12)
    print(f"Generated: {medium}")
    print(f"Length: {len(medium)}")
    
    # Example 3: Generate a strong password
    print_section("3. Strong Password (all character types guaranteed)")
    strong = generate_strong_password(16)
    print(f"Generated: {strong}")
    print(f"Length: {len(strong)}")
    
    # Example 4: Check password strength
    print_section("4. Check Password Strength")
    test_passwords = ["password", "Pass123", "MySecurePass123!"]
    
    for pwd in test_passwords:
        result = check_password_strength(pwd)
        print(f"\nPassword: {result['password']}")
        print(f"  Length: {result['length']}")
        print(f"  Has uppercase: {result['has_uppercase']}")
        print(f"  Has lowercase: {result['has_lowercase']}")
        print(f"  Has digits: {result['has_digits']}")
        print(f"  Has special chars: {result['has_special_chars']}")
        print(f"  Strength: {result['strength']}")
    
    # Example 5: Generate multiple passwords
    print_section("5. Generate Multiple Passwords at Once")
    
    print("\nSimple passwords (3):")
    simple_list = generate_multiple_passwords(3, 'simple')
    for i, pwd in enumerate(simple_list, 1):
        print(f"  {i}. {pwd}")
    
    print("\nMedium passwords (3):")
    medium_list = generate_multiple_passwords(3, 'medium')
    for i, pwd in enumerate(medium_list, 1):
        print(f"  {i}. {pwd}")
    
    print("\nStrong passwords (3):")
    strong_list = generate_multiple_passwords(3, 'strong')
    for i, pwd in enumerate(strong_list, 1):
        print(f"  {i}. {pwd}")
    
    # Final message
    print_section("✨ Done!")
    print("Try modifying the script to generate passwords with different lengths!")
    print("Change the numbers in generate_simple_password(10) to experiment!\n")


if __name__ == "__main__":
    main()
