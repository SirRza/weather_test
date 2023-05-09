from flask import Blueprint, jsonify, request
from ..models import db, Data, Redis
import redis
from datetime import datetime
import uuid as uid

redis_client = redis.Redis('127.0.0.1', port=6379, db=0)

bp = Blueprint("route", __name__)



@bp.route('/', methods = ['POST'])
def welcome():

    data = request.get_json()
    redis_flag = data.get('redis_flag',0)
    user_id = data['user_id']
    location = data['location']
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uuid = uid.uuid4()

    if redis_flag != 0 and redis_flag == "True":
        redis_data = Redis(str(uuid), user_id, location, time)
        convert_data = Redis.to_redis(redis_data)
        redis_client.hmset(f"redis_data:{convert_data['id']}" , convert_data)

        return jsonify("Stored in Redis")
    else:
        sqlite_data = Data(id=str(uuid),user_id=user_id,location=location,time=time)
        db.session.add(sqlite_data)
        db.session.commit()

        return("Stored in Sqlite")
