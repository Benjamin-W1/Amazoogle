# Example of pysimplegui

import PySimpleGUI as sg
from RequestMake import *
from RequestsSend import *

def loginScreen(message=''):
    """Display login screen to the user and accept inputs via GUI."""
    # Layout of the screen:
    layout = [
        [sg.Text("LOGIN", justification="center")],
        [sg.Text("Library Number"), sg.InputText()],
        [sg.Text("Password"), sg.InputText(password_char="*")],
        [sg.Submit()],
        [sg.Text(message)]
        ]
    # Display the window
    window = sg.Window("Login").Layout(layout)
    button, values = window.Read()
    window.close()
    # Send the login request
    result = sendLogin(values)
    if result[0]:
        """Login successful - assign variables to local variables and
           visit the main menu."""
        setLibCardNo(int(values[0]))
        setAuthCode(result[1][0])
        displayMenu()
    else:
        """Login has failed."""
        loginScreen(message="Your library card number or password was incorrect.")

def menuLibrarian():
    """Display menu for the librarian."""
    # Layout of the menu:
    layout = [
        [sg.Text("Main Menu")],
        [sg.Button("Borrowing"), sg.Button("Returns"),
             sg.Button("Add Reservations")],
        [sg.Button("View Loans and Reservations"),
             sg.Button("Add a book"), sg.Button("Add or Remove Stock")]
    ]
    # Display the window:
    window = sg.Window("Main Menu").Layout(layout)
    button, values = window.Read()
    window.close()
    # Show the appropriate screen to fulfil the request:
    if button == "Borrowing":
        borrowScreen()
    elif button == "Returns":
        returnScreen()
    elif button == "Add Reservations":
        reserveBookScreen()
    elif button == "View Loans and Reservations":
        studentInfoScreen()
    elif button == "Add a book":
        addBookScreen()
    elif button == "Add or Remove Stock":
        addRemStockScr()

def menuStudent():
    """Display menu for a student."""
    layout = [
        [sg.Text("Main Menu")],
        [sg.Button("My Loans"), sg.Button("My Reservations"),
             sg.Button("Reserve a book")],
        [sg.Button("Recommend books")]
    ]
    window = sg.Window("Main Menu").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "My Loans":
        result = sendLoanListReq([getLibCardNo()])
        loansListScreen(result)
    elif button == "My Reservations":
        result = sendReserveListReq([getLibCardNo()])
        reserveListScreen(result, getLibCardNo())
    elif button == "Reserve a book":
        reserveBookScreen()
    elif button == "Recommend books":
        result = sendRecommendReq()
        recScreen(result)

def displayMenu():
    """Choose the appropriate menu to display."""
    if getLibCardNo() == 9999999995:
        menuLibrarian()
    else:
        menuStudent()

def addBookScreen(message=''):
    """Display the screen to add a new book."""
    layout = [
        [sg.Text("Add a Book"), sg.Button("Home")],
        [sg.Text("Title", size=(20,1)), sg.InputText()],
        [sg.Text("Author", size=(20,1)), sg.InputText()],
        [sg.Text("ISBN", size=(20,1)), sg.InputText()],
        [sg.Submit()],
        [sg.Text(message)]
    ]
    window = sg.Window("Add a book").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "Home":
        # User wants to return to the main menu
        displayMenu()
    elif button == "Submit":
        try:
            # Make sure that integers are entered where needed.
            result = sendBookAddReq([values[0], values[1], int(values[2])])
        except ValueError:
            # Catch errors caused by wrong data type.
            result = [False, '''The ISBN must be a number. Enter it
                      without spaces or -.''']
        if result[0]:
            # Book added successfully.
            addBookScreen(message='Book added successfully')
        else:
            addBookScreen(message=('The book could not be added: '
                                   + result[1]))

