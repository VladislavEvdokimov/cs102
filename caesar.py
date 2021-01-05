import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    text = list(plaintext)
    for n in text:
        n = ord(n)
        if ord('a') <= n <= ord('z') or ord('A') <= n <= ord('Z'):
            if ord('z') - shift < n <= ord('z'):
                n -= 26
            elif ord('Z') - shift < n <= ord('Z'):
                n -= 26
            n += shift
            ciphertext += chr(n)
        else:
            ciphertext += chr(n)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    text = list(ciphertext)
    for n in text:
        n = ord(n)
        if ord('a') <= n <= ord('z') or ord('A') <= n <= ord('Z'):
            if ord('a') <= n < ord('a') + shift:
                n += 26
            elif ord('A') <= n < ord('A') + shift:
                n += 26
            n -= shift
            plaintext += chr(n)
        else:
            plaintext += chr(n)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    text = list(ciphertext.lower())
    for n in dictionary:
        alph = list(n)
        cip1 = ord(text[0]) - ord(alph[0])
        cip2 = ord(text[1]) - ord(alph[1])
        if cip1 < 0:
            cip1 += 26
        if cip2 < 0:
            cip2 += 26
        if cip1 == cip2:
            best_shift = cip1
    return best_shift
