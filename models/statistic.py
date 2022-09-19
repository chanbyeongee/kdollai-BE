from db import db
from . import and_
import json

init_emotion={
    "불만":0, "중립":0, "당혹":0, "기쁨":0, "걱정":0, "질투":0, "슬픔":0, "죄책감":0, "연민":0
}

class StatisticModel(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    date_YMD = db.Column(db.String(80))
    emotions = db.Column(db.String(80))
    situation = db.Column(db.String(80))
    total = db.Column(db.Integer())

    child_id = db.Column(db.Integer, db.ForeignKey('childs.id'))

    def __init__(self, date_YMD,child_id):
        self.date_YMD = date_YMD
        self.emotions = json.dumps(init_emotion)
        self.situation = ""
        self.total=0

        self.child_id = child_id

    def json(self):
        return {'date': self.date_YMD,
                "chart":{

                    'emotions': json.loads(self.emotions),
                    'situation': self.situation
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
