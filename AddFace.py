import sys
import os, time
import cognitive_face as CF
import keys as global_var
import urllib
import sqlite3
import requests
from database import connectDatabase
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
Key = global_var.key	
# connection to Microsoft cognitive face
CF.Key.set(Key)
BASE_URL = global_var.BASE_URL
CF.BaseUrl.set(BASE_URL)

db = connectDatabase()
def add_person_face_main(ufile):
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	img_folder = os.path.join(current_dir,"dataset/" + ufile)
	person_id = db.getPersonId(ufile[-2:])
	for i in os.listdir(img_folder):
		if i.endswith('.jpg'):
			print('Filename: ',i)
			# changing pathname to url
			img_url = urllib.request.pathname2url(os.path.join(img_folder,i))
			img_url = img_url[3:]										
			detect = CF.face.detect(img_url)				# detect the face
			if len(detect) != 1:
				print('From the image face is not detected')
			else:
				add_face = CF.person.add_face(img_url,global_var.personGroupId,person_id)
				print(add_face)
					
	
