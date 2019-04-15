from imageai.Detection import VideoObjectDetection
from imageai.Detection import ObjectDetection
import numpy as np
import cv2
import os

from guiai6 import Ui_Form
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
        self.ui.pushButton_2.clicked.connect(self.start)
        self.ui.pushButton.clicked.connect(self.stop)
       

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
        elif custom == "Orange":
            custom_objects = self.detector.CustomObjects(orange=True)
        elif custom == "Cell Phone":
            custom_objects = self.detector.CustomObjects(cell_phone=True)
        elif custom == "Bicycle":
            custom_objects = self.detector.CustomObjects(bicycle=True)
        elif custom == "Car":
            custom_objects = self.detector.CustomObjects(car=True)
        elif custom == "Motorcycle":
            custom_objects = self.detector.CustomObjects(motorcycle=True)
        elif custom == "Airplane":
            custom_objects = self.detector.CustomObjects(airplane=True)
        elif custom == "Bus":
            custom_objects = self.detector.CustomObjects(bus=True)
        elif custom == "Train":
            custom_objects = self.detector.CustomObjects(train=True)
        elif custom == "Truck":
            custom_objects = self.detector.CustomObjects(truck=True)
        elif custom == "Boat":
            custom_objects = self.detector.CustomObjects(boat=True)
        elif custom == "Traffic Light":
            custom_objects = self.detector.CustomObjects(traffic_light=True)
        elif custom == "Fire Hydrant":
            custom_objects = self.detector.CustomObjects(fire_hydrant=True)
        elif custom == "Stop Sign":
            custom_objects = self.detector.CustomObjects(stop_sign=True)
        elif custom == "Giraffe":
            custom_objects = self.detector.CustomObjects(giraffe=True)
        elif custom == "Backpack":
            custom_objects = self.detector.CustomObjects(backpack=True)
        elif custom == "Umbrella":
            custom_objects = self.detector.CustomObjects(umbrella=True)
        elif custom == "Handbag":
            custom_objects = self.detector.CustomObjects(handbag=True)
        elif custom == "Tie":
            custom_objects = self.detector.CustomObjects(tie=True)
        elif custom == "Suitcase":
            custom_objects = self.detector.CustomObjects(suitcase=True)
        elif custom == "Frisbee":
            custom_objects = self.detector.CustomObjects(frisbee=True)
        #end first
            
        elif custom == "Skis":
            custom_objects = self.detector.CustomObjects(skis=True)
        elif custom == "Snowboard":
            custom_objects = self.detector.CustomObjects(snowboard=True)
        elif custom == "Sports Ball":
            custom_objects = self.detector.CustomObjects(sports_ball=True)
        elif custom == "Kite":
            custom_objects = self.detector.CustomObjects(kite=True)
        elif custom == "Baseball Bat":
            custom_objects = self.detector.CustomObjects(baseball_bat=True)
        elif custom == "Baseball Glove":
            custom_objects = self.detector.CustomObjects(baseball_glove=True)
        elif custom == "Skateboard":
            custom_objects = self.detector.CustomObjects(skateboard=True)
        elif custom == "Surfboard":
            custom_objects = self.detector.CustomObjects(surfboard=True)
        elif custom == "Tennis Rack":
            custom_objects = self.detector.CustomObjects( tennis_racket=True)
        elif custom == "Bottle":
            custom_objects = self.detector.CustomObjects(bottle=True)
        elif custom == "Wine Glass":
            custom_objects = self.detector.CustomObjects(wine_glass=True)
        elif custom == "Cup":
            custom_objects = self.detector.CustomObjects(cup=True)
        elif custom == "Fork":
            custom_objects = self.detector.CustomObjects(fork=True)
        elif custom == "Knife":
            custom_objects = self.detector.CustomObjects(knife=True)
        elif custom == "Spoon":
            custom_objects = self.detector.CustomObjects(spoon=True)
        elif custom == "Bowl":
            custom_objects = self.detector.CustomObjects(bowl=True)
        elif custom == "Banana":
            custom_objects = self.detector.CustomObjects(banana=True)
        elif custom == "Apple":
            custom_objects = self.detector.CustomObjects(apple=True)
        #end seco
        elif custom == "Sandwich":
            custom_objects = self.detector.CustomObjects(sandwich=True)
        elif custom == "Broccoli":
            custom_objects = self.detector.CustomObjects(broccoli=True)
        elif custom == "Carrot":
            custom_objects = self.detector.CustomObjects(carrot=True)
        elif custom == "Hot Dog":
            custom_objects = self.detector.CustomObjects(hot_dog=True)
        elif custom == "Pizza":
            custom_objects = self.detector.CustomObjects(pizza=True)
        elif custom == "Cake":
            custom_objects = self.detector.CustomObjects(cake=True)
        elif custom == "Chair":
            custom_objects = self.detector.CustomObjects(chair=True)
        elif custom == "Couch":
            custom_objects = self.detector.CustomObjects(couch=True)
        elif custom == "Potted Plant":
            custom_objects = self.detector.CustomObjects(potted_plant=True)
        elif custom == "bed":
            custom_objects = self.detector.CustomObjects(bed=True)
        elif custom == "Dining Table":
            custom_objects = self.detector.CustomObjects(dining_table=True)
        elif custom == "Toilet":
            custom_objects = self.detector.CustomObjects(toilet=True)
        elif custom == "Tv":
            custom_objects = self.detector.CustomObjects(tv=True)
        elif custom == "Laptop":
            custom_objects = self.detector.CustomObjects(laptop=True)
        elif custom == "Mouse":
            custom_objects = self.detector.CustomObjects(mouse=True)
        elif custom == "Remote":
            custom_objects = self.detector.CustomObjects(remote=True)
        elif custom == "Keyboard":
            custom_objects = self.detector.CustomObjects(keyboard=True)
        elif custom == "Microwave":
            custom_objects = self.detector.CustomObjects(microwave=True)
        elif custom == "Oven":
            custom_objects = self.detector.CustomObjects(oven=True)
        elif custom == "Toaster":
            custom_objects = self.detector.CustomObjects(toaster=True)
        elif custom == "Sink":
            custom_objects = self.detector.CustomObjects(sink=True)
        #end th
        elif custom == "Refrigerator":
            custom_objects = self.detector.CustomObjects(refrigerator=True)
        elif custom == "Book":
            custom_objects = self.detector.CustomObjects(book=True)
        elif custom == "Clock":
            custom_objects = self.detector.CustomObjects(clock=True)
        elif custom == "Vase":
            custom_objects = self.detector.CustomObjects(vase=True)
        elif custom == "Scissors":
            custom_objects = self.detector.CustomObjects(scissors=True)
        elif custom == "Teddy Bear":
            custom_objects = self.detector.CustomObjects(teddy_bear=True)
        elif custom == "Hair Dryer":
            custom_objects = self.detector.CustomObjects(hair_dryer=True)
        elif custom == "Toothbrush":
            custom_objects = self.detector.CustomObjects(toothbrush=True)
        #end fo
        elif custom == "Parking Meter":
            custom_objects = self.detector.CustomObjects(parking_meter=True)
        elif custom == "Bench":
            custom_objects = self.detector.CustomObjects(bench=True)
        elif custom == "Bird":
            custom_objects = self.detector.CustomObjects(bird=True)
        elif custom == "Cat":
            custom_objects = self.detector.CustomObjects(cat=True)
        elif custom == "Dog":
            custom_objects = self.detector.CustomObjects(dog=True)
        elif custom == "Horse":
            custom_objects = self.detector.CustomObjects(horse=True)
        elif custom == "Sheep":
            custom_objects = self.detector.CustomObjects(sheep=True)
        elif custom == "Cow":
            custom_objects = self.detector.CustomObjects(cow=True)
        elif custom == "Elephant":
            custom_objects = self.detector.CustomObjects(elephant=True)
        elif custom == "Bear":
            custom_objects = self.detector.CustomObjects(bear=True)
        elif custom == "Zebra":
            custom_objects = self.detector.CustomObjects(zebra=True)
        #end all
            
            
      
        
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
