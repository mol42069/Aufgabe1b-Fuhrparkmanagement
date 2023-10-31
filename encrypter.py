from cryptography.fernet import Fernet


class Encrypter:

    def __init__(self):
        self.key = b'OPkCyGBuh2mhUE2jCqLxPE_H-VXL0vd06lNWFAaJFMc='
        self.fernet = Fernet(self.key)

    def encrypt(self, password):
        enc_message = self.fernet.encrypt(password.encode())
        return enc_message

    def decrypt(self, password):

        dec_message = self.fernet.decrypt(password).decode()

        return dec_message