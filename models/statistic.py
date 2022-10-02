from db import db
from . import and_
import json

init_emotion={
    "불만":0, "중립":0, "당혹":0, "기쁨":0, "걱정":0, "질투":0, "슬픔":0, "죄책감":0, "연민":0
}

init_topic={
    "취미":{"total":0,"emotion":init_emotion.copy()},
    "날씨_및_계절":{"total":0,"emotion":init_emotion.copy()},
    "반려동물":{"total":0,"emotion":init_emotion.copy()},
    "방송_미디어":{"total":0,"emotion":init_emotion.copy()},
    "식음료":{"total":0,"emotion":init_emotion.copy()},
    "학교":{"total":0,"emotion":init_emotion.copy()},
    "가족":{"total":0,"emotion":init_emotion.copy()},
    "건강":{"total":0,"emotion":init_emotion.copy()}
}

init_subtopic={
    "스포츠":{"total":0,"emotion":init_emotion.copy()},
    "여행":{"total":0,"emotion":init_emotion.copy()},
    "게임":{"total":0,"emotion":init_emotion.copy()},
    "영화_만화":{"total":0,"emotion":init_emotion.copy()},
    "방송_연예":{"total":0,"emotion":init_emotion.copy()}
}

emotion_weight={
    "중립":0,"기쁨":3, "연민":-1, "당혹":-1, "질투":-1, "걱정":-1, "불만":-2,"죄책감":-2, "슬픔":-2
}

init_badwords={
    "씨발":0, "개새끼":0, "존나":0, "자살":0
}

init_badsentences={
    "sentences":[]
}

init_relationship={}


class StatisticModel(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    date_YMD = db.Column(db.String(80))
    emotions = db.Column(db.String(80))
    emotion_score = db.Column(db.Integer())
    total = db.Column(db.Integer())

    situation = db.Column(db.String(80))
    subtopic = db.Column(db.String(80))

    badwords = db.Column(db.String(80))
    bad_sentences = db.Column(db.String(200))

    relation_ship = db.Column(db.String(200))

    child_id = db.Column(db.Integer, db.ForeignKey('childs.id'))

    def __init__(self, date_YMD,child_id):
        self.date_YMD = date_YMD
        self.emotions = json.dumps(init_emotion)
        self.emotion_score = 50
        self.total = 0

        self.situation = json.dumps(init_topic)
        self.subtopic = json.dumps(init_subtopic)

        self.badwords = json.dumps(init_badwords)
        self.bad_sentences = json.dumps(init_badsentences)

        self.relation_ship = json.dumps(init_relationship)

        self.child_id = child_id

    def emo_json(self):
        return {
            'date': self.date_YMD,
                "chart":{
                    "emotion":{
                        'emotions': json.loads(self.emotions),
                        'emotion_score': self.emotion_score,
                        'total':self.total
                    }
                }
            }

    def topic_json(self):

        situations = json.loads(self.situation)

        for key in situations.keys():
            situations[key]["score"] = 50
            for emo_key in init_emotion.keys():
                situations[key]["score"] += situations[key]["emotion"][emo_key] * emotion_weight[emo_key]

        subtopics = json.loads(self.subtopic)

        for key in subtopics.keys():
            subtopics[key]["score"] = 50
            for emo_key in init_emotion.keys():
                subtopics[key]["score"] += subtopics[key]["emotion"][emo_key] * emotion_weight[emo_key]


        return {
            'date': self.date_YMD,
                "chart":{
                    'situation':{
                        'topic': situations,
                        'subtopic': subtopics,
                    },
                }
            }

    def relation_json(self):

        relationships = json.loads(self.relation_ship)
        for key in relationships.keys():
            relationships[key]["score"] = 50
            for emo_key in init_emotion.keys():
                relationships[key]["score"] += relationships[key]["emotion"][emo_key] * emotion_weight[emo_key]

        return {'date': self.date_YMD,
                "chart":{
                    'relationship' : relationships
                    }
                }

    def bad_json(self):


        return {'date': self.date_YMD,
                "chart":{
                    "badness":{
                        'bad_words': json.loads(self.badwords),
                        "bad_sentences": json.loads(self.bad_sentences)
                    }
                }
                }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_child_id(cls, child_id):
        return cls.query.filter_by(child_id=child_id).all()

    @classmethod
    def find_by_dateYMD_with_child_id(cls, child_id, date):
        return cls.query.filter(and_(cls.child_id == child_id, cls.date_YMD == date)).first()

    @classmethod
    def find_range_with_child_id(cls, child_id, begin, latest):
        return cls.query.filter(and_(cls.date_YMD.between(begin, latest), cls.child_id == child_id)).all()

    @classmethod
    def find_by_number_with_child_id(cls, child_id, latest, number):
        return cls.query.filter(and_(cls.date_YMD < latest, cls.child_id == child_id)).order_by(cls.id.desc()).limit(
            number).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
