from PyQt6 import QtWidgets
import sys
from ui.application1 import Ui_applications
#from ui.userlogin import Ui_new_login
from ui.mentormenu import Ui_MentorMenue
from backend.list_files import list_files
from backend.set_table_data import set_table_data
app = QtWidgets.QApplication(sys.argv)

def mentor():
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
    sys.exit(app.exec())

def application():
   
    main_window = QtWidgets.QMainWindow()
    application = Ui_applications()
    # Set the table data from the Excel file
    application.setupUi(main_window)
# Set the table data from the Excel file
    if application.tableWidget is None:
       print("Table widget is not initialized.")
    else:
        print("Table widget is initialized.")
        application.tableWidget.setColumnCount(0)
        application.tableWidget.setRowCount(0)
    # Set the table data from the Excel file
        set_table_data(application, "Applications.xlsx")

    set_table_data(application, "Applications.xlsx")
    
    main_window.show()
    sys.exit(app.exec())

""" pp = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
#application = Ui_applications()
#new_login = Ui_new_login()
#new_login.setupUi(main_window)

mentor_window = QtWidgets.QMainWindow()
mentor=Ui_MentorMenue()
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
sys.exit(app.exec())

 if new_login.textEdit is None or new_login.textEdit_2 is None:
    print("Text edit fields are not initialized.")
else:
    print("Text edit fields are initialized.") """

 
""" application.setupUi(main_window)
# Set the table data from the Excel file
if application.tableWidget is None:
    print("Table widget is not initialized.")
else:
    print("Table widget is initialized.")
    application.tableWidget.setColumnCount(0)
    application.tableWidget.setRowCount(0)
    # Set the table data from the Excel file
    set_table_data(application, "Applications.xlsx")

set_table_data(application, "Applications.xlsx")
 
    
main_window.show()
sys.exit(app.exec()) """
# main.py """
if __name__ == "__main__":
    mentor()
    application()