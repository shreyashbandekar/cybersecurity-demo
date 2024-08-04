def caesar_encrypt(plaintext, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_text = ''
    
    for char in plaintext:
        if char.upper() in alphabet:
            new_position = (alphabet.index(char.upper()) + shift) % 26
            if char.isupper():
                encrypted_text += alphabet[new_position]
            else:
                encrypted_text += alphabet[new_position].lower()
        else:
            encrypted_text += char
    
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def main():
    while True:
        operation = input("Would you like to encrypt or decrypt? (e/d): ").lower()
        if operation not in ['e', 'd']:
            print("Invalid operation. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Shift value must be an integer.")
            continue
        
        if operation == 'e':
            result = caesar_encrypt(message, shift)
        else:
            result = caesar_decrypt(message, shift)
        
        print(f"Result: {result}")

        again = input("Do you want to perform another operation? (yes/no): ").lower()
        if again != 'yes':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
