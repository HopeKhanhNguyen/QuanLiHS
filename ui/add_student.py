from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 108)
        Dialog.setStyleSheet("QPushButton{\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"    min-height: 20px;\n"
"    padding: 5px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"    border: 1px solid rgba(70, 212, 255, 0.7);\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"    color: white;\n"
"}\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-bottom: 1px solid black;\n"
"    min-height: 20px;\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name_student = QtWidgets.QLineEdit(Dialog)
        self.name_student.setObjectName("name_student")
        self.gridLayout.addWidget(self.name_student, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.code_student = QtWidgets.QLineEdit(Dialog)
        self.code_student.setObjectName("code_student")
        self.gridLayout.addWidget(self.code_student, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nhập dữ liệu học sinh"))
        self.label.setText(_translate("Dialog", "Tên sinh viên:"))
        self.label_2.setText(_translate("Dialog", "Mã sinh viên:"))
        self.save.setText(_translate("Dialog", "Thêm"))
        self.cancel.setText(_translate("Dialog", "Hủy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
