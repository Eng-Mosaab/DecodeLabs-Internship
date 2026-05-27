def encrypt(text, shift):
    encrypted_text = ""

    for char in text:

        if char.isalpha():

            ascii_value = ord(char)

            if char.isupper():
                encrypted_char = chr((ascii_value - 65 + shift) % 26 + 65)

            else:
                encrypted_char = chr((ascii_value - 97 + shift) % 26 + 97)

            encrypted_text += encrypted_char

        else:
            encrypted_text += char

    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""

    for char in text:

        if char.isalpha():

            ascii_value = ord(char)

            if char.isupper():
                decrypted_char = chr((ascii_value - 65 - shift) % 26 + 65)

            else:
                decrypted_char = chr((ascii_value - 97 - shift) % 26 + 97)

            decrypted_text += decrypted_char

        else:
            decrypted_text += char

    return decrypted_text


def main():

    while True:

        print("\n===== Caesar Cipher Menu =====")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            text = input("Enter text to encrypt: ")

            try:
                shift = int(input("Enter shift value: "))

                encrypted = encrypt(text, shift)

                print("\nEncrypted Text:", encrypted)

            except ValueError:
                print("Invalid shift value.")

        elif choice == "2":

            text = input("Enter text to decrypt: ")

            try:
                shift = int(input("Enter shift value: "))

                decrypted = decrypt(text, shift)

                print("\nDecrypted Text:", decrypted)

            except ValueError:
                print("Invalid shift value.")

        elif choice == "3":
            print("Program Closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()