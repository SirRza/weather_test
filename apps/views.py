from flask import Flask,request, jsonify
from .app import db
from .model import Test

app = Flask(__name__)

@app.route('/', methods=['POST'])
def welcome():
    data = request.get_json()
    flags = data.get('hola', 0)
    if flags != 0 and flags == True:
        test = Test(location= "mashhad", redis= True, user_id=2)
        db.session.add(test)
        db.session.commit()

    return jsonify(data)
