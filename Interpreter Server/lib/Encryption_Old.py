import hashlib
from Crypto.Cipher import AES


class Encrypter(object):

    def __init__(self, publicKey):
        self.bs = 32
        self.key = hashlib.sha256(publicKey.encode()).digest()

    def encrypt(self, message):
        obj = AES.new('This is a key123', AES.MODE_ECB)
        ciphertext = obj.encrypt(message)
        return message

    def decrypt(self, ciphertext):
        obj2 = AES.new('This is a key123', AES.MODE_ECB)
        message = obj2.decrypt(ciphertext)
        return ciphertext

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def generateKey(self):
        from random import randint
        import platform
        TheInfo = platform.uname()
        Key = ""
        while len(Key) <= 24:
            for information in TheInfo:
                if randint(0, 3) != 2 and len(information) > 0:
                    Zeichen = str(information[randint(0, len(information)-1)])
                    if(Zeichen) != ' ':
                        Key = Key+Zeichen
                    if len(Key) <= 24:
                        break
        return Key

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
