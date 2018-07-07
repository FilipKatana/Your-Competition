
import os
import HidingSystem as hid
#import shutil

#Increment:od  + custom imena korisnika

class file:

    def __init__(self, name_with_extension, path, version_name, user_version_name):
        self.path = path
        self.name_with_extension = name_with_extension
        self.version_name = version_name
        self.user_version_name = user_version_name
        



    def getPath(self):
        return self.path

    



    def get_bytes(self):
        f = open(self.path + "\\" + self.name_with_extension, "rb")
        b = f.read()
        f.close()
        return b





def backup(path, file_name, version_name):
    
    
    
    p = path + "\\.backups"

    if not(os.path.isdir(p)):
        os.mkdir(p)
        hid.hide(p)
        
        
     
    if not(os.path.isdir(os.path.join(path, file_name))):
        #r
        p += "\\" + file_name[:-3]


            
    else:
        p = os.path.join(p, file_name)
        
    if not(os.path.isdir(p)):
        os.mkdir(p)
            
    p = os.path.join(p, version_name)


    


    if not(os.path.isdir(p)):
        os.mkdir(p)


    p = os.path.join(p, file_name)

    print(p)

    if os.path.isdir(os.path.join(path, file_name)):
        #Ovde uraditi shutil kopiranje
        print("This option doesnt exist yet.")
        pass
    
    else:
        f1 = open(path + "\\" + file_name, "rb")
        f2 = open(p, "wb")

        file_data = f1.read()

        f2.write(file_data)

        f1.close()
        f2.close()












