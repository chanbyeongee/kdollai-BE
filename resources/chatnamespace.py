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
        print(data)
        self.child_id = ChildModel.find_by_serial(data['serial_number']).id

    def on_SEND_MESSAGE(self,data):
        print(data)
        now = datetime.now(timezone('Asia/Seoul'))
        full_date = now.strftime("%Y%m%d%H%M%S")
        day = now.strftime("%Y%m%d")

        ampm = now.strftime('%p')
        ampm_kr = '오전' if ampm == 'AM' else '오후'

        real_time = f"{ampm_kr} {now.strftime('%#H:%M')}"

        print("DAY: ", day)
        print("TIME: ", real_time)

        my_chat = ChatModel(self.child_id, day,full_date, real_time, "USER", data['message'])
        my_chat.save_to_db()

        processed_data = main_ai.run("Hello", data['message'])

        now = datetime.now(timezone('Asia/Seoul'))
        full_date = now.strftime("%Y%m%d%H%M%S")
        day = now.strftime("%Y%m%d")

        ampm = now.strftime('%p')
        ampm_kr = '오전' if ampm == 'AM' else '오후'

        real_time = f"{ampm_kr} {now.strftime('%#H:%M')}"

        my_chat = ChatModel(self.child_id, day,full_date, real_time,"BOT", processed_data["System_Corpus"])
        my_chat.save_to_db()

        emit("RECEIVE_MESSAGE", {"response": processed_data["System_Corpus"], "day": day, 'time': real_time})

