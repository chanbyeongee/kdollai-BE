import requests
from flask_socketio import Namespace, emit, join_room, leave_room
from flask import session, request
from resources import main_ai
from models.child import ChildModel
from models.chat import ChatModel
from models.statistic import StatisticModel, emotion_weight, init_emotion
from datetime import datetime
from pytz import timezone
import json

rooms={}

class ChatNamespace(Namespace):
    user_type = ""
    room = ""
    child_id = None

    def on_connect(self):
        print("Client connected",)
        #sessioned= session.get()

    def on_disconnect(self):
        print("Client disconnected", )
        leave_room(self.room)
        rooms[self.room][self.user_type] = False
        #sessioned = session.get()

    def on_join(self,data):
        print(f"Join room with usertype: {data['type']} serial_number: {data['serial_number']}")

        self.room = data['serial_number']
        self.user_type = data['type']
        join_room(self.room)
        self.child_id = ChildModel.find_by_serial(data['serial_number']).id

        if not self.room in rooms.keys() :
            rooms[self.room] = dict()

        rooms[self.room][self.user_type] = True

    def on_SEND_MESSAGE(self,data):
        if not self.child_id :
            emit("RECEIVE_MESSAGE",{"message":"please join with serial_number"})
            return

        day, full_date, real_time = ChatNamespace.time_shift()

        print(data)
        print("DAY: ", day)
        print("TIME: ", real_time)

        my_chat = ChatModel(self.child_id, day,full_date, real_time, data["type"], data['message'])
        my_chat.save_to_db()

        if data["type"] == "CHILD" :
            processed_data = main_ai.run("Hello", data['message'])
            stat = StatisticModel.find_by_dateYMD_with_child_id(date=day,child_id=self.child_id)

            if not stat :
                stat = StatisticModel(
                    date_YMD=day,
                    child_id=self.child_id
                )

            #stat = ChatNamespace.stat_handler(stat=stat,processed_data=processed_data)
            #stat.save_to_db()

            if "SUPERVISOR" in rooms[self.room].keys():
                if rooms[self.room]["SUPERVISOR"] :
                    return

            day, full_date, real_time = ChatNamespace.time_shift()

            my_chat = ChatModel(self.child_id, day, full_date, real_time, "BOT", processed_data["System_Corpus"])
            my_chat.save_to_db()

            emit(
                "RECEIVE_MESSAGE",
                {"response": processed_data["System_Corpus"],
                 "day": day, 'time': real_time},
                to=self.room,
            )

        elif data["type"] == "SUPERVISOR":
            day, full_date, real_time = ChatNamespace.time_shift()

            my_chat = ChatModel(self.child_id, day, full_date, real_time, "SUPERVISOR", data['message'])
            my_chat.save_to_db()

            emit(
                "RECEIVE_MESSAGE",
                {"response": data['message'],
                 "day": day, 'time': real_time},
                to=self.room,
            )

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
    def stat_handler(stat,processed_data):
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
            temp_badsentences['sentences'].append(data['message'])
            stat.badwords = json.dumps(temp_badwords)
            stat.bad_sentences = json.dumps(temp_badsentences)

        # situdation handler
        temp_topic = json.loads(stat.situation)
        temp_topic[processed_data["Topic"]] += 1
        if processed_data["SubTopic"]:
            temp_subtopic = json.loads(stat.subtopic)
            temp_subtopic[processed_data["SubTopic"]] += 1
            stat.subtopic = json.dumps(temp_subtopic)
        stat.situation = json.dumps(temp_topic)

        # relationship
        temp_relationship = json.loads(stat.relation_ship)

        for key in processed_data["NER"]:
            if not key in temp_relationship.keys():
                temp_relationship[key] = init_emotion.copy()

            temp_relationship[key][processed_data["Emotion"]] += 1

        stat.relation_ship = json.dumps(temp_relationship)

        return stat