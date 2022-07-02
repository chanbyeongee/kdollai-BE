from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.employee import EmployeeModel


class Employee(Resource):
    _user_parser = reqparse.RequestParser()
    _user_parser.add_argument('birth',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )
    _user_parser.add_argument('gender',
                              type=int,
                              required=True,
                              help="This field cannot be blank."
                              )
    _user_parser.add_argument('serial_number',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )
    _user_parser.add_argument('user_id',
                              type=int,
                              required=True,
                              help="This field cannot be blank."
                              )

    parser = _user_parser
    parser.add_argument('birth',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )

    def get(self, user_id,name):
        employee = EmployeeModel.find_by_name_with_user_id(user_id,name)
        if employee:
            return employee.json(), 200
        return {'message': 'Employee not found'}, 404


    def post(self,user_id, name):
        data = Employee._user_parser.parse_args()

        if EmployeeModel.find_by_serial_with_user_id(user_id,data['serial_number']):
            return {'message': "A employee with serial '{}' already exists.".format(data['serial'])}, 400

        employee = EmployeeModel(user_id, name, **data)

        try:
            employee.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return employee.json(), 201


    def delete(self,user_id, name):
        employee = EmployeeModel.find_by_name_with_user_id(user_id,name)
        if employee:
            employee.delete_from_db()

        return {'message': 'Store deleted'}, 200

    def put(self, user_id, name):
        data = Employee.parser.parse_args()
        empolyee = EmployeeModel.find_by_name_with_user_id(user_id,name)

        if empolyee:
            empolyee.name = data['name']
            empolyee.birth = data['birth']
            empolyee.gender = data['gender']
            empolyee.serial_number = data['serial_number']
        else:
            empolyee = EmployeeModel(user_id, name, **data)

        empolyee.save_to_db()

        return empolyee.json(), 201

class EmployeeList(Resource):
    def get(self,user_id):
        employees = [employee.json() for employee in EmployeeModel.find_all_with_user_id(user_id)]
        return {'employees': employees}
