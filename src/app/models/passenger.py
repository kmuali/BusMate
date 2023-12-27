from app.api.database import db
from app.models.bank_account import BankAccount
from app.models.passenger_requests_trip import PassengerRequestsTrip

class Passenger(db.Model):
    __tablename__ = 'passenger'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    longitude = db.Column(db.Float, nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    bank_id = db.Column(db.Integer,db.ForeignKey('bank_account.id'), nullable=True)

    def set_location(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = longitude

    def set_bank_account(self, number, cvv, year, month):
        self.bank_id = BankAccount(number=number, cvv=cvv, year=year, month=month)
