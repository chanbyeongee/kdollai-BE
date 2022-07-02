from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    secondname = db.Column(db.String(80))
    password = db.Column(db.String(80))
    username = db.Column(db.String(80))
    usertype = db.Column(db.Integer) #0-parents 1-counseller 2-individual

    employees = db.relationship('EmployeeModel', backref='employees')

    def __init__(self, secondname, password,username, usertype):
        self.secondname = secondname
        self.username = username
        self.password = password
        self.usertype = usertype

    def json(self):
        return {'id':self.id, 'secondname':self.secondname, 'user_name':self.username,'user_type':self.usertype,
                'employees': [employee.json() for employee in self.employees]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
