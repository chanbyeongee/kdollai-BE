from db import db
from . import and_

class ChatModel(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    date_YMD = db.Column(db.String(80))
    date_YMDHMS = db.Column(db.String(80))
    date_Time = db.Column(db.String(80))
    direction = db.Column(db.String(80))#0-user #1-chatbot
    utterance = db.Column(db.String(80))

    child_id = db.Column(db.Integer, db.ForeignKey('childs.id'))

    def __init__(self, child_id, date_YMD, date_YMDHMS,date_Time, direction, utterance):
        self.date_YMD = date_YMD
        self.date_YMDHMS = date_YMDHMS
        self.date_Time = date_Time
        self.direction = direction
        self.utterance = utterance

        self.child_id = child_id

    def json(self):
        return {'day': self.date_YMD,'time': self.date_Time, 'direction': self.direction,'utterance':self.utterance}

    @classmethod
    def find_all_by_dateYMD_with_child_id(cls, child_id, day):
        return cls.query.filter(and_(cls.child_id == child_id, cls.date_YMD == day)).all()

    @classmethod
    def find_by_fulldate_with_child_id(cls, child_id, date):
        return cls.query.filter(and_(cls.child_id == child_id, cls.date_YMDHMS == date)).first()

    @classmethod
    def find_range_with_child_id(cls, child_id, begin, latest):
        return cls.query.filter(and_(cls.date_YMD.between(begin, latest), cls.child_id == child_id)).order_by(
            cls.id.desc()).all()

    @classmethod
    def find_by_number_with_child_id(cls, child_id, latest, number):
        return cls.query.filter(and_(cls.date_YMDHMS < latest, cls.child_id == child_id)).order_by(cls.id.desc()).limit(
            number).all()

    @classmethod
    def find_all_with_child_id(cls,child_id):
        return cls.query.filter_by(child_id=child_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