def addRemStockScr(message=''):
    """Show the GUI for adding or removing library stock."""
    layout = [
        [sg.Text("Add or Remove Stock"), sg.Button("Home")],
        [sg.Text("School Book ID"), sg.InputText()],
        [sg.Text("ISBN"), sg.InputText()],
        [sg.Button("Add item"), sg.Button("Remove item")],
        [sg.Text(message)]
    ]
    window = sg.Window("Add or Remove Stock").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "Home":
        displayMenu()
    else:
        try:
            # Check the data types are correct.
            a = [int(values[0]), int(values[1])]
            del a
        except ValueError:
            button = "Not Applicable"  # Prevent a request being made
            result = [False, "Incorrect data type for school book ID or ISBN."]
        if button == "Add item":
            result = sendStockAddRemReq([int(values[0]), int(values[1])], "stockAdd")
        elif button == "Remove item":
            result = sendStockAddRemReq([int(values[0]), int(values[1])], "stockRem")

        if result[0]:
            # The action above was taken successfully.
            addRemStockScr(message="Action completed successfully.")
        else:
            # The action did not succeed.
            addRemStockScr(message=("An error occurred: " + result[1]))

def borrowScreen(message=''):
    """Display the screen for the librarian to lend books."""
    layout = [
        [sg.Text("Borrow"), sg.Button("Home")],
        [sg.Button("Return Books")],
        [sg.Text("Library Number")],
        [sg.InputText()],
        [sg.Text("School Book ID")],
        [sg.InputText()],
        [sg.Submit()],
        [sg.Text(message)]
    ]
    window = sg.Window("Borrow Books").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "Home":
        # User wants to return to the main menu.
        displayMenu()
    elif button == "Submit":
        # User wants to send the request
        try:
            # Attempt to send request, ensuring data types are correct.
            result = sendBorrowReq([int(values[0]), int(values[1])])
        except ValueError:
            # Wrong data type for Library Number or School Book ID
            result = [False, "Wrong data type for Library Number/Book ID"]
        if result[0]:
            # Book has been borrowed successfully.
            borrowScreen(message=("Book borrowed. Due " +str(result[1])[6:])
                                  + "-" + str(result[1])[4:6] + "-"
                                  + str(result[1])[:4])
        else:
            # An error occurred.
            borrowScreen(message="""Error: either the book is not found
                or the library card number is incorrect.""")
    elif button == "Return Books":
        # User wants to go to the return book screen instead.
        returnScreen()

def returnScreen(message=''):
    """Display the menu for returning library books."""
    layout = [
        [sg.Text("Return"), sg.Button("Home")],
        [sg.Button("Borrow Books")],
        [sg.Text("School Book ID"), sg.InputText()],
        [sg.Submit()],
        [sg.Text(message)]
    ]
    window = sg.Window("Return Books").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "Home":
        # User wants to return to the main menu.
        displayMenu()
    elif button == "Submit":
        try:
            result = sendReturnReq([int(values[0])])
        except ValueError:
            result = [False, "School Book IDs must be numbers only."]
        if result[0]:
            # Book return successfully.
            returnScreen(message="Book returned successfully.")
        else:
            # An error occurred returning the book.
            returnScreen(message=("Error"+result[1]))
    elif button == "Borrow Books":
        # User wants to borrow books instead.
        borrowScreen()

def studentInfoScreen():
    """Display screen to request a students loans or reservations."""
    layout = [
        [sg.Text("Students' Loans and Reservations"), sg.Button("Home")],
        [sg.InputText("Student's Library Card Number")],
        [sg.Button("View Loans"), sg.Button("View Reservations")],
    ]
    window = sg.Window("Get student information").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "Home":
        # User wants to return to the main menu.
        displayMenu()
    elif button == "View Loans":
        loanList = sendLoanListReq(values)
        loansListScreen(loanList)
    elif button == "View Reservations":
        reserveList = sendReserveListReq(values)
        reserveListScreen(reserveList, int(values[0]))
        
