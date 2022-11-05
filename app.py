from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from flask_cors import CORS
from resources import create_api, create_socketio
from resources.config.configure import config

from db import db

#SECRET_KEY = config['DEFAULT']['SECRET_KEY']
#db_name = config['DEFAULT']['DB_NAME']+'.db'

host = "0.0.0.0"
port = 80

SECRET_KEY = "chan"
db_name="chatbot"
#SETUP
#1. virtualenv venv --python=python3.8
#2. Flask-RESTful
#3. Flask-JWT

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "chan"
api = Api(app) #API FLASK SERVER

sock = SocketIO(app,cors_allowed_origins="*")

#this will be used for login(authenticate users)
jwt = JWTManager(app) #this will make endpoint named '/auth' (username,password)
#JWT will be made based on what authenticate returns(user) and JWT will be sent to identity to identify which user has Vaild JWT

#API works with resouce
#200 ok
#201 created
#202 accepted
#400 Bad request
#404 NotFounded
#
# @jwt.user_claims_loader
# def add_claims_to_jwt(identity):  # Remember identity is what we define when creating the access token
#     if identity == 1:   # instead of hard-coding, we should read from a config file or database to get a list of admins instead
#         return {'is_admin': True}
#     return {'is_admin': False}
#
# @jwt.invalid_token_loa
#
# der
# def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
#     return jsonify({
#         'message': 'Signature verification failed.',
#         'error': 'invalid_token'
#     }), 401
#
# @jwt.unauthorized_loader
# def missing_token_callback(error):
#     return jsonify({
#         "description": "Request does not contain an access token.",
#         'error': 'authorization_required'
#     }), 401
#
# @jwt.revoked_token_loader
# def revoked_token_callback():
#     return jsonify({
#         "description": "The token has been revoked.",
#         'error': 'token_revoked'
#     }), 401
@app.route('/health')
def health():
    return "OK"

create_api(api)
create_socketio(sock)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":

    db.init_app(app)
    #app.run(port=3001,debug=True) #debug tells us what is problem
    print("Now we Run...")
    sock.run(app,host=host,port=port,debug=False)