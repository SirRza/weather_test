from flask import Flask, jsonify
from test_app.routes.test_app import bp
from test_app.models.test_app import db
from redis.exceptions import ConnectionError
from sqlalchemy import exc as sqlalchemy_exec
#from flasgger import Swagger




app = Flask(__name__)
#swagger = Swagger(app)

#Error Handler For DB ( Redi and MySQL)
@app.errorhandler(ConnectionError)
def handler_error_for_db(error):
    return jsonify({"result":"False", "Message":"Cant Connect to Redis" , "Detail":error})

@app.errorhandler(sqlalchemy_exec.OperationalError)
def handler_error_for_db(error):
    return jsonify({"result":"False", "Message":"Cant Connect to MySQL"})



#Sqllite Config
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///testData.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}@{server}/{database}'.format(user='root', server='localhost', database='test_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(bp)


with app.app_context():
    db.create_all()

