import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
# import sqlite3
from database import connectDatabase
import os                                                                       # for creating folders

db = connectDatabase()
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)

face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# if student exist in the database
# updates otherwise inserts
def insertOrUpdate(Id, Name, roll) :                                            # this function is for database
    isExist = db.isExist(Id)
    print('IsExist: ',isExist)
    if isExist:
        db.update(Id,Name)
        db.update(Id,roll,'Roll')
    else:
        db.insert(Id,Name,roll)

def add_student_main(name, roll):

    Id = roll[-2:]
    insertOrUpdate(Id, name, roll)                                                  # calling the sqlite3 database


    folderName = "user" + Id                                                        # creating the person or user folder
    folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    sampleNum = 0

    while(True):
        ret, img = cap.read()                                             # reading the camera input
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
        faces = face_detection.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5,minSize = (30,30))
        print('faces:',faces)
        for (x,y,w,h) in faces:                                                # loop will run for each face detected
            sampleNum += 1
            cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg",
                        img[y:y+h,x:x+w])                                            # Saving the faces
            size = img.shape
            print(size)
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0) ,2)                        # Forming the rectangle
            cv2.waitKey(200)                                                        # waiting time of 200 milisecond
        cv2.imshow('frame', img)                                                    # showing the video input from camera on window
        cv2.waitKey(1)
        if(sampleNum >= 10):                                                        # will take 20 faces
            break

    cap.release()                                                                   # turning the webcam off
    cv2.destroyAllWindows()                                                         # Closing all the opened windows
