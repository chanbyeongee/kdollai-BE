from db import db
from.counselor import CounselorModel

class IndexPageModel(db.Model):
    __tablename__ = 'indexPages'

    id = db.Column(db.Integer, primary_key=True)

    main_desc = db.Column(db.String(100))
    main_image = db.Column(db.String(100))
    lunch_time = db.Column(db.String(100))

    address = db.Column(db.String(100))
    post_address = db.Column(db.String(100))

    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))
    introduction = db.Column(db.String(100))

    counselor_id = db.Column(db.Integer, db.ForeignKey('counselors.id'))


    def __init__(self, main_desc,main_image,lunch_time,address,post_address,latitude,longitude,introduction,counselor_id):

        self.introduction = introduction
        self.lunch_time = lunch_time

        self.main_desc = main_desc
        self.main_image = main_image

        self.address = address
        self.post_address = post_address
        self.latitude = latitude
        self.longitude = longitude

        self.counselor_id = counselor_id

    def json(self):
        counselor = CounselorModel.find_by_id(self.counselor_id)
        return {"profile":
                    {
                        'id':self.id,
                        'name':counselor.user_subname,
                        'available': {
                            'open': counselor.available_begin,
                            'close': counselor.available_end,
                            'lunch': self.lunch_time,
                        },
                        "breif":counselor.brief_desc,
                        "thumbnail":counselor.profile,
                        'introduce':[content.strip() for content in self.introduction.split("\n") if(content.strip())]
                    },
                "main":
                    {
                        'image':self.main_image,
                        'desc':[content.strip() for content in self.main_desc.split("\n") if(content.strip())],
                        'address':self.address,
                        'post_address':self.post_address,
                        'location':{
                            "lat":self.latitude,
                            "long":self.longitude
                        }
                }
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
