from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
import psycopg2
import pandas as pd
from datetime import datetime
import io
import os

app = Flask(__name__)
app.secret_key = "secret123"

DATABASE_URL = os.getenv("DATABASE_URL", "dbname=test user=postgres password=1234 host=localhost")

def get_db():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def index():
    if "user" not in session:
        return redirect("/login")
    return render_template("app.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/api/students")
def students():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route("/api/add_student", methods=["POST"])
def add_student():
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES (%s,%s)", (data["id"], data["name"]))
    conn.commit()
    return {"status":"ok"}

@app.route("/download")
def download():
    conn = get_db()
    df = pd.read_sql("SELECT * FROM content", conn)

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)

    output.seek(0)
    filename = f"עדכון_ישיבה_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.xlsx"
    return send_file(output, download_name=filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
