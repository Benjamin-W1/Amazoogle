import PySimpleGUI as sg

def login(username, password, old_window):
    if True:
        #LOG IN SUCCESS
        search_window(old_window)
    else:
        #INVALID CREDENTIALS
        sg.Popup("Sorry your username or password is incorrect.")

def search_window(old_window):
    old_window.Close()
    
    next = [[sg.Image('media/logo - small.png', size=(178,55))],
          [sg.Text('Search: ', background_color='#FFFFFF', text_color='#000000'),sg.InputText(),sg.Submit()]]

    window = sg.Window('Amazoogle', next, element_justification='c', background_color='#FFFFFF', icon="media/icon.ico")
    event, values = window.Read()

    window.Close()

def results_window(old_window):
    old_window.Close()
    
    next = [[sg.Image('media/logo - small.png', size=(178,55))],
          [sg.Text('MED_DATA_20220803153921.csv', background_color='#FFFFFF', text_color='#000000'),sg.Text('2022/08/03/153921', background_color='#FFFFFF', text_color='#000000'),sg.Submit()]]

    window = sg.Window('Amazoogle', next, element_justification='c', background_color='#FFFFFF', icon="media/icon.ico")
    event, values = window.Read()

    window.Close()


if __name__ == "__main__":
    login_layout = [[sg.Image('media/logo - small.png', size=(178,55))],
              [sg.Text('Username: ', background_color='#FFFFFF', text_color='#000000'),sg.InputText()],
              [sg.Text('Password: ', background_color='#FFFFFF', text_color='#000000'),sg.InputText()],
              [sg.Submit()]]

    window = sg.Window('Amazoogle', login_layout, element_justification='c', background_color='#FFFFFF', icon="media/icon.ico")

    event, values = window.Read()
    login(values[1], values[2], window)
