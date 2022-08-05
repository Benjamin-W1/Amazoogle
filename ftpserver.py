import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = DummyAuthorizer()

    authorizer.add_user('user', '12345', '.', perm='elradfmwMT')  # Add user with full permissions.
    authorizer.add_anonymous(os.getcwd())  # Anonymous user with read-only privileges

    # FTP handler
    handler = FTPHandler
    handler.authorizer = authorizer

    
    handler.banner = "pyftpdlib based ftp ready."

    # Set up server to listen on any IP address at port 2121
    address=('',2121)
    server= FTPServer(address, handler)

    # Limit connections to 1
    server.max_cons = 1
    server.max_cons_per_ip = 1

    server.serve_forever()

if __name__ == "__main__":
    main()
