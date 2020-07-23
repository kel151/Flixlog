import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route("/")
def get_index():
    return render_template("index.html", entries=mongo.db.entries.find())

@app.route("/entries")
def get_entries():
    return render_template("entries.html", entries=mongo.db.entries.find())

@app.route("/entry/add", methods=["GET", "POST"])
def get_makeentry():
    if request.method == "POST":
        mongo.db.entries.insert_one(request.form.to_dict())
        return redirect(url_for('get_entries'))
    else:
        return render_template("makeentry.html", entries=mongo.db.entries.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)