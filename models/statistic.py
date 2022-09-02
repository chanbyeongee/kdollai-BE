from db import db
from . import and_
import json

init_emotion={
    "불만":0, "중립":0, "당혹":0, "기쁨":0, "걱정":0, "질투":0, "슬픔":0, "죄책감":0, "연민":0
}

class StatisticModel(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    date_Y = db.Column(db.String(80))
    date_YM = db.Column(db.String(80))
    date_day = db.Column(db.String(80))
    emotions = db.Column(db.String(80))
    situation = db.Column(db.String(80))
    child_id = db.Column(db.Integer, db.ForeignKey('childs.id'))

    def __init__(self, mtype,date_Y,date_YM,date_day,situation,child_id):
        self.mtype = mtype
        self.date_Y = date_Y
        self.date_YM = date_YM
        self.date_day = date_day
        self.emotions = json.dumps(init_emotion)
        self.situation = situation
        self.child_id = child_id

    def json(self):
        return {'date': self.date,
                'emotions': json.loads(self.emotions),
                'situation': self.situation}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_child_id(cls, child_id):
        return cls.query.filter_by(child_id=child_id).all()

    @classmethod
    def find_by_child_id_and_year(cls, child_id,year):
        return cls.query.filter(and_(cls.child_id == child_id,cls.date_Y == year)).all()

    @classmethod
    def find_by_child_id_and_ym(cls, child_id, YM):
        return cls.query.filter(and_(cls.child_id == child_id, cls.date_YM == year)).all()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
