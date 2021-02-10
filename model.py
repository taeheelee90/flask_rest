from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class WebUser(db.Model):
    __tablename__ = "webuser"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'password': self.password,
            'userid': self.userid,
            'username': self.username
        }