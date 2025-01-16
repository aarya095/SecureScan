import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

from login import LoginWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Secure Scan")
        self.setGeometry(650,250,700,500)
        self.setStyleSheet("background-color:lightblue;")

        label = QLabel(self)
        pixmap = QPixmap(os.path.abspath(r"D:\Aarya\Coding_Projects\SecureScan\icons\main1.jpeg"))
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        label.move(10, 10)

        font = QFont("Verdana",20)

        click_here_button = QPushButton("Click Here To Continue",self)
        click_here_button.setFont(font)
        click_here_button.setStyleSheet("color:black; background-color: white")
        click_here_button.adjustSize()
        click_here_button.move(160,400)
        click_here_button.clicked.connect(self.open_login_window)

    def open_login_window(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())