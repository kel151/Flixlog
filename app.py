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

@app.route('/edit_entry/<entry_id>')
def edit_entry(entry_id):
    the_entry =  mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
    all_categories =  mongo.db.categories.find()
    print(the_entry)
    return render_template('editentry.html', entry=the_entry,
                           categories=all_categories)

@app.route('/update_entry/<entry_id>', methods=["POST"])
def update_entry(entry_id):
    entries = mongo.db.entries
    entries.update( {'_id': ObjectId(entry_id)},
    {
        'entry_title':request.form.get('entry_title'),
        'entry_category':request.form.get('entry_category'),
        'entry_rating': request.form.get('entry_rating'),
        'entry_comments': request.form.get('entry_comments'),
    })
    return redirect(url_for('get_entries'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)