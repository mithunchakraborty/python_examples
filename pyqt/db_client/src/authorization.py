from PyQt5.QtWidgets import (
    QDialog, QLineEdit,
    QVBoxLayout, QPushButton,
    QInputDialog, QMessageBox,
    QWidget
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class Authorization(QWidget) :
    def __init__(self, parent=None) :
        super(Authorization, self).__init__(parent)
        self.initUI()

    def initUI(self) :
        # Create widgets
        self.login = QLineEdit()
        self.login.setPlaceholderText("Login")
        self.login.setMaximumSize(QSize(300, 40))
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setMaximumSize(QSize(300, 40))
        self.password.setEchoMode(QLineEdit.Password)
        self.accept = QPushButton("Accept")
        self.accept.setShortcut("Ctrl+Enter")
        self.accept.setMaximumSize(QSize(300, 40))

        # Create layout and add widgets
        layout = QVBoxLayout()
        widgets = [
            self.login,
            self.password,
            self.accept
        ]
        for i in widgets : layout.addWidget(i)

        # Set dialog layout
        self.setLayout(layout)
        layout.setAlignment(Qt.AlignCenter)
