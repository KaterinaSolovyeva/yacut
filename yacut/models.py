from datetime import datetime

from yacut import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id = self.id,
            original = self.original,
            short = self.short,
            timestamp = self.timestamp
        )
    
    def from_dict(self, data):
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])
