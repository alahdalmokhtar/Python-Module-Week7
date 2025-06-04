from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from .set_tabel_data import set_table_data
from admin_menu1 import Ui_MainWindow as Ui_AdminMenu1  # Assumes it's the UI class, not full window


class Ui_MainWindow(object):

    def open_admin_window(self):
        # Creates new QMainWindow and loads the Admin UI into it
        self.admin_window = QtWidgets.QMainWindow()
        self.ui_admin = Ui_AdminMenu1()
        self.ui_admin.setupUi(self.admin_window)
        self.admin_window.show()

    def load_all_chats(self):
        # Load Excel data into the table
        set_table_data(self, 'Mentors.xlsx')

    def on_search_button_clicked(self):
        search_value = self.lineeditserch.text().lower().strip()
        for row in range(self.tableWidget.rowCount()):
            if not search_value:
                self.tableWidget.setRowHidden(row, False)
                continue
            row_match = any(
                search_value in (self.tableWidget.item(row, col).text().lower() if self.tableWidget.item(row, col) else "")
                for col in range(self.tableWidget.columnCount())
            )
            self.tableWidget.setRowHidden(row, not row_match)

    def exit_app(self):
        QApplication.quit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Label (title)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 441, 61))
        font = QtGui.QFont("Miriam CLM", 28, QtGui.QFont.Weight.Bold)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0.159, x2:0.045, y2:0.131091, stop:0.994318 rgba(138, 0, 27, 255), stop:1 rgba(255, 255, 27, 255));")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        # All Chats Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 101, 23))
        self.pushButton.setStyleSheet("color: black; font: 75 12pt 'Arial';")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.load_all_chats)

        # Search Button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 70, 101, 23))
        self.pushButton_2.setStyleSheet("color: black; font: 75 12pt 'Arial';")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_search_button_clicked)

        # Exit Button
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 170, 101, 23))
        self.pushButton_3.setStyleSheet("color: black; font: 75 12pt 'Arial';")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.exit_app)

        # Preferences (Admin Menu)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 170, 101, 23))
        self.pushButton_4.setStyleSheet("color: black; font: 75 12pt 'Arial';")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.open_admin_window)

        # Search LineEdit
        self.lineeditserch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineeditserch.setGeometry(QtCore.QRect(390, 70, 231, 20))
        font = QtGui.QFont("Miriam Libre", 9, QtGui.QFont.Weight.Bold)
        self.lineeditserch.setFont(font)
        self.lineeditserch.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineeditserch.setClearButtonEnabled(True)
        self.lineeditserch.setObjectName("lineeditserch")
        self.lineeditserch.textChanged.connect(self.on_search_button_clicked)

        # ComboBox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 110, 221, 22))
        font = QtGui.QFont("Arial", 8, QtGui.QFont.Weight.Bold)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems([
            "It is appropriate to direct them within the scope of the VIT Project ",
            "It's approprite to direct them to employment though direct individual coaching",
            "It would be more appropriate for them to participate in the next VIT project ",
            "It's appropriate to direct them to the initial IT training  of the VIT project ",
            "It's appropriate for them to participate in the entire VIT project ",
            "It's appropriate to direct them to them English training within the VIT project ",
            "Should be directed to another sector",
            "other"
        ])

        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 220, 571, 192))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Datum Interview", "Last Name", "Montor"])
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.setObjectName("tableWidget")

        # Final setup
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Montor Menu"))
        self.label.setText(_translate("MainWindow", "Montor Menu"))
        self.pushButton.setText(_translate("MainWindow", "All Chats"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
        self.pushButton_4.setText(_translate("MainWindow", "Preferences"))
        self.lineeditserch.setPlaceholderText(_translate("MainWindow", "Please enter the text to search"))
