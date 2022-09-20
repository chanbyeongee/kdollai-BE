from db import db

class CounselorModel(db.Model):
    __tablename__ = 'counselors'

    id = db.Column(db.Integer, primary_key=True)
    user_subname = db.Column(db.String(80))
    password = db.Column(db.String(80))
    user_name = db.Column(db.String(80))
    user_type = db.Column(db.String(80))  # 0-parents 1-counseller 2-individual

    brief_desc = db.Column(db.String(80))
    profile = db.Column(db.String(80))
    available_begin = db.Column(db.String(80))
    available_end = db.Column(db.String(80))

    available = db.Column(db.Boolean())

    childs = db.relationship('ChildModel', backref='counselors')
    index_page = db.relationship("IndexPageModel", backref="counselors")
    reservations = db.relationship('ReservationModel', backref='counselors')

    def __init__(self, user_name, user_subname, password, breif_desc,available_begin,available_end):
        self.user_subname = user_subname
        self.user_name = user_name
        self.password = password
        self.user_type = "counselor"
        self.available = True
        self.brief_desc = breif_desc
        self.available_begin = available_begin
        self.available_end = available_end

    def json(self):
        return {'info':
            {
                'id': self.id,
                'user_subname': self.user_subname,
                'user_name': self.user_name,
                'user_type': self.user_type,
                'thumbnail': self.profile
            }
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_username(cls, user_name):
        return cls.query.filter_by(user_name=user_name).first()

    @classmethod
    def find_all(cls):
        return cls.query.filter_by(available=True).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()