from flask_restful import Resource, reqparse
from models.chat import ChatModel
from models.child import ChildModel

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)

class Statistic(Resource):
    parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, sday,eday):
        user_id = get_jwt_identity()

        child_id = ChildModel.find_by_user_id(user_id).id

        chat = ChatModel.find_by_date_with_child_id(child_id,date)
        if chat:
            return chat.json(), 200
        return {'message': 'Chat not found'}, 404

