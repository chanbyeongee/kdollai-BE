def create_api(api):
    from .user import UserRegister, User, UserLogin
    from .chat import Chat, ChatList
    from .employee import Employee, EmployeeList

    api.add_resource(Employee, '/user/<int:user_id>/employee/<string:name>')
    api.add_resource(EmployeeList, '/user/<int:user_id>/employees')
    api.add_resource(Chat, '/employee/<int:employee_id>/chat/<string:date>')
    api.add_resource(ChatList, '/employee/<int:employee_id>/chats')
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(UserLogin, '/login')

def create_socketio(sock):

    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


