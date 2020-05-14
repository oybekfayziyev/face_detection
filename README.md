                    Automatic Checker System

Used Microsoft Cognitive Face Api in order to recognize faces in the picture 
In order to run the program first need to install requirements:
    pip install -r requirements.txt




databse.py | connection with sqlite3 database
dataset | (A dataset) contains dir with faces of each student
add_student.py | make dataset and entry in DB
create_person.py | generate personId from microsoft server
add_person_faces.py | generate faceIds for each face in dataset 
train.py | trains the model in microsoft server
get_status.py | show the current status 
spreadsheet.py | makes xls sheet named reports.xlsx
detect.py | detect faces in test picture and crops and put them in Cropped_faces directory
identify.py | identify each face and marks the attendance 
