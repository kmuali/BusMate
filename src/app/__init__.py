from flask import Flask

app = Flask(__name__)

from app.views import index_view
from app.views import register_view
