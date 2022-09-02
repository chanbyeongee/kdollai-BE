# from packages.k_doll_ai_chatbot.transformer_models.aimodel import AIModel

# main_ai = AIModel()
# main_ai.model_loader()

def create_api(api):
    from .user import UserRegister, User, UserLogin
    from .chat import Chat, ChatList,ChatDay
    from .child import Child,ChildList
    from .statistic import Statistic

    api.add_resource(Child, '/child')
    api.add_resource(ChildList, '/childs')
    api.add_resource(ChatDay, '/chat/day/<string:day>')
    api.add_resource(Chat, '/chat/detail/<string:date>')
    api.add_resource(ChatList, '/chats')
    api.add_resource(Statistic,'/statistic/sday/<string:sday>/eday/<string:eday>')
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user')
    api.add_resource(UserLogin, '/login')

def create_socketio(sock):
    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


