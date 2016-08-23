
class Encrypter(object):

    def __init__(self, publicKey):
        pass
    def encrypt(self, message):
        return message
    def decrypt(self, ciphertext):
        return ciphertext
    def generateKey(self):
        from random import randint
        import platform
        TheInfo=platform.uname()
        Key=""
        i=0
        while len(Key)<=24:
            for information in TheInfo:
                if randint(0,3)!=2 and len(information)>0:
                    Zeichen=str(information[randint(0,len(information)-1)])
                    if(Zeichen)!=' ':
                        Key=Key+Zeichen
                    if len(Key)<=24:
                        break
        return Key



