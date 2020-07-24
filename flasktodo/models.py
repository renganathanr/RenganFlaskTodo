from datetime import datetime
from flasktodo import db

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='title', lazy='dynamic')

    def __repr__(self):
        return '<Title {}>'.format(self.content)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'), nullable=False)

    def __repr__(self):
        return '<Task {}>'.format(self.content)