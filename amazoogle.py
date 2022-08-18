import ftpclient

HELP = """help - displays this help page
exit - logs out from the FTP server and exits the terminal
search <searchquery> - searches the files for the search query
download <filename> - downloads the file from the server
"""

if __name__ == "__main__":
    print("Welcome to the Amazoogle FTP client.\nEnter your credentials to get started.")
    ftp_object = ftpclient.FTP_Comms()
    loggedin = False
    while loggedin == False:
        username = input("username: ")
        password = input("password: ")
        #LOGIN TO FTP SERVER AND CHECK IF CORRECT CREDENTIALS ARE PROVIDED
        if ftp_object.login(username, password):
            #LOGIN SUCCESS
            loggedin = True
            print("You are logged in as "+username+". Type 'help' to get help.")
        else:
            #LOGIN FAILURE
            print("Incorrect credentials.")

    while True:
        command = input("amazoogle > ").lower()
        if command == "help":
            print(HELP)
        elif command == "exit":
            #LOGOUT
            ftp_object.logout()
            break
        elif len(command) >= 6 and command[:6] == "search":
            #SEARCH
            if len(command.split(" ")) > 1 and len(command.split(" ")[1]) > 0:
                query = command.split(" ")[1]
                ftp_object.search(query)
            else:
                print("Enter a search query")
        elif len(command) >= 8 and command[:8] == "download":
            #download
            if len(command.split(" ")) > 1 and len(command.split(" ")[1]) > 0:
                query = command.split(" ")[1]
                ftp_object.get_file(query)
            else:
                print("Enter a file name")
        else:
            print("Invalid command, type 'help' for help.")
