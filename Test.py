import pymongo
cluster = pymongo.MongoClient("mongodb+srv://VIT_Admin:<password>@vitdiaries.tpuku.mongodb.net/vitd?retryWrites=true&w=majority")
db = cluster["vitd"]
collection = db["posts"]
post = [{
        'Author' : 'Anonymous',
        'Text' : 'Demo Text'
        },
        {
        'Author' : 'Sample',
        'Text' : 'Demo Text 2'
        },
        {
        'Author' : 'No',
        'Text' : 'Demo Text 3'
        }]
collection.insert_many(post)