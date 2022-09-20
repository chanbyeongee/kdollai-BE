from db import db

class ReservationModel(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)

    day = db.Column(db.String(80))

    begin = db.Column(db.String(80))
    end = db.Column(db.String(80))
    status = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    counselor_id = db.Column(db.Integer, db.ForeignKey('counselors.id'))
    content = db.Column(db.String(100))

    def __init__(self,day,begin,end,content,user_id,counselor_id):
        self.day = day
        self.begin = begin
        self.end = end
        self.user_id = user_id
        self.counselor_id = counselor_id
        self.status = "OPEN"
        self.content = content

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def find_by_counselor_id(cls, counselor_id):
        return cls.query.filter_by(counselor_id=counselor_id).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()