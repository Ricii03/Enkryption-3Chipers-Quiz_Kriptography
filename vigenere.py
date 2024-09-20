import string

class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def generate_key(self, text):
        key = list(self.key)
        if len(text) == len(key):
            return key
        else:
            for i in range(len(text) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)

    def encrypt(self, text):
        key = self.generate_key(text)
        cipher_text = []
        for i in range(len(text)):
            x = (ord(text[i]) + ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return "".join(cipher_text)

    def decrypt(self, cipher_text):
        key = self.generate_key(cipher_text)
        orig_text = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return "".join(orig_text)