def loansListScreen(loans):
    """Display the list of loans that a student has.
    Take a list of loans (sent from the server) as input.
    """

    bookLayout = []  # Will be populated with details of books.
    for i in range(len(loans)):
        bookLayout = bookLayout + [
            [sg.Text(loans[i][0])],
            [sg.Text(loans[i][1])],
            [sg.Text("Due " + str(loans[i][3])[6:] + "/" + str(loans[i][3])[4:6]
                     + "/" + str(loans[i][3])[:4])],
            [sg.Text("_" * 25)]
        ]
    bookLayout = bookLayout[:-1]  # Remove final horizontal line.
    if bookLayout == []:
        # No loans have been taken out.
        bookLayout = [sg.Text("The student has no loans.")]
    layout = [
        [sg.Text("Loans"), sg.Button("Home")]] + bookLayout
    window = sg.Window("Loan List").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "Home":
        # User wants to return to the main menu.
        displayMenu()

def reserveListScreen(reservations, studentID, message=""):
    """Display a list of reservations for a user."""
    bookLayout = []  # Will be populated with details of books reserved.
    for i in range(len(reservations)):
        bookLayout = bookLayout + [
            [sg.Text(reservations[i][0]), sg.Button("Delete" + str(i+1))],
            [sg.Text(reservations[i][1])],
            [sg.Text("_"*25)]
        ]
    bookLayout[:-1]  # Remove final horizontal line.
    if bookLayout == []:
        bookLayout = [[sg.Text("There are no reservations for this student.")]]
    layout = ([[sg.Text("Reservations"), sg.Button("Home")]]
              + bookLayout
              + [[sg.Text(message)]])
    window = sg.Window("Reservation List").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "Home":
        # User wants to return to the main menu.
        displayMenu()
    elif "Delete" in button:
        itemToDel = int(button[7:])  # Position of item being deleted in list.
        result = sendDelResReq([bookLayout[itemToDel][2], studentID])
        if result[0]:
            # Successfully deleted.
            del reservations[itemToDel]
            reserveListScreen(reservations, studentID, message="Successfully deleted")
        else:
            # An error occurred deleting the reservation
            reserveListScreen(reservations, studentID,
                              message="Error: The reservation could not be deleted")
            
def reserveBookScreen(message=""):
    """Display the screen used to reserve a book."""
    layout = [
        [sg.Text("Reserve"), sg.Button("Home")],
        [sg.Text("ISBN"), sg.InputText()],
        [sg.Text("Library Card No."), sg.InputText()],
        [sg.Submit()],
        [sg.Text(message)]
    ]
    if getLibCardNo() != 9999999995:
        """This is a student so should not have the option to enter
        a library card number - this is done automatically for them.
        """
        del layout[2]  # Delete option to enter card number
    window = sg.Window("Reserve Books").Layout(layout)
    button, values = window.Read()
    window.close()
    if getLibCardNo() != 9999999995:
        """This is a student so I will automatically
           put their ID in lieu of the input.
        """
        values[1] = getLibCardNo()
    if button == "Home":
        # User wants to return to the main menu
        displayMenu()
    elif button == "Submit":
        result = sendReservationReq([int(values[0]), int(values[1])])
        if result[0]:
            # Reserved successfully.
            reserveBookScreen(message="Reservation saved successfully.")
        else:
            # An error occurred.
            reserveBookScreen(message=("An error occurred:" + str(result[1])))

def recScreen(recommendations):
    """Display recommended books.
    Take, as input, a 2D list of [Title, Author] recommendations
    and display them to the user.
    """

    bookLayout = []  # Will be populated with recommendations
    for i in range(len(recommendations)):
        bookLayout = bookLayout + [
            [sg.Text(recommendations[i][0])],
            [sg.Text(recommendations[i][1])],
            [sg.Text("_" * 25)]
        ]
    if bookLayout == []:
        # No recommendations.
        bookLayout = [[sg.Text("No recommendations available at the moment!")]]
    bookLayout = bookLayout[:-1]  # Delete final horizontal line
    layout = [
        [sg.Text("Recommendations"), sg.Button("Home")]] + bookLayout
    window = sg.Window("Your Recommended Books").Layout(layout)
    button, values = window.Read()
    window.close()
    if button == "Home":
        displayMenu()


sg.theme("LightGreen5")
loginScreen()
