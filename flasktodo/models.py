from datetime import datetime
from flasktodo import db

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Title {}>'.format(self.content)
