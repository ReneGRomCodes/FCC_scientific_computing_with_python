# Learning string manipulation by building a cypher:
# In this project, you'll learn fundamental programming concepts in Python, such as variables, functions, loops, and
# conditional statements. You'll use these to code your first programs.


text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'


def vigenere(message, key, direction=1):
    """Vigenere encryption for text 'message' using 'key'. 'direction=1' encrypts, 'direction=-1' decrypts."""
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    """Encrypts 'message' using 'key'."""
    return vigenere(message, key)


def decrypt(message, key):
    """Encrypts 'message' using 'key'."""
    return vigenere(message, key, -1)


print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
