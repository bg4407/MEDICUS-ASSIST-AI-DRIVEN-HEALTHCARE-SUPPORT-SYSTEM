from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shanchow1234!",
            database="medicus_assist"
        )
        return conn
    except mysql.connector.Error as err:
        print("Database connection failed:", err)
        return None

@app.route('/register', methods=['POST'])
def register():
    try:
        print("Request received with data:", request.json)
        username = request.json.get('username')
        plain_password = request.json.get('password')

        if not plain_password or len(plain_password) < 8 or not re.search(r"[0-9]", plain_password) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", plain_password):
            return jsonify({'error': 'Password must be at least 8 characters long and include a number and a symbol.'}), 400

        conn = get_db_connection()
        if conn is None:
            return jsonify({'error': 'Database connection error'}), 500
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        if cursor.fetchone() is not None:
            conn.close()
            return jsonify({'error': 'Username already taken'}), 409
        
        hashed_password = bcrypt.generate_password_hash(plain_password).decode('utf-8')
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        print("An error occurred:", e)
        return jsonify({'error': 'Server error'}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']
        conn = get_db_connection()
        if conn is None:
            return jsonify({'error': 'Database connection error'}), 500
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and bcrypt.check_password_hash(user['password'], password):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        print("An error occurred during login:", e)
        return jsonify({'error': 'Server error during login'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
