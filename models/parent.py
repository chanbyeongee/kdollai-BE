from db import db
from .user import UserModel
from .child import ChildModel

class ParentModel(UserModel):
    __tablename__ = 'parents'

    childs = db.relationship('ChildModel', backref='parents')

    def __init__(self, user_name,user_subname,password, user_type,child_name,child_age,child_gender,serial_number):
        super().__init__(user_name,user_subname,password, user_type)
        child = ChildModel(self.id,child_name,child_age,child_gender,serial_number)
        child.save_to_db()

    def json(self):
        return {'info':{'id':self.id,'user_name':self.username, 'user_subname':self.secondname, 'user_type':self.user_type},
                'childs': [child.json() for child in self.childs]}
