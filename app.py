from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
progress = {"score": 0}
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answer = request.form.get("q1")
        if answer == "Python":
            progress["score"] = 100
        else:
            progress["score"] = 0
        return redirect(url_for("result"))
    return render_template("quiz.html")

@app.route('/result')
def result():
    return f"<h2>Your Score: {progress['score']}%</h2><br><a href='/dashboard'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
