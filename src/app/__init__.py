from flask import Flask

app = Flask(__name__)

from app.views import index_view, register_view, login_view, passenger_view, driver_view
from app.api import database

from app.models.bank_account import BankAccount
from app.models.passenger import Passenger
from app.models.trip import Trip
from app.models.driver import Driver
from app.models.microbus import Microbus
from app.models.passenger_requests_trip import PassengerRequestsTrip 

database.db.create_all()
