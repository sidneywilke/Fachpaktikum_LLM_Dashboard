from flask import Flask
from .dashboard.layout import init_dashboard
from .dashboard.callbacks import register_callbacks
from flask_cors import CORS

def create_app():
    columns = [
        {"name": "Rank", "id": "rank"},
        {"name": "Model", "id": "model"},
        {"name": "Time To First Token", "id": "ttft"},
        {"name": "Time Per Output Token", "id": "tpok"},
        {"name": "Total Generation Time", "id": "tgt"},
        {"name": "Token per Second", "id": "tps"},
        {"name": "Quality", "id": "quality"},
        {"name": "Privacy", "id": "privacy"},
        {"name": "Ethics", "id": "ethics"},
        {"name": "Bias", "id": "bias"},
        {"name": "Non-Toxicity", "id": "non-toxicity"},
    ]

    data = [
        {"rank": 1, "model": "Phi3", "ttft": 0.3, "tpok": 78, "tgt": 6.3,
         "tps": 5.3, "quality": 769, "privacy": 84.67, "ethics": 42.67, "bias": 97, "non-toxicity": 68.92},
        {"rank": 3, "model": "Gemma", "ttft": 0.4, "tpok": 53, "tgt": 12.83,
         "tps": 5.3, "quality": 769, "privacy": 83.68, "ethics": 43.33, "bias": 100, "non-toxicity": 75.52},
        {"rank": 2, "model": "Mistral 7k", 'ttft': 0.2, "tpok": 65, "tgt": 9.37,
         "tps": 3.7, "quality": 987, "privacy": 81.57, "ethics": 48.64, "bias": 100, "non-toxicity": 67.98}
    ]
    app = Flask(__name__)
    CORS(app)
    dash_app = init_dashboard(app, columns, data)
    register_callbacks(dash_app)
    return app
