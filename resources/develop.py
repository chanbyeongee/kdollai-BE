from .MOCK import *
from flask_restful import Resource, reqparse, request

class MakeMock(Resource):
    def get(self):
        counselors,child = make_account()
        make_chats(child)
        make_page(counselors)
        make_stats(child)
        return {"message":"OK"},200