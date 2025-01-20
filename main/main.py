import sys
import tkinter as tk
import os

from log_in.login import LoginWindow


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Secure Scan")
        self.geometry("700x500+450+150")
        self.configure(bg="lightblue")

        label = tk.Label(self, bg="lightblue")
        label.pack(pady=20)

        button = tk.Button(self, text="Click Here To Continue", font=("Verdana", 16),
                           bg="white", fg="black", command=self.open_login_window)
        button.place(x=220, y=400)

        self.protocol("WM_DELETE_WINDOW", sys.exit)

    def open_login_window(self):
        self.withdraw()
        login_window = LoginWindow(self)
        login_window.grab_set()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
