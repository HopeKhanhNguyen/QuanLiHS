from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from datetime import datetime
from .classDatabase import *
import time

class LoadStudent(QThread):
    edit_row = pyqtSignal(object, int, int, str)
    def __init__(self, parent, row: int, data):
        super().__init__(parent)
        self.gui = parent
        self.row = row
        self.data = list(data)
    
    def run(self):
        print(self.data)
        timeEnd = self.data[-1]
        status = True
        date_end = True
        if not timeEnd:
            timeEnd = time.time()
            status = False
            date_end = False
        currentDate = datetime.fromtimestamp(int(timeEnd)).strftime("%d-%m-%Y")
        if currentDate != datetime.fromtimestamp(int(time.time())).strftime("%d-%m-%Y") or date_end == False:
            self.data[-2] = "Chưa điểm danh hôm nay"
            self.data[2], self.data[3] = '', ''
            status = False
        self.edit_row.emit(self.gui.view, self.row, 0, str(self.row+1))
        for x, y in enumerate(self.data):
            if not y: y = ''
            else:
                try:
                    if x == len(self.data)-1: y = ''
                    if x == 2 or x == 3: y = datetime.fromtimestamp(int(y)).strftime("%H:%M:%S")
                except: y = ''
            self.edit_row.emit(self.gui.view, self.row, x + 1, str(y))
        if status == False: db.update(DB_STUDENT, f'`dateEnd` = {time.time()}, `time_in` = NULL, `time_out` = NULL, `status` = "Chưa điểm danh hôm nay"', f'`msv` = "{self.data[1]}"')