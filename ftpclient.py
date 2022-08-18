from ftplib import FTP
from re import L
from this import d
import fileValidation
import archiver_tool
import os

class FTP_Comms:
    ftp = None

    # Login. Return true iff successful.
    def login(self, username, password):
        try:
            self.ftp = FTP("127.0.0.1", username, password)
            return True
        except:
            self.ftp = None
            return False
        
    # Search for files containing keyword. Returns a list of all such filenames.
    def search(self, keyword):
        x = self.ftp.nlst()
        listToReturn = []
        for i in x:
            if keyword in i:
                listToReturn.append(i)
        return listToReturn


    # Download file with the given name. Throw error if no such file exists.
    def get_file(self, name):
        # https://stackoverflow.com/questions/11573817/how-to-download-a-file-via-ftp-with-python-ftplib
        self.ftp.retrbinary("RETR " + name ,open(name, 'wb').write)
        resp = fileValidation.validateFile(name)
        if resp == True:
            archiver_tool.store_file(name)
            return True
        else:
            os.remove(name)
            return False
        


    # Logout.
    def logout(self):
        self.ftp.quit()
