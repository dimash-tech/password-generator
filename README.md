# 🔐 Password Generator

A simple, beginner-friendly Python tool to generate secure passwords of varying complexity levels.

**Perfect for:**
- 🎓 Learning Python basics
- 🔒 Understanding password security
- 🚀 Your first GitHub repository
- 💼 Hackathon projects

## Features

✨ **Three difficulty levels:**
- **Simple** - Letters and numbers only
- **Medium** - Letters, numbers, and special characters
- **Strong** - Guaranteed mix of all character types

🛠️ **Utilities:**
- Generate single passwords
- Generate multiple passwords at once
- Check password strength
- Customizable password length

## Installation

### Prerequisites
- Python 3.6 or higher
- Git

### Clone the repository
```bash
git clone https://github.com/dimash-tech/password-generator.git
cd password-generator
```

No additional dependencies needed! Only uses Python standard library.

## Quick Start

### Run the demo
```bash
python main.py
```

This will show examples of all features in action.

### Use in your code

```python
from password_generator import generate_simple_password, generate_strong_password

# Generate a simple 10-character password
password = generate_simple_password(10)
print(f"Your password: {password}")

# Generate a strong 16-character password
secure_password = generate_strong_password(16)
print(f"Secure password: {secure_password}")
```

## API Reference

### `generate_simple_password(length=8)`
Generates a password with letters and numbers only.

```python
password = generate_simple_password(12)
# Example output: "aB3cD5eF7gH9"
```

### `generate_medium_password(length=12)`
Generates a password with letters, numbers, and special characters.

```python
password = generate_medium_password(14)
# Example output: "aB3!cD5@eF7#gH9"
```

### `generate_strong_password(length=16)`
Generates a strong password with guaranteed mix of uppercase, lowercase, digits, and special characters.

```python
password = generate_strong_password(16)
# Example output: "aB3!Cd5@Ef7#Gh9$"
```

### `check_password_strength(password)`
Analyzes a given password and returns strength analysis.

```python
result = check_password_strength("MyPass123!")
print(result['strength'])  # Output: 'Strong'
print(result['length'])    # Output: 10
```

**Returns a dictionary with:**
- `password` - The password analyzed
- `length` - Password length
- `has_uppercase` - Contains uppercase letters
- `has_lowercase` - Contains lowercase letters
- `has_digits` - Contains numbers
- `has_special_chars` - Contains special characters
- `strength` - Overall strength rating (Weak, Medium, Strong)

### `generate_multiple_passwords(count=5, difficulty='medium')`
Generates multiple passwords at once.

```python
passwords = generate_multiple_passwords(5, 'strong')
# Returns list of 5 strong passwords
```

**Parameters:**
- `count` - Number of passwords to generate
- `difficulty` - 'simple', 'medium', or 'strong'

## File Structure

```
password-generator/
├── password_generator.py   # Main module with all functions
├── main.py                 # Usage examples
├── README.md               # This file
├── LICENSE                 # MIT License
└── .gitignore             # Git ignore rules
```

## Learning Points

This project teaches:

1. **Functions** - How to write reusable functions
2. **Imports** - Using Python's standard library (`random`, `string`)
3. **Parameters** - Function arguments and defaults
4. **Return values** - How functions return data
5. **Data types** - Strings, lists, dictionaries
6. **Loops** - Using list comprehensions
7. **Conditionals** - If/else logic
8. **String methods** - Working with text

## Examples

### Example 1: Generate one password
```python
from password_generator import generate_strong_password

my_password = generate_strong_password()
print(my_password)
```

### Example 2: Check if password is strong
```python
from password_generator import check_password_strength

user_password = input("Enter your password: ")
strength = check_password_strength(user_password)

if strength['strength'] == 'Strong':
    print("✅ Great password!")
else:
    print("❌ Password is too weak")
```

### Example 3: Generate passwords for multiple accounts
```python
from password_generator import generate_multiple_passwords

accounts = ['gmail', 'github', 'twitter']
passwords = generate_multiple_passwords(3, 'strong')

for account, password in zip(accounts, passwords):
    print(f"{account}: {password}")
```

## Tips for Beginners

- 📖 Read the comments in `password_generator.py` to understand each function
- 🧪 Modify `main.py` and run it to see what happens
- 🔍 Use `help()` function: `help(generate_simple_password)`
- 📝 Try creating your own functions based on these examples
- 🚀 Extend the project with your own features!

## Possible Enhancements

Want to practice? Try adding these features:

- [ ] Save generated passwords to a file
- [ ] Add a command-line interface with arguments
- [ ] Create a password strength meter with visual feedback
- [ ] Add password history tracking
- [ ] Create a GUI with tkinter
- [ ] Add pronounceable password generation

## License

MIT License - feel free to use this in your projects!

## Contributing

This is a learning project. Feel free to fork it and make improvements!

## Questions?

- 📖 Check the code comments
- 🐍 Learn more at [python.org](https://www.python.org)
- 💬 Ask questions in GitHub Issues

---

**Happy coding!** 🎉

Made with ❤️ for beginners learning Python
