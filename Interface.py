from tkinter import *
from tkinter.ttk import *
import Caesar_cipher
import One_time_pad
'''
import des
import Three_des
import AES
'''
import Playfair_cipher
import Vigenère_cipher
import Hill_cipher


# TODO: Passar essas funções para o Main.py
def encrypt():
    # Função para encrypt a mensagem original

    text_ciphertext_message.selection_clear()

    if combo_cipher.get() == "Cesar":
        original_message = text_plaintext_message.get("1.0", END)
        key = int(entry_key.get())
        crypted_message = Caesar_cipher.caesar_cipher(original_message, key)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "Hill":
        original_message = text_plaintext_message.get("1.0", END)
        key = entry_key.get()
        crypted_message = Hill_cipher.encrypt(original_message, key)
        text_ciphertext_message.insert(window.END, crypted_message)

    elif combo_cipher.get() == "Vigenère":
        original_message = text_plaintext_message.get("1.0", END)
        key = entry_key.get()
        crypted_message = Vigenère_cipher.encrypt(original_message, key)
        text_ciphertext_message.insert(window.END, crypted_message)

    elif combo_cipher.get() == "Playfair":
        original_message = text_plaintext_message.get("1.0", END)
        key = entry_key.get()
        crypted_message = Playfair_cipher.encrypt(original_message, key)
        text_ciphertext_message.insert(window.END, crypted_message)

    elif combo_cipher.get() == "One Time Pad":
        original_message = text_plaintext_message.get("1.0", END)
        crypted_message = One_time_pad.encrypt(original_message)
        text_ciphertext_message.insert(window.END, crypted_message)
'''
    elif combo_cipher.get() == "DES - ECB":
        text_ciphertext_message.insert(0, des.ecb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "DES - CBC":
        text_ciphertext_message.insert(0, des.cbc(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "DES - CFB":
        text_ciphertext_message.insert(0, des.cfb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "DES - OFB":
        text_ciphertext_message.insert(0, des.ofb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "DES - CTR":
        text_ciphertext_message.insert(0, des.ctr(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "3DES - ECB":
        text_ciphertext_message.insert(0, Three_des.ecb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "3DES - CBC":
        text_ciphertext_message.insert(0, Three_des.cbc(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "3DES - CFB":
        text_ciphertext_message.insert(0, Three_des.cfb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "3DES - OFB":
        text_ciphertext_message.insert(0, Three_des.ofb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "3DES - CTR":
        text_ciphertext_message.insert(0, Three_des.ctr(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "AES - ECB":
        text_ciphertext_message.insert(0, AES.ecb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "AES - CBC":
        text_ciphertext_message.insert(0, AES.cbc(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "AES - CFB":
        text_ciphertext_message.insert(0, AES.cfb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "AES - OFB":
        text_ciphertext_message.insert(0, AES.ofb(entry_key.get(), text_plaintext_message.get(), 1))

    elif combo_cipher.get() == "AES - CTR":
        text_ciphertext_message.insert(0, AES.ctr(entry_key.get(), text_plaintext_message.get(), 1))
'''
def decrypt():
    # Função para decrypt a mensagem
    text_plaintext_message.selection_clear()

    if combo_cipher.get() == "Cesar":
        crypted_message = text_ciphertext_message.get("1.0", END)
        key = int(entry_key.get()) * -1
        original_message = Caesar_cipher.caesar_cipher(crypted_message, key)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "Hill":
        crypted_message = text_ciphertext_message.get("1.0", END)
        key = entry_key.get()
        original_message = Hill_cipher.decrypt(crypted_message, key)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "Vigenère":
        crypted_message = text_ciphertext_message.get("1.0", END)
        key = entry_key.get()
        original_message = Vigenère_cipher.decrypt(crypted_message, key)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "Playfair":
        crypted_message = text_ciphertext_message.get("1.0", END)
        key = entry_key.get()
        original_message = Playfair_cipher.decrypt(crypted_message, key)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "One Time Pad":
        crypted_message = text_ciphertext_message.get("1.0", END)
        original_message = One_time_pad.decrypt(crypted_message)
        text_plaintext_message.insert(END, original_message)
    '''
    elif combo_cipher.get() == "DES - ECB":
        text_plaintext_message.insert(0, des.ecb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "DES - CBC":
        text_plaintext_message.insert(0, des.cbc(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "DES - CFB":
        text_plaintext_message.insert(0, des.cfb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "DES - OFB":
        text_plaintext_message.insert(0, des.ofb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "DES - CTR":
        text_plaintext_message.insert(0, des.ctr(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "3DES - ECB":
        text_plaintext_message.insert(0, Three_des.ecb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "3DES - CBC":
        text_plaintext_message.insert(0, Three_des.cbc(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "3DES - CFB":
        text_plaintext_message.insert(0, Three_des.cfb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "3DES - OFB":
        text_plaintext_message.insert(0, Three_des.ofb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "3DES - CTR":
        text_plaintext_message.insert(0, Three_des.ctr(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "AES - ECB":
        text_plaintext_message.insert(0, AES.ecb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "AES - CBC":
        text_plaintext_message.insert(0, AES.cbc(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "AES - CFB":
        text_plaintext_message.insert(0, AES.cfb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "AES - OFB":
        text_plaintext_message.insert(0, AES.ofb(entry_key.get(), text_ciphertext_message.get(), 0))

    elif combo_cipher.get() == "AES - CTR":
        text_plaintext_message.insert(0, AES.ctr(entry_key.get(), text_ciphertext_message.get(), 0))
'''

def enviar():
    # Função para enviar mensagem criptografada
    label_key.configure("Envia mensagem cufrada")


window = Tk()
window.title("encryptor")
window.geometry('480x790')

label_cipher = Label(window, text="Cifra")
label_cipher.grid(column=0, row=0)

combo_cipher = Combobox(window, width=37)
combo_cipher['values'] = ("Cesar", "Hill", "Vigenère", "Playfair", "One Time Pad", "DES - ECB",
                          "DES - CBC", "DES - CFB", "DES - OFB", "DES - CTR","3DES - ECB", "3DES - CBC",
                          "3DES - CFB", "3DES - OFB", "3DES - CTR", "AES - ECB", "AES - CBC", "AES - CFB",
                          "AES - OFB", "AES - CTR")
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
