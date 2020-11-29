from flask import Flask, request
from helper import util
import db


app = Flask(__name__)


@app.route('/notes', methods=['GET'])
def _get_notes():
    """
    GET /notes
    - No request body
    - return the existing notes
    """
    notes = db.get_notes()
    return {"notes": notes}, 200


@app.route('/notes/create', methods=['POST'])
def _add_note():
    """
    POST /notes
    - Request body: {
        "title": String
        "content": String
    }
    - Return: {
        "id": String
        "title": String
        "content": String
    }
    """
    body = request.get_json()
    new_note = db.add_note(body['title'], body['content'])
    return new_note, 200
