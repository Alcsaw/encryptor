#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import tkinter.ttk as ttk

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

master_key = ""

def encrypt():

    label_alert.configure(text="")

    if entry_key.get() != "":
        if combo_cipher.get() == "Cesar":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            if entry_key.get().isdigit():
                key = int(entry_key.get())
                crypted_message = Caesar_cipher.caesar_cipher(original_message, key)
                entry_field.delete(0, 1000)
                entry_field.insert(0, crypted_message)
            else:
                label_alert.configure(text="Escreva a penas números no campo Chave");

        elif combo_cipher.get() == "Hill":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = Hill_cipher.make_key(entry_key.get())
            crypted_message = Hill_cipher.encrypt(original_message, key)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "Vigenère":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = Vigenère_cipher.encrypt(original_message, key)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "Playfair":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = Playfair_cipher.encrypt(original_message, key)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        if combo_cipher.get() == "One Time Pad":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            crypted_message, key = One_time_pad.encrypt(original_message)
            global master_key
            master_key = ''.join(key)
            entry_field.delete(0, 1000)
            entry_key.delete(0, 1000)
            entry_field.insert(0, crypted_message)
            entry_key.insert(0, master_key)

        '''
        elif combo_cipher.get() == "DES - ECB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = des.ecb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "DES - CBC":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = des.cbc(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "DES - CFB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = des.cfb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "DES - OFB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = des.ofb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "DES - CTR":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = des.ctr(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "3DES - ECB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = Three_des.ecb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "3DES - CBC":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = Three_des.cbc(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "3DES - CFB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = Three_des.cfb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "3DES - OFB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = Three_des.ofb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "3DES - CTR":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = Three_des.ctr(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "AES - ECB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = AES.ecb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "AES - CBC":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = AES.cbc(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "AES - CFB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = AES.cfb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "AES - OFB":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = AES.ofb(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)

        elif combo_cipher.get() == "AES - CTR":
            original_message = entry_field.get()
            original_message = original_message.replace("\n", "")
            key = entry_key.get()
            crypted_message = AES.ctr(key, original_message, 1)
            entry_field.delete(0, 1000)
            entry_field.insert(0, crypted_message)
        '''
    else:
        label_alert.configure(text="Preencha o campo chave")


def decrypt():

    label_alert.configure(text="")
    if entry_key.get() != "":
        if combo_cipher.get() == "Cesar":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            if entry_key.get().isdigit():
                key = int(entry_key.get()) * -1
                original_message = Caesar_cipher.caesar_cipher(crypted_message, key)
                entry_field.delete(0, 1000)
                entry_field.insert(0, original_message)
            else:
                label_alert.configure(text="Escreva a penas números no campo Chave")

        elif combo_cipher.get() == "Hill":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = Hill_cipher.make_key(entry_key.get())
            original_message = Hill_cipher.decrypt(crypted_message, key)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "Vigenère":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = Vigenère_cipher.decrypt(crypted_message, key)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "Playfair":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = Playfair_cipher.decrypt(crypted_message, key)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "One Time Pad":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            global master_key
            original_message = One_time_pad.decrypt(crypted_message, master_key)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)
        '''
        elif combo_cipher.get() == "DES - ECB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = des.ecb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "DES - CBC":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = des.cbc(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "DES - CFB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = des.cfb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "DES - OFB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = des.ofb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "DES - CTR":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = des.ctr(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "3DES - ECB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = Three_des.ecb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "3DES - CBC":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = Three_des.cbc(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "3DES - CFB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = Three_des.cfb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "3DES - OFB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = Three_des.ofb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "3DES - CTR":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = Three_des.ctr(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "AES - ECB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = AES.ecb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "AES - CBC":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = AES.cbc(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "AES - CFB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = AES.cfb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "AES - OFB":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = AES.ofb(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)

        elif combo_cipher.get() == "AES - CTR":
            crypted_message = entry_field.get()
            crypted_message = crypted_message.replace("\n", "")
            key = entry_key.get()
            original_message = AES.ctr(key, crypted_message, 0)
            entry_field.delete(0, 1000)
            entry_field.insert(0, original_message)
        '''
    else:
        label_alert.configure(text="Preencha o campo chave")


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


top = tkinter.Tk()
top.title("Encryptor Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your name")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=20, width=70, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg, width=70)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Enviar", command=send)
send_button.pack()

row = tkinter.Frame(top)
row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)

# Start Crypt place
label_cipher = tkinter.Label(top, text="Cifra", width=50)
label_cipher.pack()

combo_cipher = ttk.Combobox(top, values=("Cesar", "Hill", "Vigenère", "Playfair", "One Time Pad", "DES - ECB",
                          "DES - CBC", "DES - CFB", "DES - OFB", "DES - CTR","3DES - ECB", "3DES - CBC",
                          "3DES - CFB", "3DES - OFB", "3DES - CTR", "AES - ECB", "AES - CBC", "AES - CFB",
                          "AES - OFB", "AES - CTR"), width=50)
combo_cipher.set("Cesar")  # set the selected item
combo_cipher.pack()

label_key_size = tkinter.Label(top, text="Tamanho da Chave", width=50)
label_key_size.pack()

combo_key_size = ttk.Combobox(top, values=("128", "192", "256"), width=50)
combo_key_size.set("128")  # set the selected item
combo_key_size.pack()

label_key = tkinter.Label(top, text="Chave", width=50)
label_key.pack()

entry_key = tkinter.Entry(top, width=52)
entry_key.pack()

row = tkinter.Frame(top)
row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)

button_encrypt = tkinter.Button(top, text="Encriptar", command=encrypt)
button_encrypt.pack()

row = tkinter.Frame(top)
row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)

button_decrypt = tkinter.Button(top, text="Decriptar", command=decrypt)
button_decrypt.pack()

label_alert = tkinter.Label(top, text="", fg="red")
label_alert.pack()

row = tkinter.Frame(top)
row.pack(side=tkinter.TOP, fill=tkinter.X, padx=5, pady=5)

# End Crypt place

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = "127.0.0.1"      # input('Enter host: ')
PORT = "33000"           # input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
