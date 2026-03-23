import os

files = {

"app.py": '''from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
import psycopg2
import pandas as pd
from datetime import datetime
import io

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
''',

"requirements.txt": '''flask
psycopg2-binary
pandas
xlsxwriter
gunicorn
''',

"templates/login.html": '''<!DOCTYPE html>
<html>
<head>
<title>Login</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="d-flex justify-content-center align-items-center vh-100 bg-light">

<form method="post" class="p-4 bg-white shadow rounded">
<h3 class="mb-3 text-center">התחברות</h3>
<input name="username" class="form-control mb-2" placeholder="שם משתמש">
<input name="password" type="password" class="form-control mb-3" placeholder="סיסמה">
<button class="btn btn-primary w-100">כניסה</button>
</form>

</body>
</html>
''',

"templates/app.html": '''<!DOCTYPE html>
<html>
<head>
<title>מערכת</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
<script src="/static/app.js"></script>
</head>
<body class="bg-light">

<div class="container mt-4">

<h2 class="text-center">ברוך הבא למערכת ישיבת בין הזמנים</h2>

<div class="d-flex justify-content-between my-3">
<a href="/logout" class="btn btn-danger">התנתק</a>
<button class="btn btn-secondary">⚙️ הגדרות</button>
<a href="/download" class="btn btn-success">הורדת אקסל</a>
</div>

<input id="search" class="form-control mb-3" placeholder="חיפוש...">

<table class="table table-bordered bg-white">
<thead>
<tr><th>ת"ז</th><th>שם</th></tr>
</thead>
<tbody id="table"></tbody>
</table>

<button onclick="loadData()" class="btn btn-primary">רענן</button>

</div>

</body>
</html>
''',

"static/app.js": '''async function loadData(){
    let res = await fetch("/api/students")
    let data = await res.json()

    let table = document.getElementById("table")
    table.innerHTML = ""

    data.forEach(row=>{
        let tr = "<tr><td>"+row[0]+"</td><td>"+row[1]+"</td></tr>"
        table.innerHTML += tr
    })
}

window.onload = loadData

document.addEventListener("input", function(e){
    if(e.target.id==="search"){
        let val = e.target.value.toLowerCase()
        document.querySelectorAll("#table tr").forEach(tr=>{
            tr.style.display = tr.innerText.toLowerCase().includes(val) ? "" : "none"
        })
    }
})
''',

"schema.sql": '''CREATE TABLE IF NOT EXISTS students(
    id TEXT PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS content(
    id TEXT,
    name TEXT,
    total INTEGER
);
''',

"render.yaml": '''services:
  - type: web
    name: yeshiva-system
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: yeshiva-db
          property: connectionString

databases:
  - name: yeshiva-db
    plan: free
'''
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("הפרויקט נוצר בהצלחה!")