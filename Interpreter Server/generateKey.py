from lib.Encryption import Encrypter


if __name__ == '__main__':
    Encryption = Encrypter("Sample")
    Keyfile = open("key.key", 'w')
    Keyfile.write(str(Encryption.generateKey()))
    Keyfile.close()
