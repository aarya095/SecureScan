import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("500x350+500+200")

def close_window():
    root.destroy()

def get_username():
    input_username = enter_username.get()

def get_password():
    input_username = enter_password.get()

login_label = tk.Label(root, text="Log In",font=("Times",40))
login_label.place(x=180, y=12)

enter_username = tk.Text(root, width=50, height=1.5, font=("Arial",10))
enter_username.place(x=50,y=100)

enter_password = tk.Text(root, width=50, height=1.5, font=("Arial",10))
enter_password.place(x=50,y=160)

login = tk.Button(root, text="Log In",
                      font=("Arial",12), width=30, height=2,
                      bg="black",fg="white",
                      command=close_window)
login.place(x=115,y=250)

root.mainloop()