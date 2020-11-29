from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)


@app.route('/notes')
def get_notes():
    client = MongoClient("mongodb://127.0.0.1:27017")

    db = client.notes

    notes_table = db.notes

    cursor = notes_table.find({})

    notes = []

    for document in cursor:
        title = document["title"]
        content = document["content"]
        note = {"title": title, "content": content}
        notes.append(note)

    return {"notes": notes}



if __name__ == '__main__':
    app.run()
