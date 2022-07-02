from flask_restful import Resource, reqparse
from models.chat import ChatModel

class Chat(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('direction',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )
    parser.add_argument('line',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )
    parser.add_argument('doll_id',
                            type=int,
                            required=True,
                            help="This field cannot be blank."
                            )
    def get(self, employee_id, date):
        chat = ChatModel.find_by_date_with_employee_id(employee_id,date)
        if chat:
            return chat.json(), 200
        return {'message': 'Chat not found'}, 404

    def post(self, employee_id,date):
        data = Chat.parser.parse_args()

        if ChatModel.find_by_date_with_employee_id(employee_id,date):
            return {'message': "A chat with date '{}' already exists.".format(data['date'])}, 400

        chat = ChatModel(employee_id, date, **data)

        try:
            chat.save_to_db()
        except Exception as e:
            return {"message": "An error occurred creating the chat."}, 500

        return chat.json(), 201

    def delete(self, employee_id, date):
        chat = ChatModel.find_by_date_with_employee_id(employee_id,date)
        if chat:
            chat.delete_from_db()

        return {'message': 'Chat deleted'}, 200

class ChatList(Resource):
    def get(self, employee_id):
        chats = [chat.json() for chat in ChatModel.find_all_with_employee_id(employee_id)]
        return {'chats': chats}
