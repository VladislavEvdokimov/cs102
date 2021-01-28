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
        h = ord(n)
        if ord("a") <= h <= ord("z") or ord("A") <= h <= ord("Z"):
            if ord("z") - shift < h <= ord("z"):
                h -= 26
            elif ord("Z") - shift < h <= ord("Z"):
                h -= 26
            h += shift
            ciphertext += chr(h)
        else:
            ciphertext += chr(h)
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
        h = ord(n)
        if ord("a") <= h <= ord("z") or ord("A") <= h <= ord("Z"):
            if ord("a") <= h < ord("a") + shift:
                h += 26
            elif ord("A") <= h < ord("A") + shift:
                h += 26
            h -= shift
            plaintext += chr(h)
        else:
            plaintext += chr(h)
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
