from flask import Flask, render_template
from flask_pymongo import pymongo
app = Flask(__name__)
CONNECTION_STRING = "mongodb+srv://VIT_Admin:pizza@vitdiaries.tpuku.mongodb.net/vitd?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('vitd')
user_collection = pymongo.collection.Collection(db, 'posts')

@app.route('/')
def hello():
    post_all = (list(user_collection.find({}, {'_id':0})))
    # print(post_all)
    return render_template("index.html", post_all = post_all)

if __name__ == "__main__":
    app.run(debug=True)