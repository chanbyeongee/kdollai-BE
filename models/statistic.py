from db import db
from . import and_

class StatisticModel(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    mtype = db.Column(db.Integer) #0-day, 1-week 2-month, 3-year
    date = db.Column(db.String(80)) #day - YYYY-MM-DD ,week - YYYY-MM-DD(start), month - YYYY-MM , year - YYYY
    emotion_bullman = db.Column(db.Integer)
    emotion_normal = db.Column(db.Integer)
    emotion_embarrassed = db.Column(db.Integer)
    emotion_delight = db.Column(db.Integer)
    emotion_worry = db.Column(db.Integer)
    emotion_envy = db.Column(db.Integer)
    emotion_sadness = db.Column(db.Integer)
    emotion_guilty = db.Column(db.Integer)
    emotion_empathy = db.Column(db.Integer)


    situation = db.Column(db.String(80))

    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def __init__(self, mtype,date,emo_list,situation,employee_id):
        self.mtype = mtype
        self.date = date
        self.emotion_bullman = emo_list[0]
        self.emotion_normal = emo_list[1]
        self.emotion_embarrassed = emo_list[2]
        self.emotion_delight = emo_list[3]
        self.emotion_worry = emo_list[4]
        self.emotion_envy = emo_list[5]
        self.emotion_sadness = emo_list[6]
        self.emotion_guilty = emo_list[7]
        self.emotion_empathy = emo_list[8]
        self.situation = situation
        self.employee_id = employee_id

    def json(self):
        return {'type': self.type, 'date': self.date,
                'emotion': {'bullman': self.emotion_bullman,'normal': self.emotion_normal,
                            'embarrassed': self.emotion_embarrassed,'delight': self.emotion_delight,
                            'worry': self.emotion_worry,'envy': self.envy,
                            'sadness': self.emotion_sadness,'guilty': self.emotion_guilty,
                            'empathy': self.emotion_empathy},
                'situation': self.situation}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_employee_id(cls, employee_id):
        return cls.query.filter_by(employee_id=employee_id).all()

    @classmethod
    def find_by_employee_id_and_type(cls, mtype, employee_id):
        return cls.query.filter(and_(cls.mtype == mtype, cls.employee_id == employee_id)).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
