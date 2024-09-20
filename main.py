import tkinter as tk
from tkinter import filedialog, messagebox
from VigenereCipher.vigenere import VigenereCipher
from PlayfairCipher.playfair import PlayfairCipher
from HillCipher.hill import HillCipher

import tkinter as tk
from tkinter import ttk

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher Program")

        # Create frames
        self.input_frame = ttk.Frame(root)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)

        self.key_frame = ttk.Frame(root)
        self.key_frame.grid(row=1, column=0, padx=10, pady=10)

        self.button_frame = ttk.Frame(root)
        self.button_frame.grid(row=2, column=0, padx=10, pady=10)

        # Input text frame
        self.label_input = ttk.Label(self.input_frame, text="Masukkan teks:")
        self.label_input.grid(row=0, column=0, padx=5, pady=5)

        self.text_input = tk.Text(self.input_frame, height=10, width=50)
        self.text_input.grid(row=1, column=0, padx=5, pady=5)

        # Key input frame
        self.label_key = ttk.Label(self.key_frame, text="Masukkan kunci (min 12 karakter):")
        self.label_key.grid(row=0, column=0, padx=5, pady=5)

        self.key_input = tk.Entry(self.key_frame, width=50)
        self.key_input.grid(row=1, column=0, padx=5, pady=5)

        # Button frame
        self.button_encrypt_vigenere = ttk.Button(self.button_frame, text="Enkripsi Vigenere", command=self.encrypt_vigenere)
        self.button_encrypt_vigenere.grid(row=0, column=0, padx=5, pady=5)

        self.button_decrypt_vigenere = ttk.Button(self.button_frame, text="Dekripsi Vigenere", command=self.decrypt_vigenere)
        self.button_decrypt_vigenere.grid(row=0, column=1, padx=5, pady=5)

        # Add more buttons and frames as needed
        self.button_encrypt_playfair = ttk.Button(self.button_frame, text="Enkripsi Playfair", command=self.encrypt_playfair)
        self.button_encrypt_playfair.grid(row=1, column=0, padx=5, pady=5)

        self.button_decrypt_playfair = ttk.Button(self.button_frame, text="Dekripsi Playfair", command=self.decrypt_playfair)
        self.button_decrypt_playfair.grid(row=1, column=1, padx=5, pady=5)

        self.button_encrypt_hill = ttk.Button(self.button_frame, text="Enkripsi Hill", command=self.encrypt_hill)
        self.button_encrypt_hill.grid(row=2, column=0, padx=5, pady=5)

        self.button_decrypt_hill = ttk.Button(self.button_frame, text="Dekripsi Hill", command=self.decrypt_hill)
        self.button_decrypt_hill.grid(row=2, column=1, padx=5, pady=5)

        # Use a more modern GUI theme
        self.root.style = ttk.Style()
        self.root.style.theme_use("clam")

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        with open(file_path, "r") as file:
            self.text_input.insert(tk.END, file.read())

    def encrypt_vigenere(self):
        key = self.key_input.get()
        text = self.text_input.get("1.0", tk.END).strip()
        
        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter")
            return
        
        cipher = VigenereCipher(key)
        encrypted_text = cipher.encrypt(text.upper())
        self.text_input.delete("1.0", tk.END)
        self.text_input.insert(tk.END, encrypted_text)

    def decrypt_vigenere(self):
        key = self.key_input.get()
        cipher_text = self.text_input.get("1.0", tk.END).strip()
        
        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter")
            return

        cipher = VigenereCipher(key)
        decrypted_text = cipher.decrypt(cipher_text.upper())
        self.text_input.delete("1.0", tk.END)
        self.text_input.insert(tk.END, decrypted_text)

    def encrypt_playfair(self):
        key = self.key_input.get()
        text = self.text_input.get("1.0", tk.END).strip()
        
        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter")
            return
        
        cipher = PlayfairCipher(key)
        encrypted_text = cipher.encrypt(text.upper())
        self.text_input.delete("1.0", tk.END)
        self.text_input.insert(tk.END, encrypted_text)

    def decrypt_playfair(self):
        key = self.key_input.get()
        cipher_text = self.text_input.get("1.0", tk.END).strip()
        
        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter")
            return

        cipher = PlayfairCipher(key)
        decrypted_text = cipher.decrypt(cipher_text.upper())
        self.text_input.delete("1.0", tk.END)
        self.text_input.insert(tk.END, decrypted_text)

    def encrypt_hill(self):
        key_input = self.key_input.get().split(",")  # Mengharapkan kunci dalam format yang sesuai
        try:
            key = [[int(num) for num in row.split()] for row in key_input]
            hill_cipher = HillCipher(key)
            text = self.text_input.get("1.0", tk.END).strip()

            encrypted_text = hill_cipher.encrypt(text.upper())
            self.text_input.delete("1.0", tk.END)
            self.text_input.insert(tk.END, encrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def decrypt_hill(self):
        key_input = self.key_input.get().split(",")  # Mengharapkan kunci dalam format yang sesuai
        try:
            key = [[int(num) for num in row.split()] for row in key_input]
            hill_cipher = HillCipher(key)
            cipher_text = self.text_input.get("1.0", tk.END).strip()

            decrypted_text = hill_cipher.decrypt(cipher_text.upper())
            self.text_input.delete("1.0", tk.END)
            self.text_input.insert(tk.END, decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()