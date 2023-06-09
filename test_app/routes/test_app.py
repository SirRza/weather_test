from flask import Blueprint, jsonify, request
from ..models.test_app import db, Data, Redis
from datetime import datetime
import uuid as uid
import redis


redis_client = redis.Redis('redis', port=6380, db=0)


bp = Blueprint("route", __name__)



@bp.route('/', methods = ['POST'])
def welcome():
  """
    Store data in Redis or SQLite.

    ---
    tags:
      - Data For Test
    parameters:
      - in: body
        name: data
        description: Data to store
        schema:
          type: object
          properties:
            redis_flag:
              type: string
              description: Flag indicating whether to store data in Redis
            user_id:
              type: integer
              description: User ID
            location:
              type: string
              description: Location
          required:
            - user_id
            - location
          required: false
    responses:
      201:
        description: Data stored successfully
        schema:
          type: object
          properties:
            message:
              type: string
          example:
            message: Stored in Redis
      202:
        description: Request to Store in Sqlite
        schema:
          type: object
          properties:
            message:
              type: string
          example:
            message: Stored in Sqlite
    """

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

      response = jsonify({"Result":"True", "Message":f"Your data Stored in Redis at {time}"})
      response.status_code = 201
      return response
  else:
      sqlite_data = Data(id=str(uuid),user_id=user_id,location=location,time=time)
      db.session.add(sqlite_data)
      db.session.commit()

      response = jsonify({"Result":"True", "Message":f"Your data Stored in Mysql at {time}"})
      response.status_code = 202
      return response
