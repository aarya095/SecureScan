import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt  # Correct import for Qt.AlignCenter

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Centered Text Example")
        self.setGeometry(100, 100, 400, 200)

        # Create a QLineEdit widget for single-line input
        line_edit = QLineEdit(self)
        line_edit.setAlignment(Qt.AlignCenter)  # Center the text inside the text field

        # Create a layout and add the widget
        layout = QVBoxLayout(self)
        layout.addWidget(line_edit)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
