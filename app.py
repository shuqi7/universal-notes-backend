from flask import Flask
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

