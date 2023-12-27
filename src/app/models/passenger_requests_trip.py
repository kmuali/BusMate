from app.api.database import db

class PassengerRequestsTrip(db.Model):
    __tablename__ = 'passenger_requests_trip'

    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.id'), primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'), primary_key=True)
    description = db.Column(db.String(1023), nullable=False)
    is_cash = db.Column(db.Boolean, nullable=False)
    is_riding = db.Column(db.Boolean, nullable=False)
    is_accepted = db.Column(db.Boolean, nullable=False)
    fee_amount = db.Column(db.Float, nullable=False)
