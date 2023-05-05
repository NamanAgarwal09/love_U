from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)


@app.route("/")
def home():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return render_template("home.html", test_Line=random.choice(list(data.values())))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/add_Fuck_data', methods=['GET', 'POST'])
def addData():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        f = open("data.json", "a")
        a = str(request.form.get('number'))
        text = str(request.form.get('name'))
        print(text)
        f.write(f' "{a}" : "{text}",\n ')
        f.close()
        return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
