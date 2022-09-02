from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required,get_jwt_identity
from models.child import ChildModel


class Child(Resource):
    _user_parser = reqparse.RequestParser()
    _user_parser.add_argument('child_name',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )
    _user_parser.add_argument('child_age',
                              type=int,
                              required=True,
                              help="This field cannot be blank."
                              )
    _user_parser.add_argument('child_gender',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )
    _user_parser.add_argument('serial_number',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )

    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        child = ChildModel.find_by_user_id(user_id)
        if child:
            return {'child' : child.json()}, 200

        return {'message': 'Child not found'}, 404

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()

        data = Child._user_parser.parse_args()

        if ChildModel.find_by_serial_number(data['serial_number']):
            return {'message': "A serial_number '{}' already exists.".format(data['serial_number'])}, 400

        child = ChildModel(user_id, data['child_name'],data['child_age'],data['child_gender'],data['serial_number'])

        try:
            child.save_to_db()
        except:
            return {"message": "An error occurred creating the child info."}, 500

        return child.json(), 201

    @jwt_required()
    def delete(self):
        user_id = get_jwt_identity()

        child = ChildModel.find_by_user_id(user_id)
        if child:
            child.delete_from_db()

        return {'message': 'Child deleted'}, 200

    @jwt_required()
    def put(self):
        user_id = get_jwt_identity()

        data = Child._user_parser.parse_args()
        child = ChildModel.find_by_user_id(user_id)

        if child:
            child.name = data['child_name']
            child.age = data['child_age']
            child.gender = data['child_gender']
            child.serial_number = data['serial_number']
        else:
            child = ChildModel(user_id,data['child_name'],data['child_age'],data['child_gender'],data['serial_number'])

        child.save_to_db()

        return child.json(), 201

class ChildList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        childs = [child.json() for child in ChildModel.find_all_with_user_id(user_id)]
        return {'childs': childs}
