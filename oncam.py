from imageai.Detection import ObjectDetection
#from imageai.Detection import VideoObjectDetection
import os
import cv2
import numpy
execution_path = os.getcwd()

cam = cv2.VideoCapture(0)
#detector = VideoObjectDetection()
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
#detector.loadModel(detection_speed="fast")
mirror = True
while True:
    ret_val, img = cam.read()
    if mirror:
      img = cv2.flip(img, 1)
      #detected_image_array, detections = detector.detectObjectsFromImage(output_type="array", input_image="array" )
      #detector.loadModel(detection_speed="fast")
    
      detected_image_array,detections = detector.detectObjectsFromImage(input_type="array", input_image=img , output_type="array")
      ###DETECED ALL
      #custom_objects = detector.CustomObjects(person=True)
      #detected_image_array,detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects,input_type="array", input_image=img , output_type="array")
      ###CUSTOMDETECED 
        #video_path = detector.detectObjectsFromVideo(camera_input=camera,output_file_path=os.path.join(execution_path, "camera_detected_video"), frames_per_second=20, log_progress=True, minimum_percentage_probability=40)

       # % 

      for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        print("--------------------------------")

    
      
      cv2.imshow('my webcam', detected_image_array)
      if cv2.waitKey(1) == 27:
        break # กด esc เพื่อออก


    





camera.release()
cv2.destroyAllWindows()

