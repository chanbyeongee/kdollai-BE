from packages.pue_AI.aimodel import AIModel

main_ai = AIModel()
main_ai.model_loader()

def create_api(api):
    from .user import UserRegister, User, UserLogin
    from .chat import RangeChatList, AllChatList,YMDChatList,NumberChatList
    from .child import Child,ChildList
    from .statistic import RangeStatistic, ListStatistic

    api.add_resource(Child, '/child')
    api.add_resource(ChildList, '/childs')

    #chat
    api.add_resource(NumberChatList, '/chats/latest/<string:date>/number/<int:number>')
    api.add_resource(RangeChatList, '/chats/latest/<string:end>/from/<string:begin>')
    api.add_resource(YMDChatList, '/chats/day/<string:day>')
    api.add_resource(AllChatList, '/chats/allday')

    # belonged to chart
    api.add_resource(RangeStatistic,'/statistic/range/sday/<string:sday>/eday/<string:eday>')
    api.add_resource(ListStatistic, '/statistic/list/sday/<string:sday>/eday/<string:eday>')
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user')
    api.add_resource(UserLogin, '/login')

def create_socketio(sock):
    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


