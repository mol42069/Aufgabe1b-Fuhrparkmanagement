import encrypter

class User:

    def __init__(self, username, password, permission=0):

        self.username = username
        self.permission = permission
        self.encrypter = encrypter.Encrypter()
        self.password = self.encrypter.encrypt(password)

        return

    def check_password(self, pw):
        temp_pw = self.encrypter.decrypt(self.password)
        if pw == temp_pw:
            return True
        else:
            return False

    def change_pw(self, old_pw, new_pw1, new_pw2):

        if self.check_password(old_pw):
            if new_pw1 == new_pw2:
                self.password = self.encrypter.encrypt(new_pw1)
                return True
        else:
            return False

