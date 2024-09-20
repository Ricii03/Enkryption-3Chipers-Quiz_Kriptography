import numpy as np

class HillCipher:
    def __init__(self, key):
        self.key_matrix = self.create_key_matrix(key)
        self.modulus = 26
        self.key_size = self.key_matrix.shape[0]

        if self.key_size != self.key_matrix.shape[1]:
            raise ValueError("Matriks kunci harus berbentuk persegi")

    def create_key_matrix(self, key):
        """Mengonversi kunci string menjadi matriks kunci."""
        key = key.upper().replace(" ", "")  # Mengubah kunci menjadi huruf kapital dan menghapus spasi
        key_length = len(key)

        # Pastikan ukuran kunci membentuk matriks persegi
        size = int(np.sqrt(key_length))
        if size * size != key_length:
            raise ValueError("Panjang kunci harus berupa kuadrat sempurna (contoh: 4 untuk 2x2, 9 untuk 3x3)")

        key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape(size, size)
        return key_matrix

    def _matrix_mod_inverse(self, matrix, modulus):
        """Menghitung invers dari matriks modulo tertentu."""
        determinant = int(np.round(np.linalg.det(matrix)))  # Menentukan determinan
        
        if determinant == 0:
            raise ValueError("Determinant cannot be zero.")
        
        # Menghitung invers determinan
        determinant_inv = pow(determinant, -1, modulus)
        # Menghitung invers matriks
        matrix_mod_inv = determinant_inv * np.round(np.linalg.inv(matrix)).astype(int) % modulus
        return matrix_mod_inv % modulus

    def encrypt(self, text):
        text = text.upper().replace(" ", "")
        padded_text = text
        
        # Pastikan panjang teks kelipatan dari ukuran kunci
        while len(padded_text) % self.key_size != 0:
            padded_text += 'X'
        
        # Konversi teks ke angka
        text_numeric = np.array([ord(char) - ord('A') for char in padded_text]).reshape(-1, self.key_size)
        
        # Enkripsi
        encrypted_numeric = (text_numeric @ self.key_matrix) % self.modulus
        
        # Mengonversi kembali ke huruf
        encrypted_text = ''.join(chr(num + ord('A')) for num in encrypted_numeric.flatten())
        return encrypted_text

    def decrypt(self, cipher_text):
        # Menghitung invers matriks kunci
        key_matrix_inv = self._matrix_mod_inverse(self.key_matrix, self.modulus)

        # Konversi ciphertext ke angka
        cipher_numeric = np.array([ord(char) - ord('A') for char in cipher_text]).reshape(-1, self.key_size)

        # Dekripsi
        decrypted_numeric = (cipher_numeric @ key_matrix_inv) % self.modulus
        
        # Mengonversi kembali ke huruf
        decrypted_text = ''.join(chr(num + ord('A')) for num in decrypted_numeric.flatten())
        return decrypted_text

# Contoh penggunaan:
if __name__ == "__main__":
    # Kunci dapat berupa string
    key = "GYBNQKURP"  # Contoh kunci untuk matriks 3x3
    
    hill = HillCipher(key)

    text = "HELLO"
    encrypted = hill.encrypt(text)
    print("Encrypted:", encrypted)

    decrypted = hill.decrypt(encrypted)
    print("Decrypted:", decrypted)
