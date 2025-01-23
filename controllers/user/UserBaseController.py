#!C:/Users/1chi/AppData/Local/Microsoft/WindowsApps/python.exe
from  controllers.ApiController import ApiController
import sys
from data.user_dao import *
import json
class UserBaseController( ApiController):
    
    def __init__(self):
        super().__init__()
        self.response.meta.add('ctr', 'UserBaseController')
        
    
    def do_get(self):
        return {'user' : 'works'}
    
    def do_post(self): # Signup
        db_context = self.access_manager_data.db_context
        user_dao = db_context.user_dao
        body = sys.stdin.read()
        if len(body) < 3:
            self.end_with(400, "Body must not be empty")
        try:
            j = json.loads(body)
        except ValueError:
            self.end_with(400, "Body must be valid json")
       
        try:
            user = User(
                name= j['user-name'],
                email= j['user-email'],
                password= j['user-password'])
        except:
            self.end_with(422, "Body must have props: user-name, user-email, user-password")


        user_dao.add_user( user )
            
        return "Created"


    
    

    