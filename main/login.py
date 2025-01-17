import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from database.db_connection import DatabaseConnection

class DatabaseThread(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self, query, params):
        super().__init__()
        self.query = query
        self.params = params
        self.db_connection = DatabaseConnection()
        self.db_connection.connect_to_database()

    def run(self):
        if not self.db_connection.get_connection():
            self.result_signal.emit("Failed to connect to the database.")
            return

        try:
            result = self.db_connection.fetch_all(self.query, self.params)
            if result:
                self.result_signal.emit(f"Query Result: {result}")
            else:
                self.result_signal.emit("No results found.")
        except Exception as e:
            self.result_signal.emit(f"Error: {str(e)}")

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(750, 350, 500, 350)

        login_label = QLabel("Log In", self)
        login_label.setFont(QFont("Tahoma", 40))
        login_label.move(150, 12)

        self.enter_username = QLineEdit(self)
        self.enter_username.setPlaceholderText("Username")
        self.enter_username.setFont(QFont("Arial", 10))
        self.enter_username.setGeometry(50, 120, 400, 40)

        self.enter_password = QLineEdit(self)
        self.enter_password.setPlaceholderText("Password")
        self.enter_password.setFont(QFont("Arial", 10))
        self.enter_password.setEchoMode(QLineEdit.Password)
        self.enter_password.setGeometry(50, 180, 400, 40)

        login_button = QPushButton("Log In", self)
        login_button.setFont(QFont("Tahoma", 15))
        login_button.setStyleSheet("background-color: black; color:white;")
        login_button.setGeometry(115, 260, 270, 50)
        login_button.clicked.connect(self.verify_user_credentials)

    def verify_user_credentials(self):
        username = self.enter_username.text()
        password = self.enter_password.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Username or password cannot be empty")
            return

        query = "SELECT * FROM login WHERE username=%s AND password=%s"
        params = (username, password)

        # Run the database query in a separate thread
        self.db_thread = DatabaseThread(query, params)
        self.db_thread.result_signal.connect(self.handle_query_result)
        self.db_thread.start()

    def handle_query_result(self, message):
        QMessageBox.information(self, "Query Result", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
