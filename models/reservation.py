from db import db
from .counselor import CounselorrModel

class ReservationModel(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)

    thumbnails = db.Column(db.String(160))
    main_desc = db.Column(db.String(100))
    address = db.Column(db.String(100))
    location = db.Column(db.String(100))
    reservation_times = db.Column(db.String(100))


    counselor_id = db.Column(db.Integer, db.ForeignKey('counselors.id'))

    def __init__(self, thumbnails,main_desc,address,location,counselor_id):
        self.thumbnails = thumbnails
        self.main_desc = main_desc
        self.address = address
        self.location = location
        self.counselor_id = counselor_id

    def json(self):
        return {"info":{'id':self.id, 'thumbnails':self.thumbnails, 'address':self.address,'location':self.location},
                "counselor": CounselorrModel.find_by_id(self.counselor_id)
                }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_counselor_id(cls, counselor_id):
        return cls.query.filter_by(counselor_id=counselor_id).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
