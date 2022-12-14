import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions
    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "FTP server ready, client connected."

    # Instantiate FTP server class and listen on 0.0.0.0:21
    address = ('', 21)
    server = FTPServer(address, handler)

    # Limit to one connection at a time.
    server.max_cons = 1
    server.max_cons_per_ip = 1

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()
