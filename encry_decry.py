def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Non-alphabetical characters remain unchanged
            result += char
    return result

def main():
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for shift.")
    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Defaulting to encrypt.")
        mode = 'encrypt'
    output = caesar_cipher(message, shift, mode)
    print(f"Result: {output}")

if __name__ == "__main__":
    main()