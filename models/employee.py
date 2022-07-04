from db import db
from . import and_


class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    birth = db.Column(db.String(80))
    gender = db.Column(db.Integer) #0-male 1-female
    serial_number = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    chats = db.relationship('ChatModel', backref='employees')

    statistics = db.relationship('StatisticModel', backref='employees')

    def __init__(self,user_id, serial_number, name,birth,gender):
        self.name = name
        self.birth = birth
        self.gender = gender
        self.serial_number = serial_number
        self.user_id = user_id

    def json(self):
        days = [statistic.json() for statistic in self.statistics if statistic.type == 0]
        weeks = [statistic.json() for statistic in self.statistics if statistic.type == 1]
        months = [statistic.json() for statistic in self.statistics if statistic.type == 2]
        years = [statistic.json() for statistic in self.statistics if statistic.type == 3]
        return {'id': self.id, 'name': self.name, 'birth':self.birth, 'gender':self.gender,'serial_number':self.serial_number,
                'chats':[chat.json() for chat in self.chats],
                'statistics':{'days': days, 'weeks': weeks, 'months': months, 'years': years}
                }

    @classmethod
    def find_by_name_with_user_id(cls, user_id, name):
        return cls.query.filter(and_(cls.user_id == user_id, cls.name == name)).all()

    @classmethod
    def find_by_serial_with_user_id(cls, user_id, serial_number):
        return cls.query.filter(and_(cls.user_id == user_id, cls.serial_number == serial_number)).first()

    @classmethod
    def find_all_with_user_id(cls,user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def find_by_serial(cls, SN):
        return cls.query.filter_by(serial_number=SN).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
