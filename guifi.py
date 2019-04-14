from imageai.Detection import VideoObjectDetection
from imageai.Detection import ObjectDetection
import numpy as np
import cv2
import os

from guiai import Ui_Form
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt, QThread, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication

class StartWindows(QMainWindow):
    def __init__(self,camera=None, parent=None):
        super(StartWindows, self).__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
#detector
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.execution_path = os.getcwd()
        self.detector.setModelPath( os.path.join(self.execution_path , "yolo.h5"))
        self.detector.loadModel(detection_speed="fast")

#button
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.stop)

#camera
        self.camera = cv2.VideoCapture(0)
#timer
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update)

    def start(self): 
        self.update_timer.start(30)

    def stop(self):
        self.update_timer.stop()

    def update(self):
        ret,frame =self.camera.read()
        frame=cv2.flip(frame,1)
        #detected
        detected_image_array, detections = self.detector.detectCustomObjectsFromImage(output_type="array",input_type="array", input_image= frame,display_percentage_probability=True, display_object_name=True)
        #resize
        detected_image_array = cv2.resize(detected_image_array,(801,391))
        height, width, channel = detected_image_array.shape
        bytesPerLine = 3 * width

        qImg = QImage(detected_image_array.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        pixmap01 = QPixmap.fromImage(qImg)
        pixmap_image = QPixmap(pixmap01)
        self.ui.label.setPixmap(pixmap_image)
        self.ui.label.show();
if __name__ == '__main__':
    app = QApplication([])
    window = StartWindows()
    window.show()
    app.exit(app.exec_())
