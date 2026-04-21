from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Memory(db.Model):
    __tablename__ = "memories"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(120), nullable=False)
    quote = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text)
    is_text_only = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "quote": self.quote,
            "image": self.image_url,
            "isTextOnly": self.is_text_only,
            "createdAt": self.created_at.strftime("%B %d, %Y")
        }