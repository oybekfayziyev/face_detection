from AddFace import add_person_face_main
from AddPerson import add_student_main
from CreatePerson import create_person_main
from CreateGroup import create_person_group_main
from demo import demo_main
from detect import detect_main
from identify import identify_main, getStatus
from spreadsheet import spreadsheet_main

menu = ''''
    1. Add Person to Database
    2. Add Person Face
    3. Create Person
    4. Create Person Group
    5. Detect Face
    6. Status    
    7. Read List Student File
    8. DEMO
    9. Exit
'''

def main():    
    print('\n\n\tWelcome to Automatic Checker System:')
    print(menu)
    inp = input('Please provide one of the options: ')
    if inp == '1':
        name = input("Enter student's name : ")
        roll = input("Enter student's Roll Number : ")
        add_student_main(name,roll)
    elif inp == '2':
        userfile = input('Enter user file name: ')
        add_person_face_main(userfile)
    elif inp == '3':
        userfile = input('Enter user file name: ')
        create_person_main(userfile)
    elif inp == '4':
        create_person_group_main()
    elif inp == '5':
        img = input('Enter Image Name: ')
        detect_main(img)
    elif inp == '6':
        getStatus()    
    elif inp == '7':
        spreadsheet_main();
    elif inp == '8':
        demo_main()
    
    elif inp == '9':
        exit()
    
    else:
        print('Please select only given options!')

        


if __name__ == "__main__":
   
    main()