# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 550)
        MainWindow.setStyleSheet("*{\n"
"    outline: None;\n"
"}\n"
"QTableView::item,\n"
"QTreeView::item,\n"
"QListView::item {\n"
"    /* padding: 4px; */\n"
"    min-height: 32px;\n"
"    border-color: transparent;\n"
"}\n"
"QTableView::item:selected,\n"
"QTreeView::item:selected,\n"
"QListView::item:selected {\n"
"    background-color: rgba(0, 170, 255, 0.7);\n"
"    color: #ffffff;\n"
"}\n"
"QTableView {\n"
"    background-color: rgba(189, 189, 189, 0.7);\n"
"    border-radius: 4px;\n"
"    border: 1px solid #f2f2f2;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(255, 255, 255);\n"
"    text-transform: uppercase;\n"
"    background-color: #232629;\n"
"    padding: 0 5px;\n"
"    height: 20px;\n"
"    font-weight: bold;\n"
"    border-radius: 0px;\n"
"    border-right: 1px solid;\n"
"    border-bottom: 1px solid;\n"
"    border-color: white;\n"
"    font-size: 10px;\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"    min-height: 20px;\n"
"    padding: 7px;\n"
"    padding-left: 15px;\n"
"    text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"    border: 1px solid rgba(70, 212, 255, 0.7);\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgba(0, 0, 0, 0.3);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: white;\n"
"    padding-left: 10px;\n"
"    border-radius: 0px;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    background-color: rgba(35, 38, 41, 0.75);\n"
"    border: 2px solid rgba(255, 255, 255, 0.2);\n"
"    border-width: 0 0 2px 0;\n"
"    font-weight: bold;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"    border-bottom: 1px solid rgb(83, 86, 93);\n"
"    selection-background-color: rgba(189, 189, 189, 0.7);\n"
"    selection-color: white;\n"
"    font-size: 10px;\n"
"    padding: 3px;\n"
"    font-weight: bold;\n"
"}\n"
"#frame_button{\n"
"    border: 1px solid black;\n"
"}\n"
"QGroupBox {\n"
"    background: transparent;\n"
"    border: 2px solid #4f5b62;\n"
"    border-radius: 4px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: black;\n"
"    padding: 10px;\n"
"    background: transparent;\n"
"    height: 36px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_view = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_view.sizePolicy().hasHeightForWidth())
        self.frame_view.setSizePolicy(sizePolicy)
        self.frame_view.setObjectName("frame_view")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_view)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_button = QtWidgets.QWidget(self.frame_view)
        self.frame_button.setObjectName("frame_button")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_button)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_student_btn = QtWidgets.QPushButton(self.frame_button)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../assert/images/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_student_btn.setIcon(icon)
        self.add_student_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_student_btn.setObjectName("add_student_btn")
        self.horizontalLayout.addWidget(self.add_student_btn)
        self.excel_btn = QtWidgets.QPushButton(self.frame_button)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../assert/images/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.excel_btn.setIcon(icon1)
        self.excel_btn.setIconSize(QtCore.QSize(20, 20))
        self.excel_btn.setObjectName("excel_btn")
        self.horizontalLayout.addWidget(self.excel_btn)
        self.diem_danh_btn = QtWidgets.QPushButton(self.frame_button)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\../assert/images/diem_danh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.diem_danh_btn.setIcon(icon2)
        self.diem_danh_btn.setIconSize(QtCore.QSize(20, 20))
        self.diem_danh_btn.setObjectName("diem_danh_btn")
        self.horizontalLayout.addWidget(self.diem_danh_btn)
        self.view_result_btn = QtWidgets.QPushButton(self.frame_button)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\../assert/images/research-center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_result_btn.setIcon(icon3)
        self.view_result_btn.setIconSize(QtCore.QSize(20, 20))
        self.view_result_btn.setObjectName("view_result_btn")
        self.horizontalLayout.addWidget(self.view_result_btn)
        self.export_qrCode_btn = QtWidgets.QPushButton(self.frame_button)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\../assert/images/qr-code.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_qrCode_btn.setIcon(icon4)
        self.export_qrCode_btn.setIconSize(QtCore.QSize(20, 20))
        self.export_qrCode_btn.setObjectName("export_qrCode_btn")
        self.horizontalLayout.addWidget(self.export_qrCode_btn)
        self.setting_cam_btn = QtWidgets.QPushButton(self.frame_button)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui\\../assert/images/cam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_cam_btn.setIcon(icon5)
        self.setting_cam_btn.setIconSize(QtCore.QSize(20, 20))
        self.setting_cam_btn.setObjectName("setting_cam_btn")
        self.horizontalLayout.addWidget(self.setting_cam_btn)
        self.verticalLayout.addWidget(self.frame_button)
        self.groupBox = QtWidgets.QGroupBox(self.frame_view)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.view = QtWidgets.QTableWidget(self.groupBox)
        self.view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.view.setObjectName("view")
        self.view.setColumnCount(6)
        self.view.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.view.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        item.setFont(font)
        self.view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setItem(2, 5, item)
        self.view.horizontalHeader().setStretchLastSection(True)
        self.view.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.view, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2.addWidget(self.frame_view)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Điểm danh sinh viên"))
        self.add_student_btn.setText(_translate("MainWindow", "Thêm học sinh"))
        self.excel_btn.setText(_translate("MainWindow", "Import Excel"))
        self.diem_danh_btn.setText(_translate("MainWindow", "Bắt đầu điểm danh"))
        self.view_result_btn.setText(_translate("MainWindow", "Xem kết quả"))
        self.export_qrCode_btn.setText(_translate("MainWindow", "Xuất QR Code"))
        self.setting_cam_btn.setText(_translate("MainWindow", "Cài đặt camera"))
        item = self.view.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.view.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên Sinh Viên"))
        item = self.view.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mã Học Sinh"))
        item = self.view.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time in"))
        item = self.view.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time out"))
        item = self.view.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tình trạng"))
        __sortingEnabled = self.view.isSortingEnabled()
        self.view.setSortingEnabled(False)
        self.view.setSortingEnabled(__sortingEnabled)
        self.view.setColumnWidth(0, 10)
        self.view.setColumnWidth(1, 180)
        self.view.setColumnWidth(2, 150)
        self.view.setColumnWidth(3, 200)
        self.view.setColumnWidth(4, 200)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
