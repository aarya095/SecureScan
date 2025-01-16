import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QApplication


class LoginWindow(QWidget):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(750, 350,500,350)

        login_label = QLabel("Log In",self)
        login_label.setFont(QFont("Tahoma",40))
        login_label.move(150, 12)

        self.enter_username = QLineEdit(self)
        self.enter_username.setPlaceholderText("Username")
        self.enter_username.setFont(QFont("Arial", 10))
        self.enter_username.setGeometry(50,120,400,40)

        self.enter_password = QLineEdit(self)
        self.enter_password.setPlaceholderText("Password")
        self.enter_password.setFont(QFont("Arial",10))
        self.enter_password.setEchoMode(QLineEdit.Password)
        self.enter_password.setGeometry(50,180,400,40)

        login_button = QPushButton("Log In",self)
        login_button.setFont(QFont("Tahoma", 15))
        login_button.setStyleSheet("background-color: black; color:white;")
        login_button.setGeometry(115, 260, 270, 50)
        login_button.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())