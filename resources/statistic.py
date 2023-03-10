from flask_restful import Resource
from models.chat import ChatModel
from models.child import ChildModel
from models.statistic import StatisticModel, init_emotion, emotion_color
import json
import operator
import copy

sentences = {
    "불만" : [
        "{name}이가 현재 삶에 만족하지 못하는 것 같아요.",
        "어떠한 점에서 불만을 느끼는지 대화를 나눠보는 건 어떨까요?"
    ],
    "중립":[
        "{name}이는 최근에 큰 문제는 없었어요.",
        "하지만 말하지 못하는 마음을 감추고 있을 지도 몰라요.",
        "오늘도 평소처럼 대화를 나눠보시는 건 어떨까요?"
    ],
    "당혹":[
        "최근에 {name}이가 놀랄 만한 일이 있었나봐요.",
        "아이에게 평소보다 조심스럽게 다가가 보는 건 어떨까요?"
    ],
    "기쁨":[
        "최근에 {name}이는 기쁨이 충만한 것 같아요.",
        "함께 기뻤던 일에 대해서 얘기를 나눠보는 건 어떨까요?"
    ],
    "걱정":[
        "요즘 {name}이에게 걱정스러운 일이 있나봐요.",
        "아이가 어떤 상황에 놓여있는지 살펴보고 대화를 나눠보는 건 어떨까요?",
    ],
    "질투":[
        "{name}이가 남에게 질투를 느끼며 스트레스를 받고 있어요.",
        "이럴 때일 수록 자존감을 복돋아줄 수 있는 응원 한마디 어떨까요?"
    ],
    "슬픔":[
        "{name}이의 마음에 비가 잔뜩 내리고 있네요.",
        "무슨 일이 있었는지 물어보면서 천천히 접근해보세요."
    ],
    "죄책감":[
        "{name}이가 스스로 책임질 일 때문에 힘들어 하고 있는것 같아요.",
        "오늘은 아이의 말에 조금 더 귀 기울여 주는 건 어떨까요?"
    ],
    "연민":[
        "최근 {name}이가 무언가를 불쌍해 하고 있어요.",
        "따듯한 마음을 가진 아이가 올바르게 성장할 수 있게 격려해주세요."
    ]
}



def find_max_emotion(stats):
    ret_emotions = copy.deepcopy(init_emotion)
    total_cnt = 0

    for stat in stats:
        temp = json.loads(stat.emotions)
        total_cnt += stat.total

        for key in ret_emotions.keys():
            ret_emotions[key] += temp[key]

    max_key = max(ret_emotions,key=ret_emotions.get)

    return max_key

def find_three_emotion(stats):
    ret_emotions = copy.deepcopy(init_emotion)
    total_cnt = 0

    for stat in stats:
        temp = json.loads(stat.emotions)
        total_cnt += stat.total

        for key in ret_emotions.keys():
            ret_emotions[key] += temp[key]

    sorted_x = sorted(ret_emotions.items(), key=operator.itemgetter(1), reverse=True)

    ret = [content[0] for content in sorted_x[:3]]

    return ret

class RecentWords(Resource):
    def get(self,day):
        child_id = 1


        stats = StatisticModel.find_by_number_with_child_id(child_id,day,7)
        child = ChildModel.find_by_id(child_id)

        if not stats:
            return {"message":[f"최근 1주일 간 이용한 기록이 없네요... 저는 {child.name[1:]}이와 더 이야기를 나누고 싶어요!"]}

        emo_key = find_max_emotion(stats)

        return {"message":[sentence.format(name=child.name[1:]) for sentence in sentences[emo_key]]}

class RecentUse(Resource):
    def get(self):
        child_id = 1
        chats = ChatModel.find_all_with_child_id(child_id)

        if not chats:
            return {"message":None}
        else :
            recent=chats[-1]
            return {"message":recent.date_YMD}

class RecentEmotions(Resource):
    def get(self,day):
        child_id = 1

        stats = StatisticModel.find_by_number_with_child_id(child_id,day,7)

        keys = find_three_emotion(stats)

        return {
            "message":[{"name":key,"color":emotion_color[key]} for key in keys]
        }

class RecentScenario(Resource):
    def get(self,day):

        if day == "20221004":
            return {"message":[
                {
                    "name":"여행/취미 관련 대화",
                    "number":2
                },
                {
                    "name":"학교/교우/성적 관련 대화",
                    "number":1
                },
                {
                    "name": "가족/친척 관련 대화",
                    "number": 4
                }
            ]}
        elif day == "20221003":
            return {"message": [
                {
                    "name": "건강 관련 대화",
                    "number": 3
                },
                {
                    "name": "반려동물 관련 대화",
                    "number": 4
                },
                {
                    "name": "스포츠 관련 대화",
                    "number": 1
                }
            ]}
        else :
            return {"message": [
                {
                    "name": "방송/연예 관련 대화",
                    "number": 1
                },
                {
                    "name": "영화/방송 관련 대화",
                    "number": 1
                },
                {
                    "name": "게임",
                    "number": 1
                }
            ]}
