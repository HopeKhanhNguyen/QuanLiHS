from PyQt5.QtWidgets import QDialog
from ui.add_student import Ui_Dialog
from tkinter import messagebox

class AddStudent(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.save.clicked.connect(self.doneAdd)
        self.cancel.clicked.connect(self.reject)

    def doneAdd(self):
        if self.name_student.text().strip() == '' or self.code_student.text().strip() == '': messagebox.showerror("Xảy ra lỗi", "Vui lòng nhập đủ thông tin"); return
        self.name = self.name_student.text()
        self.msv = self.code_student.text() 
        self.accept()