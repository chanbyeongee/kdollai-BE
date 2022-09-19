from flask_restful import Resource, reqparse
from models.chat import ChatModel
from models.child import ChildModel

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)

class NumberChatList(Resource):
    def get(self,date, number):
        child_id = 1
        chats = [chat.json() for chat in ChatModel.find_by_number_with_child_id(child_id,date,number)]
        return {'chats': chats}, 200

class RangeChatList(Resource):
    def get(self,end,begin):
        child_id = 1
        chats = [chat.json() for chat in ChatModel.find_range_with_child_id(child_id, begin,end)]

        return {'chats': chats}, 200

class YMDChatList(Resource):
    def get(self,day):
        child_id = 1
        chats = [chat.json() for chat in ChatModel.find_all_by_dateYMD_with_child_id(child_id,day)]

        return {'chats': chats},200

class AllChatList(Resource):
    def get(self):
        child_id = 1
        chats = [chat.json() for chat in ChatModel.find_all_with_child_id(child_id)]

        return {'chats': chats},200
