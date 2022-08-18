import PySimpleGUI as sg
import ftpclient

def login(username, password, old_window):
    resp = ftp.login(username,password)
    if resp:
        #LOG IN SUCCESS
        search_window(old_window)
    else:
        #INVALID CREDENTIALS
        sg.Popup("Sorry your username or password is incorrect.")
        login_window()

def search_window(old_window):
    old_window.Close()
    
    l = []
    next = [
          [sg.Image('media/logo - small.png', size=(178,55))],
          [sg.Text('Search: ', background_color='#FFFFFF', text_color='#000000'),sg.InputText(),sg.Submit()],
          [sg.Listbox(l, size=(70, 10), key='-LIST-',enable_events=True)],
          [sg.Button('Download',key='-DOWNLOAD-')]
          ]

    window = sg.Window('Amazoogle', next, element_justification='c', background_color='#FFFFFF', icon="media/icon.ico")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            ftp.logout()
            break
        elif event == '-DOWNLOAD-':
            filename = l[window.Element('-LIST-').Widget.curselection()[0]]
            resp = ftp.get_file(filename)
            if resp:
                sg.Popup("File downloaded")
            else:
                sg.Popup("File format is invalid!")
        elif event == 'Submit':
            searchQuery = values[1].upper()
            #SEARCH FTP AND RETURN VALUES AS LIST
            results = ftp.search(searchQuery)
            l = []
            for result in results:
                l.append(result)
            window.Element('-LIST-').update(values=l)

def login_window():
    login_layout = [[sg.Image('media/logo - small.png', size=(178,55))],
              [sg.Text('Username: ', background_color='#FFFFFF', text_color='#000000'),sg.InputText()],
              [sg.Text('Password: ', background_color='#FFFFFF', text_color='#000000'),sg.InputText()],
              [sg.Submit()]]

    window = sg.Window('Amazoogle', login_layout, element_justification='c', background_color='#FFFFFF', icon="media/icon.ico")

    event, values = window.Read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        pass
    elif event == "Submit":
        login(values[1], values[2], window)

if __name__ == "__main__":
    ftp = ftpclient.FTP_Comms()
    login_window()
