from app.api.database import db

class Microbus(db.Model):
    __tablename__ = 'microbus'

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer,db.ForeignKey('driver.id'), nullable=False)
    plate_number = db.Column(db.String(20), unique=True, nullable=False)
