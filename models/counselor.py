from db import db
from models.user import UserModel

class CounselorModel(UserModel):
    __tablename__ = 'counselors'

    available_time = db.Column(db.String(80)) #dict

    brief_desc = db.Column(db.String(80)) #dict

    childs = db.relationship('ChildModel', backref='counselors')
    reservation = db.relationship('ReservationModel', backref='counselors')

    def __init__(self, user_name, user_subname, password, usertype,breif_desc):
        super().__init__(user_name, user_subname, password, usertype)
        self.brief_desc = breif_desc

    def json(self):
        return {'info':{'id': self.id, 'secondname': self.secondname, 'user_name': self.username, 'user_type': self.usertype,'brief_desc':self.breif_desc},
                'childs': [child.json() for child in self.childs]}

    @classmethod
    def find_by_reservation_id(cls, id):
        return cls.query.filter_by(reservation_id=id).first()