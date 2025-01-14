import tkinter as tk

def hide_window():
    root.destroy()

root = tk.Tk()
root.title("Secure Scan")
root.geometry("500x400+500+200")

button = tk.Button(root, text="Click here to Continue", width=40, height=2, command=hide_window)
button.place(x=110,y=300)

root.mainloop()