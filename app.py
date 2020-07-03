import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "mav"
app.config["MONGO_URI"] = "mongodb+srv://floppypancake:ms3ser342@myfirstcluster-frg8m.mongodb.net/mav?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_entries")
def get_entries():
    return render_template("entries.html", entries=mongo.db.entries.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)