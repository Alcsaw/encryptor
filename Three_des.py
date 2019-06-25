from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

BLOCK_SIZE = 8
iv = b'\xbd\xbe"r\xca\x19"\xdd'


def ecb(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_ECB)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES3.new(chave, DES3.MODE_ECB)
        decifra = unpad(decifra.decrypt(msg), BLOCK_SIZE).decode("utf-8")
        return decifra


def cbc(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_CBC, iv)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES3.new(chave, DES3.MODE_CBC, IV=iv)
        decifra = unpad(decifra.decrypt(msg), BLOCK_SIZE).decode("utf-8")
        return decifra

def cfb(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_CFB, iv)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES3.new(chave, DES3.MODE_CFB, IV=iv)
        decifra = unpad(decifra.decrypt(msg), BLOCK_SIZE).decode("utf-8")
        return decifra


def ofb(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_OFB, iv)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES3.new(chave, DES3.MODE_OFB, IV=iv)
        decifra = unpad(decifra.decrypt(msg), BLOCK_SIZE).decode("utf-8")
        return decifra


def ctr(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_CTR, nonce=b'', initial_value=iv)
        msg = cifra.encrypt(msg)
        return msg
    else:
        decifra = DES3.new(chave, DES3.MODE_CTR, nonce=b'', initial_value=iv)
        decifra = unpad(decifra.decrypt(msg), BLOCK_SIZE).decode("utf-8")
        return decifra