from db import db
from .child import ChildModel

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_subname = db.Column(db.String(80))
    password = db.Column(db.String(80))
    user_name = db.Column(db.String(80))
    user_type = db.Column(db.String(80)) #0-parents 1-counseller 2-individual

    childs = db.relationship('ChildModel', backref='users')

    def __init__(self, user_name,user_subname,password, user_type):
        self.user_subname = user_subname
        self.user_name = user_name
        self.password = password
        self.user_type = user_type

    def json(self):
        return {'info':{'id':self.id, 'user_subname':self.user_subname, 'user_name':self.user_name,'user_type':self.user_type},
                'childs': [child.json() for child in self.childs]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_child_data(self,child_name,child_age,child_gender,serial_number):
        child = ChildModel(self.id,child_name,child_age,child_gender,serial_number)
        child.save_to_db()

    @classmethod
    def find_by_username(cls, user_name):
        return cls.query.filter_by(user_name=user_name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
