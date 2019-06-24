from Crypto.Cipher import DES
# from Crypto.Util.Padding import pad, unpad    # IDK Y, but this isn't comming with my Pycrypto installation
from Padding import pad, unpad

BLOCK_SIZE = 8
iv = b'\xbd\xbe"r\xca\x19"\xdd'


def ecb(chave, msg, op):
    if op == 1:
        cifra = DES.new(chave, DES.MODE_ECB)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES.new(chave, DES.MODE_ECB)
        print(f'\nMensagem decifrada: {unpad(decifra.decrypt(msg), BLOCK_SIZE).decode("utf-8")}')
        return decifra


def cbc(chave, msg, op):
    if op == 1:
        cifra = DES.new(chave, DES.MODE_CBC, iv)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES.new(chave, DES.MODE_CBC, IV=iv)
        return decifra


def cfb(chave, msg, op):
    if op == 1:
        cifra = DES.new(chave, DES.MODE_CFB, iv)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES.new(chave, DES.MODE_CFB, IV=iv)
        return decifra


def ofb(chave, msg, op):
    if op == 1:
        cifra = DES.new(chave, DES.MODE_OFB, iv)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES.new(chave, DES.MODE_OFB, IV=iv)
        return decifra

def ctr(chave, msg, op):
    if op == 1:
        cifra = DES.new(chave, DES.MODE_CTR, nonce=b'', initial_value=iv)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES.new(chave, DES.MODE_CTR, nonce=b'', initial_value=iv)
        return decifra