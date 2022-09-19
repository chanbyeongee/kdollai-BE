from .MOCK import make_dummy
from flask_restful import Resource, reqparse, request

class MakeMock(Resource):
    def get(self):
        make_dummy()
        return {"message":"OK"},200