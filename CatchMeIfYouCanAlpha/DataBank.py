import re
import firebase_admin
from firebase_admin import db

class FireBaseDataBank(): 

    cred_obj = firebase_admin.credentials.Certificate('Data/key.json')
    
    def establish(self):
        
         firebase_admin.initialize_app(self.cred_obj,{
             
             'databaseURL': 'https://catchmeifyoucan-fe0ff-default-rtdb.europe-west1.firebasedatabase.app/'

             })
            
    
    def create_user(self, username, password,score): 
        ref = db.reference('Useres')
        ref.set({
                    username : {
                        'name' : username, 
                        'password' : password,
                        'score' : score
                    }
        })
        return True
    
    def update_user_score(self,username="",score=0): 
        ref = db.reference('Useres')
        emp_ref = ref.child(f'{username}') 
        emp_ref.update({
            'score' : score
        })

    def get_ref(self, username): 
        ref = db.reference('Useres')
        emp_ref = ref.child(username)
        return emp_ref

    def get_score(self, username): 
        child = self.get_ref(username)
        return child.child("score").get()
    
    def useres_ref(self): 
        return db.collections.Collection('Useres')
    

    def check_user_input_data(self, username, password): 
        child = self.get_ref(username)
        if(child.child("name").get() == username and child.child("password").get() == password): 
            return True
        else: 
            return False
    
    def check_user_exist(self, username): 
        child = self.get_ref(username)
        if(child.child("name").get() == username): 
            return True
        else: 
            return False

