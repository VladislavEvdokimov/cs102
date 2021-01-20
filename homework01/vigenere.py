def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for f in range(len(plaintext)):
        l = plaintext[f]
        keyword = keyword.upper()
        shift = ord(keyword[f % len(keyword)]) - ord("A")
        f = 0
        if l.islower():
            ciphertext += chr(ord("a") + ((ord(l) - ord("a") + shift) % 26))
        elif l.isupper():
            ciphertext += chr(ord("A") + ((ord(l) - ord("A") + shift) % 26))
        else:
            ciphertext += l
        f += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for f in range(len(ciphertext)):
        l = ciphertext[f]
        keyword = keyword.upper()
        shift = ord(keyword[f % len(keyword)]) - ord("A")
        f = 0
        if l.islower():
            plaintext += chr(ord("a") + ((ord(l) - ord("a") - shift) % 26))
        elif l.isupper():
            plaintext += chr(ord("A") + ((ord(l) - ord("A") - shift) % 26))
        else:
            plaintext += l
        f += 1
    return plaintext
