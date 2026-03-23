from flask import Flask
from flask_cors import CORS
from config import Config
from models import db, Seder, Day

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

    if not Seder.query.first():
        db.session.add_all([
            Seder(name="בוקר", start="08:00", amount=50, late=5),
            Seder(name="צהריים", start="13:00", amount=40, late=5),
            Seder(name="ערב", start="19:00", amount=60, late=5),
        ])

    if not Day.query.first():
        for d in ["א","ב","ג","ד","ה","ו"]:
            db.session.add(Day(name=d, active=True))

    db.session.commit()

from routes import register
register(app)

@app.route("/")
def home():
    return "OK"
