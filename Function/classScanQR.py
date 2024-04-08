from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .classDatabase import *
import cv2, time
from datetime import datetime
data = []
class DiemDanh(QThread):
    
    edit_row = pyqtSignal(object, object, object, object)
    loadAccount = pyqtSignal()
    
    def __init__(self, parent: QObject) -> None:
        super().__init__(parent)
        self.gui = parent
        
    def run(self):
        camera_index = self.gui.cam_index
        self.cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        last_qr_time = 0

        if not self.cap.isOpened():
            print(f"Không thể mở camera với index: {camera_index}")
            return

        detector = cv2.QRCodeDetector()

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Không thể nhận frame từ camera. Đang thoát...")
                break

            value, points, _ = detector.detectAndDecode(frame)

            current_time = round(time.time())
            if value and (current_time - last_qr_time > 5 or value != last_qr_value):
                name, msv = value.split("|")
                data = db.query(DB_STUDENT, '*', f'`msv` = "{msv}"')
                if data != []:
                    data = data[0]
                    if data[-2] != 'Đã điểm danh':
                        print(data)
                        if data[-2].strip() == '' or data[-2] == "Chưa điểm danh hôm nay":
                            db.update(DB_STUDENT, f'`time_in` = {current_time}, `status` = "Chưa kết thúc"', f'`msv` = "{msv}"')
                        elif data[-2] == "Chưa kết thúc":
                            db.update(DB_STUDENT, f'`time_out` = {current_time}, `status` = "Đã điểm danh"', f'`msv` = "{msv}"')
                    self.loadAccount.emit()
                last_qr_value = value
                last_qr_time = current_time

            if self.gui.show_cam == True:cv2.imshow('Camera', frame)
            else: cv2.destroyAllWindows()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.gui.show_cam = False
                self.gui.data['show_cam'] = "Show camera screen"

        self.cap.release()
        cv2.destroyAllWindows()
    
    def stop(self):
        try:
            self.cap.release()
            # cv2.destroyAllWindows()
        except: pass
        self.terminate()