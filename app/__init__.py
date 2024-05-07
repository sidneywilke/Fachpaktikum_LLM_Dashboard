from flask import Flask
from .dashboard.layout import init_dashboard
from .dashboard.callbacks import register_callbacks
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    dash_app = init_dashboard(app)
    register_callbacks(dash_app)
    return app
