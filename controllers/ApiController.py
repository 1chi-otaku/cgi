import json
from models.RestModel import *
class ApiController:

    def __init__(self):
        self.response = RestModel()

        
    def end_with(self, status_code: int=200, data: any= None):
        if status_code != 200:
            self.response.status = RestStatus(status_code)
            print(f"Status: {status_code} {self.response.status.reasonPhrase}")
        self.response.data = data
        print("Content-Type: application/json; charset=utf-8")
        print()
        print(json.dumps(dict(self.response.__dict__())))
        exit()


    def serve(self, access_manager_data):
        self.access_manager_data = access_manager_data
        method = access_manager_data["envs"]["REQUEST_METHOD"]

        self.response.meta = RestMeta({
            'service': 'Server Application',
            'group': 'KN-P-213',
            'method': method
        })
        action_name = f"do_{method.lower()}"
        controller_action = getattr( self, action_name, None)
        if controller_action == None:
            self.end_with(405, f"Method {method} not supported in requested endpoint")
        else:
            self.end_with(data =controller_action())
