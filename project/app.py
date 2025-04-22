
from cs50 import SQL
from flask import Flask, render_template, request
from flask_session import Session




# Configure application
app = Flask(__name__)

db = SQL("sqlite:///project.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mcqs",methods=["GET","POST"])
def mcqs():
    chapter = request.form.get("chapter")
    subject = request.form.get("subject")
    if chapter == "All":
        mcqs = db.execute("select * from mcqs where subject = ? ",subject)
        return render_template("mcqs.html",mcqs = mcqs)
    else:
        mcqs = db.execute("select * from mcqs where chapter = ? AND subject = ? ",chapter,subject)
        return render_template("mcqs.html",mcqs = mcqs)

@app.route("/plan",methods=["GET","POST"])
def plan():
    return render_template("plan.html")


@app.route("/subjects")
def subjects():
    subjects = db.execute("select count(distinct chapter),subject from mcqs group by subject")
    return render_template("subjects.html",subjects = subjects)

@app.route("/chapters", methods=["GET", "POST"])
def chapters():
    subject = request.form.get("subject")
    chapters = db.execute("select chapter,count(question) from mcqs where subject = ? group by chapter order by chapter_number ",subject)
    total_que = db.execute("select count(question) from mcqs where subject = ?",subject)
    return render_template("chapters.html",chapters = chapters,total_que = total_que,subject = subject)

@app.route("/motivation",methods=["GET","POST"])
def motivation():
    return render_template("motivation.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

