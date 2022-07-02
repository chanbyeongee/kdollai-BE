from db import db
from . import and_

class ChatModel(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80))
    direction = db.Column(db.Integer)#0-sender(counseller) #1-receive(children)
    line = db.Column(db.String(80))
    emotion = db.Column(db.String(80))
    situation = db.Column(db.String(80))

    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def __init__(self, employee_id, date, direction, line, emotion, situation):
        self.date = date
        self.direction = direction
        self.line = line
        self.emotion = emotion
        self.situation =situation
        self.employee_id = employee_id

    def json(self):
        return {'date': self.date, 'direction': self.direction,'line':self.line, 'emotion':self.emotion, 'situation': self.situation}

    @classmethod
    def find_by_date_with_employee_id(cls, employee_id, date):
        return cls.query.filter(and_(cls.employee_id == employee_id, cls.date == date)).first()

    @classmethod
    def find_all_with_employee_id(cls,employee_id):
        return cls.query.filter_by(employee_id=employee_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
