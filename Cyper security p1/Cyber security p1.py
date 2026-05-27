import string


def check_password_strength(password):
    length = len(password)

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = (
        (length >= 8)
        + has_upper
        + has_lower
        + has_digit
        + has_symbol
    )

    print("\nPassword Analysis:")
    print(f"Characters Used : {length}")
    print(f"Uppercase       : {has_upper}")
    print(f"Lowercase       : {has_lower}")
    print(f"Digits          : {has_digit}")
    print(f"Symbols         : {has_symbol}")

    if length < 8:
        strength = "Weak"

    elif score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    else:
        strength = "Strong"

    print(f"\nPassword Strength : {strength}")

    return strength


def main():
    while True:
        password = input("\nEnter your password: ")

        if password.lower() == "exit":
            print("Program Closed.")
            break

        strength = check_password_strength(password)

        if strength == "Strong":
            print("Excellent password security.")
            break

        print("\nSuggestions:")
        print("- Use at least 8 characters")
        print("- Add uppercase letters")
        print("- Add lowercase letters")
        print("- Add numbers")
        print("- Add symbols")

        print("\n1. Try Again")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "2":
            print("Program Closed.")
            break

        elif choice != "1":
            print("Invalid choice.")


if __name__ == "__main__":
    main()