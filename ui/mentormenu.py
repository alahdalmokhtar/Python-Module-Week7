

from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from pathlib import Path

#sys.path
sys.path.append(str(Path(__file__).parent.parent))

#recall the function from  backend
from backend.list_files import list_files
from backend.set_table_data import set_table_data

class Ui_MentorMenue(object):
    def setupUi(self, MentorMenue):
        MentorMenue.setObjectName("MentorMenue")
        MentorMenue.resize(994, 524)
        MentorMenue.setStyleSheet("font: 700 10pt \"Times New Roman\";\n"
                                  "background-color: rgb(170, 170, 170);")
        self.centralwidget = QtWidgets.QWidget(parent=MentorMenue)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 140, 811, 301))
        self.tableWidget.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")

        headers = ["Date", "Name Sure Name", "Mail", "Telephone", "Post code",
                   "State", "Status", "Economical Situatie"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item.setText(header)

        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 471, 121))
        self.label.setStyleSheet("background-color: rgb(165, 170, 169);")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/eng.alahdal/Downloads/logo-1.png"))
        self.label.setObjectName("label")

        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 140, 150, 321))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setStyleSheet("color: rgb(255, 0, 0);\n"
                                    "background-color: rgb(100, 108, 102);")
        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton("Search", parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton("All Applications", parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QtWidgets.QPushButton("Back Menue", parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QtWidgets.QPushButton("Exit", parent=self.layoutWidget)
        self.verticalLayout.addWidget(self.pushButton_4)

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 151, 111))
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/eng.alahdal/Downloads/mm.png"))
        self.label_3.setScaledContents(True)

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 40, 211, 71))
        self.label_2.setStyleSheet("font: 700 18pt \"Times New Roman\";")
        self.label_2.setText("Mentor Menue")

        MentorMenue.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MentorMenue)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 21))
        MentorMenue.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MentorMenue)
        MentorMenue.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MentorMenue)
        self.lineEdit.textChanged.connect(self.search_action)# connect text change to search action
        self.pushButton_2.clicked.connect(self.submitted_projects_action)
        #self.pushButton_4.clicked.connect(self.projects_arrivals_action)
        self.pushButton_5.clicked.connect(self.back_to_menu)
        self.pushButton_4.clicked.connect(self.exit_app)

    def search_action(self):
        """Filter the table based on the text in the line edit."""
        search_text = self.lineEdit.text()
        print(f"🔍  search :  {search_text}")
    
        for row in range(self.tableWidget.rowCount()):
           item = self.tableWidget.item(row, 2)
           match = search_text.lower() in item.text().lower() if item else False
           self.tableWidget.setRowHidden(row, not match)

    def submitted_projects_action(self):
        print("  All application")
        """ app = QtWidgets.QApplication(sys.argv)
        mentor_window = QtWidgets.QMainWindow()
        mentor = Ui_MentorMenue()
        mentor.setupUi(mentor_window)
    # Check if the text edit fields are initialized
        if mentor.tableWidget is None:
          print("Table widget is not initialized.")
        else:
          print("Table widget is initialized.")
          mentor.tableWidget.setColumnCount(0)
          mentor.tableWidget.setRowCount(0)
          set_table_data(mentor, "Mentors.xlsx")
        set_table_data(mentor, "Mentors.xlsx")
        mentor_window.show()
        sys.exit(app.exec()) """
        self.mentor_ui = Ui_MentorMenue()
        self.main_window = QtWidgets.QMainWindow()
        self.application = Ui_MentorMenue()
        self.application.setupUi(self.main_window)

        if self.application.tableWidget is None:
          print("Table widget is not initialized.")
        else:
           print("Table widget is initialized.")
           self.application.tableWidget.setColumnCount(0)
           self.application.tableWidget.setRowCount(0)
        set_table_data(self.application, "Mentors.xlsx")

        self.main_window.show()

    def projects_arrivals_action(self):
        print("  Projects Arrivals")
        QtWidgets.QMessageBox.information(None, "Projects Arrivals", "")

    def back_to_menu(self):
        print("  Back Menue")
        """ QtWidgets.QMessageBox.information(None, "Back Menu", "") """
        from usermenue import Ui_usermenue  # Move import here
        self.user_window = QtWidgets.QMainWindow()
        self.user_ui = Ui_usermenue()
        self.user_ui.setupUi(self.user_window)
        self.user_window.show()


    def exit_app(self):
        print("  Exit")
        QtWidgets.QApplication.quit()

def mentor():
    app = QtWidgets.QApplication(sys.argv)
    mentor_window = QtWidgets.QMainWindow()
    ui = Ui_MentorMenue()
    ui.setupUi(mentor_window)

    try:
        set_table_data(ui, "Mentors.xlsx")
    except Exception as e:
        print(f"Error loading table data: {e}")

    mentor_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    mentor()
