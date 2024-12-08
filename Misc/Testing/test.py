def Cencrypt(pt, key):
    # Ensure key is between 1 and 26
    if not 1 <= key <= 26:
        print("Key must be between 10 and 26.")
        return
    
    # Filter out non-alphabetic characters
    pt = ''.join(filter(str.isalpha, pt)).upper()
    
    Ctransform('encrypt', pt, key)


def Cdecrypt(ct, key):
    # Ensure key is between 1 and 26
    if not 0 <= key <= 26:
        print("Key must be between 0 and 26.")
        return
    
    # Filter out non-alphabetic characters
    ct = ''.join(filter(str.isalpha, ct)).upper()

    if key == 0:
        print("Entering brute force mode...")
        for i in range(1, 26):
            Ctransform('decrypt', ct, i)
    else:
        Ctransform('decrypt', ct, key)


def Ctransform(mode, text, key):
    # Determine the shift direction based on the mode
    shift = key if mode == 'encrypt' else -key

    # Shift each letter by the key
    transformed_text = ''.join(chr((ord(c) - ord('A') + shift) % 26 + ord('A')) for c in text)

    # Print the result based on the mode
    if mode == 'encrypt':
        print("Ciphertext:", transformed_text)
    else:
        print("Plaintext:", transformed_text)



def Tencrypt(pt, key):
    # Ensure key is between 1 and len(pt)
    if not 1 <= key <= len(pt):
        print("Key must be between 1 and the length of the plaintext.")
        return

    # Filter out non-alphabetic characters and convert to uppercase
    pt = ''.join(filter(str.isalpha, pt)).upper()
    print("pt: ", pt)
    return Ttransform('encrypt', pt, key)


def Tdecrypt(ct, key):
    # Ensure key is valid or perform brute-force if key is 0
    if key == 0:
        brute_force(ct)
        return
    elif not 1 <= key <= len(ct):
        print("Key must be between 1 and the length of the ciphertext.")
        return

    # Filter out non-alphabetic characters and convert to uppercase
    ct = ''.join(filter(str.isalpha, ct)).upper()
    return Ttransform('decrypt', ct, key)


def Ttransform(mode, text, key):
    num_cols = key
    num_rows = len(text) // num_cols
    if len(text) % num_cols:
        num_rows += 1

    grid = [''] * num_cols

    if mode == 'encrypt':
        # Add padding (if necessary) to make the text fit the grid
        padding = (num_rows * num_cols) - len(text)
        text += 'X' * padding

        for row in range(num_rows):
            for col in range(num_cols):
                idx = row * num_cols + col
                if idx < len(text):
                    grid[col] += text[idx]

        # Print the encrypted result
        print("Ciphertext: " + ''.join(grid))
    
    elif mode == 'decrypt':
        col_length = len(text) // key
        if len(text) % key:
            col_length += 1
        
        # Split the text into columns for decryption
        plain_grid = [''] * num_rows
        k = 0
        
        for col in range(num_cols):
            for row in range(num_rows):
                if k < len(text):
                    plain_grid[row] += text[k]
                    k += 1

        # Join the rows back
        decrypted_text = ''.join(plain_grid)

        # When in 'decrypt' mode and you use the correct key, strip padding 'X'
        if mode == 'decrypt':
            decrypted_text = decrypted_text.rstrip('X')

        return decrypted_text



def brute_force(ciphertext):
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    max_key = len(ciphertext) // 2

    for key in range(1, max_key + 1):
        print(f"\nTrying key = {key}")
        plaintext = Ttransform('decrypt', ciphertext, key)
        print(f"Plaintext: {plaintext}")



def cipher_main(encrypt_func, decrypt_func):
    while True:
        print()
        print(f"Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
        choice = input("Choice: ").lower()

        if choice == 'e':
            pt = input("Enter plaintext: ")
            key = int(input("Enter key: "))
            encrypt_func(pt, key)
        elif choice == 'd':
            ct = input("Enter ciphertext: ")
            key = int(input("Enter key (enter '0' if you want use brute force to decrypt): "))
            decrypt_func(ct, key)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("Enter 'c' for Caesar cipher, 't' for Transposition cipher, or 'q' to quit.")
        choice = input("Choice: ").lower()

        if choice == 'c':
            cipher_main(Cencrypt, Cdecrypt)
        elif choice == 't':
            cipher_main(Tencrypt, Tdecrypt)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
