import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import gdown

# URL of the Google Drive file
url = 'https://drive.google.com/uc?id=1Wf3DG50m5J-r-hx0W8qyafKbjh-Bc5kn'

# Download the file from Google Drive
output = 'Users.xlsx'
gdown.download(url, output, quiet=False)

# Read the Excel file
df = pd.read_excel(output, engine='openpyxl')

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')

        self.layout = QVBoxLayout()

        self.user_label = QLabel('Username:')
        self.layout.addWidget(self.user_label)

        self.user_input = QLineEdit()
        self.layout.addWidget(self.user_input)

        self.pass_label = QLabel('Password:')
        self.layout.addWidget(self.pass_label)

        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.pass_input)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.check_login)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def check_login(self):
        username = self.user_input.text()
        password = self.pass_input.text()

        user_data = df[(df['user'] == username) & (df['password'] == password)]

        if not user_data.empty:
            role = user_data['role'].values[0]
            if role == 'Admin':
                self.show_message('Login Successful', 'Welcome Admin!')
            elif role == 'User':
                self.show_message('Login Successful', 'Welcome User!')
            else:
                self.show_message('Error', 'Unknown role!')
        else:
            self.show_message('Error', 'Invalid username or password!')

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())

