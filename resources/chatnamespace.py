from flask_socketio import Namespace, emit
from flask import session, request
from resources import main_ai
from models.child import ChildModel
from models.chat import ChatModel
from datetime import datetime
from pytz import timezone

class ChatNamespace(Namespace):

    def on_connect(self):
        print("Client connected",)
        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected", )
        #sessioned = session.get()

    def on_SET_CHILD_ID(self,data):
        self.child_id = ChildModel.find_by_serial(data['serial_number']).id

    def on_SEND_MESSAGE(self,data):
        print(data)
        now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")
        print("DAY: ", now[:8])
        print("TIME: ", now[8:])

        my_chat = ChatModel(self.child_id, now[:8], now, "USER", data['message'])
        my_chat.save_to_db()

        processed_data = main_ai.run("Hello", data['message'])

        now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")
        my_chat = ChatModel(self.child_id, now[:8], now,"BOT", processed_data["System_Corpus"])
        my_chat.save_to_db()

        emit("RECEIVE_MESSAGE", {"response": processed_data["System_Corpus"], "day": now[:8], 'time': now[8:]})

