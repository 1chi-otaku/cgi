#!C:/Users/1chi/AppData/Local/Microsoft/WindowsApps/python.exe
from  controllers.ApiController import ApiController
class UserBaseController( ApiController):
    
    def __init__(self):
        super().__init__()
        self.response.meta.add('ctr', 'UserBaseController')
        
    
    def do_get(self):
        return {'user' : 'works'}
    
    def do_post(self): # Signup
        self.db_context = self.access_manager_data['db_context']
        return {'post' : 'works'}
        #return {'db': self.db_context.test_connection()}

    
    

    