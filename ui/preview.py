# Form implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_search(object):
    def setupUi(self, search):
        search.setObjectName("search")
        search.resize(613, 429)
        search.setStyleSheet("font: 9pt \"Times New Roman\";\n"
"background-color: rgb(165, 170, 169);")
        self.centralwidget = QtWidgets.QWidget(parent=search)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(348, 140, 241, 31))
        self.comboBox.setStyleSheet("background-color: rgb(230, 253, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(30, 190, 561, 192))
        self.treeWidget.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidget.header().setDefaultSectionSize(200)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 70, 261, 101))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(350, 80, 241, 45))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget1)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        search.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=search)
        self.statusbar.setObjectName("statusbar")
        search.setStatusBar(self.statusbar)

        self.retranslateUi(search)
        QtCore.QMetaObject.connectSlotsByName(search)

    def retranslateUi(self, search):
        _translate = QtCore.QCoreApplication.translate
        search.setWindowTitle(_translate("search", "Search"))
        self.comboBox.setItemText(0, _translate("search", "It is appropriate to direct them within the scope of the VIT Project"))
        self.comboBox.setItemText(1, _translate("search", "It\'s approprite to direct them to employment though direct individual coaching"))
        self.comboBox.setItemText(2, _translate("search", "It would be more appropriate for them to participate in the next VIT projectIt would be more appropriate for them to participate in the next VIT project"))
        self.comboBox.setItemText(3, _translate("search", "It\'s appropriate to direct them to the initial IT training  of the VIT project"))
        self.comboBox.setItemText(4, _translate("search", "It\'s appropriate for them to participate in the entire VIT project"))
        self.treeWidget.headerItem().setText(0, _translate("search", "Datem Interview"))
        self.treeWidget.headerItem().setText(1, _translate("search", "Last Name"))
        self.treeWidget.headerItem().setText(2, _translate("search", "Mentor"))
        self.pushButton.setText(_translate("search", "All Chats"))
        self.pushButton_2.setText(_translate("search", "Search"))
        self.pushButton_3.setText(_translate("search", "prefferences"))
        self.pushButton_4.setText(_translate("search", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    search = QtWidgets.QMainWindow()
    ui = Ui_search()
    ui.setupUi(search)
    search.show()
    sys.exit(app.exec())
