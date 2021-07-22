from flask import Flask, render_template, request, redirect
from flask_pymongo import pymongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Cant_say'

CONNECTION_STRING = "mongodb+srv://VIT_Admin:pizza@vitdiaries.tpuku.mongodb.net/vitd?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('vitd')
user_collection = pymongo.collection.Collection(db, 'posts')

@app.route('/', methods=['GET', 'POST'])
def home():
    post_all = (list(user_collection.find({}, {'_id':0}).sort("_id", -1)))
    return render_template("index.html", post_all = post_all)

@app.route('/about')
def aboutus():
    return render_template("about.html")

@app.route('/news')
def newss():
    return render_template("news.html")

@app.route('/contact')
def contactus():
    return render_template("contact.html")

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
    if request.method=="POST":
        author = request.form['author']
        text = request.form['post']
        user_collection.insert_one({'Author': author, 'Text':text})
        return redirect("/")
    return render_template("newpost.html")

if __name__ == "__main__":
    app.run(debug=True)