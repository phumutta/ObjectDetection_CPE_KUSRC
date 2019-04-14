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
        
       

#button
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.stop)
       

#camera
        self.camera = cv2.VideoCapture(0)
#timer
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update)

    def start(self):
        model=self.ui.comboBox.currentText()
        print(model)
        
        if model == "YOLO V3":
            self.yolo()
        elif model == "YOLO TINY":
            self.yolo_tiny()
        elif model == "RESNET":
            self.resnet()


        
           
 
    def yolo(self):
        self.update_timer.start(30)
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath( os.path.join(self.execution_path , "yolo.h5"))
        self.detector.loadModel(detection_speed="flash")
        print("###you are use yolo model###")
    def yolo_tiny(self):
        self.update_timer.start(30)
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath( os.path.join(self.execution_path , "yolo-tiny.h5"))
        self.detector.loadModel(detection_speed="flash")
        print("###you are use yolo_tiny model###")

    def resnet(self):
        self.update_timer.start(30)
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath( os.path.join(self.execution_path , "resnet50_coco_best_v2.0.1.h5"))
        self.detector.loadModel(detection_speed="fastest")
        print("###you are use resnet model###")

    def stop(self):
        self.update_timer.stop()
        

    def update(self):
        
        ret,frame =self.camera.read()
        frame=cv2.flip(frame,1)
        #detected
        custom=self.ui.comboBox_2.currentText()
        print(custom)
        if custom == "Person":
            custom_objects = self.detector.CustomObjects(person=True)
        elif custom == "orange":
            custom_objects = self.detector.CustomObjects(orange=True)
        elif custom == "Cell Phone":
            custom_objects = self.detector.CustomObjects(cell_phone=True)
        
        detected_image_array,detections = self.detector.detectCustomObjectsFromImage(custom_objects=custom_objects,input_type="array", input_image=frame , output_type="array")
        
        #detected_image_array, detections = self.detector.detectCustomObjectsFromImage(custom_objects=custom_objects,output_type="array",input_type="array", input_image= frame,display_percentage_probability=True, display_object_name=True)
        for eachObject in detections:
            print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
            
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
