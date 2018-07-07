
import os
import HidingSystem as hid

#Increment:od  + custom imena korisnika

class file:

    def __init__(self, name_with_extension, path, version_name, user_version_name):
        self.path = path
        self.name_with_extension = name_with_extension
        self.version_name = version_name
        self.user_version_name = user_version_name
        



    def backup(self):
        p = self.path + "\\.backups"

        if not(os.path.isdir(p)):
            os.mkdir(p)
            hid.hide(p)

        p += "\\" + self.name_with_extension[:-3]

        if not(os.path.isdir(p)):
            os.mkdir(p)


        p += "\\" + str(self.version_name)


        if not(os.path.isdir(p)):
            os.mkdir(p)


        p += "\\" + self.name_with_extension

        print(p)

        

        f1 = open(self.path + "\\" + self.name_with_extension, "rb")
        f2 = open(p, "wb")

        file_data = f1.read()

        f2.write(file_data)

        f1.close()
        f2.close()


    def getPath(self):
        return self.path

    



    def get_bytes(self):
        f = open(self.path + "\\" + self.name_with_extension, "rb")
        b = f.read()
        f.close()
        return b


















