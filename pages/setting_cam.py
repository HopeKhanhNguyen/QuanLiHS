from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui.setting_cam import Ui_Dialog
import cv2

class SettingCamera(QDialog, Ui_Dialog):
    index_cam = None
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.view_frame.setBaseSize(640, 480)
        
        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 // 60)
        self.scan_cam_btn.clicked.connect(self.scan_cameras)
        self.selected_cam_btn.clicked.connect(self.selected)
        self.list_camera.currentIndexChanged.connect(self.change_cam)
        self.scan_cameras()

    def change_cam(self):
        self.camera = cv2.VideoCapture(self.list_camera.currentIndex())
        
    def selected(self):
        if self.list_camera.currentText() != "Không có camera":
            self.index_cam = self.list_camera.currentIndex()
        self.accept()
        
    def scan_available_cameras(self):
        available_cameras = []
        for camera_index in range(5):
            camera = cv2.VideoCapture(camera_index)
            if camera.isOpened():
                camera_name = f"Camera {camera_index + 1}"
                available_cameras.append(camera_name)
                camera.release()
        return available_cameras

    def scan_cameras(self):
        self.available_cameras = self.scan_available_cameras()
        self.list_camera.clear()
        if self.available_cameras != []:
            for camera_name in self.available_cameras:
                self.list_camera.addItem(camera_name)
        else:
            self.list_camera.addItem("Không có camera")
    
    def update_frame(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.view_frame.setPixmap(QPixmap.fromImage(image))
    
    def closeEvent(self, event):
        self.camera.release()
        event.accept()