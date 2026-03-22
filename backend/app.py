from flask import Flask
from flask_cors import CORS
from models import db, Seder, Day
from auth import auth
from attendance import attendance

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.secret_key = "secret"

db.init_app(app)
app.register_blueprint(auth)
app.register_blueprint(attendance)

# ===== יצירת סדרים וימים אוטומטית =====
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
# =======================================

@app.route("/")
def home():
    return "API Running"

if __name__ == "__main__":
    app.run()