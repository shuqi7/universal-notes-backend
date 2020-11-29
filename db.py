from pymongo import MongoClient


client = MongoClient("mongodb://127.0.0.1:27017")


db = client.notes

notes_table = db.notes

cursor = notes_table.find({})

for document in cursor:
      print(document)


#
# entry = {"title": "new note 2", "content": "chen liu is good"}
#
#
# notes_table.insert_one(entry)
