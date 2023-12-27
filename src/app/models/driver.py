from app.api.database import db

class Driver(db.Model):
    __tablename__ = 'driver'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    longitude = db.Column(db.Float, nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('bank_account.id'), nullable=True)
