# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_camera.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 584)
        Dialog.setMinimumSize(QtCore.QSize(680, 584))
        Dialog.setMaximumSize(QtCore.QSize(680, 584))
        Dialog.setStyleSheet("*{\n"
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
"    padding-right: 15px;\n"
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
"    background-color: rgb(58, 60, 62);\n"
"    selection-background-color: rgb(0, 141, 212);\n"
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
"    padding-top: 20px;\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.view_frame = QtWidgets.QLabel(self.groupBox)
        self.view_frame.setMinimumSize(QtCore.QSize(640, 480))
        self.view_frame.setText("")
        self.view_frame.setPixmap(QtGui.QPixmap("Screenshot 2023-11-18 010820.png"))
        self.view_frame.setObjectName("view_frame")
        self.gridLayout.addWidget(self.view_frame, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selected_cam_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_cam_btn.sizePolicy().hasHeightForWidth())
        self.selected_cam_btn.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assert/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selected_cam_btn.setIcon(icon)
        self.selected_cam_btn.setIconSize(QtCore.QSize(20, 20))
        self.selected_cam_btn.setObjectName("selected_cam_btn")
        self.horizontalLayout.addWidget(self.selected_cam_btn)
        self.scan_cam_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_cam_btn.sizePolicy().hasHeightForWidth())
        self.scan_cam_btn.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assert/images/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scan_cam_btn.setIcon(icon1)
        self.scan_cam_btn.setIconSize(QtCore.QSize(20, 20))
        self.scan_cam_btn.setObjectName("scan_cam_btn")
        self.horizontalLayout.addWidget(self.scan_cam_btn)
        self.list_camera = QtWidgets.QComboBox(self.frame)
        self.list_camera.setObjectName("list_camera")
        self.list_camera.addItem("")
        self.horizontalLayout.addWidget(self.list_camera)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "View"))
        self.selected_cam_btn.setText(_translate("Dialog", "Chọn camera"))
        self.scan_cam_btn.setText(_translate("Dialog", "Scan Camera"))
        self.list_camera.setItemText(0, _translate("Dialog", "Camera 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())