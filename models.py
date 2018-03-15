from app import db

class Person(db.Model):

    __tablename__ = 'people'

    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    email = db.Column(db.String(255))
    address = db.Column(db.String(255))


    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_all(self):
        return Person.query.all()

    @staticmethod
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self, name):
        return "<Person {} >".format(self.name)