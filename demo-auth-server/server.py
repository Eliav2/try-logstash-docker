# simple flask server to test authentication

import json
import base64
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'appdeps')))
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'success', 'message': 'Welcome to the auth server!'})

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']
        if username == 'admin' and password == 'admin':
            return jsonify({'status': 'success', 'message': 'Logged in successfully!'})
        
        # else return error unauthorized
        return jsonify({'status': 'error', 'message': 'Unauthorized'}), 401

            


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
            