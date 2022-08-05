from ftplib import FTP

"""
ftp = FTP("127.0.0.1", 'user', '12345')

ftp.dir()  # This lists the files as with list -- so can prettify the names


# I am advised by SO that this will fetch a file
# https://stackoverflow.com/questions/11573817/how-to-download-a-file-via-ftp-with-python-ftplib
A = filename
ftp = ftplib.FTP("IP")
ftp.login("USR Name", "Pass")
ftp.cwd("/Dir")
try:
    ftp.retrbinary("RETR " + filename ,open(A, 'wb').write)
except:
    print "Error"
"""

ftp = FTP("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")
ftp.encoding = "utf-8"

# local file name you want to upload
filename = "examplefile700.txt"
with open(filename, "wb") as file:
    # use FTP's RETR command to download the file
    ftp.retrbinary(f"RETR {filename}", file.write)
