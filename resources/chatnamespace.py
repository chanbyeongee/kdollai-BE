import requests
from flask_socketio import Namespace, emit, join_room, leave_room, close_room
from flask import session, request
from resources import main_ai
from models.child import ChildModel
from models.chat import ChatModel
from models.statistic import StatisticModel, emotion_weight, init_emotion
from datetime import datetime
from pytz import timezone
import json
import eventlet

rooms={
}

simple_scenarios={
    0:"정말? 무슨일 있었어?",
    1:"저런... 많이 힘들었겠다. 부모님은 이 사실에 대해 알고 계시니?",
    2:"부모님은 항상 채민이를 사랑하고 있어. 부모님께 먼저 말을 걸어 보는건 어떠니?",
    3:"그건 부모님이 너무 바쁘셔서 실수하신것 같아... 다시한번 말씀드리면 진지하게 들어주실 거야"
}
counter=0
class ChatNamespace(Namespace):
    user_type = ""
    room = ""
    child_id = None

    def on_connect(self):
        print("Client connected")
        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected")
        leave_room(request.sid)
        close_room(request.sid)
        if rooms[self.room]["SUPERVISOR"] == request.sid:
            rooms[self.room]["SUPERVISOR"] = None
        else :
            rooms[self.room]["USER"] = None
        #sessioned = session.get()

    def on_join(self,data):
        global counter
        print(f"Join room with usertype: {data['type']} serial_number: {data['serial_number']} sid:{request.sid}")

        self.user_type = data['type']
        self.room = data['serial_number']

        join_room(request.sid)
        counter=0
        if self.room not in rooms.keys():
            rooms[self.room] = {"SUPERVISOR":None,"USER":None}

        rooms[self.room][self.user_type] = request.sid

        self.child_id = ChildModel.find_by_serial(data['serial_number']).id

    def on_SEND_MESSAGE(self,data):
        global counter
        if not self.child_id :
            emit("RECEIVE_MESSAGE",{"message":"please join with serial_number"})
            return

        day, full_date, real_time = ChatNamespace.time_shift()

        print(data)
        print("DAY: ", day)
        print("TIME: ", real_time)



        if data["type"] == "USER" :

            my_chat = ChatModel(self.child_id, day, full_date, real_time, data["type"], data['message'])
            my_chat.save_to_db()

            if rooms[self.room]["SUPERVISOR"] :
                emit(
                    "RECEIVE_MESSAGE",
                    {"response": data['message'],
                     "day": day, 'time': real_time},
                    to=rooms[self.room]["SUPERVISOR"],
                )

            else:
                processed_data = main_ai.run("Hello", data['message'])
                day, full_date, real_time = ChatNamespace.time_shift()

                my_chat = ChatModel(self.child_id, day, full_date, real_time, "BOT", simple_scenarios[counter])
                my_chat.save_to_db()

                emit(
                    "RECEIVE_MESSAGE",
                    {
                        "response": simple_scenarios[counter],
                        "day": day, 'time': real_time},
                        to=rooms[self.room]["USER"],
                )
                counter+=1
                counter%=4

        elif data["type"] == "SUPERVISOR":
            day, full_date, real_time = ChatNamespace.time_shift()

            if rooms[self.room]["USER"]:
                my_chat = ChatModel(self.child_id, day, full_date, real_time, "SUPERVISOR", data['message'])
                my_chat.save_to_db()
                emit(
                    "RECEIVE_MESSAGE",
                    {"response": data['message'],
                     "day": day, 'time': real_time},
                    to=rooms[self.room]["USER"],
                )
            else :
                emit(
                    "RECEIVE_MESSAGE",
                    {"response": "현재 연결된 인형이 없습니다. 인형이 켜져있는 상태인지 확인해보세요.",
                     "day": day, 'time': real_time},
                    to=rooms[self.room]["SUPERVISOR"],
                )

        eventlet.sleep(0)

    @staticmethod
    def time_shift():
        now = datetime.now(timezone('Asia/Seoul'))
        full_date = now.strftime("%Y%m%d%H%M%S")
        day = now.strftime("%Y%m%d")

        ampm = now.strftime('%p')
        ampm_kr = '오전' if ampm == 'AM' else '오후'

        real_time = f"{ampm_kr} {now.strftime('%#H:%M')}"

        return day, full_date, real_time

    @staticmethod
    def stat_handler(stat,processed_data,msg):
        # emotion handler
        temp_emotion = json.loads(stat.emotions)
        temp_emotion[processed_data['Emotion']] += 1
        stat.emotions = json.dumps(temp_emotion)
        stat.emotion_score += emotion_weight[processed_data['Emotion']]

        # badness handler
        if processed_data["Danger_Flag"]:
            temp_badwords = json.loads(stat.badwords)
            for word in processed_data["Danger_Words"]:
                temp_badwords[word] += 1
            temp_badsentences = json.loads(stat.bad_sentences)
            temp_badsentences['sentences'].append(msg)
            stat.badwords = json.dumps(temp_badwords)
            stat.bad_sentences = json.dumps(temp_badsentences)

        # situation handler
        temp_topic = json.loads(stat.situation)
        temp_topic[processed_data["Topic"]]["total"] += 1
        temp_topic[processed_data["Topic"]]["emotion"][processed_data['Emotion']] += 1
        if processed_data["SubTopic"]:
            temp_subtopic = json.loads(stat.subtopic)
            temp_subtopic[processed_data["SubTopic"]]["total"] += 1
            temp_subtopic[processed_data["SubTopic"]]["emotion"][processed_data['Emotion']] += 1
            stat.subtopic = json.dumps(temp_subtopic)
        stat.situation = json.dumps(temp_topic)

        # relationship
        temp_relationship = json.loads(stat.relation_ship)

        for key in processed_data["NER"]:
            if key not in temp_relationship.keys():
                temp_relationship[key] = {}
                temp_relationship[key]["emotion"] = init_emotion.copy()
            temp_relationship[key]["emotion"][processed_data["Emotion"]] += 1
        stat.relation_ship = json.dumps(temp_relationship)

        stat.save_to_db()
