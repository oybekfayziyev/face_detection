import cv2
import os
import sys

def detect_main(image):
	# cam = cv2.VideoCapture(1)
	# Xml file for face detection
	if './pics' in image:		
		image = image;
	else:	
		image = './pics/' + image + '.jpg'
	
	face_detection = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	img = cv2.imread(image)	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
	
	if not os.path.exists('./StudentFaces'):
		os.makedirs('./StudentFaces')
	i = 0
	print("detected = {}".format(len(faces)))
	for x,y,w,h in faces:
		cv2.imwrite('./StudentFaces/face' + str(i + 1) + '.jpg', img[y:y+h,x:x+w])
		i = i + 1 

if __name__ == "__main__":
	if len(sys.argv) is not 1:
		
		detect_main(sys.argv[1])
