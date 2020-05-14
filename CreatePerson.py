import sys
import cognitive_face as CF
import keys as global_var
from database import connectDatabase
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def create_person_main(data):
    db = connectDatabase()       # initialization database
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    Key = global_var.key
    CF.Key.set(Key)

    BASE_URL = global_var.BASE_URL  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)

    print("personGroupId = %s" %(global_var.personGroupId))

    
    res = CF.person.create(global_var.personGroupId, data)
    #print("res = {}".format(res)) 
    print(res)
    Id = data[-2:]

    is_exist = db.isExist(Id)
    if is_exist:
        db.update(Id,res['personId'],'personId')
        
    print("Person ID successfully added to the database")
   