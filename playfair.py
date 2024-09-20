class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.matrix = self.create_matrix()

    def create_matrix(self):
        # Membuat matriks 5x5 berdasarkan kunci
        key = "".join(sorted(set(self.key), key=self.key.index))  # Menghilangkan duplikasi
        key = key.replace('J', 'I')  # Menggabungkan I dan J
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Tanpa J
        for char in key:
            alphabet = alphabet.replace(char, "")
        matrix_string = key + alphabet
        matrix = [matrix_string[i:i + 5] for i in range(0, len(matrix_string), 5)]
        return matrix

    def prepare_text(self, text):
        text = text.upper().replace("J", "I")
        prepared_text = []
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i + 1]
                if a == b:
                    prepared_text.append(a + 'X')
                    i += 1
                else:
                    prepared_text.append(a + b)
                    i += 2
            else:
                prepared_text.append(a + 'X')
                i += 1
        return prepared_text

    def find_position(self, char):
        for row in range(5):
            for col in range(5):
                if self.matrix[row][col] == char:
                    return row, col
        return None

    def encrypt(self, text):
        prepared_text = self.prepare_text(text)
        cipher_text = ""

        for pair in prepared_text:
            row1, col1 = self.find_position(pair[0])
            row2, col2 = self.find_position(pair[1])

            if row1 == row2:  # Same row
                cipher_text += self.matrix[row1][(col1 + 1) % 5]
                cipher_text += self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Same column
                cipher_text += self.matrix[(row1 + 1) % 5][col1]
                cipher_text += self.matrix[(row2 + 1) % 5][col2]
            else:  # Rectangle
                cipher_text += self.matrix[row1][col2]
                cipher_text += self.matrix[row2][col1]

        return cipher_text

    def decrypt(self, cipher_text):
        prepared_text = self.prepare_text(cipher_text)
        plain_text = ""

        for pair in prepared_text:
            row1, col1 = self.find_position(pair[0])
            row2, col2 = self.find_position(pair[1])

            if row1 == row2:  # Same row
                plain_text += self.matrix[row1][(col1 - 1) % 5]
                plain_text += self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Same column
                plain_text += self.matrix[(row1 - 1) % 5][col1]
                plain_text += self.matrix[(row2 - 1) % 5][col2]
            else:  # Rectangle
                plain_text += self.matrix[row1][col2]
                plain_text += self.matrix[row2][col1]

        return plain_text.replace('X', '')  # Menghapus huruf X yang ditambahkan