from app.api.database import db

class Trip(db.Model):
    __tablename__ = 'trip'

    id = db.Column(db.Integer, primary_key=True)
    from_longitude = db.Column(db.Float, nullable=False)
    from_latitude = db.Column(db.Float, nullable=False)
    to_longitude = db.Column(db.Float, nullable=False)
    to_latitude = db.Column(db.Float, nullable=False)
    driver_id = db.Column(db.Integer,db.ForeignKey('driver.id'), nullable=False)
    is_full = db.Column(db.Boolean, nullable=False)
