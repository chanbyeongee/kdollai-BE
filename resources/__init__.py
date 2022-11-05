from packages.doll_AI.aimodel import AIModel

main_ai = AIModel()

def create_api(api):
    from .user import UserRegister, User, UserLogin
    from .chat import RangeChatList, AllChatList,YMDChatList,NumberChatList
    from .child import Child,ChildList
    from .stat_emo import EmotionRangeStatList, EmotionAllStatList, EmotionYMDStatList, EmotionNumberStatList
    from .stat_bad import BadRangeStatList, BadAllStatList, BadYMDStatList, BadNumberStatList
    from .stat_relation import RelationRangeStatList, RelationAllStatList, RelationYMDStatList, RelationNumberStatList
    from .stat_topic import TopicRangeStatList, TopicAllStatList, TopicYMDStatList, TopicNumberStatList
    from .statistic import RecentWords, RecentUse, RecentScenario, RecentEmotions
    from .reservations import GetCounselors, GetPageInfo,MakeReservation,\
        GetUserReservation,GetCounselorReservation, AcceptReservation, RejectReservation,CancleReservation
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
    # simplestat
    api.add_resource(RecentWords, '/stat/recent/words/today/<string:day>')
    api.add_resource(RecentUse,'/stat/recent/use')
    api.add_resource(RecentEmotions, '/stat/recent/emotions/<string:day>')
    api.add_resource(RecentScenario, '/stat/recent/scenario/<string:day>')

    #emotion
    api.add_resource(EmotionNumberStatList, '/stat/emotion/latest/<string:date>/before/<int:number>')
    api.add_resource(EmotionRangeStatList, '/stat/emotion/latest/<string:end>/from/<string:begin>')
    api.add_resource(EmotionYMDStatList, '/stat/emotion/day/<string:day>')
    api.add_resource(EmotionAllStatList, '/stat/emotion/allday')

    #situation
    api.add_resource(TopicNumberStatList, '/stat/topic/latest/<string:date>/before/<int:number>')
    api.add_resource(TopicRangeStatList, '/stat/topic/latest/<string:end>/from/<string:begin>')
    api.add_resource(TopicYMDStatList, '/stat/topic/day/<string:day>')
    api.add_resource(TopicAllStatList, '/stat/topic/allday')

    #badwords
    api.add_resource(BadNumberStatList, '/stat/bad/latest/<string:date>/before/<int:number>')
    api.add_resource(BadRangeStatList, '/stat/bad/latest/<string:end>/from/<string:begin>')
    api.add_resource(BadYMDStatList, '/stat/bad/day/<string:day>')
    api.add_resource(BadAllStatList, '/stat/bad/allday')

    #relationship
    api.add_resource(RelationNumberStatList, '/stat/relation/latest/<string:date>/before/<int:number>')
    api.add_resource(RelationRangeStatList, '/stat/relation/latest/<string:end>/from/<string:begin>')
    api.add_resource(RelationYMDStatList, '/stat/relation/day/<string:day>')
    api.add_resource(RelationAllStatList, '/stat/relation/allday')

    # belonged to user
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user')
    api.add_resource(UserLogin, '/login')

    # belonged to counselor
    api.add_resource(GetCounselors, '/consultings')
    api.add_resource(GetPageInfo, '/consulting/page/<int:id>')

    #get reservations
    api.add_resource(MakeReservation, '/reservation/make')
    api.add_resource(GetUserReservation, '/reservations/user/<int:id>')
    api.add_resource(GetCounselorReservation, '/reservations/counselor/<int:id>')
    api.add_resource(AcceptReservation, '/reservation/<int:id>/accept')
    api.add_resource(RejectReservation, '/reservation/<int:id>/reject')
    api.add_resource(CancleReservation, '/reservation/<int:id>/cancle')

def create_socketio(sock):
    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


