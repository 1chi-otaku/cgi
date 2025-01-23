import json

class ApiController:
    def end_with(self, status_code: int=200, data: any= None):
        if status_code != 200:
            print(f"Status: {status_code} {self.phrase_by_code(status_code)}")
        if data != None:
            print("Content-Type: text/plain; charset=utf-8")
            print()
            print(json.dumps(data))
            exit()
        else:
            print("Content-Length: 0")
            print()
        exit()


    def phrase_by_code(self, status_code: int) -> str:
        match status_code:
            case 200: return "OK"
            case 405: return "Methond Not Allowed"
            case 415: return "Unsupported Media Type"
            case _: return ""
    

    def serve(self, access_manager_data):
        self.access_manager_data = access_manager_data
        action_name = f"do_{access_manager_data["envs"]["REQUEST_METHOD"].lower()}"
        controller_action = getattr( self, action_name, None)
        if controller_action == None:
            self.end_with(405, f"Method {access_manager_data["envs"]["REQUEST_METHOD"]} not supported in requested endpoint")
        else:
            self.end_with(data =controller_action())
