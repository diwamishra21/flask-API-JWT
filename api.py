'''
Author- Diwaker
Date- 30/05/2021
Code Objective- This file is a flask API to authorize users using JWT(JSON Web Tokens). User can access public API directly but after login they needed token to use private APIs. This is a standard way to secure your API from unauthorize access.
Prerequisite- knowledge and installation of python and flask
Code running- python api.py
Access URLs on brpwser-
http://localhost:5000/unprotected
http://localhost:5000/login (Usrname- admin, Password- secret)
in response you will get a token, Use this token using GET method to access protected Data
http://localhost:5000/protected?token=<your token>

'''


# import important libraries
from flask import Flask, jsonify, request, make_response
import jwt 
import datetime
from functools import wraps

# calling flask constructor
app = Flask(__name__)

# it should be unique and hard to guess and should take from an external file
app.config['SECRET_KEY'] = 'thisisthesecretkey'

# decorator function to check token in case of protected APIs
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated

# public API route 
@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'})

# private API route 
@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'This is only available for people with valid tokens.'})

# login route
@app.route('/login')
def login():
    auth = request.authorization

    # for testing purpose, we are only checking password = secret
    if auth and auth.password == 'secret':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=300)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

# running our app
if __name__ == '__main__':
    app.run(debug=True)