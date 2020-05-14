# connection to database
import sqlite3

class connectDatabase:

    def __init__(self):
        self.connect = sqlite3.connect('Face-Database')        
    
    def getPersonId(self,id):
        query = "SELECT * FROM Students WHERE ID = " + id
        cursor = self.connect.cursor()
        cursor.execute(query)        
        row = cursor.fetchone()
        person_id = row[3]        
        return person_id

    def insert(self,id,name,roll=None):
        query = "INSERT INTO Students(ID, Name, Roll) VALUES(?, ?, ?)"
        cursor = self.connect.execute(query,(id,name,roll))
        self.connect.commit()
    
    def update(self,id,data,value = 'Name'):
        query = "UPDATE Students SET %s = ? WHERE ID = ?"%value
        cursor = self.connect.execute(query,(data,id))
        self.connect.commit()

    def isExist(self,id):
        query = "SELECT * FROM Students WHERE ID = " + id
        cursor = self.connect.execute(query)       
        for row in cursor:
            return True
        
        return False
       
    def __del__(self):
   
        self.connect.close()
