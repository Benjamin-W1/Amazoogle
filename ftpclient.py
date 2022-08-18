from ftplib import FTP

class FTP_Comms:
    ftp = None

    # Login. Return true iff successful.
    def login(self, username, password):
        try:
            self.ftp = FTP("127.0.0.1", username, password)
            return True
        except ftplib.error_perm:
            self.ftp = None
            return False


    def get_file(self, name):
        # https://stackoverflow.com/questions/11573817/how-to-download-a-file-via-ftp-with-python-ftplib
        self.ftp.retrbinary("RETR " + filename ,open(name, 'wb').write)


    def logout(self):
        self.ftp.quit()
