from models.user import UserModel
from models.chat import ChatModel
from models.statistic import StatisticModel
from models.child import ChildModel
import json

def make_dummy():
    user = UserModel(
        user_name="well87865@gmail.com",
        user_subname="Chanee",
        password="123123",
        user_type="parent"
    )
    user.save_to_db()

    child = ChildModel(
        child_name="이동현",
        child_age=23,
        child_gender="male",
        user_id=user.id,
        serial_number="abcd1234"
    )
    child.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220917",
        date_YMDHMS="20220917171522",
        direction="USER",
        utterance="안녕 도담아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220917",
        date_YMDHMS="202209171715326",
        direction="BOT",
        utterance="오랜만이야 동현아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220918",
        date_YMDHMS="20220918190022",
        direction="USER",
        utterance="학교에서 친구랑 싸웠어..."
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220918",
        date_YMDHMS="20220918190027",
        direction="BOT",
        utterance="정말? 많이 슬펐겠다..."
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220919",
        date_YMDHMS="20220919080140",
        direction="USER",
        utterance="이따 학교 끝나고 보자!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220919",
        date_YMDHMS="20220919080145",
        direction="BOT",
        utterance="그래! 이따 보자!"
    )
    chat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220917",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["중립"]+=1
    stat.emotions = json.dumps(temp)
    stat.total +=1
    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220918",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["슬픔"] += 1
    stat.emotions = json.dumps(temp)
    stat.total +=1
    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220919",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["기쁨"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 1
    stat.save_to_db()


mocks = {
    '1':{
        'setup':{
            "length":1,
            "keys":[['name']],
            "timer":1,
            "is_continue":False,
            "is_response":True,
            'is_last':False,
            "next":'2'
        },
        "text":[
            "{0}님이 느끼시는 감정의 이유에 대하여 좀 더 자세한 설명이 가능할까요?"
        ],
        "response":{
            "type":"input",
            "is_store":True,
            "is_redirection":False,
            "store_key":"worry-1",
        }
    },
    '2':{
        "setup":{
            "length":4,
            "keys":[[],['name','worry-1'],['name'],[],['책 추천','노래 추천','대화하기','상담사 연결']],
            "timer":5,
            "is_continue":False,
            "is_response":True,
            'is_last':False,
            "next": '3'
        },
        "text":[
            "그렇군요..적당한 걱정은 도움이 되지만 지나친 불안은 문제 해결을 방해하죠.",
            "{0}님께서는 '{1}' 이라고 말씀하셨고 정말 걱정이 될만한 이유라고 생각이 들어요.",
            "제가 {0}님에게 도움이 되길 원해요!",
            "다음 중에서 골라주실래요?",
            "| {0} | {1} | {2} | {3} |"
        ],
        "response":{
            "next":'input',
            "is_store":False,
            "is_redirection":False,
            "store_key":None
        }
    },
    '3':{
        "setup":{
            "length":3,
            "keys":[['name'],[],[]],
            "timer":4,
            "is_continue": False,
            "is_response": True,
            'is_last':False,
            "next": '4'
        },
        "text":[
            "{0}님의 말씀해주신 그런 고민들은 정말이지 누구에게나 머리 아프게 만들죠",
            "그래서 더욱 제대로 된 판단이 필요해요. 생각하시는 해결 방법을 적고 생각을 정리해보는 시간을 가져봐요!",
            "(자신이 생각하는 해결 방법을 적어주세요)"
               ],

        "response":{
            "next":'input',
            "is_store":False,
            "is_redirection":False,
            "store_key":None
        }
    },
    '4':{
        "setup":{
            "length":1,
            "keys":[[]],
            "next":'5',
            "timer":2,
            "is_continue": False,
            'is_last':False,
            "is_response": True,
        },
        "text":[
            "좋아요, 그럼 그 방법의 장단점은요?"
               ],

        "response":{
            "next":'input',
            "is_store":False,
            "is_redirection":False,
            "store_key":None
        },
    },
    '5':{
        "setup":{
            "length":1,
            "keys":[[]],
            "timer":2,
            "is_continue": False,
            "is_response": True,
            'is_last':False,
            "next": '6'
        },
        "text":[
            "언제 실행하는 것이 가장 좋을까요?"
               ],

        "response":{
            "next":'input',
            "is_store":False,
            "is_redirection":False,
            "store_key":None
        }
    },
    '6':{
        "setup":{
            "length":2,
            "keys":[[],[]],
            "timer": 4,
            'is_last':True,
            "is_continue": False,
            "is_response": False,
            "next": None
        },
        "text":[
            "좋아요! 지금 세워본 방법이 실제로 도움이 되지 않더라도 이렇게 정리하는 것 만으로도 문제를 이해하고 해결하는데 큰 도움이 되죠!!",
            "마지막으로 이 말을 전해요! 사라져라 지겨운 걱정들아..!! -빨간 머리 앤-"
               ]
    }
}