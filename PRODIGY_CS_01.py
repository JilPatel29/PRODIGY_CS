def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the ASCII offset based on uppercase or lowercase
            offset = 65 if char.isupper() else 97
            
            # Calculate the shifted position
            if mode == 'encrypt':
                new_position = (ord(char) - offset + shift) % 26
            else:  # decrypt
                new_position = (ord(char) - offset - shift) % 26
            
            # Convert back to character and add to result
            result += chr(new_position + offset)
        else:
            result += char
    return result

def main():
    while True:
        
        mode = input("Enter 'encrypt' or 'decrypt' (or 'quit' to exit): ").lower()
        if mode == 'quit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please try again.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (1-25): "))
        
        if not 1 <= shift <= 25:
            print("Shift value must be between 1 and 25. Please try again.")
            continue
        
        # Process the message and display result
        result = caesar_cipher(message, shift, mode)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()