from flask_socketio import Namespace, emit
from flask import session, request
from app import main_ai

class ChatNamespace(Namespace):

    def on_connect(self):
        print("Client connected",)
        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected", )
        #sessioned = session.get()

    def on_message(self,data):
        print(data)
        processed_data = main_ai.run("Hello",data)
        print(processed_data["System_Corpus"])
        emit("server_response",processed_data["System_Corpus"])

    #
    #
    # def get(self, name):
    #     employee = EmployeeModel.find_by_name(name)
    #     if employee:
    #         return employee.json()
    #     return {'message': 'Employee not found'}, 404
    #
    #
    # def post(self, name):
    #     data = Employee._user_parser.parse_args()
    #
    #     if EmployeeModel.find_by_serial(data['serial_number']):
    #         return {'message': "A employee with serial '{}' already exists.".format(data['serial'])}, 400
    #
    #     employee = EmployeeModel(name, **data)
    #
    #     try:
    #         employee.save_to_db()
    #     except:
    #         return {"message": "An error occurred creating the store."}, 500
    #
    #     return employee.json(), 201
    #
    #
    # def delete(self, name):
    #     employee = EmployeeModel.find_by_name(name)
    #     if employee:
    #         employee.delete_from_db()
    #
    #     return {'message': 'Store deleted'}
    #
    # def put(self, name):
    #     data = Employee.parser.parse_args()
    #     empolyee = EmployeeModel.find_by_name(name)
    #
    #     if empolyee:
    #         empolyee.name = data['name']
    #         empolyee.birth = data['birth']
    #         empolyee.gender = data['gender']
    #         empolyee.serial_number = data['serial_number']
    #     else:
    #         empolyee = EmployeeModel(name, **data)
    #
    #     empolyee.save_to_db()
    #
    #     return empolyee.json()

class EmployeeList(Resource):
    @jwt_required
    def get(self):
        employees = [employee.json() for employee in EmployeeModel.find_all()]
        return {'employees': employees}
