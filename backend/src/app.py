from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

# Database connection function
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shanchow1234!",
        database="medicus_assist"
    )
    return conn

@app.route('/')
def home():
    return jsonify({'message': 'Healthcare Chatbot API'})

@app.route('/info', methods=['GET'])
def get_info():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT info FROM information")  # Example SQL query
    info = cursor.fetchone()
    conn.close()
    return jsonify({'info': info})

@app.route('/appointment', methods=['POST'])
def schedule_appointment():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    # Example SQL command to insert appointment
    cursor.execute("INSERT INTO appointments (details) VALUES (%s)", (data['details'],))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Appointment scheduled', 'details': data})

# Registration Route
@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    email = request.json['email']
    plain_password = request.json['password']
    hashed_password = bcrypt.generate_password_hash(plain_password).decode('utf-8')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', 
                   (username, hashed_password, email))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'User registered successfully'}), 201

# Login Route
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user = cursor.fetchone()
    conn.close()
    
    if user and bcrypt.check_password_hash(user['password'], password):
        # Generate token (session or JWT)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
