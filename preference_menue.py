import sys
from PyQt6 import QtWidgets
from prfrence_menue import Ui_prefrence_menu  # the generated UI class

# Dummy windows for the three app sections:
class ApplicationsWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Applications")
        self.resize(300, 200)
        label = QtWidgets.QLabel("Applications Window", self)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)

class MentorMeetingWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mentor Meeting")
        self.resize(300, 200)
        label = QtWidgets.QLabel("Mentor Meeting Window", self)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)

class InterviewsWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interviews")
        self.resize(300, 200)
        label = QtWidgets.QLabel("Interviews Window", self)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)

class PreferenceMenuApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_prefrence_menu()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.btn_applications.clicked.connect(self.open_applications)
        self.ui.btn_mentor.clicked.connect(self.open_mentor)
        self.ui.btn_interviews.clicked.connect(self.open_interviews)
        self.ui.btn_close.clicked.connect(self.close)

        # Store windows so they don't get garbage collected
        self.applications_win = None
        self.mentor_win = None
        self.interviews_win = None

    def open_applications(self):
        if self.applications_win is None:
            self.applications_win = ApplicationsWindow()
        self.applications_win.show()

    def open_mentor(self):
        if self.mentor_win is None:
            self.mentor_win = MentorMeetingWindow()
        self.mentor_win.show()

    def open_interviews(self):
        if self.interviews_win is None:
            self.interviews_win = InterviewsWindow()
        self.interviews_win.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PreferenceMenuApp()
    window.show()
    sys.exit(app.exec())
