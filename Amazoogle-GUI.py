import tkinter as tk
from functools import partial

# GUI config
window = tk.Tk()
window.iconbitmap(r".\media\icon.ico")
window.title("Amazoogle GUI")
window.geometry('300x300')
window.configure(bg='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Nav Bar
## Logo Image
img = tk.PhotoImage(file='media\logo - small.png')
logo_lbl = tk.Label(
    window,
    image=img,
    borderwidth=0
)
logo_lbl.grid(row=0, column=0, columnspan=2)
logo_lbl.grid_rowconfigure(1, weight=1)
logo_lbl.grid_columnconfigure(1, weight=1)

# LOGIN
def validateLogin(username, password):
    return
usernameLabel = tk.Label(window, text="User Name: ", bg='white').grid(row=1, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(window, textvariable=username).grid(row=1, column=1)  
passwordLabel = tk.Label(window,text="Password: ", bg='white').grid(row=2, column=0)  
password = tk.StringVar()
passwordEntry = tk.Entry(window, textvariable=password, show='*').grid(row=2, column=1)  
validateLogin = partial(validateLogin, username, password)

#login button
loginButton = tk.Button(window, text="Login", command=validateLogin).grid(row=3, column=0)  



window.mainloop()
