# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
from models import UserManager

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shanchow1234!",
        database="medicus_assist"
    )
    return conn

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user_manager = UserManager(get_db_connection())
    success = user_manager.create_user(data['username'], data['email'], data['password'])
    if success:
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'message': 'Failed to register user'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user_manager = UserManager(get_db_connection())
    if user_manager.verify_user(data['username'], data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
