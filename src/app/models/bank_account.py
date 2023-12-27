from app.api.database import db

class BankAccount(db.Model):
    __tablename__ = 'bank_account'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=True)
    cvv = db.Column(db.String(3), nullable=True)
    year = db.Column(db.String(2), nullable=True)
    month = db.Column(db.String(2), nullable=True)
