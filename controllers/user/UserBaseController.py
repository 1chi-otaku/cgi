#!C:/Users/1chi/AppData/Local/Microsoft/WindowsApps/python.exe


class UserBaseController():

    # def __init__(self):
    #     super().__init__()
    #     self.response.meta.add('ctr', 'UserBaseController')

    def do_get(self):
        return {'user' : 'works'}
    

    def serve(self, access_manager_data):
        self.access_manager_data = access_manager_data

    # def do_post(self):
    #     db_context = self.am_data.db_context
    #     user_dao = db_context.user_dao
    #     body = sys.stdin.read()
    #     if len(body) < 3:
    #         self.end_with(400, "Body must not be empty")

    #     try:
    #         j = json.loads(body)
    #     except ValueError:
    #         self.end_with(400, "Invalid JSON")

    #     try:
    #         user = User(
    #             name=j['user-name'],
    #             email=j['user-email'],
    #             password=j['user-password']
    #         )
    #     except ValueError:
    #         self.end_with(422, "Body must have props: 'user-name', 'user-email', 'user-password'" )

    #     if not user_dao.is_login_free(user.email):
    #         self.end_with(422, " 'user-email' in use")

    #     user_dao.add_user(user)

    #     return "User Created"