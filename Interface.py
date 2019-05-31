from tkinter import *

from tkinter.ttk import *


# TODO: Passar essas funções para o Main.py
def encrypt():
    # Função para encrypt a mensagem original
    label_key.configure("Encripta mensagem original")


def decrypt():
    # Função para decrypt a mensagem
    label_key.configure("Decripta mensagem criptografada")


def enviar():
    # Função para enviar mensagem criptografada
    label_key.configure("Envia mensagem cufrada")


window = Tk()
window.title("encryptor")
window.geometry('480x790')

label_cipher = Label(window, text="Cifra")
label_cipher.grid(column=0, row=0)

combo_cipher = Combobox(window, width=37)
combo_cipher['values'] = ("Cesar", "Hill", "Vigenère", "Playfair", "One Time Pad", "DES", "3DES - ECB", "3DES - CBC",
                          "3DES - CFB", "3DES - OFB", "3DES - CTR", "AES - ECB", "AES - CBC", "AES - CFB", "AES - OFB",
                          "AES - CTR")
combo_cipher.current(0)  # set the selected item
combo_cipher.grid(column=0, row=1)

label_key_size = Label(window, text="Tamanho da Chave")
label_key_size.grid(column=0, row=2)

combo_key_size = Combobox(window, width=37)
combo_key_size['values'] = ("128", "192", "256")
combo_key_size.current(0)  # set the selected item
combo_key_size.grid(column=0, row=3)

label_key = Label(window, text="Chave")
label_key.grid(column=0, row=4)

entry_key = Entry(window, width=40)
entry_key.grid(column=0, row=5)

label_plaintext_message = Label(window, text="Mensagem em texto plano")
label_plaintext_message.grid(column=0, row=6)

text_plaintext_message = Text(window, width=30, height=10)
text_plaintext_message.grid(column=0, row=7)

button_encrypt = Button(window, text="Encriptar", command=encrypt)
button_encrypt.grid(column=0, row=8)

label_ciphertext_message = Label(window, text="Mensagem Cifrada")
label_ciphertext_message.grid(column=0, row=9)

text_ciphertext_message = Text(window, width=30, height=10)
text_ciphertext_message.grid(column=0, row=10)


button_decrypt = Button(window, text="Decriptar", command=decrypt)
button_decrypt.grid(column=0, row=11)

button_send = Button(window, text="Enviar", command=enviar)
button_send.grid(column=0, row=12)

window.mainloop()
