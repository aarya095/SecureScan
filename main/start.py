import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Start")

        self.setGeometry(600,250,800,600)
        layout = QVBoxLayout()

if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec_())