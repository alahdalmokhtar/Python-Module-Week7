from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QDialog
import sys

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("login_window.ui", self)

        # Connect buttons
        self.login_button.clicked.connect(self.login)
        self.exit_button.clicked.connect(self.close)

        self.apply_styles()

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if username == "admin" and password == "1234":
            self.error_label.setText("Login successful!")
            self.error_label.setStyleSheet("color: green;")
        else:
            self.error_label.setText("Invalid username or password.")
            self.error_label.setStyleSheet("color: red;")

    def apply_styles(self):
        self.setStyleSheet("""
            QDialog {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                                                  stop:0 rgba(0, 0, 0, 100),
                                                  stop:1 rgba(255, 255, 255, 255));
            }
            QLineEdit {
                border: 2px solid #5A5A5A;
                border-radius: 15px;
                padding: 8px;
                background-color: #FFFFFF;
                font-size: 14px;
            }
            QPushButton {
                background-color: #e0e0e0;
                border-radius: 10px;
                padding: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #b0b0b0;
            }
            QLabel#error_label {
                font-style: italic;
                font-size: 12px;
                padding-top: 4px;
                padding-bottom: 4px;
            }
            QLabel#forgot_label {
                color: blue;
                font-size: 10pt;
                padding-top: 10px;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
