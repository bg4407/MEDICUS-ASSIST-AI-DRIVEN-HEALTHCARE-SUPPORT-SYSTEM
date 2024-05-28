from app import db  # Import the db instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Add more fields as needed, e.g., email, password_hash, etc.

    def __repr__(self):
        return '<User %r>' % self.username