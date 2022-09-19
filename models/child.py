from db import db
from . import and_


class ChildModel(db.Model):
    __tablename__ = 'childs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer())
    gender = db.Column(db.String(80)) #0-male 1-female
    serial_number = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    chats = db.relationship('ChatModel', backref='childs')
    statistics = db.relationship('StatisticModel', backref='childs')

    def __init__(self,user_id,child_name, child_age,child_gender,serial_number):
        self.user_id = user_id
        self.name = child_name
        self.age = child_age
        self.gender = child_gender
        self.serial_number = serial_number


    def json(self):
        return {'info':{'id': self.id, 'name': self.name, 'age':self.age, 'gender':self.gender,'serial_number':self.serial_number},
                'chats':[chat.json() for chat in self.chats]
                }

    @classmethod
    def find_by_name_with_user_id(cls, user_id, name):
        return cls.query.filter(and_(cls.user_id == user_id, cls.name == name)).all()

    @classmethod
    def find_by_serial_number(cls, serial_number):
        return cls.query.filter(cls.serial_number == serial_number).first()

    @classmethod
    def find_by_user_id(cls,user_id):
        return cls.query.filter_by(user_id=user_id).first()

    @classmethod
    def find_by_serial(cls, SN):
        return cls.query.filter_by(serial_number=SN).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
