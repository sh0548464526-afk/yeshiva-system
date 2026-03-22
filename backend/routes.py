from flask import Blueprint, request, jsonify
from models import db, Student, Day, Seder, Attendance
from logic import calc_day

api = Blueprint("api", __name__)

@api.route("/students")
def students():
    return jsonify([{"tz":s.tz,"name":s.name} for s in Student.query.all()])

@api.route("/students", methods=["POST"])
def save_students():
    Student.query.delete()
    for r in request.json:
        db.session.add(Student(**r))
    db.session.commit()
    return {"ok":True}

@api.route("/attendance/full")
def full():
    sedarim = Seder.query.all()
    data = Attendance.query.all()

    res=[]
    for r in data:
        total = calc_day({
            "s1":r.s1,"s2":r.s2,"s3":r.s3
        }, sedarim)

        res.append({
            "tz":r.tz,
            "day":r.day,
            "s1":r.s1,
            "s2":r.s2,
            "s3":r.s3,
            "total":total
        })
    return jsonify(res)

@api.route("/attendance", methods=["POST"])
def save_att():
    for r in request.json:
        ex = Attendance.query.filter_by(tz=r["tz"],day=r["day"]).first()
        if ex:
            ex.s1=r["s1"]; ex.s2=r["s2"]; ex.s3=r["s3"]
        else:
            db.session.add(Attendance(**r))
    db.session.commit()
    return {"ok":True}