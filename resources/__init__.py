from packages.pue_AI.aimodel import AIModel

main_ai = AIModel()

def create_api(api):
    from .user import UserRegister, User, UserLogin
    from .chat import RangeChatList, AllChatList,YMDChatList,NumberChatList
    from .child import Child,ChildList
    from .statistic import RangeStatList, AllStatList, YMDStatList, NumberStatList
    from .develop import MakeMock

    # dev
    api.add_resource(MakeMock, '/make-mock')

    #child
    api.add_resource(Child, '/child')
    api.add_resource(ChildList, '/childs')

    #chat
    api.add_resource(NumberChatList, '/chats/latest/<string:date>/number/<int:number>')
    api.add_resource(RangeChatList, '/chats/latest/<string:end>/from/<string:begin>')
    api.add_resource(YMDChatList, '/chats/day/<string:day>')
    api.add_resource(AllChatList, '/chats/allday')

    # belonged to chart
    api.add_resource(NumberStatList, '/stat/latest/<string:date>/before/<int:number>')
    api.add_resource(RangeStatList, '/stat/latest/<string:end>/from/<string:begin>')
    api.add_resource(YMDStatList, '/stat/day/<string:day>')
    api.add_resource(AllStatList, '/stat/allday')


    # belonged to user
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user')
    api.add_resource(UserLogin, '/login')

def create_socketio(sock):
    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


