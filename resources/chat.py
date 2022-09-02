from flask_restful import Resource, reqparse
from models.chat import ChatModel
from models.child import ChildModel

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)

class Chat(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('direction',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )
    parser.add_argument('utterance',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )
    parser.add_argument('emotion',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
                            )
    parser.add_argument('situation',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    @jwt_required()
    def get(self, date):
        user_id = get_jwt_identity()

        child_id = ChildModel.find_by_user_id(user_id).id

        chat = ChatModel.find_by_date_with_child_id(child_id,date)
        if chat:
            return chat.json(), 200
        return {'message': 'Chat not found'}, 404

    @jwt_required()
    def post(self, date):

        user_id = get_jwt_identity()
        child_id = ChildModel.find_by_user_id(user_id).id

        data = Chat.parser.parse_args()

        date_YMD = date[:8]

        chat = ChatModel(child_id, date_YMD,date,date[8:], data['direction'],data['utterance'],data['emotion'],data['situation'])

        try:
            chat.save_to_db()
        except Exception as e:
            return {"message": "An error occurred creating the chat."}, 500

        return chat.json(), 201

    @jwt_required()
    def delete(self, date):
        user_id = get_jwt_identity()
        child_id = ChildModel.find_by_user_id(user_id).id

        chat = ChatModel.find_by_date_with_child_id(child_id ,date)
        if chat:
            chat.delete_from_db()

        return {'message': 'Chat deleted'}, 200

class ChatList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        child_id = ChildModel.find_by_user_id(user_id).id

        chats = [chat.json() for chat in ChatModel.find_all_with_child_id(child_id)]
        return {'chats': chats}

class ChatDay(Resource):
    @jwt_required()
    def get(self,day):
        user_id = get_jwt_identity()

        child_id = ChildModel.find_by_user_id(user_id).id

        chats = [chat.json() for chat in ChatModel.find_all_by_day_with_child_id(child_id,day)]
        return {'chats': chats}
