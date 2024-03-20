#Caesar Cipher Algorithm Based: 

def is_uppercase(char):
    return 'A' <= char <= 'Z'

def is_lowercase(char):
    return 'a' <= char <= 'z'

def caesar_cipher(message, shift, encrypt=True):
    result_message = ""
    if encrypt:
        for char in message:
            if is_uppercase(char):
                result_message += chr((ord(char) - 65 + shift) % 26 + 65)
            elif is_lowercase(char):
                result_message += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                # Keep non-alphabetic characters unchanged
                result_message += char
                
    else:  # Decryption
        for char in message:
            if is_uppercase(char):
                result_message += chr((ord(char) - 65 - shift) % 26 + 65)
            elif is_lowercase(char):
                result_message += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                # Keep non-alphabetic characters unchanged
                result_message += char

    return result_message

def main():
    operation = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if operation == "encrypt":
        encrypted_message = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted_message)
    elif operation == "decrypt":
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
