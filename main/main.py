import tkinter as tk
from tkinter import Toplevel

import os


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Secure Scan")
        self.geometry("700x500+450+150")
        self.configure(bg="lightblue")



        # Create image label
        label = tk.Label(self, bg="lightblue")
        label.pack(pady=20)

        # Button
        button = tk.Button(self, text="Click Here To Continue", font=("Verdana", 16),
                           bg="white", fg="black", command=self.open_login_window)
        button.pack(pady=20)

    def open_login_window(self):
        self.withdraw()  # Hide the main window

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
