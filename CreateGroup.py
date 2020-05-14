import cognitive_face as CF
from keys import personGroupId,key,BASE_URL
import sys

# key = 'c896f38adb3946cbba4457ecdc2a35f1'
# connection to the cognitive face api
def create_person_group_main():
    CF.Key.set(key)
    url = BASE_URL 
    CF.BaseUrl.set(url)
    # getting list
    personGroups = CF.person_group.lists()
    for personGroup in personGroups:
        if personGroupId == personGroup['personGroupId']:
            print(personGroupId + " already exists.")
            sys.exit()
    # if person id is not exist create person id
    res = CF.person_group.create(personGroupId)
    print(res)
