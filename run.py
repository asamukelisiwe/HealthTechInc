from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/index.html", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["M"]
        session['username'] = user
        return redirect(url_for("dashboard"))
    else:
        return render_template("index.html")

@app.route("/Signup.html", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    else:
        return render_template("Signup.html")

@app.route("/dashboard.html")
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template("dashboard.html", name=username)
    else:
        return redirect(url_for("login"))

@app.route("/medicalHistory.html")
def medicalHistory():
    if 'username' in session:
        return render_template("medicalHistory.html")
    else:
        return redirect(url_for("login"))

@app.route("/patientFiles.html")
def patientFiles():
    if 'username' in session:
        return render_template("patientFiles.html")
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("login"))
@app.route("/registerPatient.html")
def registerPatient():
    if 'username' in session:
        return render_template("registerPatient.html")
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)