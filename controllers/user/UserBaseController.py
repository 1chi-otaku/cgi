#!C:/Users/1chi/AppData/Local/Microsoft/WindowsApps/python.exe
from  controllers.ApiController import ApiController
class UserBaseController( ApiController):
        
    def do_get(self):
        return {'user' : 'works'}
    
    

    