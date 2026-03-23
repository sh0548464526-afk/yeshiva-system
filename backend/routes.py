
from flask import request, jsonify, send_file
from models import db, Student, Day, Seder, Attendance
from logic import calc_day
import io, datetime
from openpyxl import Workbook

def register(app):

    @app.route("/attendance/full")
    def full():
        s = Seder.query.all()
        data = Attendance.query.all()
        res=[]
        for r in data:
            total = calc_day({"s1":r.s1,"s2":r.s2,"s3":r.s3}, s)
            res.append({
                "tz":r.tz,"day":r.day,
                "s1":r.s1,"s2":r.s2,"s3":r.s3,
                "total":total
            })
        return jsonify(res)

    @app.route("/attendance", methods=["POST"])
    def save():
        for r in request.json:
            ex = Attendance.query.filter_by(tz=r["tz"],day=r["day"]).first()
            if ex:
                ex.s1=r["s1"]; ex.s2=r["s2"]; ex.s3=r["s3"]
            else:
                db.session.add(Attendance(**r))
        db.session.commit()
        return {"ok":True}

    @app.route("/export")
    def export():
        data = full().json
        wb=Workbook(); ws=wb.active
        ws.append(["תז","יום","ס1","ס2","ס3","סהכ"])
        for r in data:
            ws.append([r["tz"],r["day"],r["s1"],r["s2"],r["s3"],r["total"]])
        f=io.BytesIO(); wb.save(f); f.seek(0)
        name="ישיבה_"+datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")+".xlsx"
        return send_file(f, as_attachment=True, download_name=name)

    @app.route("/phone-api", methods=["POST"])
    def phone():
        return {"status":"ready"}
