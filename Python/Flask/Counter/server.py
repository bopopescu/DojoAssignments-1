from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "seckey"

@app.route('/')
def home():
    if "count" in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("index.html", num=session['count'])

@app.route('/button', methods=["POST"])
def button():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods = ["POST"])
def reset():
    session['count'] = 0
    return redirect('/')
app.run(debug=True)