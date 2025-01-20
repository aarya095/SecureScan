import tkinter as tk
from tkinter import messagebox
from database.db_connection import DatabaseConnection
import bcrypt
import sys

class LoginWindow(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Log In")
        self.geometry("400x300+550+250")

        tk.Label(self, text="Log In", font=("Tahoma", 20)).place(x=150,y=20)

        tk.Label(self, text="Username:", font=("Arial", 12)).place(x=50, y=80)
        self.enter_username = tk.Entry(self, font=("Arial", 12))
        self.enter_username.place(x=150, y=80, width=200)

        tk.Label(self, text="Password:", font=("Arial", 12)).place(x=50, y=120)
        self.enter_password = tk.Entry(self, font=("Arial", 12), show="*")
        self.enter_password.place(x=150, y=120, width=200)

        login_button = tk.Button(self, text="Log In", font=("Tahoma",14), bg="black",fg="white",
                                 command=self.verify_user_credentials)
        login_button.place(x=150, y=180)

        self.protocol("WM_DELETE_WINDOW", sys.exit)

    def verify_user_credentials(self):
        username = self.enter_username.get().strip()
        password = self.enter_password.get().strip()

        if not username or not password:
            messagebox.showwarning("Login Failed","Please enter both username and password")
            return

        db = DatabaseConnection()
        db.connect_to_database()

        if db.connection:
            query = "select password from login where username=%s"
            result = db.fetch_all(query, (username,))

            db.close_connection()

            if result:
                stored_hashed_password = result[0][0]

                if bcrypt.checkpw(password.encode(), stored_hashed_password.encode()):
                    messagebox.showinfo("Login Success","Welcome to Secure Scan")
                    self.destroy()
                    self.master.destroy()
                else:
                    messagebox.showerror("Login Failed", "Invalid username or password")

            else:
                messagebox.showerror("Login Failed","Invalid username or password")
        else:
            messagebox.showerror("Database Error","Could not connect to database")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    login_window = LoginWindow(root)
    login_window.mainloop()