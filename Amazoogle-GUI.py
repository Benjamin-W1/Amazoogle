import tkinter as tk

window = tk.Tk()
window.iconbitmap(r".\icon.ico")
window.title("Amazoogle GUI")
window.geometry('2560x1440')

img = tk.PhotoImage(file='logo.png')
tk.Label(
    window,
    image=img
).pack()


window.mainloop()
